import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *



class Aplication:
    def __init__(self):
        self.valor = 1
        self.ventana1 = tk.Tk()
        self.ventana1.title("Controles con ttk")
        self.ventana1.geometry("600x400")
        self.label = ttk.Label(self.ventana1, text= self.valor)
        self.label.grid(column=0,row=0)
        self.label.configure(foreground= "#5e4bb3")
        self.boton1 = ttk.Button(self.ventana1, text= "Aumentar", command= self.aumentar)
        self.boton1.grid(column= 0, row= 1)
        self.boton2 = ttk.Button(self.ventana1, text= "Disminuir", command= self.disminuir)
        self.boton2.grid(column= 0, row= 2)


        self.ventana1.mainloop()
    def aumentar(self):
        self.valor = self.valor+1
        self.label.configure(text= self.valor)
    def disminuir(self):
        self.valor = self.valor-1
        self.label.configure(text= self.valor)




inciar = Aplication()

