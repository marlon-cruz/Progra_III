import tkinter as tk


class Aplication:
    def __init__(self):
        #Etiqueta01
        self.formulario01 = tk.Tk()
        self.formulario01.title('operaciones basicas')
        self.formulario01.geometry('400x600')

        self.label01 = tk.Label(self.formulario01, text='ingrese el numero: ')
        self.label01.grid(column=0,row=0)

        self.dato01 = tk.StringVar()
        self.entry01 = tk.Entry(self.formulario01, width=10, textvariable= self.dato01)
        self.entry01.grid(column=0,row=1)

        self.label01 = tk.Label(self.formulario01, text='ingrese el numero: ')
        self.label01.grid(column=0, row=2)

        self.dato02 = tk.StringVar()
        self.entry02 = tk.Entry(self.formulario01, width=10, textvariable=self.dato02)
        self.entry02.grid(column=0, row=3)

        self.boton01 = tk.Button(self.formulario01, text='Multiplicar', command= self.calcular)
        self.boton01.grid(column=0,row=4)
        # Etiqueta02

        self.label02 = tk.Label(self.formulario01, text= 'Resultado: ')
        self.label02.grid(column=0, row=5)
        self.formulario01.mainloop()

    def calcular(self):
        valor1 =int(self.dato01.get())
        valor2 = int(self.dato02.get())
        resul = f'Resultado: {valor1 * valor2}'
        self.label02.configure(text = resul)

ejecutar = Aplication()