Aquí tienes el `README.md` detallado y listo para copiar y pegar en tu repositorio:  

---

### 📄 **README.md - SentinelOne Incident Checker**  

```md
# SentinelOne Incident Checker 🚀  

### Herramienta para agilizar la clasificación de incidentes en el EDR de SentinelOne 🔍  

Este proyecto está diseñado para automatizar el análisis de incidentes detectados en SentinelOne, facilitando la evaluación de amenazas mediante consultas automáticas a **VirusTotal** y **Claude AI**.  

✅ **¿Qué hace esta herramienta?**  
1. **Extrae automáticamente el `SHA256` del incidente** desde un reporte de SentinelOne.  
2. **Consulta en VirusTotal** para obtener información sobre cuántos motores antivirus lo detectan como malicioso y en cuántos sandboxes ha sido analizado.  
3. **Analiza la amenaza con Claude AI**, obteniendo una conclusión breve sobre su naturaleza.  
4. **Proporciona una interfaz gráfica con Tkinter** donde el usuario puede pegar el reporte, analizarlo y copiar el resultado.  

---

## 📂 **Estructura del Proyecto**  

📁 **sentinelone-incident-checker/** _(directorio raíz)_  
│── 📄 `main.py` ➝ **Ejecuta la aplicación** y conecta todas las partes del proyecto.  
│── 📄 `virustotal_api.py` ➝ **Consulta VirusTotal** con el `SHA256` del archivo analizado.  
│── 📄 `gpt_analysis.py` ➝ **Realiza la consulta a Claude AI** y genera una conclusión.  
│── 📄 `config.py` ➝ **Manejo de claves API** (NO debe subirse al repositorio).  
│── 📄 `.env` ➝ **Almacena las claves API** de forma segura (excluido con `.gitignore`).  
│── 📄 `requirements.txt` ➝ **Lista de dependencias** necesarias para ejecutar el proyecto.  
│── 📄 `README.md` ➝ **Explicación detallada del proyecto**.  

---

## 🛠️ **Instalación y Configuración**  

### 🔹 1️⃣ **Clonar el repositorio**  
```bash
git clone https://github.com/TU-USUARIO-GITHUB/sentinelone-incident-checker.git
cd sentinelone-incident-checker
```

### 🔹 2️⃣ **Crear un entorno virtual y activarlo**  
```bash
python -m venv venv
# Para Windows:
venv\Scripts\activate
# Para Linux/macOS:
source venv/bin/activate
```

### 🔹 3️⃣ **Instalar las dependencias**  
```bash
pip install -r requirements.txt
```

### 🔹 4️⃣ **Configurar claves API**  
Antes de ejecutar el programa, debes agregar tus claves API en un archivo `.env`.  
Crea el archivo **`.env`** en el directorio raíz y añade lo siguiente:  

```ini
VIRUSTOTAL_API_KEY="tu-api-key-aquí"
CLAUDE_API_KEY="tu-api-key-aquí"
```

*(Este archivo no debe subirse a GitHub, ya que contiene información sensible).*

---

## 🚀 **Cómo Usar la Aplicación**  

Ejecuta la aplicación con:  
```bash
python main.py
```

👨‍💻 **Pasos en la Interfaz Gráfica:**  
1️⃣ **Pega el reporte de SentinelOne** en el cuadro de entrada.  
2️⃣ **Haz clic en "Analizar Amenaza"** para iniciar el proceso.  
3️⃣ **Espera los resultados** de VirusTotal y Claude AI.  
4️⃣ **Usa el botón "Copiar Resultado"** si deseas guardar la conclusión.  
5️⃣ **Si necesitas analizar otro reporte, usa el botón "Borrar"** para limpiar el cuadro de entrada.  

---

## 🔍 **Explicación de los Archivos**  

### 📌 `main.py`
- Inicia la interfaz gráfica con **Tkinter**.  
- Permite al usuario pegar un reporte y analizarlo con un clic.  
- Conecta las funciones de análisis de **VirusTotal** y **Claude AI**.  
- Muestra los resultados en la interfaz.  

### 📌 `virustotal_api.py`
- Extrae el `SHA256` del reporte y lo consulta en VirusTotal.  
- Recupera:  
  ✅ Número de motores antivirus que detectaron el archivo como malicioso.  
  ✅ Número de sandboxes donde ha sido analizado.  

### 📌 `gpt_analysis.py`
- Toma la información del reporte de SentinelOne y los datos de VirusTotal.  
- Envía esta información a **Claude AI** para obtener un análisis breve.  
- Devuelve una conclusión sobre si la amenaza es un **Verdadero Positivo**, **Falso Positivo** o **Sospechoso**.  

### 📌 `.env`
- Almacena las claves API necesarias para usar VirusTotal y Claude AI.  

### 📌 `requirements.txt`
- Lista de dependencias necesarias para ejecutar el proyecto, incluyendo:  
  ```txt
  requests
  python-dotenv
  anthropic
  tkinter
  pyperclip
  ```
  *(Asegura que el entorno tenga las librerías correctas con `pip install -r requirements.txt`).*

---

## 📌 **Ejemplo de Análisis**
```txt
🔍 Analizando en VirusTotal...
✅ VirusTotal detectó 27 motores antivirus marcándolo como malicioso.
🧪 Sandboxes con detecciones: 0

🤖 Enviando a Claude para análisis...
🎯 **Conclusión de Claude:**
El archivo parece ser un troyano con alta probabilidad de ser malicioso. Se recomienda precaución y revisión manual.
```

---

## 📜 **Notas Importantes**  
- Si el `SHA256` no se encuentra en el reporte de SentinelOne, la aplicación mostrará un mensaje de error.  
- La API de VirusTotal tiene un **límite de consultas**, por lo que se recomienda no abusar del servicio gratuito.  
- Si Claude AI no responde correctamente, asegúrate de tener saldo en tu cuenta de **Anthropic API**.  

---

## 👨‍💻 **Contribución**  
Si deseas mejorar este proyecto, **haz un fork y envía un pull request**.  

---

## 📜 **Licencia**  
Este proyecto es de código abierto bajo la licencia **MIT**.  

---

🔥 **Desarrollado por [TU NOMBRE]** 🚀  
```

---

### ✅ **Siguiente paso:**  
Guarda este archivo como `README.md`, agrégalo al repositorio y súbelo con los siguientes comandos:

```bash
git add README.md
git commit -m "Añadido README detallado"
git push origin main
```

