# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ventana2 = tk.Tk()
ventana2.title("Controles TTK")
ventana2.config(bg="#000000")
ventana2.geometry("600x400")


style = ttk.Style(ventana2)
style.theme_use("clam")

radio_var = tk.IntVar()
style.configure("radio.TRadiobutton", background="#006573", foreground="#ffffff", borderwidth=3)
style.map("radio.TRadiobutton", background=[("active", "#943f68")], foreground=[("active", "#f8f8f8")])


radio_0 = ttk.Radiobutton(master=ventana2, variable=radio_var, text="Rojo", value=0, style="radio.TRadiobutton")
radio_0.place(x=256, y=42)


radio_1 = ttk.Radiobutton(master=ventana2, variable=radio_var, text="Azul", value=1, style="radio.TRadiobutton")
radio_1.place(x=256, y=66)


radio_2 = ttk.Radiobutton(master=ventana2, variable=radio_var, text="Amarillo", value=2, style="radio.TRadiobutton")
radio_2.place(x=256, y=90)

style.configure("button1.TButton", background="#000000", foreground="#13d0ff", borderwidth=5)
style.map("button1.TButton", background=[("active", "#364ea4")], foreground=[("active", "#4000ff")])

button1 = ttk.Button(master=ventana2, text="Cambiar", style="button1.TButton", command= lambda : cambioColor())
button1.place(x=255, y=166, width=80, height=40)

style.configure("button2.TButton", background="#2497d6", foreground="#ffffff")
style.map("button2.TButton", background=[("active", "#0300a7")], foreground=[("active", "#fdfdfd")])

button2 = ttk.Button(master=ventana2, text="Salir", style="button2.TButton", command= lambda : salir())
button2.place(x=253, y=240, width=80, height=40)


def cambioColor():
    match radio_var.get():
        case 0:
             ventana2.config(background="red")
        case 1:
            ventana2.config(background="blue")
        case 2:
            ventana2.config(background="yellow")

def salir():
    exit()


ventana2.mainloop()