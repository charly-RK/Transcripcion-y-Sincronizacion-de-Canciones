# Transcripci-n-y-Sincronizaci-n-de-Canciones
LyriSync es una herramienta de escritorio que permite transcribir canciones en formato .mp3, extrayendo la letra y generando archivos de texto con sincronización temporal. Posteriormente, estos archivos pueden utilizarse para mostrar la letra de la canción en tiempo real mientras se reproduce, simulando una experiencia tipo karaoke.


#pip install pygame pillow mutagen


#############################################################################

Instalación de FFmpeg (Windows)
Ve al sitio oficial de descargas: https://ffmpeg.org/download.html

Descarga la versión correspondiente a tu sistema operativo (Windows).

Extrae el contenido del archivo .zip.

Copia la ruta de la carpeta bin del FFmpeg extraído.

Añade esta ruta a la variable de entorno PATH de tu sistema:

Abre el Panel de Control → Sistema y Seguridad → Sistema → Configuración avanzada del sistema → Variables de entorno.

En "Variables del sistema", selecciona Path → Editar → Nuevo → pega la ruta copiada → Aceptar.

###############################################################################



#Primero, ejecuta el script transcriptor.py

Se abrirá una ventana para que selecciones un archivo .mp3.
El script procesará el archivo y generará un archivo .txt con la letra y los tiempos de la canción seleccionada.

Una vez generado el archivo .txt, ejecuta el archivo principal:

    #main.py


Este script te permitirá:

Seleccionar la canción en formato .mp3.

Seleccionar el archivo .txt generado con la letra y los tiempos.

El programa reproducirá la canción mostrando la letra sincronizada en pantalla.
