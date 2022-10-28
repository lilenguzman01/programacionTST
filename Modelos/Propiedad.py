class Propiedad:
    Nombre = ""
    Direccion = ""
    Contacto = ""
   #Id_Tipo = 0 # variable null por defecto en tabla
   #Id_Estado =  0 # variable null por defecto en tabla
   #Id_Operatoria_Comercial = 0 # variable null por defecto en tabla
   #Id_Propietario =  0 # variable null por defecto en tabla
    
    def __init__(self, nombre, direccion, contacto):
        self.Nombre = Nombre
        self.Direccion = direccion
        self.Contacto = contacto

    def get_Nombre(self):
        return self.Nombre

    def getDireccion(self):
        return self.Direccion

    def getContacto(self):
        return self.Contacto

    def setNombre(self,nombre):
        self.Nombre = nombre
    
    def setDireccion(self,direccion):
        self.Direccion = direccion
    
    