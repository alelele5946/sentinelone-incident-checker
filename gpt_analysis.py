import anthropic
import os

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")  # Usa tu API Key de Claude

client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

def analizar_con_claude(reporte_sentinelone, num_detected, num_sandboxes):
    """Consulta a Claude para obtener un análisis breve en 5 frases."""
    
    
    prompt = f"""
    Eres un experto en ciberseguridad. Analiza la siguiente amenaza basada en el reporte de SentinelOne.


    **Quiero que solamente mirando este reporte {reporte_sentinelone}, me expliques en tres oraciones máximo para que podría servir el archivo que se ha encuarentenado en caso de que fuese legitimo.
    en caso de ser un cracker para un programa explica muy brevemente para que sirve ese programa
    """

    try:
        response = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=250,
            temperature=0.5,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text.strip()
    
    except Exception as e:
        return f"❌ Error en la solicitud a Claude AI: {e}"






