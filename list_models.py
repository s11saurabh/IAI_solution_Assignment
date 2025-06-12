

from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

for model in genai.list_models():
   
    methods = getattr(model, "supportedMethods", None) or getattr(model, "supported_methods", None) or getattr(model, "methods", None)
    print(model.name, "→ methods:", methods)
