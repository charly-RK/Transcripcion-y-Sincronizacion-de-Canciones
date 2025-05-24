import pygame
import time
import threading
import random
from mutagen.mp3 import MP3
import os

COLORES = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F06292', '#9575CD', '#64B5F6']

musica_pausada = False
tiempo_inicio = 0
tiempo_pausado = 0
duracion_total = 0
ruta_musica = ""
ruta_letra = ""
letra = []

def cargar_letra(ruta):
    datos = []
    with open(ruta, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            if linea.startswith("["):
                partes = linea.split("]")
                try:
                    tiempo = int(float(partes[0][1:]))
                    texto = partes[1].strip()
                    datos.append((tiempo, texto))
                except:
                    pass
    return datos

def cargar_musica(filedialog, elementos_ui):
    global ruta_musica, duracion_total, musica_pausada, tiempo_inicio, letra
    ruta_musica = filedialog.askopenfilename(filetypes=[("Archivos MP3", "*.mp3")])
    if ruta_musica:
        pygame.mixer.music.load(ruta_musica)
        audio = MP3(ruta_musica)
        duracion_total = audio.info.length
        elementos_ui['barra_progreso']['value'] = 0
        elementos_ui['btn_play'].config(state='normal')
        elementos_ui['lbl_titulo'].config(text=os.path.basename(ruta_musica).replace('.mp3', ''))
        reproducir_musica(elementos_ui)

def reproducir_musica(elementos_ui):
    global tiempo_inicio, musica_pausada, tiempo_pausado
    pygame.mixer.music.play()
    tiempo_inicio = time.time()
    tiempo_pausado = 0
    musica_pausada = False
    elementos_ui['btn_play'].config(text="⏸️ Pausar")
    threading.Thread(target=actualizar_tiempo, args=(elementos_ui,), daemon=True).start()

def toggle_play_pause(elementos_ui):
    global musica_pausada, tiempo_inicio, tiempo_pausado
    if musica_pausada:
        pygame.mixer.music.unpause()
        tiempo_inicio = time.time() - tiempo_pausado
        musica_pausada = False
        elementos_ui['btn_play'].config(text="⏸️ Pausar")
    else:
        pygame.mixer.music.pause()
        tiempo_pausado = time.time() - tiempo_inicio
        musica_pausada = True
        elementos_ui['btn_play'].config(text="▶️ Reanudar")

def cambiar_volumen(valor):
    pygame.mixer.music.set_volume(float(valor) / 100)

def mostrar_subtitulos(letra, lbl_letra):
    global tiempo_inicio
    frase_actual = None
    while True:
        if pygame.mixer.music.get_busy() and not musica_pausada and letra:
            tiempo_actual = int(time.time() - tiempo_inicio)
            nueva_frase = None
            for i in range(len(letra)):
                if i + 1 < len(letra):
                    if letra[i][0] <= tiempo_actual < letra[i + 1][0]:
                        nueva_frase = letra[i][1]
                        break
                else:
                    if letra[i][0] <= tiempo_actual:
                        nueva_frase = letra[i][1]
            if nueva_frase and nueva_frase != frase_actual:
                frase_actual = nueva_frase
                lbl_letra.actualizar_letra(frase_actual)
        time.sleep(0.1)

def actualizar_tiempo(elementos_ui):
    global duracion_total
    while pygame.mixer.music.get_busy():
        if not musica_pausada:
            tiempo_transcurrido = time.time() - tiempo_inicio
            actualizar_barra_progreso(tiempo_transcurrido, elementos_ui)
            elementos_ui['lbl_tiempo'].config(
                text=f"{format_tiempo(tiempo_transcurrido)} / {format_tiempo(duracion_total)}"
            )
        time.sleep(1)

def format_tiempo(segundos):
    minutos, segundos = divmod(int(segundos), 60)
    return f"{minutos:02d}:{segundos:02d}"

def actualizar_barra_progreso(tiempo_actual, elementos_ui):
    if duracion_total > 0:
        progreso = (tiempo_actual / duracion_total) * 100
        elementos_ui['barra_progreso']['value'] = progreso

def on_progress_click(event, barra_progreso, elementos_ui):
    global tiempo_inicio, tiempo_pausado
    if duracion_total > 0:
        x = event.x
        ancho = barra_progreso.winfo_width()
        porcentaje = x / ancho
        nuevo_tiempo = porcentaje * duracion_total
        pygame.mixer.music.set_pos(nuevo_tiempo)
        tiempo_inicio = time.time() - nuevo_tiempo
        tiempo_pausado = nuevo_tiempo
        actualizar_barra_progreso(nuevo_tiempo, elementos_ui)
