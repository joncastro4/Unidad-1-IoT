import json
from curso import Curso
from estudiante import Estudiante
from clase import Clase

class Inscrito(Clase): 
    def __init__(self, estudiantes=None, curso=None):
        #self.is_single_object = estudiantes and curso
        self.is_single_object = estudiantes is not None and curso is not None
        if self.is_single_object:
            self.__estudiantes = estudiantes
            self.__curso = curso
        else:
            super().__init__()

    def to_dictionary(self):
        if self.is_single_object:
            return {
            "curso": self.__curso.to_dictionary(),
            "estudiantes":  self.__estudiantes.to_dictionary()
            }
        else:
            return [obj.to_dictionary() for obj in self.collection]

# --------------------------------------------------------------------------------------------        
    # estudiante --------------------------------------------
    @property
    def estudiantes(self):
        return self.__estudiantes

    @estudiantes.setter
    def estudiantes(self, nuevos_estudiantes):
        if isinstance(nuevos_estudiantes, Estudiante) and nuevos_estudiantes.is_collection:
            self.__estudiantes = nuevos_estudiantes
        else:
            raise ValueError("El objeto debe ser una instancia de la clase Estudiante que actúe como colección.")

    @estudiantes.deleter
    def estudiantes(self):
        self.__estudiantes = Estudiante()
        self.__estudiantes.is_collection = True
        print("Lista de estudiantes eliminada.")

    # curso --------------------------------------------
    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, nuevo_curso):
        if not isinstance(nuevo_curso, Curso):
            raise TypeError("El nuevo curso debe ser una instancia de la clase Curso.")
        self.__curso = nuevo_curso

    @curso.deleter
    def curso(self):
        self.__curso = None
        print("Curso eliminado.")

# --------------------------------------------------------------------------------------------    

if __name__ == "__main__":
    inscrito = Inscrito()
    inscrito = inscrito.read_json('inscrito.json')
    #print(inscrito.to_dictionary())

    estudiante0 = Estudiante("Fer", "De León", "Azpilcueta", "LEAA950930MDGNZN03", "8711087111")
    estudiante1 = Estudiante("Luis", "De la Cruz", "De Todos Los Santos", "1587426983", "8711596258")
    estudiante_collection = Estudiante()
    estudiante_collection.create(estudiante0)
    estudiante_collection.create(estudiante1)
    curso0 = Curso("Mongo", 5, "Ramirin", "Software", 4)
    inscrito.create(Inscrito(estudiante_collection, curso0))
    
    #print(inscrito.to_dictionary())
    inscrito.to_json('prueba_inscrito')