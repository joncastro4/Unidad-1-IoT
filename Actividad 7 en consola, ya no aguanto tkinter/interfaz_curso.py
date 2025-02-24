from Curso import Curso

class ICurso:
    def __init__(self, curso=None):
        self.isJson = curso is None
        self.curso = curso if curso else Curso()
        if self.isJson:
            json_data = self.curso.obtener_json()
            self.cursos = self.curso.json_a_objeto(json_data).entidades
        else:
            self.cursos = [self.curso]

    def guardar_cursos(self):
        self.curso.transformar_json("curso")
        self.curso.guardar_en_mongodb(database_name="Escuela", collection_name="cursos")

    def menu(self):
        while True:
            print("\n1. Insertar")
            print("2. Ver")
            print("3. Modificar")
            print("4. Eliminar")
            print("5. Menu Principal\n")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.insertar()
            elif opcion == "2":
                self.ver()
            elif opcion == "3":
                self.modificar()
            elif opcion == "4":
                self.eliminar()
            elif opcion == "5":
                if self.isJson:
                    self.guardar_cursos()
                break
            else:
                print("\nOpción no válida, intente nuevamente.\n")

    def insertar(self):
        nombre = input("Ingrese el nombre del curso: ")
        descripcion = input("Ingrese la descripción del curso: ")
        fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
        fecha_fin = input("Ingrese la fecha de fin (YYYY-MM-DD): ")
        profesor = input("Ingrese el nombre del profesor: ")
        
        nuevo_curso = Curso(nombre, descripcion, fecha_inicio, fecha_fin, profesor)
        self.curso.agregar(nuevo_curso)
        self.cursos.append(nuevo_curso)

        if self.isJson:
            self.guardar_cursos()
        print("Curso agregado exitosamente.\n")
        return nuevo_curso

    def ver(self):
        if self.cursos:
            for index, curso in enumerate(self.cursos):
                print(f"{index}. {curso}")
        else:
            print("No hay cursos para mostrar.\n")

    def modificar(self, curso=None):
        if curso is None:
            self.ver()
            try:
                index = int(input("Ingrese el índice del curso a modificar: "))
                if index < 0 or index >= len(self.cursos):
                    print("Índice inválido.\n")
                    return

                curso = self.cursos[index]
            except ValueError:
                print("Índice inválido.\n")
                return

        nombre = input(f"Ingrese el nuevo nombre del curso (actual: {curso.nombre}): ") or curso.nombre
        descripcion = input(f"Ingrese la nueva descripción del curso (actual: {curso.descripcion}): ") or curso.descripcion
        fecha_inicio = input(f"Ingrese la nueva fecha de inicio (YYYY-MM-DD) (actual: {curso.fecha_inicio}): ") or curso.fecha_inicio
        fecha_fin = input(f"Ingrese la nueva fecha de fin (YYYY-MM-DD) (actual: {curso.fecha_fin}): ") or curso.fecha_fin
        profesor = input(f"Ingrese el nuevo nombre del profesor (actual: {curso.profesor}): ") or curso.profesor
        
        curso.nombre = nombre
        curso.descripcion = descripcion
        curso.fecha_inicio = fecha_inicio
        curso.fecha_fin = fecha_fin
        curso.profesor = profesor

        print("Curso modificado exitosamente.\n")

        if self.isJson:
            self.guardar_cursos()

    def eliminar(self):
        self.ver()
        try:
            index = int(input("Ingrese el índice del curso a eliminar: "))
            if index < 0 or index >= len(self.cursos):
                print("Índice inválido.\n")
                return
            resultado = self.curso.eliminar(index)
            del self.cursos[index]

            if self.isJson:
                self.guardar_cursos()
            print("Curso eliminado exitosamente.\n")
        except ValueError:
            print("Índice inválido.\n")