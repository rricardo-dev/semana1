from dotenv import load_dotenv
import os 

load_dotenv()
chave = os.getenv("MINHA_CHAVE")
print(f"Chave carregada: {chave}")
print("Versão 2 do projeto")
