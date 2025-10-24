import tkinter as tk


class Aplication:
    def __init__(self):
        #Etiqueta01
        self.formulario01 = tk.Tk()
        self.formulario01.title('Nota del computo')
        self.formulario01.geometry('400x300')

        self.label01 = tk.Label(self.formulario01, text='ingrese la nota del primer laboratorio: ')
        self.label01.pack()
        self.dato01 = tk.StringVar()
        self.entry01 = tk.Entry(self.formulario01, width=10, textvariable= self.dato01)
        self.entry01.pack()

        self.label02 = tk.Label(self.formulario01, text='ingrese la nota del segundo laboratorio: ')
        self.label02.pack()
        self.dato02 = tk.StringVar()
        self.entry02 = tk.Entry(self.formulario01, width=10, textvariable=self.dato02)
        self.entry02.pack()

        self.label03 = tk.Label(self.formulario01, text='ingrese la nota del parcial: ')
        self.label03.pack()
        self.dato03= tk.StringVar()
        self.entry03 = tk.Entry(self.formulario01, width=10, textvariable=self.dato03)
        self.entry03.pack()


        self.label01 = tk.Label(self.formulario01, text='Nota final de computo: 0.0 ')
        self.label01.pack()

        self.boton01 = tk.Button(self.formulario01, text='Calcular', command= self.calcular)
        self.boton01.pack()
        # Etiqueta02
        self.formulario01.mainloop()

    def calcular(self):
        valor1 =float(self.dato01.get())
        valor2 =float(self.dato02.get())
        valor3 =float(self.dato03.get())

        resul = f': {(valor1 * 0.3) + (valor2 * 0.3) + (valor3 * 0.4)}'
        self.label01.configure(text = f"Nota final de computo: {resul}")

ejecutar = Aplication()