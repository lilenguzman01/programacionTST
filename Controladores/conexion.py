import mysql.connector
try:
    miBase = mysql.connector.connect( 
        host='localhost',
        port=3306,
        user='root',
        password='dino94',
        db='bbdd_bienes_raices_future'
    )
    if miBase.is_connected(): #si se conecto a la base de datos  imprimo mensaje "conexion exitosa"
        print("conexion exitosa")

except:
    print("conexion fallida")#si no se conecto a la base de datos imprimo el mensaje "conexion fallida"

print(miBase) 
cursor = miBase.cursor()#creo objeto cursor
cursor.execute("SHOW TABLES")
for i in cursor:
    print(i)

cursor.execute("SELECT * FROM cliente")
resultado=cursor.fetchall()
for i in resultado:
    print(i)

#cierro conexion
if miBase.is_connected():
    cursor.close()
    miBase.close()
    print("cierro conexion")