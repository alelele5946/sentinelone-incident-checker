import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# API Keys
VT_API_KEY = os.getenv("VT_API_KEY")

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

# Verificar que las claves estén bien cargadas
if not VT_API_KEY:
    raise ValueError("❌ ERROR: No se encontró la API Key de VirusTotal. Verifica .env.")



if not CLAUDE_API_KEY:
    raise ValueError("❌ ERROR: No se encontró la API Key de CLAUDE. Verifica .env.")
