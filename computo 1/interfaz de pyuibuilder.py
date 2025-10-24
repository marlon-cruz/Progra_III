# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ventana1 = tk.Tk()
ventana1.title("Controles con ttk")
ventana1.config(bg="#E4E2E2")
ventana1.geometry("600x400")


style = ttk.Style(ventana1)
style.theme_use("clam")

style.configure("button3.TButton", background="#000000", foreground="#0bfbff")
style.map("button3.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button3 = ttk.Button(master=ventana1, text="Salir", style="button3.TButton", command= lambda : salir())
button3.place(x=506, y=318, width=80, height=40)

style.configure("button2.TButton", background="#000000", foreground="#ffffff")
style.map("button2.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button2 = ttk.Button(master=ventana1, text="Disminuir", style="button2.TButton",command= lambda : disminuir())
button2.place(x=243, y=222, width=113, height=44)

style.configure("button1.TButton", background="#000000", foreground="#ffffff")
style.map("button1.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

button1 = ttk.Button(master=ventana1, text="Aumentar", style="button1.TButton", command= lambda : aumentar())
button1.place(x=232, y=136, width=133, height=42)

style.configure("label1.TLabel", background="#ffffff", foreground="#fa1414", relief=tk.GROOVE, anchor="center")
label1 = ttk.Label(master=ventana1, text="0", style="label1.TLabel")
label1.configure(anchor="center")
label1.place(x=201, y=43, width=200, height=46)


def aumentar():
    valor = int(label1.cget("text"))
    valor = valor + 1
    label1.configure(text=valor)


def disminuir():
    valor = int(label1.cget("text"))
    valor = valor - 1
    label1.configure(text=valor)

def salir():
    exit()



ventana1.mainloop()