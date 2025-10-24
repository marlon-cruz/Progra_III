import os
import tkinter as tk
from tkinter import ttk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Proyecto")
main.config(bg="#E4E2E2")
main.geometry("700x400")


style = ttk.Style(main)
style.theme_use("clam")

txtnum1 = tk.Label(master=main, text="Ingrese un numero")
txtnum1.config(bg="#ffffff", fg="#000", font=("Arial", 13, ), cursor="circle")
txtnum1.place(x=273, y=37, width=186, height=40)

style.configure("btn2.TButton", background="#E4E2E2", foreground="#000")
style.map("btn2.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

btn2 = ttk.Button(master=main, text="Salir", style="btn2.TButton")
btn2.place(x=432, y=204)

style.configure("btn1.TButton", background="#E4E2E2", foreground="#000")
style.map("btn1.TButton", background=[("active", "#E4E2E2")], foreground=[("active", "#000")])

btn1 = ttk.Button(master=main, text="Ejecutar", style="btn1.TButton")
btn1.place(x=221, y=203, width=80, height=40)

style.configure("num1.TEntry", fieldbackground="#fff", foreground="#000")

num1 = ttk.Entry(master=main, style="num1.TEntry")
num1.place(x=302, y=96, width=130, height=40)


main.mainloop()