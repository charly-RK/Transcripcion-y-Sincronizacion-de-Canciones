import whisper
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Ocultar ventana principal de Tkinter
Tk().withdraw()

# Mostrar dialogo para seleccionar archivo
archivo_audio = askopenfilename(
    title="Selecciona una canción (.mp3)",
    filetypes=[("Archivos de audio", "*.mp3")]
)

# Verificar si se selecciono un archivo
if not archivo_audio:
    print("No se seleccionó ningún archivo.")
    exit()

# Obtener nombre de la cancion sin extension
nombre_cancion = os.path.splitext(os.path.basename(archivo_audio))[0]
archivo_salida = f"{nombre_cancion}.txt"

# Cargar el modelo Whisper
#tiny (el mas rapido, menos preciso)
#base
#small
#medium
#large (el mas lento y mas preciso) RECOMENDADO

model = whisper.load_model("large")

# Transcribir el archivo seleccionado
result = model.transcribe(archivo_audio)

# Guardar la transcripcion en un archivo de texto
with open(archivo_salida, "w", encoding="utf-8") as f:
    for segment in result['segments']:
        start = int(segment['start'])
        texto = segment['text'].strip()
        f.write(f"[{start}] {texto}\n")

print(f"Transcripción guardada en {archivo_salida}")
