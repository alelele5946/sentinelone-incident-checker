import tkinter as tk
from tkinter import scrolledtext, messagebox
import pyperclip
from virustotal_api import consultar_virustotal
from gpt_analysis import analizar_con_claude

def analizar_threat():
    """Función que toma el input del usuario, extrae el SHA256, consulta VirusTotal y obtiene la conclusión de Claude."""
    reporte_sentinelone = input_text.get("1.0", tk.END).strip()

    if not reporte_sentinelone:
        messagebox.showwarning("Error", "Por favor, introduce un reporte de SentinelOne.")
        return

    # Extraer el SHA256 del reporte
    sha256 = None
    for line in reporte_sentinelone.split("\n"):
        if "SHA256:" in line:
            sha256 = line.split("SHA256:")[1].strip()
            break

    if not sha256:
        messagebox.showwarning("Error", "No se encontró el hash SHA256 en el reporte.")
        return

    # Mostrar mensaje de carga
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "🔍 Analizando en VirusTotal...\n")

    # Consultar VirusTotal
    num_detected, num_sandboxes = consultar_virustotal(sha256)

    output_text.insert(tk.END, f"✅ VirusTotal detectó {num_detected} motores antivirus marcándolo como malicioso.\n")
    output_text.insert(tk.END, f"🧪 Sandboxes con detecciones: {num_sandboxes}\n\n")
    output_text.insert(tk.END, "🤖 Enviando a Claude para análisis...\n")

    # Consultar Claude
    conclusion = analizar_con_claude(reporte_sentinelone, num_detected, num_sandboxes)

    # Mostrar la conclusión en la interfaz
    output_text.insert(tk.END, f"🎯 **Conclusión de Claude:**\n{conclusion}\n")

def copiar_resultado():
    """Copia TODO el contenido del resultado al portapapeles."""
    resultado = output_text.get("1.0", tk.END).strip()
    
    if resultado:
        pyperclip.copy(resultado)
        messagebox.showinfo("Copiado", "El resultado completo ha sido copiado al portapapeles.")
    else:
        messagebox.showwarning("Error", "No hay contenido disponible para copiar.")

def borrar_input():
    """Limpia el campo de entrada para pegar un nuevo threat report."""
    input_text.delete("1.0", tk.END)

# Crear ventana
root = tk.Tk()
root.title("SentinelOne Threat Analyzer")
root.geometry("800x600")

# Etiqueta de instrucciones
tk.Label(root, text="Pega el Threat Report de SentinelOne:", font=("Arial", 12)).pack(pady=5)

# Caja de texto para input
input_text = scrolledtext.ScrolledText(root, width=90, height=10)
input_text.pack(pady=5)

# Contenedor para botones de acción
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# Botón para analizar
btn_analizar = tk.Button(frame_botones, text="🔍 Analizar Amenaza", font=("Arial", 12), command=analizar_threat)
btn_analizar.pack(side=tk.LEFT, padx=10)

# Botón para borrar input
btn_borrar = tk.Button(frame_botones, text="🗑 Borrar", font=("Arial", 12), command=borrar_input)
btn_borrar.pack(side=tk.LEFT, padx=10)

# Caja de texto para output
tk.Label(root, text="Resultado:", font=("Arial", 12)).pack(pady=5)
output_text = scrolledtext.ScrolledText(root, width=90, height=10, wrap=tk.WORD)
output_text.pack(pady=5)

# Botón para copiar resultado
btn_copiar = tk.Button(root, text="📋 Copiar Resultado", font=("Arial", 12), command=copiar_resultado)
btn_copiar.pack(pady=10)

# Iniciar la aplicación
root.mainloop()
