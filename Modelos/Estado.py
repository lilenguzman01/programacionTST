class Estado:
    Nombre_Estado = ""
    
    def __init__(self,n_estado):
        self.Nombre_Estado = n_estado

    def getNombre_Estado(self):
        return self.Nombre_Estado


    def setNombre_Estado(self,n_estado):
        self.Nombre_Estado = n_estado

    def _str(self):
        print("Nombre Estado: " + self.Nombre_Estado)