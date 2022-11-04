from os import system #importo system para usar la funcion clear y limpiar la pantalla
from Controladores import Conexion
import Modelos.OperatoriaComercial
import Modelos.Propiedad
import Modelos.Propietario
import Modelos.Tipo
import Modelos.Estado
import funciones
conectar=Conexion.conectar()#realizo conexion con la base de datos me retorna
                            # la base de datos y el cursor
baseDatos = conectar[0]# a baseDatos le asigno la base de datos que tiene el objeto conectar
cursor = conectar[1]# a cursor le asigno el cursor que tiene el objeto conectar

def cerrarConexion():#cierro la conexion con la base de datos y cierro el cursor
    baseDatos.close()
    cursor.close()

def ingresarPropiedad():#metodo que ingresa una propiedad a la base de datos
    if baseDatos.is_connected():#si hay conexion con la base de datos
            propiedad = funciones.cargarDatosPropiedad()#metodo que solicita al usuario que ingrese datos 
                                        #de la propiedad(nombre, direccion, contacto )

def menuPrincipal():
    system("cls") #limpio la pantalla
    continuar = True#cuando es false quiere decir que el usuario quiere cerrar el programa
    while(continuar):#se muestra el menu por pantalla hasta que el usuario 
                     #quiera cerrar el programa
        opcionIngresadaCorrecta = False #cuando el usuario ingrese una opcion 
                                        #correcta cambia a True
        while(not opcionIngresadaCorrecta):#mientras no se ingrese una opcion correcta 
                                           #se imprime por pantalla el menu principal
            print("""
                Menu Principal
                1- Agregar Propiedad
                2- Eliminar Propiedad
                3- Modificar Propiedad
                4- Listar Todas Las Propiedades
                5- Listar Las Propiedades Disponibles Para La Venta
                6- Listar Las Propiedades Disponibles Para Alquiler
                7- Listar las Propiedades Vendidas
                8- Listar las Propiedades Alquiladas
                9- Cerrar Programa
                """)
            opcion = int(input("Seleccione una Opcion del Menu: \n"))
            if opcion < 1 or opcion > 9:
                print("Opcion Incorrecta.")
            elif opcion == 9:
                cerrarConexion()#cierro la conexion a la base de datos
                print("Gracias Por Usar El Programa")
                continuar = False #deja de mostrar el menu de opciones
                break #finaliza el programa
            else:
                opcionIngresadaCorrecta = True#la opcin ingresada es correcta. 
                ejecutarOpcion(opcionIngresadaCorrecta)#llamo a la funcion
                                                       #ejecutarOpcion que se encarga 
                                                       # de llamar a la funcion correspondiente 
                                                       # a la opcion seleccionada

def ejecutarOpcion(opcion):
    match opcion:
        case 1: ingresarPropiedad()
"""case 2: eliminarPropiedad()
        case 3: modificarPropiedad()
        case 4: listarPropiedad()
        case 5: listarPropiedadVenta()
        case 6: listarPropiedadAlquiler()
        case 7: listarPropiedadesVendidas()
        case 8: listarPropiedadesAlquiladas()
        case 9: desconectar()
"""     
                
menuPrincipal()



