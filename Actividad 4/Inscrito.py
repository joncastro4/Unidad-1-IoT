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
                "estudiantes": [estudiante.diccionario() for estudiante in self.estudiantes]
            }
        else:
            for inscrito in self.entidades:
                diccionarios.append(inscrito.diccionario())
        return diccionarios

    def __str__(self):
        if self.isObject:
            estudiantes_info = "\n".join([str(est) for est in self.estudiantes])
            return f"Curso: {self.curso}\nEstudiantes inscritos:\n{estudiantes_info}"
        else:
            return f"Cantidad de inscritos: {len(self.entidades)}"

if __name__ == "__main__":
    estudiante1 = Estudiante("Estudiante 1", "Apellido Paterno 1", "Apellido Materno 1", "1990-01-01", "1111111111")
    estudiante2 = Estudiante("Estudiante 2", "Apellido Paterno 2", "Apellido Materno 2", "1991-02-15", "2222222222")

    curso1 = Curso("Curso 1", "Descripcion 1", "2025-02-01", "2025-06-30", "Profesor 1")

    inscrito = Inscrito(curso1, [estudiante1, estudiante2])

    print("Inscrito en formato diccionario:")
    print(inscrito.diccionario())