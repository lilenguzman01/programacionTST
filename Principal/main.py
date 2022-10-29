def menu():
    print("Alumnos: \nEnrique Ripoli \nIvan Gomez\nLilen Guzman\nSergio Muguruza\n")
    print("Seleccione una opción del menú\n")
    print("1- Agregar Propiedad")
    print("2- Eliminar Propiedad")
    print("3- Modificar Propiedad")
    print("4- Listar Todas Las Propiedades")
    print("5- Listar Las Propiedades Disponibles Para La Venta")
    print("6- Listar Las Propiedades Disponibles Para Alquiler")
    print("7- Listar las Propiedades Vendidas")
    print("8- Listar las Propiedades Alquiladas")
    print("9- Salir")

def menu_opciones(opcion):#llama a la funcion correspondiente segun la opción seleccionada
    seguir = True
    match opcion:
        case 1: ingresarPropiedad()
        case 2: eliminarPropiedad()
        case 3: modificarPropiedad()
        case 4: listarPropiedad()
        case 5: listarPropiedadVenta()
        case 6: listarPropiedadAlquiler()
        case 7: listarPropiedadesVendidas()
        case 8: listarPropiedadesAlquiladas()
        case 9: seguir = False
                salir()
    return seguir



def salir():

seguir = True
while (seguir):
    menu()
    try:
    opcion= int(input(""))

    seguir = menu_opciones(opcion)
    except:
        print("Opcion Incorrecta")

