import tkinter as tk
from logging import disable
from tkinter import ttk
from tkinter import messagebox as mb
import empleados
class EmpleadosForm:
    def __init__(self):
        self.empleados = empleados.EmpleadosDatos()
        self.ventana1 = tk.Tk()
        self.ventana1.title("Gestin de Empleados")
        self.ventana1.geometry("600x400")
        self.ventana1.config(bg= "#0066ff")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        #Aquí se colocan las funciones que despliega cada frame
        self.nuevoEmpleado()
        self.mostrarEmpleado()
        self.editarEmpleadoForm()
        self.eliminarEmpleadoFrom()
        self.cuaderno1.grid(column=0, row=0, padx=20, pady=20)
        self.ventana1.mainloop()

    def nuevoEmpleado(self):
        self.frameNuevoEmpleado = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.frameNuevoEmpleado, text="Nuevo Empleado")
        self.labelframeNuevo = ttk.LabelFrame(self.frameNuevoEmpleado, text="Empleado")
        self.labelframeNuevo.grid(column=0, row=0, padx=5, pady=10)
        #label e input para nombre
        self.NuevoNombre = ttk.Label(self.labelframeNuevo, text="Nombre:")
        self.NuevoNombre.grid(column=0, row=0, padx=4, pady=4)
        self.varNombre = tk.StringVar()
        self.entryNombre = ttk.Entry(self.labelframeNuevo, textvariable=self.varNombre)
        self.entryNombre.grid(column=1, row=0, padx=4, pady=4)
        # label e input para apellido P
        self.NuevoApellidoP = ttk.Label(self.labelframeNuevo, text="Apellido paterno:")
        self.NuevoApellidoP.grid(column=0, row=1, padx=4, pady=4)
        self.varApellidoP = tk.StringVar()
        self.entryApellidoP = ttk.Entry(self.labelframeNuevo, textvariable=self.varApellidoP)
        self.entryApellidoP.grid(column=1, row=1, padx=4, pady=4)
        # label e input para apellido M
        self.NuevoApellidoM = ttk.Label(self.labelframeNuevo, text="Apellido Materno:")
        self.NuevoApellidoM.grid(column=0, row=2, padx=4, pady=4)
        self.varApellidoM = tk.StringVar()
        self.entryApellidoM = ttk.Entry(self.labelframeNuevo, textvariable=self.varApellidoM)
        self.entryApellidoM.grid(column=1, row=2, padx=4, pady=4)
        # label e input para email
        self.NuevoEmail = ttk.Label(self.labelframeNuevo, text="Email:")
        self.NuevoEmail.grid(column=0, row=3, padx=4, pady=4)
        self.varEmail = tk.StringVar()
        self.entryEmail = ttk.Entry(self.labelframeNuevo, textvariable=self.varEmail)
        self.entryEmail.grid(column=1, row=3, padx=4, pady=4)
        # label e date para fechaContrato
        self.NuevoContrato = ttk.Label(self.labelframeNuevo, text="Fecha contrato: (2025-12-31)")
        self.NuevoContrato.grid(column=0, row=4, padx=4, pady=4)
        self.varDate = tk.StringVar()
        self.entryDate = ttk.Entry(self.labelframeNuevo, textvariable=self.varDate)
        self.entryDate.grid(column=1, row=4, padx=4, pady=4)
        # label e input para notas
        self.Nuevonotas = ttk.Label(self.labelframeNuevo, text="Notas: ")
        self.Nuevonotas.grid(column=0, row=5, padx=4, pady=4)
        self.varnotas = tk.StringVar()
        self.entryNotas = tk.Text(self.labelframeNuevo, wrap='word',height=4, width= 20)
        self.entryNotas.grid(column=1, row=5, padx=4, pady=4)
        #Boton para insertar datos
        self.boton1 = ttk.Button(self.labelframeNuevo, text="Guardar", command=self.insertarNuevoEmpleado)
        self.boton1.grid(column=1, row=6, padx=4, pady=4)



    def insertarNuevoEmpleado(self):
        try:
            datos = (self.varNombre.get(),
                     self.varApellidoP.get(),
                     self.varApellidoM.get(),
                     self.varEmail.get(),
                     self.varDate.get(),
                     self.entryNotas.get('1.0', 'end-1c')
                     )
            self.empleados.insertar(datos)
            mb.showinfo("Información", "Datos de empleado Guardado")
            self.varNombre.set("")
            self.varApellidoP.set("")
            self.varApellidoM.set("")
            self.varEmail.set("")
            self.varDate.set("")
            self.mostrarentryNotas.delete('1.0', tk.END)
        except():
            mb.showerror("Error al agregar los datos", "Los datos no mudieron ser cargados")

    def mostrarEmpleado(self):
        self.framemostrarEmpleado = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.framemostrarEmpleado, text="mostrar Empleado")
        self.labelframemostrar = ttk.LabelFrame(self.framemostrarEmpleado, text="Empleado")
        self.labelframemostrar.grid(column=0, row=0, padx=5, pady=10)
        #ID para el text variable
        self.mostrarId = ttk.Label(self.labelframemostrar, text="ID:")
        self.mostrarId.grid(column=0, row=0, padx=4, pady=4)
        self.varMostrarId = tk.StringVar()
        self.mostrarentryNombre = ttk.Entry(self.labelframemostrar, textvariable=self.varMostrarId)
        self.mostrarentryNombre.grid(column=1, row=0, padx=4, pady=4)
        #label e input para nombre
        self.mostrarNombre = ttk.Label(self.labelframemostrar, text="Nombre:")
        self.mostrarNombre.grid(column=0, row=1, padx=4, pady=4)
        self.varMostrarNombre = tk.StringVar()
        self.mostrarentryNombre = ttk.Entry(self.labelframemostrar, textvariable=self.varMostrarNombre, state= 'disabled')
        self.mostrarentryNombre.grid(column=1, row=1, padx=4, pady=4)
        # label e input para apellido P
        self.mostrarApellidoP = ttk.Label(self.labelframemostrar, text="Apellido paterno:")
        self.mostrarApellidoP.grid(column=0, row=2, padx=4, pady=4)
        self.varMostrarApellidoP = tk.StringVar()
        self.mostrarentryApellidoP = ttk.Entry(self.labelframemostrar, textvariable=self.varMostrarApellidoP, state= 'disabled')
        self.mostrarentryApellidoP.grid(column=1, row=2, padx=4, pady=4)
        # label e input para apellido M
        self.mostrarApellidoM = ttk.Label(self.labelframemostrar, text="Apellido Materno:")
        self.mostrarApellidoM.grid(column=0, row=3, padx=4, pady=4)
        self.varMostrarApellidoM = tk.StringVar()
        self.mostrarentryApellidoM = ttk.Entry(self.labelframemostrar, textvariable=self.varMostrarApellidoM, state= 'disabled')
        self.mostrarentryApellidoM.grid(column=1, row=3, padx=4, pady=4)
        # label e input para email
        self.mostrarEmail = ttk.Label(self.labelframemostrar, text="Email:")
        self.mostrarEmail.grid(column=0, row=4, padx=4, pady=4)
        self.varMostrarEmail = tk.StringVar()
        self.mostrarentryEmail = ttk.Entry(self.labelframemostrar, textvariable=self.varMostrarEmail, state= 'disabled')
        self.mostrarentryEmail.grid(column=1, row=4, padx=4, pady=4)
        # label e date para fechaContrato
        self.mostrarContrato = ttk.Label(self.labelframemostrar, text="Fecha contrato: (2025-12-31)")
        self.mostrarContrato.grid(column=0, row=5, padx=4, pady=4)
        self.varMostrarDate = tk.StringVar()
        self.mostrarentryDate = ttk.Entry(self.labelframemostrar, textvariable=self.varMostrarDate, state= 'disabled')
        self.mostrarentryDate.grid(column=1, row=5, padx=4, pady=4)
        # label e input para notas
        self.mostrarnotas = ttk.Label(self.labelframemostrar, text="Notas: ")
        self.mostrarnotas.grid(column=0, row=6, padx=4, pady=4)
        self.varMostrarnotas = tk.StringVar()
        self.mostrarentryNotas = tk.Text(self.labelframemostrar, wrap='word',height=4, width= 20, state= 'disabled')
        self.mostrarentryNotas.config(state="disabled")
        self.mostrarentryNotas.grid(column=1, row=6, padx=4, pady=4)
        #Boton para mostrar datos
        self.boton1 = ttk.Button(self.labelframemostrar, text="Consultar", command=self.insertarmostrarEmpleado)
        self.boton1.grid(column=1, row=7, padx=4, pady=4)

    def insertarmostrarEmpleado(self):
        try:
            datos = (self.varMostrarId.get())
            respuesta = self.empleados.mostrar(datos)
            self.mostrarentryNotas.config(state='normal')
            if len(respuesta) > 0:
                self.varMostrarNombre.set(respuesta[0][1])
                self.varMostrarApellidoP.set(respuesta[0][2])
                self.varMostrarApellidoM.set(respuesta[0][3])
                self.varMostrarEmail.set(respuesta[0][4])
                self.varMostrarDate.set(respuesta[0][5])
                self.mostrarentryNotas.delete('1.0', tk.END)
                self.mostrarentryNotas.insert('1.0', respuesta[0][6])
            else:
                mb.showinfo("Información", "No existe un artículo con dicho código")
            self.mostrarentryNotas.config(state="disabled")
        except():
            mb.showerror("Error al agregar los datos", "Los datos no mudieron ser cargados")
    def editarEmpleadoForm(self):
        self.frameeditarEmpleado = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.frameeditarEmpleado, text="Editar Empleado")
        self.labelframeeditar = ttk.LabelFrame(self.frameeditarEmpleado, text="Empleado")
        self.labelframeeditar.grid(column=0, row=0, padx=5, pady=10)
        #ID para el text variable
        self.editarId = ttk.Label(self.labelframeeditar, text="ID:")
        self.editarId.grid(column=0, row=0, padx=4, pady=4)
        self.vareditarId = tk.StringVar()
        self.editarentryNombre = ttk.Entry(self.labelframeeditar, textvariable=self.vareditarId)
        self.editarentryNombre.grid(column=1, row=0, padx=4, pady=4)
        #label e input para nombre
        self.editarNombre = ttk.Label(self.labelframeeditar, text="Nombre:")
        self.editarNombre.grid(column=0, row=1, padx=4, pady=4)
        self.vareditarNombre = tk.StringVar()
        self.editarentryNombre = ttk.Entry(self.labelframeeditar, textvariable=self.vareditarNombre )
        self.editarentryNombre.grid(column=1, row=1, padx=4, pady=4)
        # label e input para apellido P
        self.editarApellidoP = ttk.Label(self.labelframeeditar, text="Apellido paterno:")
        self.editarApellidoP.grid(column=0, row=2, padx=4, pady=4)
        self.vareditarApellidoP = tk.StringVar()
        self.editarentryApellidoP = ttk.Entry(self.labelframeeditar, textvariable=self.vareditarApellidoP )
        self.editarentryApellidoP.grid(column=1, row=2, padx=4, pady=4)
        # label e input para apellido M
        self.editarApellidoM = ttk.Label(self.labelframeeditar, text="Apellido Materno:")
        self.editarApellidoM.grid(column=0, row=3, padx=4, pady=4)
        self.vareditarApellidoM = tk.StringVar()
        self.editarentryApellidoM = ttk.Entry(self.labelframeeditar, textvariable=self.vareditarApellidoM )
        self.editarentryApellidoM.grid(column=1, row=3, padx=4, pady=4)
        # label e input para email
        self.editarEmail = ttk.Label(self.labelframeeditar, text="Email:")
        self.editarEmail.grid(column=0, row=4, padx=4, pady=4)
        self.vareditarEmail = tk.StringVar()
        self.editarentryEmail = ttk.Entry(self.labelframeeditar, textvariable=self.vareditarEmail )
        self.editarentryEmail.grid(column=1, row=4, padx=4, pady=4)
        # label e date para fechaContrato
        self.editarContrato = ttk.Label(self.labelframeeditar, text="Fecha contrato: (2025-12-31)")
        self.editarContrato.grid(column=0, row=5, padx=4, pady=4)
        self.vareditarDate = tk.StringVar()
        self.editarentryDate = ttk.Entry(self.labelframeeditar, textvariable=self.vareditarDate )
        self.editarentryDate.grid(column=1, row=5, padx=4, pady=4)
        # label e input para notas
        self.editarnotas = ttk.Label(self.labelframeeditar, text="Notas: ")
        self.editarnotas.grid(column=0, row=6, padx=4, pady=4)
        self.vareditarnotas = tk.StringVar()
        self.editarentryNotas = tk.Text(self.labelframeeditar, wrap='word',height=4, width= 20 )
        self.editarentryNotas.grid(column=1, row=6, padx=4, pady=4)
        #Boton para editar datos
        self.boton1 = ttk.Button(self.labelframeeditar, text="Editar", command=self.editarempleado)
        self.boton1 = ttk.Button(self.labelframeeditar, text="Editar", command=self.editarempleado)
        self.boton1.grid(column=1, row=7, padx=4, pady=4)

    def editarempleado(self):
        try:
            datos = (
                     self.vareditarNombre.get(),
                     self.vareditarApellidoP.get(),
                     self.vareditarApellidoM.get(),
                     self.vareditarEmail.get(),
                     self.vareditarDate.get(),
                     self.editarentryNotas.get('1.0', 'end-1c'),
                     self.vareditarId.get()
                     )
            respuesta = self.empleados.editar(datos)
            print(datos)
            if  respuesta > 0:
                self.vareditarId.set("")
                self.vareditarNombre.set("")
                self.vareditarApellidoP.set("")
                self.vareditarApellidoM.set("")
                self.vareditarEmail.set("")
                self.vareditarDate.set("")
                self.editarentryNotas.delete('1.0', tk.END)
                mb.showinfo("Información", "Datos de empleado actualizados con exito")
            else:
                mb.showinfo("Información", "No existe un empleado con dicho identificador")
        except():
            mb.showerror("Error al modificar los datos", "Los datos no pudieron ser cargados")


    def eliminarEmpleadoFrom(self):
        self.frameeliminarEmpleado = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.frameeliminarEmpleado, text="eliminar Empleado")
        self.labelframeeliminar = ttk.LabelFrame(self.frameeliminarEmpleado, text="Empleado")
        self.labelframeeliminar.grid(column=0, row=0, padx=5, pady=10)
        #ID para el text variable
        self.eliminarId = ttk.Label(self.labelframeeliminar, text="ID:")
        self.eliminarId.grid(column=0, row=0, padx=4, pady=4)
        self.vareliminarId = tk.StringVar()
        self.eliminarentryID = ttk.Entry(self.labelframeeliminar, textvariable=self.vareliminarId)
        self.eliminarentryID.grid(column=1, row=0, padx=4, pady=4)

        #Boton para eliminar datos
        self.boton1 = ttk.Button(self.labelframeeliminar, text="Eliminar", command=self.eliminarEmpleado)
        self.boton1.grid(column=1, row=7, padx=4, pady=4)

    def eliminarEmpleado(self):
        try:
            datos = (self.vareliminarId.get())
            respuesta = self.empleados.eliminar(datos)
            if respuesta > 0:
                 self.vareliminarId.set("")
                 mb.showinfo("Información", "El empleado se ha eliminado exitosamente")
            else:
                 mb.showinfo("Información", "No existe un empleado con dicho identificador")
        except():
                 mb.showerror("Error al modificar los datos", "Los datos no pudieron ser cargados")
formEmpleados = EmpleadosForm()