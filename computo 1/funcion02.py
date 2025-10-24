import tkinter
import tkinter as tk
from os import get_blocking
from tkinter.messagebox import showerror


class Aplication:
    def __init__(self):
        def numero(self, numero):
            texto = self.calculo.cget('text')
            texto = texto + str(numero)
            self.calculo.configure(text=texto)
        #variables
        def limpiar():
            self.opciones = ""
            self.numero1 = 0
            self.numero2 = 0
            self.calculo.configure(text="")
        def opcion(self, opc):
            print(self.opciones)
            if self.opciones == "":
                self.opciones = opc
                self.numero1 = int( self.calculo.cget('text'))
                self.calculo.configure(text="")
            else:
                tk.messagebox.showerror("Error", "Ya existe una opcion seleccionada")

        def resultado(self,opc):
            match opc:
                case "+":
                    self.numero2 = int(self.calculo.cget('text'))
                    resultadoObtenido = str(self.numero1 + self.numero2)
                case "-":
                    self.numero2 = int(self.calculo.cget('text'))
                    resultadoObtenido = str(self.numero1 - self.numero2)
                case "/":
                    self.numero2 = int(self.calculo.cget('text'))
                    resultadoObtenido = str(self.numero1 / self.numero2)
                case "*":
                    self.numero2 = int(self.calculo.cget('text'))
                    resultadoObtenido = str(self.numero1 * self.numero2)
                case _:
                    resultadoObtenido = "No es posible calcularlo"
            self.calculo.configure(text = resultadoObtenido)


        self.opciones = ""
        self.numero1 = 0
        self.numero2 = 0
        #Ventana
        self.ventana = tk.Tk()
        self.ventana.title('Calculadora')
        self.ventana.geometry('600x400')
        #Titulo
        self.titulo = tk.Label(self.ventana, text='Calculadora', bg='#494d54', font= 'areal 30')
        self.titulo.pack(fill= tk.X)
        #mostrar el resultado
        self.calculo = tk.Label(self.ventana, text='', width= 20, background= 'blue', font='areal 10')
        self.calculo.configure(fg="white")
        self.calculo.pack(padx=10, pady=10)

        #calculadora
        self.frame = tk.Frame(self.ventana, bg="lightgrey", width= 500, height=200, background='blue')
        self.frame.pack(padx=10, pady=10)

        self.numero1 = 0
        self.numero1 = 0

        #numeros ha calcular
        self.boton1 = tk.Button(self.frame, width= 5, height=3, text= '1', command= lambda: numero(self,1) )
        self.boton1.grid(row=3, column= 0,padx= 5, pady= 5)
        self.boton2 = tk.Button(self.frame, width= 5, height=3, text= '2', command= lambda: numero(self,2) )
        self.boton2.grid(row=3, column= 1 ,padx= 5, pady= 5)
        self.boton3 = tk.Button(self.frame, width= 5, height=3, text= '3', command= lambda: numero(self,3) )
        self.boton3.grid(row=3, column= 2 ,padx= 5, pady= 5)
        self.boton4 = tk.Button(self.frame, width= 5, height=3, text= '4', command= lambda: numero(self,4) )
        self.boton4.grid(row=2, column= 0 ,padx= 5, pady= 5)
        self.boton5 = tk.Button(self.frame, width=5, height=3, text='5', command= lambda: numero(self,5) )
        self.boton5.grid(row=2, column=1 ,padx= 5, pady= 5)
        self.boton6 = tk.Button(self.frame, width=5, height=3, text='6', command= lambda: numero(self,6) )
        self.boton6.grid(row=2, column=2 ,padx= 5, pady= 5)
        self.boton7 = tk.Button(self.frame, width=5, height=3, text='7', command= lambda: numero(self,7) )
        self.boton7.grid(row=1, column=0 ,padx= 5, pady= 5)
        self.boton8 = tk.Button(self.frame, width=5, height=3, text='8', command= lambda: numero(self,8) )
        self.boton8.grid(row=1, column=1 ,padx= 5, pady= 5)
        self.boton9 = tk.Button(self.frame, width=5, height=3, text='9', command= lambda: numero(self,9) )
        self.boton9.grid(row=1, column=2 ,padx= 5, pady= 5)
        self.boton0 = tk.Button(self.frame, width=5, height=3, text='0', command= lambda:numero(self,0)  )
        self.boton0.grid(row=4, column=0 ,padx= 5, pady= 5)
        #Opciones de calculo calculo
        self.suma = tk.Button(self.frame, width=5, height=3, text='+',command= lambda :opcion(self,"+"))
        self.suma.grid(row=1, column=3 ,padx= 5, pady= 5)
        self.resta = tk.Button(self.frame, width=5, height=3, text='-',command= lambda :opcion(self,"-"))
        self.resta.grid(row=2, column=3 ,padx= 5, pady= 5)
        self.multi = tk.Button(self.frame, width=5, height=3, text='*',command= lambda :opcion(self,"*"))
        self.multi.grid(row=3, column=3 ,padx= 5, pady= 5)
        self.div = tk.Button(self.frame, width=5, height=3, text='/',command= lambda : opcion(self,"/"))
        self.div.grid(row=4, column=3 ,padx= 5, pady= 5)
        self.resul = tk.Button(self.frame, width=5, height=3, text='=', command= lambda : resultado(self,self.opciones))
        self.resul.grid(row=4, column=2,padx= 5, pady= 5)
        self.resul = tk.Button(self.frame, width=5, height=3, text='C', command= limpiar)
        self.resul.grid(row=4, column=1,padx= 5, pady= 5)
        self.ventana.mainloop()
ejecutar = Aplication()