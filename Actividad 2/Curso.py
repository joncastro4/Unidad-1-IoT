from Entidad import Entidad

class Curso(Entidad):
    def __init__(self, nombre = None, descripcion = None, fecha_inicio = None, fecha_fin = None, profesor = None):
        self.isObject = nombre and descripcion and fecha_inicio and fecha_fin and profesor

        if self.isObject:
            self.nombre = nombre
            self.descripcion = descripcion
            self.fecha_inicio = fecha_inicio
            self.fecha_fin = fecha_fin
            self.profesor = profesor
        else:
            super().__init__()

    def __str__(self):
        if self.isObject:
            return f"Curso: {self.nombre}, Descripción: {self.descripcion}, Fecha de inicio: {self.fecha_inicio}, Fecha de fin: {self.fecha_fin}, Profesor: {self.profesor}"
        else:
            return f"Cantidad de cursos: {len(self.entidades)}"

if __name__ == "__main__":
    cursos = Curso()

    curso1 = Curso("Curso 1", "Descripcion 1", "2025-02-01", "2025-06-30", "Profesor 1")
    curso2 = Curso("Curso 2", "Descripcion 2", "2025-03-15", "2025-08-01", "Profesor 2")
    curso3 = Curso("Curso 3", "Descripcion 3", "2025-04-01", "2025-09-30", "Profesor 3")

    print(cursos.agregar(curso1))
    print(cursos.agregar(curso2))
    print(cursos.agregar(curso3))

    for curso in cursos.ver():
        print(curso)

    curso_modificado = Curso("Curso Modificado", "Descripcion modificada", "2025-03-15", "2025-08-01", "Profesor modificado")
    print(cursos.modificar(0, curso_modificado))

    for curso in cursos.ver():
        print(curso)

    print(cursos.eliminar(1))

    for curso in cursos.ver():
        print(curso)
