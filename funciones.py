from Controladores import conexion
import Modelos.OperatoriaComercial
import Modelos.Propiedad
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
    print("Cargar Nueva Propiedad")
    idPropietario=consultaPropietario()
    idOperatoria=consultaOperatoria()
    idEstado=consultaEstado()
    idTipo=consultaTipo()
    nombre= input("Ingrese Nombre de la Propiedad:")
    direccion = input("Ingrese Direccion de la Propiedad:")
    contacto = input("Ingrese Contacto de la Propiedad:")

    nuevaPropiedad = Modelos.Propiedad.Propiedad(idTipo,idEstado,idOperatoria,idPropietario,nombre,direccion,contacto)
    cargarPropiedadBaseDatos(nuevaPropiedad)#carga la propiedad recien creadad a la base de datos

def cargarPropiedadBaseDatos(nuevaPropiedad):#carga la propiedad recien creadad a la base de datos
    system("cls")  # limpio la pantalla
    print("Cargando la Nueva Propiedad a la Base de Datos")
    if baseDatos.is_connected():  # si hay conexion con la base de datos
        sentenciaSql = "INSERT INTO propiedad(Nombre,Direccion,Contacto,Id_Tipo,Id_Estado,Id_Operatoria_Comercial,Id_Propietario) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}')"  # sentencia sql
        cursor.execute(sentenciaSql.format(nuevaPropiedad.get_Nombre(),nuevaPropiedad.getDireccion(),nuevaPropiedad.getContacto(),nuevaPropiedad.get_Id_Tipo(),nuevaPropiedad.get_Id_Estado(),nuevaPropiedad.get_Id_Operatoria_Comercial(),nuevaPropiedad.get_Id_Propietario()))
        baseDatos.commit()# agrego los cambios en la base de datos

        print("Se Cargo la Nueva Propiedad")

def consultaTipo():#obtiene el id del tipo que se quiere poner en
    #la tabla propiedad
    system("cls") #limpio la pantalla
    print("Cargar Tipo")
    tiposExistentes = tuplaTipos()#obtengo los tipos existentes en la base de datos

    if len(tiposExistentes) == 0:#no hay tipos registrados
            print("No hay Tipos registrados. Debe cargar un Tipo para obtener el Id.")
            idTipo=cargarNuevoTipo() #cargo un Nuevo Tipo
            print(idTipo)
            print("id idTipo")
    else:#hay Tipos registradas
        opcion = int(input("""Existen Tipos registrados en la base de datos
        1- Seleccionar Tipo  registrado para utilizar su Id.
        2- Cargar un Tipo, para utilizar su Id.
        """))
        if opcion == 1:
            idTipo=seleccionarTiposExistentes(tiposExistentes)  #selecciona el id de un tipo existente
        else:#cargo un Nuevo Tipo
            idTipo = cargarNuevoTipo()  # cargo un Nuevo Tipo

    return idTipo
def seleccionarTiposExistentes(tiposExistentes):#sseleccionar id de Tipo existente
    #para agregar a la propiedad
    print ("seleccionar Tipo Existente")
    seguir = True
    while seguir:
        if baseDatos.is_connected():  # si hay conexion con la base de datos
            listarOperatorias(tiposExistentes)  # muestra por panbtalla el listado de Tipo
            id = int(input("Seleccionar el Id de un Tipo Existente: "))
            iMaximo = maximoIdTipo()  # recibe el maximo numero de id que hay en la tabla tipo

            if id < 1 or id > iMaximo:  # se fija si el id seleccionado esta een el rango de los id
                # que hay en tabla Tipo
                print("Opcion Incorrecta")  # si el id seleccionado no es correcto
            else:
                seguir = False  # el id Tipo fue seleccionado correctamentre
                # corta el while

    return id  # retorna el id seleccionado

def maximoIdTipo():  # retorna el maximo id de la tabla Tipo

    if baseDatos.is_connected():  # si hay conexion con la base de datos
        sentenciaId = "select max(Id_Tipo) from tipo"  # obtengo el id
        # del ultimo tipo cargado
        cursor.execute(sentenciaId)
        i = cursor.fetchone()
    return i[0]  # retorna el valor almacenado en la posicion del indice 0


def cargarNuevoTipo(): #cargo un Nuevo Tipo

    print("Cargar Nuevo Tipo")
    if baseDatos.is_connected():  # si hay conexion con la base de datos
        nombre = input("Ingrese Nombre del Tipo: ")
        tipo = Modelos.Tipo.Tipo(nombre)  # creo el objeto tipo
        # perteneciente a la clase tipo
        sentenciaSql = "INSERT INTO tipo(Nombre_Tipo) VALUES('{0}')"  # sentencia sql
        cursor.execute(sentenciaSql.format(tipo.getNombre_Tipo()))
        baseDatos.commit()# agrego los cambios en la base de datos
        i = maximoIdOperatoria()
        print("Se Ingreso un Nuevo Tipo")
    return i

def tuplaTipos(): #obtengo los tipos existentes en la base de datos

    if baseDatos.is_connected():  # si hay conexion con la base de datos
        sentencia = "SELECT Id_Tipo,Nombre_Tipo FROM tipo ORDER BY Id_Tipo"  # escribo sentencia sql
        cursor.execute(sentencia)
        nombresTipos = cursor.fetchall()  # aca retorna una tupla

    return nombresTipos  # retorna el listado de los tipos


def consultaEstado():#obtiene el id del propietario que se quiere poner en 
    #la tabla propiedad
    #system("cls") #limpio la pantalla
    print("Ingresar Id del estado de la propiedad\n")
    nombresEstados = tuplaEstados()#pide el listado de los estados
    if len(nombresEstados) == 0:#no hay estados registrados
            print("No hay estados registrados.")
            idEstado=cargarNuevoEstado()#carga un nuevo estado (ejemplo: disponible, no disponible, disponible proximamente, etc)
    else:#hay estados registrados
        opcion = int(input("""Existen estados registrados en la base de datos
        1- Seleccionar estado Existente, para utilizar su Id.
        2- Cargar un nuevo estado, para utilizar su Id.
        """))
        if opcion == 1:
            idEstado=seleccionarEstadoExistente(nombresEstados)#selecciona el nombre de un estado existente a la propiedad
        else:#cargo un nuevo estado    
            idEstado=cargarNuevoEstado()
    return idEstado


def maximoIdEstado():#retorna el maximo id de la tabla estado
    
    if baseDatos.is_connected():#si hay conexion con la base de datos
        sentenciaIdEstado="select max(Id_Estado) from estado"#obtengo el id del nuevo estado
        cursor.execute(sentenciaIdEstado)
        i=cursor.fetchone()
    return i[0]#retorna el valor almacenado en la posicion del indice 0


def listarEstados(nombresEstados):#muestra los estados cargados en la base de datos
    print("Listado de estados\n")
    if len(nombresEstados) == 0:#si no hay estados
            print("No hay propietarios registrados")
    else:#hay estados registrados. Muestro su id y nombre
        for i in nombresEstados:
            
            datosEstado = "Id Estado: {0}-- Nombre: {1}"
            print(datosEstado.format(i[0],i[1]))
            
        print("\n")    



def tuplaEstados():#retorna el listado de estados
    if baseDatos.is_connected():#si hay conexion con la base de datos
            sentenciaEstado = "SELECT Id_Estado,Nombre_Estado FROM estado ORDER BY Id_Estado"#escribo sentencia sql
            cursor.execute(sentenciaEstado)
            nombresEstados = cursor.fetchall()# aca retorna una tupla
            
    return nombresEstados#retorna el listado de propietarios


def seleccionarEstadoExistente(nombresEstados):#el usuario selecciona el id de un estado
    #existente para cargar a la propiedad
    seguir = True
    while seguir:
        if baseDatos.is_connected():#si hay conexion con la base de datos
            listarPropietarios(nombresEstados)#muestra por pantalla el listado de estados
            id = int(input("Seleccionar el Id de un Estado: "))
            iMaximoEstado=maximoIdEstado()#recibe el maximo numero de id que hay en la tabla estado
            
            if id<1 or id>iMaximoEstado: #se fija si el id seleccionado esta en el rango de los id
                #que hay en tabla estado
                print("Opcion Incorrecta")#si el id seleccionado no es correcto
            else:
                seguir = False#el id estado fue seleccionado correctamentre
                #corta el while

    return id

def cargarNuevoEstado():#carga un nuevo estado a la base de datos
    if baseDatos.is_connected():#si hay conexion con la base de datos
        nombre = input("Ingrese Nombre del Estado: ")
        

        est = Modelos.Estado.Estado(nombre)#creo el objeto est
        #perteneciente a la clase estado
              
        sentenciaSqlEstado="INSERT INTO estado (Nombre_Estado) VALUES('{0}')"#sentencia sql
        cursor.execute(sentenciaSqlEstado.format(est.getNombre_Estado()))
        baseDatos.commit()#agrego los cambios en la base de datos
        i=maximoIdEstado()
        print("Se Ingreso un Nuevo Estado a la Tabla Estado")
    return i    
#
def consultaOperatoria():#obtiene el id de la operatoria comercial que se quiere poner en
    #la tabla propiedad
    system("cls") #limpio la pantalla
    print("Cargar Operatoria Comercial")
    operatoriasExistentes = tuplaOperatorias()#obtengo las operatorias comerciales
                                                # existentes en la base de datos
    if len(operatoriasExistentes) == 0:#no hay Operatorias Comerciales registradas
            print("No hay Operatorias Comerciales registradas. Debe cargar una Operatoria Comerciale para obtener el Id.")
            idOperatoria=cargarNuevaOperatoria() #cargo una nueva operatoria comercial
            print(idOperatoria)
            print("id nueva vacia")
    else:#hay Operatorias Comerciales registradas
        opcion = int(input("""Existen Operatorias Comerciales registradas en la base de datos
        1- Seleccionar Operatoria Comercial  registrada para utilizar su Id.
        2- Cargar una nueva Operatoria Comercial, para utilizar su Id.
        """))
        if opcion == 1:
            idOperatoria=seleccionarOperatoriaoExistente(operatoriasExistentes)#selecciona el id de una opertatoria existente
        else:#cargo una nueva operatoria comercial
            idOperatoria=cargarNuevaOperatoria()

    return idOperatoria
def cargarNuevaOperatoria():

    print("Cargar Nueva Operatoria")
    if baseDatos.is_connected():  # si hay conexion con la base de datos
        nombre = input("Ingrese Nombre de la Operatoria Comercial: ")
        operatoria = Modelos.OperatoriaComercial.OperatoriaComercial(nombre) # creo el objeto operatoria
        # perteneciente a la clase OperatoriaComercial
        print(operatoria.getNombre_Operatoria_Comercial())

        sentenciaSql = "INSERT INTO operatoriacomercial(Nombre_Operatoria_Comercial) VALUES('{0}')"  # sentencia sql
        cursor.execute(sentenciaSql.format(operatoria.getNombre_Operatoria_Comercial()))
        baseDatos.commit()# agrego los cambios en la base de datos
        i = maximoIdOperatoria()
        print("Se Ingreso una Nueva operatoria")
    return i


def maximoIdOperatoria():  # retorna el maximo id de la tabla Operatoria_Comercial

    if baseDatos.is_connected():  # si hay conexion con la base de datos
        sentenciaId = "select max(Id_Operatoria_Comercial) from operatoriacomercial"  # obtengo el id
        # de la ultima operatoria cargada
        cursor.execute(sentenciaId)
        i = cursor.fetchone()
    return i[0]  # retorna el valor almacenado en la posicion del indice 0


def seleccionarOperatoriaoExistente(operatoriasExistentes):#sseleccionar id de operatoria comercial existente
    #para agregar a la propiedad
    print ("seleccionar Operatoria Existente")
    seguir = True
    while seguir:
        if baseDatos.is_connected():  # si hay conexion con la base de datos
            listarOperatorias(operatoriasExistentes)  # muestra por panbtalla el listado de Operatoria Comercial
            id = int(input("Seleccionar el Id de una Operatoria Comercial: "))
            iMaximo = maximoIdOperatoria()  # recibe el maximo numero de id que hay en la tabla Operatoria Comercial

            if id < 1 or id > iMaximo:  # se fija si el id seleccionado esta een el rango de los id
                # que hay en tabla Operatoria Comercial
                print("Opcion Incorrecta")  # si el id seleccionado no es correcto
            else:
                seguir = False  # el id Operatoria Comercial fue seleccionado correctamentre
                # corta el while

    return id  # retorna el id seleccionado




def listarOperatorias(operatoriasExistentes):# muestra el listado de operatorias comerciales cargadas en la base de datos
    print("Operatorias Comerciales\n")
    if len(operatoriasExistentes) == 0:  # si no hay propietarios
        print("No hay Operatorias Comerciales registrados")
    else:  # hay Operatorias Comerciales registradas. Muestro su id y nombre
        for i in operatoriasExistentes:
            datosOperatorias = "Id Operatorias Comerciales: {0}-- Nombre: {1}"
            print(datosOperatorias.format(i[0], i[1]))

        print("\n")
def tuplaOperatorias(): #obtengo las operatorias cargadas en la base de datos

    if baseDatos.is_connected():  # si hay conexion con la base de datos
        sentencia = "SELECT Id_Operatoria_Comercial,Nombre_Operatoria_Comercial FROM operatoriacomercial ORDER BY Id_Operatoria_Comercial"  # escribo sentencia sql
        cursor.execute(sentencia)
        nombresOperatorias = cursor.fetchall()  # aca retorna una tupla

    return nombresOperatorias  # retorna el listado de las Operatorias Comerciales

def consultaPropietario():#obtiene el id del propietario que se quiere poner en 
    #la tabla propiedad
    #system("cls") #limpio la pantalla
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


def suprimirPropiedad():#borra una propiedad existente de la base de datos
    seguir = True
    while seguir:
        if baseDatos.is_connected():  # si hay conexion con la base de datos
            sentenciaListado="SELECT Id_Propiedad,Nombre,Direccion FROM propiedad"
            cursor.execute(sentenciaListado)
            listado=cursor.fetchall()# aca retorna una tupla
            listarPropiedades(listado)# muestra las Propiedades cargados en la base de datos
            maxIdPropiedad=maximoIdListadoPropiedades()# retorna el maximo id de la tabla propietario
            id=int(input("Seleccione el Id de una Propiedad:"))
            if id<0 or id>maxIdPropiedad:
                print("Id incorrecto")
            else:
                print("Se elimina la propiedad con Id: ")
                print(id)
                sentenciaEliminar="DELETE FROM propiedad WHERE Id_Propiedad={0}"
                cursor.execute(sentenciaEliminar.format(id))
                baseDatos.commit()#agrego los cambios en la base de datos
                seguir=False


def maximoIdListadoPropiedades():  # retorna el maximo id de la tabla propietario

    if baseDatos.is_connected():  # si hay conexion con la base de datos
        sentenciaId = "select max(Id_Propiedad) from propiedad"  # obtengo el id del nuevo propietario
        cursor.execute(sentenciaId)
        i = cursor.fetchone()
    return i[0]  # retorna el valor almacenado en la posicion del indice 0


def listarPropiedades(listado):  # muestra las Propiedades cargados en la base de datos
    print("Listado de Propiedades\n")

    if len(listado) == 0:  # si no hay propietarios
        print("No hay Propiedades registradas")
    else:  # hay Propiedades registradas. Muestro su id , nombre y direccion
        for i in listado:
            datosPropiedades = "Id Propiedad: {0}-- Nombre: {1}-- Dierección: {2}"
            print(datosPropiedades.format(i[0], i[1],i[2]))

        print("\n")


def actualizarPropiedad():#actuaqliza la propiedad de la base de datos
    seguir = True
    while seguir:
        if baseDatos.is_connected():  # si hay conexion con la base de datos
            sentenciaListado = "SELECT Id_Propiedad,Nombre,Direccion FROM propiedad"
            cursor.execute(sentenciaListado)
            listado = cursor.fetchall()  # aca retorna una tupla
            listarPropiedades(listado)  # muestra las Propiedades cargados en la base de datos
            maxIdPropiedad = maximoIdListadoPropiedades()  # retorna el maximo id de la tabla propietario
            id = int(input("Seleccione el Id de una Propiedad:"))
            if id < 0 or id > maxIdPropiedad:
                print("Id incorrecto")
            else:
                print("Se Modifica la propiedad con Id: ")
                print(id)
                nombre=input("Ingrese Nuevo Nombre de la Propiedad")
                sentenciaActualizar = "UPDATE propiedad SET Nombre='{0}'where Id_Propiedad='{1}'"
                cursor.execute(sentenciaActualizar.format(nombre,id))
                baseDatos.commit()  # agrego los cambios en la base de datos
                print("Se Actualizo la Propiedad")
                seguir = False

  
def muestraPropiedad():
    if baseDatos.is_connected():  # si hay conexion con la base de datos
        sentenciaListado="SELECT Id_Propiedad,Nombre,Direccion FROM propiedad"
        cursor.execute(sentenciaListado)
        listado=cursor.fetchall()# aca retorna una tupla
        print(listarPropiedades(listado))# muestra las Propiedades cargados en la base de datos
  

def propDisponibleVenta():#PROPIEDADES DISPONIBLES PARA LA VENTA
    if baseDatos.is_connected():  # si hay conexion con la base de datos
        sentenciaListado="SELECT Nombre_Estado, Nombre_Tipo, P.Nombre, P.Direccion, P.Contacto, OPC.Nombre_Operatoria_Comercial FROM propiedad Pr inner join estado E on  Pr.Id_Estado=E.Id_Estado inner join Propietario P on Pr.Id_Propietario=P.Id_Propietario inner join tipo T on Pr.Id_Tipo=T.Id_Tipo INNER JOIN operatoriacomercial OPC on Pr.Id_Operatoria_Comercial=OPC.Id_Operatoria_Comercial Where Nombre_Operatoria_Comercial = 'venta' and Nombre_Estado ='Disponible'"
        cursor.execute(sentenciaListado)
        listado=cursor.fetchall()# aca retorna una tupla
        print(listarPropiedades(listado))# muestra las Propiedades cargados en la base de datos
  
def propDisponibleAlquiler():#PROPIEDADES DISPONIBLES PARA ALQUILER
    if baseDatos.is_connected():  # si hay conexion con la base de datos
        sentenciaListado="SELECT Nombre_Estado, Nombre_Tipo, P.Nombre, P.Direccion, P.Contacto, OPC.Nombre_Operatoria_Comercial FROM propiedad Pr inner join estado E on  Pr.Id_Estado=E.Id_Estado inner join Propietario P on Pr.Id_Propietario=P.Id_Propietario inner join tipo T on Pr.Id_Tipo=T.Id_Tipo INNER JOIN operatoriacomercial OPC on Pr.Id_Operatoria_Comercial=OPC.Id_Operatoria_Comercial Where Nombre_Operatoria_Comercial = 'alquiler' and Nombre_Estado ='Disponible'"
        cursor.execute(sentenciaListado)
        listado=cursor.fetchall()# aca retorna una tupla
        print(listarPropiedades(listado))# muestra las Propiedades cargados en la base de datos  

def propNoDisponibleAlquiler():#PROPIEDADES  NO DISPONIBLES PARA ALQUILER
    if baseDatos.is_connected():  # si hay conexion con la base de datos
        sentenciaListado="SELECT Nombre_Estado, Nombre_Tipo, P.Nombre, P.Direccion, P.Contacto, OPC.Nombre_Operatoria_Comercial FROM propiedad Pr inner join estado E on  Pr.Id_Estado=E.Id_Estado inner join Propietario P on Pr.Id_Propietario=P.Id_Propietario inner join tipo T on Pr.Id_Tipo=T.Id_Tipo INNER JOIN operatoriacomercial OPC on Pr.Id_Operatoria_Comercial=OPC.Id_Operatoria_Comercial Where Nombre_Operatoria_Comercial = 'alquiler' and Nombre_Estado ='NoDisponible'"
        cursor.execute(sentenciaListado)
        listado=cursor.fetchall()# aca retorna una tupla
        print(listarPropiedades(listado))# muestra las Propiedades cargados en la base de datos           
 
def propNoDisponibleVenta():#PROPIEDADES  NO DISPONIBLES PARA VENTA
    if baseDatos.is_connected():  # si hay conexion con la base de datos
        sentenciaListado="SELECT Nombre_Estado, Nombre_Tipo, P.Nombre, P.Direccion, P.Contacto, OPC.Nombre_Operatoria_Comercial FROM propiedad Pr inner join estado E on  Pr.Id_Estado=E.Id_Estado inner join Propietario P on Pr.Id_Propietario=P.Id_Propietario inner join tipo T on Pr.Id_Tipo=T.Id_Tipo INNER JOIN operatoriacomercial OPC on Pr.Id_Operatoria_Comercial=OPC.Id_Operatoria_Comercial Where Nombre_Operatoria_Comercial = 'Venta' and Nombre_Estado ='NoDisponible'"
        cursor.execute(sentenciaListado)
        listado=cursor.fetchall()# aca retorna una tupla
        print(listarPropiedades(listado))# muestra las Propiedades cargados en la base de datos

    #################################################################################


