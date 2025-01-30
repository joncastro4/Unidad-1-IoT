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
                "estudiantes": [estudiante.diccionario() for estudiante in self.estudiantes]
            }
        else:
            for inscrito in self.entidades:
                diccionarios.append(inscrito.diccionario())
        return diccionarios
    
    def obtener_json(self):
        with open("inscrito.json", 'r') as file:
            data = json.load(file)
            print("contenido del json:", data)  # depuración
            return data if isinstance(data, list) else []
        
    def json_a_objeto(self):
        data = self.obtener_json()
        
        if isinstance(data, list):  # verificar si es una lista de diccionarios
            for inscrito in data:
                curso = Curso(**inscrito["curso"])  # suponer que Curso tiene un constructor adecuado
                estudiantes = [Estudiante(**est) for est in inscrito["estudiantes"]]
                self.agregar(Inscrito(curso, estudiantes))
        return self
    
    def __str__(self):
        if self.isObject:
            return f"Curso: {self.curso}, Estudiantes: {', '.join(str(est) for est in self.estudiantes)}"
        else:
            return "\n".join(str(inscrito) for inscrito in self.entidades)
        
    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    inscritos = Inscrito()

    inscritos.json_a_objeto()

    print(inscritos.ver())