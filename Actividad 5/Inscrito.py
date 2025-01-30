from Curso import Curso
from Estudiante import Estudiante
from Entidad import Entidad

class Inscrito(Entidad):
    def __init__(self, curso=None, estudiantes=None):
        self.isObject = curso is not None and estudiantes is not None

        if self.isObject:
            self.curso = curso
            self.estudiantes = estudiantes
        else:
            super().__init__()

    def diccionario(self):
        diccionarios = []
        if self.isObject:
            return {
                "curso": self.curso.diccionario(),
                "estudiantes": self.estudiantes.diccionario()
            }
        else:
            for inscrito in self.entidades:
                diccionarios.append(inscrito.diccionario())
        return diccionarios

if __name__ == "__main__":
    estudiantes = Estudiante()

    estudiante1 = Estudiante("estudiante 1", "apellido paterno 1", "apellido materno 1", "1990-01-01", "1111111111")
    estudiante2 = Estudiante("estudiante 2", "apellido paterno 2", "apellido materno 2", "1991-02-15", "2222222222")

    estudiantes.agregar(estudiante1)
    estudiantes.agregar(estudiante2)

    curso1 = Curso("curso 1", "descripcion 1", "2025-02-01", "2025-06-30", "profesor 1")

    inscrito = Inscrito(curso1, estudiantes)

    print("inscrito en formato diccionario:")
    print(inscrito.diccionario())

    inscrito.transformar_json("inscrito")
