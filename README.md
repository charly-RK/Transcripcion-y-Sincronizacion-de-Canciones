
# 🎵 **LyriSync - Transcripción y Sincronización de Canciones**


**LyriSync** es una herramienta de escritorio que permite transcribir canciones en formato `.mp3`, extrayendo la letra y generando archivos de texto con sincronización temporal. Posteriormente, estos archivos pueden utilizarse para mostrar la letra de la canción en tiempo real mientras se reproduce, simulando una experiencia tipo karaoke.

---

## ✨ **Características principales**

- 🎧 **Transcripción de canciones desde archivos MP3**
- 🕒 **Generación de archivos de texto con sincronización temporal**
- 🎤 **Reproducción de canciones con visualización de letras al estilo karaoke**
- 🖱️ **Interfaz gráfica sencilla e intuitiva**

---

## 🖥️ **Requisitos del sistema**

- `Python 3.6` o superior  
- `FFmpeg` instalado y configurado en el `PATH` del sistema  
- Sistema operativo **Windows** (probado en Windows 10)

---

## 📦 **Dependencias**

Este proyecto utiliza las siguientes bibliotecas de Python:

- `pip install pygame pillow mutagene`
```



## 🔧 **Instalación**

### 1. Instalar Python

Asegúrate de tener Python instalado. 

### 2. Instalar FFmpeg (Windows)

1. Ve al sitio oficial de descargas: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)  
2. Descarga la versión correspondiente a tu sistema operativo (Windows)  
3. Extrae el contenido del archivo `.zip`  
4. Copia la ruta de la carpeta `bin` del FFmpeg extraído  
5. Añade esta ruta a la variable de entorno `PATH` de tu sistema  

   Panel de Control → Sistema y Seguridad → Sistema → Configuración avanzada del sistema → Variables de entorno


   En "Variables del sistema":
   - Selecciona `Path` → **Editar** → **Nuevo** → pega la ruta copiada → **Aceptar**

### 3. Instalar dependencias de Python



## ▶️ **Uso del programa**

### 1. Transcribir una canción

Ejecuta el script `transcriptor.py`:


transcriptor.py


🗂️ Se abrirá una ventana para que selecciones un archivo `.mp3`. El script generará un archivo `.txt` con la letra y los tiempos de la canción.

### 2. Reproducir canción con letra sincronizada

Una vez generado el archivo `.txt`, ejecuta el script principal:

 main.py


Este script te permitirá:

1. Seleccionar la canción en formato `.mp3`  
2. Seleccionar el archivo `.txt` generado  
3. Mostrar la letra sincronizada en pantalla 🎶

