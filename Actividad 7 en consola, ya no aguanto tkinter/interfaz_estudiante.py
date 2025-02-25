from Estudiante import Estudiante

class IEstudiante:
    def __init__(self, estudiante=None):
        self.isJson = estudiante is None
        self.estudiante = estudiante if estudiante else Estudiante()
        if self.isJson:
            json_data = self.estudiante.obtener_json()
            self.estudiantes = self.estudiante.json_a_objeto(json_data).entidades
        else:
            if estudiante.isObject:
                estudiantes = Estudiante()
                estudiantes.agregar(estudiante)
                self.estudiantes = estudiantes
            else:
                self.estudiantes = estudiante

    def guardar_estudiantes(self):
        self.estudiante.transformar_json("estudiante")

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
                    self.guardar_estudiantes()
                break
            else:
                print("\nOpción no válida, intente nuevamente.\n")

    def insertar(self):
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido_paterno = input("Ingrese el apellido paterno del estudiante: ")
        apellido_materno = input("Ingrese el apellido materno del estudiante: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
        telefono = input("Ingrese el teléfono del estudiante: ")
        
        nuevo_estudiante = Estudiante(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono)
        self.estudiante.agregar(nuevo_estudiante)

        if self.isJson:
            self.guardar_estudiantes()
        print("Estudiante agregado exitosamente.\n")
        return nuevo_estudiante

    def ver(self):
        if self.estudiantes:
            for index, estudiante in enumerate(self.estudiantes):
                print(f"{index}. {estudiante}")
        else:
            print("No hay estudiantes para mostrar.\n")

    def modificar(self, estudiante=None):
        if estudiante is None:
            self.ver()
            try:
                index = int(input("Ingrese el índice del estudiante a modificar: "))
                if index < 0 or index >= len(self.estudiantes):
                    print("Índice inválido.\n")
                    return

                estudiante = self.estudiantes[index]
            except ValueError:
                print("Índice inválido.\n")
                return

        nombre = input(f"Ingrese el nuevo nombre del estudiante: ") or estudiante.nombre
        apellido_paterno = input(f"Ingrese el nuevo apellido paterno del estudiante: ") or estudiante.apellido_paterno
        apellido_materno = input(f"Ingrese el nuevo apellido materno del estudiante: ") or estudiante.apellido_materno
        fecha_nacimiento = input(f"Ingrese la nueva fecha de nacimiento (YYYY-MM-DD): ") or estudiante.fecha_nacimiento
        telefono = input(f"Ingrese el nuevo teléfono del estudiante: ") or estudiante.telefono
        
        estudiante.nombre = nombre
        estudiante.apellido_paterno = apellido_paterno
        estudiante.apellido_materno = apellido_materno
        estudiante.fecha_nacimiento = fecha_nacimiento
        estudiante.telefono = telefono

        print("Estudiante modificado exitosamente.\n")

        if self.isJson:
            self.guardar_estudiantes()

    def eliminar(self, index=None):
        if index is None:
            self.ver()
            try:
                index = int(input("Ingrese el índice del estudiante a eliminar: "))
            except ValueError:
                print("Índice inválido.\n")
                return

        if index < 0 or index >= len(self.estudiantes):
            print("Índice inválido.\n")
            return

        resultado = self.estudiante.eliminar(index)
        del self.estudiantes[index]
        print(resultado)

        if self.isJson:
            self.guardar_estudiantes()