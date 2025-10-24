from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class Cal(App):
    def build(self):
        self.ventana = GridLayout(cols= 2, padding =15, spacing = 10)
        self.titulo = Label(
            text="Resultado de la operacion",
            font_size = "20sp",
            halign = "center"
        )
        self.ventana.add_widget(self.titulo)

        self.resultado = Label(text = "0.00")
        self.ventana.add_widget(self.resultado)
        #Texbox+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #Label de numeros
        self.labeltext1 = Label(
            text="Numero 1",
            halign="right"
        )
        self.labelText2 = Label(
            text="Numero 2",
            halign="left"
        )
        self.ventana.add_widget(self.labeltext1)
        self.ventana.add_widget(self.labelText2)

        self.textbox1 = TextInput(multiline = False)
        self.textbox2 = TextInput(multiline = False)
        self.ventana.add_widget(self.textbox1)
        self.ventana.add_widget(self.textbox2)
        #RadioButton

        #Opcion 1 -------------------------------------------------------------------------------------------------------------------------
        self.labelOpc1 = Label(
            text="Suma",
            halign = "right"
        )
        self.opcCheck1 = CheckBox(

        group='opciones', active=False
        )
        self.opcCheck1.bind(
            on_press= lambda instance: self.seleccionado("suma")
        )
        self.ventana.add_widget(self.labelOpc1)
        self.ventana.add_widget(self.opcCheck1)
        # Opcion 2 -------------------------------------------------------------------------------------------------------------------------
        self.labelOpc2 = Label(
            text="resta",
            halign="right"
        )
        self.opcCheck2 = CheckBox(
            group='opciones', active=False
        )
        self.opcCheck2.bind(
            on_press= lambda instance: self.seleccionado("resta")
        )
        self.ventana.add_widget(self.labelOpc2)
        self.ventana.add_widget(self.opcCheck2)
        # Opcion 3 -------------------------------------------------------------------------------------------------------------------------
        self.labelOpc3 = Label(
            text="Multiplicación",
            halign="right"
        )
        self.opcCheck3 = CheckBox(
            group='opciones', active=False
        )
        self.opcCheck3.bind(
            on_press= lambda instance: self.seleccionado("multi")
        )
        self.ventana.add_widget(self.labelOpc3)
        self.ventana.add_widget(self.opcCheck3)
        # Opcion 4 -------------------------------------------------------------------------------------------------------------------------
        self.labelOpc4 = Label(
            text="Divición",
            halign="right"
        )
        self.opcCheck4 = CheckBox(
            group='opciones', active=False
        )
        self.opcCheck4.bind(
            on_press= lambda instance: self.seleccionado("div")
        )
        self.ventana.add_widget(self.labelOpc4)
        self.ventana.add_widget(self.opcCheck4)
        # boton calcular **********************************************************************************************

        self.calcular = Button(text="Calcular")
        self.calcular.bind(
            on_press= lambda instance: self.realizarCalculo("")
        )
        self.ventana.add_widget(self.calcular)
        self.precaucion = Label(text="")
        self.ventana.add_widget(self.precaucion)
        ################boton de salir#################
        self.salir = Button(text="Salir")
        self.salir.bind(
            on_press= self.stop
        )
        self.ventana.add_widget(self.salir)

        ########### Variables a utilizar
        self.opcionActual = ""
        self.numero1 = 0
        self.numero2 = 0


        return self.ventana

    def seleccionado(self,value):
        if self.opcionActual != value:
           self.opcionActual = value
        else:
            self.opcionActual = ""
            return


    def realizarCalculo(self,value):
        try:
            num1 = float(self.textbox1.text)
            num2 = float(self.textbox2.text)
            match self.opcionActual:
                case "suma":
                    self.resultado.text = str(num1 + num2)
                case "resta":
                    self.resultado.text = str(num1 - num2)
                case "multi":
                    self.resultado.text = str(num1 * num2)
                case "div":
                    self.resultado.text = str(num1 / num2)
                case _:
                    self.precaucion.text = "Se necesitan todos los datos para realizar la operación"
        except ValueError:
            self.precaucion.text = "Se necesitan todos los datos para realizar la operación"

if __name__ == "__main__":
    Cal().run()