import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    TETO_SEGURANCA = 934.00
    CAMINHO_DADOS = "../data/"
    MODELO_LLM = "gemini-1.5-flash-latest"