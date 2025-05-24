import pygame
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from interfaz import LetraAnimada, configurar_estilo
import funciones as fx
import threading

pygame.init()
pygame.mixer.init()

root = tk.Tk()
root.title("🎶 Charly-RK ")
root.geometry("920x620")
root.configure(bg='#0d0d0d')
root.resizable(False, False)
configurar_estilo()

icono_img = ImageTk.PhotoImage(Image.open("recursos/imagen1.jpg"))
root.iconphoto(True, icono_img)

main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=25)

lbl_titulo = tk.Label(main_frame, text="🎵 Elige una canción", font=('Montserrat', 22, 'bold'),
                      bg='#0d0d0d', fg='white')
lbl_titulo.pack(pady=(0, 20))

lbl_letra = LetraAnimada(main_frame)
lbl_letra.config(font=('Segoe UI', 18), wraplength=850)
lbl_letra.pack(pady=20, fill=tk.BOTH, expand=True)

barra_progreso = ttk.Progressbar(main_frame, orient='horizontal', length=800, mode='determinate')
barra_progreso.pack(pady=10)

lbl_tiempo = tk.Label(main_frame, text="00:00 / 00:00", font=('Segoe UI', 10), bg='#0d0d0d', fg='#aaaaaa')
lbl_tiempo.pack()

control_frame = ttk.Frame(main_frame)
control_frame.pack(pady=30)

btn_cargar = ttk.Button(control_frame, text="📂 Cargar Música", command=lambda: fx.cargar_musica(filedialog, elementos_ui))
btn_cargar.grid(row=0, column=0, padx=12)

btn_play = ttk.Button(control_frame, text="▶️ Reproducir", command=lambda: fx.toggle_play_pause(elementos_ui), state='disabled')
btn_play.grid(row=0, column=1, padx=12)

btn_cargar_letra = ttk.Button(control_frame, text="📄 Cargar Letra", command=lambda: cargar_letra_y_mostrar())
btn_cargar_letra.grid(row=0, column=3, padx=12)

vol_frame = ttk.Frame(control_frame)
vol_frame.grid(row=0, column=2, padx=12)

tk.Label(vol_frame, text="🔊", font=('Segoe UI', 12), bg='#0d0d0d', fg='white').pack(side=tk.LEFT)

volumen = tk.Scale(vol_frame, from_=0, to=100, orient=tk.HORIZONTAL, command=fx.cambiar_volumen,
                   bg='#0d0d0d', fg='white', troughcolor='#333', highlightthickness=0,
                   sliderrelief='flat', length=120)
volumen.set(50)
volumen.pack(side=tk.LEFT)

elementos_ui = {
    'btn_play': btn_play,
    'lbl_titulo': lbl_titulo,
    'barra_progreso': barra_progreso,
    'lbl_tiempo': lbl_tiempo
}

def cargar_letra_y_mostrar():
    ruta = filedialog.askopenfilename(title="Selecciona el archivo de letra (.txt)", filetypes=[("Archivos de texto", "*.txt")])
    if ruta:
        fx.letra = fx.cargar_letra(ruta)
        lbl_letra.config(text="")
        threading.Thread(target=fx.mostrar_subtitulos, args=(fx.letra, lbl_letra), daemon=True).start()

barra_progreso.bind('<Button-1>', lambda e: fx.on_progress_click(e, barra_progreso, elementos_ui))

root.mainloop()
