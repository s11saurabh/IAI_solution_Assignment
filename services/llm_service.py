
import os
import json
from datetime import datetime
import google.generativeai as genai
from models.schemas import InvoiceAnalysis, ChatMessage

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


class LLMService:
    def __init__(self):
        self.model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

    async def analyze_invoice(
        self,
        policy_text: str,
        invoice_text: str,
        employee_name: str,
        invoice_filename: str
    ) -> InvoiceAnalysis:
        prompt = f"""
You are an expert financial analyst tasked with analyzing employee invoice reimbursements against company policy.

COMPANY POLICY:
{policy_text}

INVOICE:
Employee Name: {employee_name}
Filename: {invoice_filename}
Content:
{invoice_text}

REQUIREMENTS:
1. reimbursement_status
2. reimbursable_amount
3. total_amount
4. reason
5. detailed_breakdown

Respond in JSON:
{{
  "invoice_filename": "{invoice_filename}",
  "employee_name": "{employee_name}",
  "reimbursement_status": "",
  "reimbursable_amount": 0,
  "total_amount": 0,
  "reason": "",
  "detailed_breakdown": {{}},
  "date_analyzed": "{datetime.now().isoformat()}"
}}
"""
        try:
            response = self.model.generate_content(prompt)
            text = response.text.strip()
            try:
                analysis_data = json.loads(text)
            except json.JSONDecodeError:
                # attempt to extract JSON substring
                start = text.find("{")
                end = text.rfind("}") + 1
                if start != -1 and end != -1:
                    snippet = text[start:end]
                    analysis_data = json.loads(snippet)
                else:
                    raise
            return InvoiceAnalysis(**analysis_data)
        except Exception as e:
            return InvoiceAnalysis(
                invoice_filename=invoice_filename,
                employee_name=employee_name,
                reimbursement_status="Declined",
                reimbursable_amount=0.0,
                total_amount=0.0,
                reason=f"LLM service error: {e}",
                detailed_breakdown={},
                date_analyzed=datetime.now().isoformat()
            )

    async def chat_with_context(
        self,
        query: str,
        chat_history: list[ChatMessage],
        vector_store
    ) -> str:
        docs = await vector_store.search(query, limit=5)
        context = "\n".join(d["content"] for d in docs)
        history = "\n".join(f"{m.role}: {m.content}" for m in chat_history[-5:])
        prompt = f"""
You are an assistant for invoice reimbursement queries.

CONTEXT:
{context}

HISTORY:
{history}

QUERY: {query}

Answer in markdown.
"""
        response = self.model.generate_content(prompt)
        return response.text



