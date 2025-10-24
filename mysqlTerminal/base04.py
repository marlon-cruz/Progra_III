import  mysql.connector
conexion1 = mysql.connector.connect(host="localhost",user="root", passwd="", database = "db2")
cursor1 =  conexion1.cursor()

sql="DELETE FROM `articulos` WHERE Id = 17"

cursor1.execute(sql)
conexion1.commit()
conexion1.close()
print("Datos Eliminados con exito")