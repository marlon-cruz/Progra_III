import  mysql.connector
conexion1 = mysql.connector.connect(host="localhost",user="root", passwd="", database = "db2")
cursor1 =  conexion1.cursor()

sql="insert into articulos(descripcion, precio) values (%s,%s)"

datos = ('queso', 2.00)

cursor1.execute(sql,datos)
conexion1.commit()


conexion1.close()

print("Se han guardado")