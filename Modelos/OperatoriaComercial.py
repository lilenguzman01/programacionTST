class OperatoriaComercial:
    Nombre_Operatoria_Comercial = ""

    def __init__(self, Nombre_Operatoria_Comercial):
        self.Nombre_Operatoria_Comercial = Nombre_Operatoria_Comercial

    def getNombre_Operatoria_Comercial(self):
        return self.Nombre_Operatoria_Comercial

    def setNombre_Operatoria_Comercial(self, Nombre_Operatoria):
        self.Nombre_Operatoria_Comercial = Nombre_Operatoria


    def _str(self):
        print("\nNombre de la operatoria: " + self.Nombre_Operatoria_Comercial)


        
    
