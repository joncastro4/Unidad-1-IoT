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

    def agregar(self, curso):
        if isinstance(curso, Curso) and curso.isObject:
            self.entidades.append(curso)
            return f"Curso '{curso.nombre}' agregado exitosamente."
        return "Error: El objeto no es un curso válido."

    def ver(self):
        return self.entidades

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
    
    def __str__(self):
        if self.isObject:
            return f"Curso: {self.nombre}, Descripción: {self.descripcion}, Fecha de inicio: {self.fecha_inicio}, Fecha de fin: {self.fecha_fin}, Profesor: {self.profesor}"
        else:
            return f"Cantidad de cursos: {len(self.entidades)}"


if __name__ == "__main__":
    cursos = Curso()

    curso1 = Curso("Curso 1", "Descripcion 1", "2025-02-01", "2025-06-30", "Profesor 1")
    curso2 = Curso("Curso 2", "Descripcion 2", "2025-03-01", "2025-07-30", "Profesor 2")

    print(cursos.agregar(curso1))
    print(cursos.agregar(curso2))

    print("Cursos en formato diccionario:")
    print(cursos.diccionario())
