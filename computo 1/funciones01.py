import tkinter as tk
from gc import enable
from tkinter.messagebox import showerror

class Aplication:
    def __init__(self):
        def numero(self, numero):
            texto = self.viewResult.cget('text')
            texto = texto + str(numero)
            self.viewResult.configure(text=texto)
        def clear(self):
            self.viewResult.configure(text="")
            self.operador = ""
            self.numero1 = ""
            self.numero2 = ""
        def operador(self, op):
            if self.operador != "":
                tk.messagebox.showerror("ERROR", "No se puede elejir más de un operador")
            else:
                numero = self.viewResult.cget("text")
                self.numero1 = numero

                self.operador = op
                self.viewResult.configure(text="")

        def result(self):
            actual = self.viewResult.cget("text")
            self.numero2 = self.viewResult.cget("text")
            match self.operador:
                case "+":
                    resultado = str(int(self.numero1) + int(self.numero2))
                case "-":
                    resultado = str(int(self.numero1) - int(self.numero2))
                case "*":

                    resultado = str(int(self.numero1) * int(self.numero2))
                case "/":
                    resultado = str(int(self.numero1) / int(self.numero2))
                case _:
                    resultado = "No es posible Realizar la operacion"


            self.viewResult.configure(text= resultado)


        #variables
        self.operador = ""
        self.numero1 = ""
        self.numero2 = ""

        #configuracion de ventana
        self.ventana = tk.Tk()
        self.ventana.title("Un ejercicio de prueba")
        self.ventana.geometry('600x400')
        self.ventana.configure(bg= 'black')
        #configuracion de mostrar resultado
        self.viewResult = tk.Label(self.ventana,width= 20, font= 'Areal 20', background= 'white', text='')
        self.viewResult.pack(pady= 10, padx= 10)
        #configuracion del frame
        self.frame = tk.Frame(self.ventana, width= 400, height= 300)
        self.frame.pack(pady= 20)
        #configuracion de los botones
        self.boton1 = tk.Button(self.frame, width=3, height= 3, background= '#3738a1', text='1', font= 'areal 10', command= lambda :numero(self, 1))
        self.boton1.grid(column=1,row=3)
        self.boton2 = tk.Button(self.frame, width=3, height=3, background='#3738a1', text='2', font= 'areal 10',command= lambda :numero(self, 2))
        self.boton2.grid(column=2, row=3)
        self.boton3 = tk.Button(self.frame, width=3, height=3, background='#3738a1', text='3', font= 'areal 10',command= lambda :numero(self, 3))
        self.boton3.grid(column=3, row=3)
        self.boton4 = tk.Button(self.frame, width=3, height=3, background='#3738a1', text='4', font= 'areal 10',command= lambda :numero(self, 4))
        self.boton4.grid(column=1, row=2)
        self.boton5 = tk.Button(self.frame, width=3, height=3, background='#3738a1', text='5', font= 'areal 10',command= lambda :numero(self, 5))
        self.boton5.grid(column=2, row=2)
        self.boton6 = tk.Button(self.frame, width=3, height=3, background='#3738a1', text='6', font= 'areal 10',command= lambda :numero(self, 6))
        self.boton6.grid(column=3, row=2)
        self.boton7 = tk.Button(self.frame, width=3, height=3, background='#3738a1', text='7', font= 'areal 10',command= lambda :numero(self, 7))
        self.boton7.grid(column=1, row=1)
        self.boton8 = tk.Button(self.frame, width=3, height=3, background='#3738a1', text='8', font= 'areal 10',command= lambda :numero(self, 8))
        self.boton8.grid(column=2, row=1)
        self.boton9 = tk.Button(self.frame, width=3, height=3, background='#3738a1', text='9', font= 'areal 10',command= lambda :numero(self, 9))
        self.boton9.grid(column=3, row=1)
        self.boton0 = tk.Button(self.frame, width=3, height=3, background='#3738a1', text='0', font= 'areal 10',command= lambda :numero(self, 0))
        self.boton0.grid(column=2, row=4)

        #configuracion de opciones de operaciones
        self.suma = tk.Button(self.frame, width=3, height=3, background='#3738a1', text='+', font= 'areal 10',command= lambda :operador(self, "+"))
        self.suma.grid(column=4, row=1)
        self.resta = tk.Button(self.frame, width=3, height=3, background='#3738a1', text='-', font= 'areal 10',command= lambda :operador(self, "-"))
        self.resta.grid(column=4, row=2)
        self.div = tk.Button(self.frame, width=3, height=3, background='#3738a1', text='/', font= 'areal 10',command= lambda :operador(self, "/"))
        self.div.grid(column=4, row=3)
        self.multi = tk.Button(self.frame, width=3, height=3, background='#3738a1', text='*', font= 'areal 10',command= lambda :operador(self, "*"))
        self.multi.grid(column=4, row=4)
        self.clear = tk.Button(self.frame, width=3, height=3, background='#3738a1', text='C', font='areal 10',command= lambda :clear(self))
        self.clear.grid(column=1, row=4)

        self.clear = tk.Button(self.frame, width=3, height=3, background='#3738a1', text='=', font='areal 10', command=lambda: result(self))
        self.clear.grid(column=3, row=4)

        self.ventana.mainloop()



