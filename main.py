from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import zipfile, tempfile, os, json
from datetime import datetime
from services.pdf_processor import PDFProcessor
from services.llm_service import LLMService
from services.vector_store import VectorStore
from models.schemas import InvoiceAnalysisResponse, ChatRequest, ChatResponse
from utils.helpers import setup_logging

app = FastAPI(title="Invoice Reimbursement System", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

pdf_processor = PDFProcessor()
llm_service = LLMService()
vector_store = VectorStore()
logger = setup_logging()

@app.on_event("startup")
async def startup_event():
    await vector_store.initialize()

@app.post("/analyze-invoices", response_model=InvoiceAnalysisResponse)
async def analyze_invoices(
    policy_file: UploadFile = File(...),
    invoices_zip: UploadFile = File(...),
    employee_name: str = Form(...)
):
    if not policy_file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Policy file must be a PDF")
    if not invoices_zip.filename.endswith('.zip'):
        raise HTTPException(status_code=400, detail="Invoices must be in a ZIP file")

    with tempfile.TemporaryDirectory() as temp_dir:
        policy_path = os.path.join(temp_dir, policy_file.filename)
        with open(policy_path, "wb") as f:
            f.write(await policy_file.read())

        zip_path = os.path.join(temp_dir, invoices_zip.filename)
        with open(zip_path, "wb") as f:
            f.write(await invoices_zip.read())

        invoice_dir = os.path.join(temp_dir, "invoices")
        os.makedirs(invoice_dir, exist_ok=True)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(invoice_dir)

        policy_text = pdf_processor.extract_text(policy_path)

        results = []
        # Recursively find all PDF files in invoice_dir
        for root, _, files in os.walk(invoice_dir):
            for fname in files:
                if not fname.lower().endswith('.pdf'):
                    continue
                invoice_path = os.path.join(root, fname)
                invoice_text = pdf_processor.extract_text(invoice_path)

                analysis = await llm_service.analyze_invoice(
                    policy_text, invoice_text, employee_name, fname
                )

                await vector_store.store_analysis(
                    invoice_id=f"{employee_name}_{fname}_{datetime.now().isoformat()}",
                    invoice_text=invoice_text,
                    analysis=analysis,
                    employee_name=employee_name,
                    invoice_filename=fname,
                    date=datetime.now().isoformat()
                )

                results.append(analysis)

        return InvoiceAnalysisResponse(
            success=True,
            message=f"Successfully analyzed {len(results)} invoices",
            results=results
        )




@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        response = await llm_service.chat_with_context(request.query, request.chat_history, vector_store)
        return ChatResponse(response=response, success=True)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}
