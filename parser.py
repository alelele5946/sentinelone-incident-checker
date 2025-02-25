import re

def extraer_sha256(texto):
    """
    Extrae el SHA256 de un reporte de SentinelOne.
    
    :param texto: String con el reporte completo
    :return: SHA256 si se encuentra, None si no se encuentra
    """
    sha256_pattern = re.search(r"SHA256:\s*([a-fA-F0-9]{64})", texto)
    
    if sha256_pattern:
        return sha256_pattern.group(1)  # Devuelve el SHA256 encontrado
    else:
        print("❌ No se encontró SHA256 en el reporte.")
        return None
