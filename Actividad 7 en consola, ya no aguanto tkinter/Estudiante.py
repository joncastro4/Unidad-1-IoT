import json

from Entidad import Entidad

class Estudiante(Entidad):
    def __init__(self, nombre=None, apellido_paterno=None, apellido_materno=None, fecha_nacimiento=None, telefono=None):
        self.isObject = nombre and apellido_paterno and apellido_materno and fecha_nacimiento and telefono

        if self.isObject:
            self.nombre = nombre
            self.apellido_paterno = apellido_paterno
            self.apellido_materno = apellido_materno
            self.fecha_nacimiento = fecha_nacimiento
            self.telefono = telefono
        else:
            super().__init__()

    def __str__(self):
        if self._modo_lista:
            return f"Lista de estudiantes:\n{super().__str__()}" 
        else:
            return (f"Estudiante: {self.nombre} {self.apellido_materno}\n"
                    f"Email: {self.apellido_paterno}\n"
                    f"Edad: {self.fecha_nacimiento}\n"
                    f"Teléfono: {self.telefono}")
        
    def diccionario(self):
        diccionarios = []
        if self.isObject:
            return {
                "nombre": self.nombre,
                "apellido_paterno": self.apellido_paterno,
                "apellido_materno": self.apellido_materno,
                "fecha_nacimiento": self.fecha_nacimiento,
                "telefono": self.telefono
            }
        else:
            for estudiante in self.entidades:
                diccionarios.append(estudiante.diccionario())
        return diccionarios
    
    def obtener_json(self):
        with open("estudiante.json", 'r') as file:
            return (json.load(file))
        
    def json_a_objeto(self, json = None):
        for estudiante in json:
            self.agregar(Estudiante(estudiante["nombre"], estudiante["apellido_paterno"], estudiante["apellido_materno"], estudiante["fecha_nacimiento"], estudiante["telefono"]))
        return self

    def __str__(self):
        if self.isObject:
            return f"Estudiante: {self.nombre}, Apellido Paterno: {self.apellido_paterno}, Apellido Materno: {self.apellido_materno}, Fecha de Nacimiento: {self.fecha_nacimiento}, Telefono: {self.telefono}"
        else:
            return f"Estudiantes: {(self.entidades)}"
        
    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    estudiantes = Estudiante()

    estudiante = Estudiante("Estudiante 1", "Apellido Paterno 1", "Apellido Materno 1", "1990-01-01", "1111111111")

    estudiantes = estudiantes.json_a_objeto()

    estudiantes.agregar(estudiante)

    print(estudiantes.ver())

    estudiantes.transformar_json("estudiante")