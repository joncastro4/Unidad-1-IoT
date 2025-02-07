import json

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
    
    def obtener_json(self):
        with open("inscrito.json", 'r') as file:
            return (json.load(file))
        
    def json_a_objeto(self, json_data = None):
        if isinstance(json_data, str):
            json_data = json.loads(json_data)

        for inscrito in json_data:
            curso = Curso(inscrito["curso"]["nombre"], inscrito["curso"]["descripcion"], inscrito["curso"]["fecha_inicio"], inscrito["curso"]["fecha_fin"], inscrito["curso"]["profesor"])

            if isinstance(inscrito["estudiantes"], dict):
                inscrito["estudiantes"] = [inscrito["estudiantes"]]

            if isinstance(inscrito["estudiantes"], list):
                e = Estudiante().json_a_objeto(inscrito["estudiantes"])

            if e.ver():
                self.agregar(Inscrito(curso, e))

        return self

    def __str__(self):
        if self.isObject:
            return f"Curso: {self.curso}, Estudiantes: {self.estudiantes}"
        else:
            return f"Inscritos: {(self.entidades)}"
        
    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    inscritos = Inscrito()
    curso = Curso()
    estudiante = Estudiante()

    json = inscritos.obtener_json()

    inscritos.json_a_objeto(json)

    est = Estudiante("Estudiante 1", "Apellido Paterno 1", "Apellido Materno 1", "1990-01-01", "1111111111")
    estudiante.agregar(est)

    est = Estudiante("Estudiante 2", "Apellido Paterno 2", "Apellido Materno 2", "1991-02-15", "2222222222")
    estudiante.agregar(est)

    curso = Curso("Curso 1", "Descripcion 1", "2025-02-01", "2025-06-30", "Profesor 1")

    inscritos.agregar(Inscrito(curso, estudiante))

    inscritos.diccionario()

    inscritos.transformar_json("inscrito")
