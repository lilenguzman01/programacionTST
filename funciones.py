from Controladores import conexion
import Modelos.OperatoriaComercial
import Modelos.Propiedad
#from Modelos import Propietario
import Modelos.Propietario
import Modelos.Tipo
import Modelos.Estado
from os import system #importo system para usar la funcion clear y limpiar la pantalla

conectar=conexion.conectar()#realizo conexion con la base de datos me retorna
                            # la base de datos y el cursor
baseDatos = conectar[0]# a baseDatos le asigno la base de datos que tiene el objeto conectar
cursor = conectar[1]# a cursor le asigno el cursor que tiene el objeto conectar

def cargarDatosPropiedad():
    system("cls") #limpio la pantalla
    idPropietario=consultaPropietario()
    idOperatoria=consultaOperatoria()

    
    

    #si hay propietarios le pregunto si quiere seleccionar
    # #si no hay le aviso que no hay propietarios 
    #o else si quiere cargar uno nuevo
def consultaOperatoria():#obtiene el id de la operatoria cpmercial que se quiere poner en 
    #la tabla propiedad
    system("cls") #limpio la pantalla
    

def consultaPropietario():#obtiene el id del propietario que se quiere poner en 
    #la tabla propiedad
    system("cls") #limpio la pantalla
    print("Ingresar Id del Propietario\n")
    nombresPropietarios = tuplaPropietarios()#pide el listado de los propietarios
    if len(nombresPropietarios) == 0:#no hay propietarios registrados
            print("No hay propietarios registrados. Debe cargar un Propietario para obtener el Id.")
            idPropietario=cargarNuevoPropietario()#carga un nuevo propietario
    else:#hay propietarios registrados
        opcion = int(input("""Existen Propietarios en la base de datos
        1- Seleccionar Propietario Existente, para utilizar su Id.
        2- Cargar un nuevo propietario, para utilizar su Id.
        """))
        if opcion == 1:
            idPropietario=seleccionarPropietarioExistente(nombresPropietarios)#selecciona el nombre de un propietario existente a la propiedad
        else:#cargo un nuevo propietario    
            idPropietario=cargarNuevoPropietario()
    return idPropietario

def maximoId():#retorna el maximo id de la tabla propietario
    
    if baseDatos.is_connected():#si hay conexion con la base de datos
        sentenciaId="select max(Id_Propietario) from propietario"#obtengo el id del nuevo propietario
        cursor.execute(sentenciaId)
        i=cursor.fetchone()
    return i[0]#retorna el valor almacenado en la posicion del indice 0

def listarPropietarios(nombresPropietarios):#muestra los propietarios cargados en la base de datos
    print("Listado de propietarios\n")
    if len(nombresPropietarios) == 0:#si no hay propietarios
            print("No hay propietarios registrados")
    else:#hay propietarios registrados. Muestro su id y nombre
        for i in nombresPropietarios:
            
            datosPropietarios = "Id Propietario: {0}-- Nombre: {1}"
            print(datosPropietarios.format(i[0],i[1]))
            
        print("\n")    

          
        
    
def tuplaPropietarios():#retorna el listado de propietarios
    if baseDatos.is_connected():#si hay conexion con la base de datos
            sentencia = "SELECT Id_Propietario,nombre FROM propietario ORDER BY Id_Propietario"#escribo sentencia sql
            cursor.execute(sentencia)
            nombresPropietarios = cursor.fetchall()# aca retorna una tupla
            
    return nombresPropietarios#retorna el listado de propietarios

def seleccionarPropietarioExistente(nombresPropietarios):#el usuario selecciona el id de un propietario
    #existente para cargar a la propiedad
    seguir = True
    while seguir:
        if baseDatos.is_connected():#si hay conexion con la base de datos
            listarPropietarios(nombresPropietarios)#muestra por panbtalla el listado de propietarios
            id = int(input("Seleccionar el Id de un Propietario: "))
            iMaximo=maximoId()#recibe el maximo numero de id que hay en la tabla propietrio
            
            if id<1 or id>iMaximo: #se fija si el id seleccionado esta een el rango de los id
                #que hay en tabla propietario 
                print("Opcion Incorrecta")#si el id seleccionado no es correcto
            else:
                seguir = False#el id propietariofue seleccionado correctamentre
                #corta el while
               

    return id #retorna el id seleccionado           

def cargarNuevoPropietario():#carga un nuevo propietario a la base de datos
    if baseDatos.is_connected():#si hay conexion con la base de datos
        nombre = input("Ingrese Nombre del Propietario: ")
        direccion = input("Ingrese Direccion del Propietario: ")
        contacto = input("Ingrese Contacto del Propietario: ")

        propie = Modelos.Propietario.Propietario(nombre, direccion, contacto)#creo el objeto propie 
        #perteneciente a la clase Propietario
              
        sentenciaSql="INSERT INTO propietario(nombre, direccion, contacto) VALUES('{0}','{1}','{2}')"#sentencia sql
        cursor.execute(sentenciaSql.format(propie.getNombre(),propie.getDireccion(),propie.getContacto()))
        baseDatos.commit()#agrego los cambios en la base de datos
        i=maximoId()
        print("Se Ingreso un Nuevo Propietario a la Tabla Propietario")
    return i    
#listadoPropietarios()

cargarDatosPropiedad()
#i=cargarNuevoPropietario()
