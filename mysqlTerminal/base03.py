import  mysql.connector
conexion1 = mysql.connector.connect(host="localhost",user="root", passwd="", database = "db2")
cursor1 =  conexion1.cursor()

sql="UPDATE articulos SET  descripcion = %s, precio = %s WHERE Id = %s"

datos = ('telefono' ,2.,16)

cursor1.execute(sql,datos)
conexion1.commit()
conexion1.close()

print("Datos actualizados con exito", datos[0])