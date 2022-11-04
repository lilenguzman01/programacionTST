import mysql.connector

#realizo conexion 
def conectar():
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
        cursor = miBase.cursor(buffered=True)
        return [miBase, cursor]#retorno la base de datos y el cursor así puedo usarlos
    except:
        print("Conexion fallida. Error")#si no se conecto a la base de datos imprimo el mensaje "conexion fallida"


#cierro conexion
