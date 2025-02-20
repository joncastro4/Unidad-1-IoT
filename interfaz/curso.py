import json
from clase import Clase

class Curso(Clase):
    def __init__(self, nombre_curso=None, cuatrimestre=None, profesor=None, carrera=None, creditos=None):
        self.is_single_object = nombre_curso and cuatrimestre and profesor and carrera and creditos
        if self.is_single_object:
            self.__nombre_curso = nombre_curso
            self.__cuatrimestre = cuatrimestre
            self.__profesor = profesor
            self.__carrera = carrera
            self.__creditos = creditos
        else:
            super().__init__()

    def to_dictionary(self):
        if self.is_single_object:
            return {
                "nombre_curso": self.__nombre_curso,
                "cuatrimestre": self.__cuatrimestre,
                "profesor": self.__profesor,
                "carrera": self.__carrera,
                "creditos": self.__creditos
            }
        else:
            return [obj.to_dictionary() for obj in self.collection]

# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
    @property
    def nombre_curso(self):
        return self.__nombre_curso
    
    @nombre_curso.setter
    def nombre_curso(self, nuevo_nombre_curso):
        if not nuevo_nombre_curso:
            raise ValueError("El nombre_curso del curso no puede estar vacío")
        self.__nombre_curso = nuevo_nombre_curso
    
    @nombre_curso.deleter
    def nombre_curso(self):
        self.__nombre_curso = None

    # --------------------------------------------------------------------------------------------
    @property
    def cuatrimestre(self):
        return self.__cuatrimestre

    @cuatrimestre.setter
    def cuatrimestre(self, nuevo_cuatrimestre):
        if not nuevo_cuatrimestre:
            raise ValueError("El nombre_curso del cuatrimestre no puede estar vacío")
        if nuevo_cuatrimestre <= 0:
            raise ValueError("El cuatrimestre debe ser mayor a 0")
        self.__cuatrimestre = nuevo_cuatrimestre

    @cuatrimestre.deleter
    def cuatrimestre(self):
        self.__cuatrimestre = None

    # --------------------------------------------------------------------------------------------
    @property
    def profesor(self):
        return self.__profesor

    @profesor.setter
    def profesor(self, nuevo_profesor):
        if not nuevo_profesor:
            raise ValueError("El profesor no puede estar vacío")
        self.__profesor = nuevo_profesor

    @profesor.deleter
    def profesor(self):
        self.__profesor = None

    # --------------------------------------------------------------------------------------------
    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self, nueva_carrera):
        if not nueva_carrera:
            raise ValueError("La carrera no puede estar vacía")
        self.__carrera = nueva_carrera

    @carrera.deleter
    def carrera(self):
        self.__carrera = None

    # --------------------------------------------------------------------------------------------
    @property
    def creditos(self):
        return self.__creditos

    @creditos.setter
    def creditos(self, nuevos_creditos):
        if nuevos_creditos <= 0:
            raise ValueError("Los créditos deben ser mayores a 0")
        self.__creditos = nuevos_creditos

    @creditos.deleter
    def creditos(self):
        self.__creditos = None
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

if __name__ == "__main__":
    cursos = Curso()
    cursos.read_json('cursos.json')
    instancia = cursos.to_dictionary()
    print(instancia)
    cursos.create(Curso("Appis", 5, "Igmar Salazar", "TICs", 8))
    #print(cursos.to_dictionary())
    cursos.to_json('prueba_cursos')