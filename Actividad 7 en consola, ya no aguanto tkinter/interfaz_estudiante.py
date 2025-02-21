from Estudiante import Estudiante

class IEstudiante:
    def __init__(self, estudiante=None):
        self.isJson = estudiante is None
        self.estudiante = estudiante if estudiante else Estudiante()
        if self.isJson:
            json_data = self.estudiante.obtener_json()
            self.estudiantes = self.estudiante.json_a_objeto(json_data).entidades

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
        telefono = input("Ingrese el telefono del estudiante: ")
        
        nuevo_estudiante = Estudiante(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono)
        self.estudiante.agregar(nuevo_estudiante)

        if self.isJson:
            self.guardar_estudiantes()

        print("Estudiante agregado exitosamente.\n")

    def ver(self):
        if self.estudiantes:
            for index, estudiante in enumerate(self.estudiantes):
                print(f"{index}. {estudiante}")
        else:
            print("No hay estudiantes para mostrar.\n")

    def modificar(self):
        self.ver()
        try:
            index = int(input("Ingrese el índice del estudiante a modificar: "))
            nombre = input("Ingrese el nuevo nombre del estudiante: ")
            apellido_paterno = input("Ingrese el nuevo apellido paterno del estudiante: ")
            apellido_materno = input("Ingrese el nuevo apellido materno del estudiante: ")
            fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento (YYYY-MM-DD): ")
            telefono = input("Ingrese el nuevo telefono del estudiante: ")
            
            nuevo_estudiante = Estudiante(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono)
            resultado = self.estudiante.modificar(index, nuevo_estudiante)
            self.estudiantes[index] = nuevo_estudiante

            if self.isJson:
                self.guardar_estudiantes()

            print(resultado)
        except ValueError:
            print("Índice inválido.\n")

    def eliminar(self):
        self.ver()
        try:
            index = int(input("Ingrese el índice del estudiante a eliminar: "))
            self.estudiante.eliminar(index)

            if self.isJson:
                self.guardar_estudiantes()

        except IndexError:
            print("Índice inválido.\n")
        except ValueError:
            print("Índice inválido.\n")
