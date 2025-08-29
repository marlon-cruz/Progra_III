import tkinter as tk
from tokenize import blank_re


class Aplication:
    def __init__(self):
        self.valor = 1
        self.ventana01 = tk.Tk()
        self.ventana01.geometry('600x400')
        self.ventana01.title('botones')
        self.ventana01.configure(background='white')

        self.label01 = tk.Label(self.ventana01, text= self.valor)
        self.label01.grid(column=5, row=1)
        self.label01.configure(foreground= 'red')

        self.buton01 = tk.Button(self.ventana01, text = 'Suma', command = self.sumar)
        self.buton01.grid(column = 1, row = 2)


        self.buton01 = tk.Button(self.ventana01, text='Resta', command=self.resta)
        self.buton01.grid(column=3, row=2)
        self.ventana01.mainloop()

    def sumar(self):
        self.valor = self.valor + 1
        self.label01.configure(text= self.valor)
    def resta(self):
        self.valor = self.valor-1
        self.label01.configure(text = self.valor)



