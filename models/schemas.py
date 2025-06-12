from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class InvoiceAnalysis(BaseModel):
    invoice_filename: str
    employee_name: str
    reimbursement_status: str
    reimbursable_amount: float
    total_amount: float
    reason: str
    detailed_breakdown: Dict[str, Any]
    date_analyzed: str

class InvoiceAnalysisResponse(BaseModel):
    success: bool
    message: str
    results: List[InvoiceAnalysis]

class ChatMessage(BaseModel):
    role: str
    content: str
    timestamp: Optional[str] = None

class ChatRequest(BaseModel):
    query: str
    chat_history: List[ChatMessage] = []

class ChatResponse(BaseModel):
    response: str
    success: bool
    error_message: Optional[str] = None
