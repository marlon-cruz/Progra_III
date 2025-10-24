import mysql.connector

class EmpleadosDatos:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost",
                                              user="root",
                                              passwd="",
                                              database="db2")
        return conexion

    def insertar(self,datos):
        try:
            conection = self.abrir()
            cursor = conection.cursor()
            sql = "insert into empleado(nombre, apellido_paterno,apellido_materno,email,fecha_contrato,notas ) values (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, datos)
            conection.commit()
            conection.close()
        except Exception as e:
            print(f"Error al cargar {e} con los datos {datos}")

    def mostrar(self, datos):
        try:
            conection=self.abrir()
            cursor=conection.cursor()
            sql= f"select * from empleado where empleado_id = {datos[0]}"
            cursor.execute(sql, datos)
            conection.close()
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al cargar {e} con los datos {datos[0]}")

    def editar(self, datos):
        try:
            conection = self.abrir()
            cursor = conection.cursor()
            sql = f"update empleado set nombre = %s, apellido_paterno = %s,apellido_materno = %s,email = %s,fecha_contrato = %s,notas = %s where empleado_id = %s"
            cursor.execute(sql, datos)
            print(cursor)
            conection.commit()
            conection.close()
            return cursor.rowcount
        except Exception as e:
            print(f"Error al cargar {e} con los datos {datos[0]}")
    def eliminar(self, datos):
        try:
            conection = self.abrir()
            cursor = conection.cursor()
            sql = f"Delete from empleado where empleado_id = {datos[0]}"
            cursor.execute(sql, datos)
            print(cursor)
            conection.commit()
            conection.close()
            return cursor.rowcount
        except Exception as e:
            print(f"Error al cargar {e} con los datos {datos[0]}")