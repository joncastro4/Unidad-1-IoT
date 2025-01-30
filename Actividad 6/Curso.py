import json

from Entidad import Entidad

class Curso(Entidad):
    def __init__(self, nombre=None, descripcion=None, fecha_inicio=None, fecha_fin=None, profesor=None):
        self.isObject = nombre and descripcion and fecha_inicio and fecha_fin and profesor

        if self.isObject:
            self.nombre = nombre
            self.descripcion = descripcion
            self.fecha_inicio = fecha_inicio
            self.fecha_fin = fecha_fin
            self.profesor = profesor
        else:
            super().__init__()

    def diccionario(self):
        diccionarios = []
        if self.isObject:
            return {
                "nombre": self.nombre,
                "descripcion": self.descripcion,
                "fecha_inicio": self.fecha_inicio,
                "fecha_fin": self.fecha_fin,
                "profesor": self.profesor
            }
        else:
            for curso in self.entidades:
                diccionarios.append(curso.diccionario())
        return diccionarios
    
    def obtener_json(self):
        with open("curso.json", 'r') as file:
            return (json.load(file))
        
    def json_a_objeto(self):
        json = self.obtener_json()
        for curso in json:
            self.agregar(Curso(curso["nombre"], curso["descripcion"], curso["fecha_inicio"], curso["fecha_fin"], curso["profesor"]))
        return self

    def __str__(self):
        if self.isObject:
            return f"Curso: {self.nombre}, Descripción: {self.descripcion}, Fecha de inicio: {self.fecha_inicio}, Fecha de fin: {self.fecha_fin}, Profesor: {self.profesor}"
        else:
            return f"Cantidad de cursos: {len(self.entidades)}"
        
    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    curso = Curso()

    curso.json_a_objeto()

    print(curso.ver())