import requests
import json
from config import VT_API_KEY  # Importamos la API Key desde config.py

def consultar_virustotal(sha256):
    url = f"https://www.virustotal.com/api/v3/files/{sha256}"
    headers = {"x-apikey": VT_API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        # Extraer información clave
        total_engines = data["data"]["attributes"]["last_analysis_stats"]
        sandbox_reports = data["data"]["attributes"].get("sandbox_verdicts", {})

        # Filtrar sandboxes que NO sean 'undetected'
        num_sandboxes = sum(1 for verdict in sandbox_reports.values() if verdict.get("category") != "undetected")

        # Contar detecciones por antivirus
        num_detected = total_engines.get("malicious", 0) + total_engines.get("suspicious", 0)

        # Mostrar resultados
        print(f"\n🔍 **Análisis de VirusTotal para el archivo:** {sha256}")
        print(f"📌 Motores antivirus detectando como malicioso: {num_detected}")
        print(f"🧪 Número de Sandboxes con detecciones (excluyendo 'undetected'): {num_sandboxes}")

        return num_detected, num_sandboxes

    else:
        print(f"❌ Error al consultar VirusTotal. Código de respuesta: {response.status_code}")
        return None, None

