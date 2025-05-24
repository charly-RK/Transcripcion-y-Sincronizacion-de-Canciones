import tkinter as tk
from tkinter import ttk
import random

COLORES = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F06292', '#9575CD', '#64B5F6']

class LetraAnimada(tk.Label):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.ultimo_texto = None
        self.config(bg='#121212', fg='white', font=('Consolas', 20), justify='center', anchor='center', wraplength=800)

    def actualizar_letra(self, texto):
        if texto != self.ultimo_texto:
            color = random.choice(COLORES)
            self.config(text=texto, fg=color)
            self.ultimo_texto = texto

def configurar_estilo():
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TFrame', background='#0d0d0d')
    style.configure('TButton',
                    font=('Segoe UI', 11, 'bold'),
                    foreground='white',
                    background='#1db954',
                    borderwidth=0,
                    focusthickness=0,
                    focuscolor='none',
                    padding=10)
    style.map('TButton',
              background=[('active', '#1ed760')],
              foreground=[('disabled', '#444')])
    style.configure('Horizontal.TProgressbar',
                    thickness=12,
                    troughcolor='#1a1a1a',
                    bordercolor='#1a1a1a',
                    background='#1db954',
                    lightcolor='#1db954',
                    darkcolor='#1db954')
