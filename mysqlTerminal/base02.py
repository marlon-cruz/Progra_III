
import  mysql.connector
conexion1 = mysql.connector.connect(host="localhost",user="root", passwd="", database = "db2")
cursor1 =  conexion1.cursor()

cursor1.execute("SELECT * FROM `articulos` ")

for articulo in cursor1:
    print(articulo)


conexion1.close()