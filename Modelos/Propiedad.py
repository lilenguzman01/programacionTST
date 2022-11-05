class Propiedad:
    Id_Tipo = ""
    Id_Estado = ""
    Id_Operatoria_Comercial = ""
    Id_Propietario = ""   
    Nombre = ""
    Direccion = ""
    Contacto = ""
  
    def __init__(self, Id_Tipo, Id_Estado, Id_Operatoria_Comercial, Id_Propietario, nombre, direccion, contacto):
        self.Id_Tipo = Id_Tipo
        self.Id_Estado = Id_Estado
        self.Id_Operatoria_Comercial = Id_Operatoria_Comercial
        self.Id_Propietario = Id_Propietario        
        self.Nombre = nombre
        self.Direccion = direccion
        self.Contacto = contacto

    def get_Id_Tipo(self):
        return self.Id_Tipo

    def get_Id_Estado(self):
        return self.Id_Estado

    def get_Id_Operatoria_Comercial(self):
        return self.Id_Operatoria_Comercial

    def get_Id_Propietario(self):
        return self.Id_Operatoria_Comercial

    def get_Nombre(self):
        return self.Nombre

    def getDireccion(self):
        return self.Direccion

    def getContacto(self):
        return self.Contacto

    def setId_Tipo(self,Id_Tipo):
        self.Id_Tipo = Id_Tipo

    def setId_Estado(self,Id_Estado):
        self.Id_Estado = Id_Estado

    def setId_Operatoria_Comercial(self,Id_Operatoria_Comercial):
        self.Id_Operatoria_Comercial = Id_Operatoria_Comercial

    def setId_Propietario(self,Id_Propietario):
        self.Id_Propietario = Id_Propietario

    def setNombre(self,nombre):
        self.Nombre = nombre
    
    def setDireccion(self,direccion):
        self.Direccion = direccion
    
    def setContacto(self,contacto):
        self.Contacto = contacto
    
    def _str(self):
        print("")


        print("Nombre Propiedad: "+self.Nombre)
        print("\nDireccion Propiedad: "+self.Direccion)
        print("Contacto Propiedad: "+self.Contacto)

    