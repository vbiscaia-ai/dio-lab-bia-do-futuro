from groq import Groq

client = Groq(os.getenv("API_KEY"))

print("--- MODELOS DISPONÍVEIS NA SUA CONTA GROQ ---")
try:
    models = client.models.list()
    for model in models.data:
        print(f"MODELO: {model.id}")
except Exception as e:
    print(f"Erro ao listar: {e}")