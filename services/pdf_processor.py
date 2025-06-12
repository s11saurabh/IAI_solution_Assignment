import PyPDF2

class PDFProcessor:
    def extract_text(self, pdf_path: str) -> str:
        text = ""
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for p in reader.pages:
                text += (p.extract_text() or "") + "\n"
        return text.strip()
