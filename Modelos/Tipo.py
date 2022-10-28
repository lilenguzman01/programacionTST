class Tipo:
    Nombre_Tipo = ""
    
    def __init__(self,n_tipo):
        self.Nombre_Tipo = n_tipo

    def getNombre_Tipo(self):
        return self.Nombre_Tipo


    def setNombre_Tipo(self,n_tipo):
        self.Nombre_Tipo = n_tipo

    def _str(self):
        print("Nombre Tipo: " + self.Nombre_Tipo)