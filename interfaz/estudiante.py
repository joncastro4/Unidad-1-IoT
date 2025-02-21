import json
from clase import Clase

class Estudiante(Clase):
    def __init__(self, nombre=None, ap_paterno=None, ap_materno=None, curp=None, telefono=None):
        self.is_single_object = nombre and ap_paterno and ap_materno and curp and telefono
        if self.is_single_object:
            self.__nombre = nombre
            self.__ap_paterno = ap_paterno
            self.__ap_materno = ap_materno
            self.__curp = curp
            self.__telefono = telefono
            self.is_collection = False
        else:
            super().__init__()

    def to_dictionary(self):
        if self.is_single_object:
            return {
                "nombre": self.__nombre,
                "ap_paterno": self.__ap_paterno,
                "ap_materno": self.__ap_materno,
                "curp": self.__curp,
                "telefono": self.__telefono
            }
        else:
            return [obj.to_dictionary() for obj in self.collection]

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise ValueError("El nombre no puede estar vacío")
        self.__nombre = nuevo_nombre
    
    @nombre.deleter
    def nombre(self):
        self.__nombre = None

    # --------------------------------------------------------------------------------------------
    @property
    def ap_paterno(self):
        return self.__ap_paterno

    @ap_paterno.setter
    def ap_paterno(self, nuevo_ap_paterno):
        if not nuevo_ap_paterno:
            raise ValueError("El ap_paterno no puede estar vacío")
        self.__ap_paterno = nuevo_ap_paterno

    @ap_paterno.deleter
    def ap_paterno(self):
        self.__ap_paterno = None
    
    # --------------------------------------------------------------------------------------------
    @property
    def ap_materno(self):
        return self.__ap_materno

    @ap_materno.setter
    def ap_materno(self, nuevo_ap_materno):
        if not nuevo_ap_materno:
            raise ValueError("El nombre no puede estar vacío")
        self.__ap_materno = nuevo_ap_materno

    @ap_materno.deleter
    def ap_materno(self):
        self.__ap_materno = None

    # --------------------------------------------------------------------------------------------
    @property
    def curp(self):
        return self.__curp

    @curp.setter
    def curp(self, nueva_curp):
        if not nueva_curp:
            raise ValueError("La curp no puede estar vacía")
        self.__curp = nueva_curp

    @curp.deleter
    def curp(self):
        self.__curp = None

    # --------------------------------------------------------------------------------------------
    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        if len(nuevo_telefono) < 10:
            raise ValueError("El teléfono debe tener 10 caracteres")
        self.__telefono = nuevo_telefono

    @telefono.deleter
    def telefono(self):
        self.__telefono = None

# --------------------------------------------------------------------------------------------			

if __name__ == "__main__":
    estudiantes = Estudiante()
    estudiantes.read_json('estudiantes.json')
    #print("Colección de objetos:", estudiantes.to_dictionary())
    estudiante_nuevo = Estudiante("Jonathan", "Castro", "Saenz", "COSJ950123HDFTRN01", "5512345678")
    estudiantes.create(estudiante_nuevo)
    estudiantes.to_json("prueba_estudiantes")
    print("Estudiantes guardado como prueba_estudiantes.json")