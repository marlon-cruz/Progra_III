import tkinter as tk


class Aplication:
    def __init__(self):
        #Etiqueta01
        self.formulario01 = tk.Tk()
        self.formulario01.title('Calculadora edad')
        self.formulario01.geometry('400x300')

        self.label01 = tk.Label(self.formulario01, text='ingrese el Año de nacimiento: ')
        self.label01.pack()

        self.dato01 = tk.StringVar()
        self.entry01 = tk.Entry(self.formulario01, width=10, textvariable= self.dato01)
        self.entry01.pack()

        self.label01 = tk.Label(self.formulario01, text='Resultado: ')
        self.label01.pack()

        self.boton01 = tk.Button(self.formulario01, text='Calcular', command= self.calcular)
        self.boton01.pack()
        # Etiqueta02
        self.formulario01.mainloop()

    def calcular(self):
        valor1 =int(self.dato01.get())
        resul = f'Resultado: {2025 - valor1}'
        self.label01.configure(text = resul + " Años")

ejecutar = Aplication()