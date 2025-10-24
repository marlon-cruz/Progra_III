
import  mysql.connector
from kivy.geometry import circumcircle


class articulo:
    def abrir(self):
        conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="ugb01")
        return conexion1

    def guardar(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "insert into productos(nombre, precio) values (%s,%s)"
        cursor.excecute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT nombre, precio FROM `productos` where codigo = %s"
        cursor.excecute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.fetchall()

    def recuperar_todas(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT nombre, precio FROM `productos`"
        cursor.excecute(sql)
        cone.commit()
        cone.close()
        return cursor.fetchall()

    def baja(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "DELETE FROM `productos` WHERE codigo = %s"
        cursor.excecute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount()


    def modificar(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "UPDATE productos SET  nombre = %s, precio = %s WHERE codigo = %s"
        cursor.excecute(sql, datos)
        cone.commit()
        cone.close()
