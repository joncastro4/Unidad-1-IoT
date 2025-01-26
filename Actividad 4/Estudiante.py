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

    def __str__(self):
        if self.isObject:
            return f"Estudiante: {self.nombre}, Apellido Paterno: {self.apellido_paterno}, Apellido Materno: {self.apellido_materno}, Fecha de Nacimiento: {self.fecha_nacimiento}, Telefono: {self.telefono}"
        else:
            return f"Cantidad de estudiantes: {len(self.entidades)}"

if __name__ == "__main__":
    estudiantes = Estudiante()

    estudiante1 = Estudiante("Estudiante 1", "Apellido Paterno 1", "Apellido Materno 1", "1990-01-01", "1111111111")
    estudiante2 = Estudiante("Estudiante 2", "Apellido Paterno 2", "Apellido Materno 2", "1991-02-15", "2222222222")

    print(estudiantes.agregar(estudiante1))
    print(estudiantes.agregar(estudiante2))

    print("Estudiantes en formato diccionario:")
    print(estudiantes.diccionario())