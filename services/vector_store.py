import os, numpy as np
from pymongo import MongoClient
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

    async def initialize(self):
        cs = os.getenv("MONGODB_CONNECTION_STRING")
        client = MongoClient(cs)
        self.collection = client.invoice_reimbursement.analyses

    async def store_analysis(self, invoice_id: str, invoice_text: str, analysis, employee_name: str, invoice_filename: str, date: str):
        content = f"Employee:{employee_name}\nFilename:{invoice_filename}\nStatus:{analysis.reimbursement_status}\nAmount:{analysis.reimbursable_amount}\nReason:{analysis.reason}\nText:{invoice_text}"
        emb = self.embedding_model.encode(content).tolist()
        doc = {
            "invoice_id": invoice_id,
            "employee_name": employee_name,
            "invoice_filename": invoice_filename,
            "reimbursement_status": analysis.reimbursement_status,
            "reimbursable_amount": analysis.reimbursable_amount,
            "total_amount": analysis.total_amount,
            "reason": analysis.reason,
            "detailed_breakdown": analysis.detailed_breakdown,
            "date": date,
            "content": content,
            "embedding": emb
        }
        self.collection.insert_one(doc)

    async def search(self, query: str, limit: int = 5, filters=None):
        qe = self.embedding_model.encode(query).tolist()
        docs = list(self.collection.find(filters or {}))
        sims = []
        for d in docs:
            e = d.get("embedding")
            if e:
                v1, v2 = np.array(qe), np.array(e)
                sim = float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
                sims.append((sim, d))
        sims.sort(key=lambda x: x[0], reverse=True)
        return [{"content": d["content"], "metadata": {"employee_name": d["employee_name"], "invoice_filename": d["invoice_filename"], "reimbursement_status": d["reimbursement_status"], "reimbursable_amount": d["reimbursable_amount"], "date": d["date"]}, "similarity": s} for s, d in sims[:limit]]
