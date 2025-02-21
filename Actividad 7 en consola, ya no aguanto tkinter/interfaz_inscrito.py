from Inscrito import Inscrito
from Curso import Curso
from Estudiante import Estudiante
from interfaz_curso import ICurso
from interfaz_estudiante import IEstudiante

class IInscrito:
    def __init__(self, inscrito=None):
        self.isJson = inscrito is None
        self.inscrito = inscrito if inscrito else Inscrito()
        if self.isJson:
            json_data = self.inscrito.obtener_json()
            self.inscritos = self.inscrito.json_a_objeto(json_data).entidades

    def guardar_inscritos(self):
        self.inscrito.transformar_json("inscrito")

    def menu(self):
        while True:
            print("\n1. Insertar")
            print("2. Agregar Estudiantes a Curso")
            print("3. Ver")
            print("4. Modificar Curso")
            print("5. Modificar Estudiante")
            print("6. Eliminar Curso")
            print("7. Eliminar Estudiante")
            print("8. Menu Principal\n")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.insertar()
            elif opcion == "2":
                self.agregar_estudiantes()
            elif opcion == "3":
                self.ver()
            elif opcion == "4":
                self.modificar_curso()
            elif opcion == "5":
                self.modificar_estudiante()
            elif opcion == "6":
                self.eliminar_curso()
            elif opcion == "7":
                self.eliminar_estudiante()
            elif opcion == "8":
                if self.isJson:
                    self.guardar_inscritos()
                break
            else:
                print("\nOpción no válida, intente nuevamente.\n")

    def insertar(self):
        iCur = ICurso()
        curso = iCur.insertar()

        iEst = IEstudiante()
        estudiantes = Estudiante()
        while True:
            estudiante = iEst.insertar()
            estudiantes.agregar(estudiante)
            
            otro = input("Agregar otro estudiante? (s/n): ")
            if otro.lower() != 's':
                break
        
        nuevo_inscrito = Inscrito(curso, estudiantes)
        self.inscrito.agregar(nuevo_inscrito)
        print("Inscripción agregada exitosamente.\n")

    def ver(self):
        if self.inscritos:
            for index, inscrito in enumerate(self.inscritos):
                print(f"{index}. Curso: {inscrito.curso.nombre}, Descripción: {inscrito.curso.descripcion}, Fecha de inicio: {inscrito.curso.fecha_inicio}, Fecha de fin: {inscrito.curso.fecha_fin}, Profesor: {inscrito.curso.profesor}")
                print("   Estudiantes:")
                for idx, estudiante in enumerate(inscrito.estudiantes.entidades):
                    print(f"      - ID: {idx}, Nombre: {estudiante.nombre}, Apellido Paterno: {estudiante.apellido_paterno}, Apellido Materno: {estudiante.apellido_materno}, Fecha de Nacimiento: {estudiante.fecha_nacimiento}, Teléfono: {estudiante.telefono}")
        else:
            print("No hay inscritos para mostrar.\n")

    def modificar_curso(self):
        self.ver()
        try:
            index = int(input("Ingrese el índice del inscrito a modificar: "))
            inscrito = self.inscritos[index]
            
            curso_interface = ICurso(inscrito.curso)
            curso_interface.modificar()
            print("Curso modificado exitosamente.\n")
        except (IndexError, ValueError):
            print("Índice inválido.\n")

    def modificar_estudiante(self):
        self.ver()
        try:
            index = int(input("Ingrese el índice del inscrito: "))
            inscrito = self.inscritos[index]
            estudiante_idx = int(input("Ingrese el ID del estudiante a modificar: "))
            
            if estudiante_idx < 0 or estudiante_idx >= len(inscrito.estudiantes.entidades):
                print("ID de estudiante inválido.\n")
                return
            
            estudiante_interface = IEstudiante(inscrito.estudiantes.entidades[estudiante_idx])
            estudiante_interface.modificar()
            print("Estudiante modificado exitosamente.\n")
        except (IndexError, ValueError):
            print("Índice inválido.\n")

    def eliminar_curso(self):
        self.ver()
        try:
            index = int(input("Ingrese el índice del curso a eliminar: "))
            resultado = self.inscrito.eliminar(index)
            del self.inscritos[index]
            print(resultado)
        except IndexError:
            print("Índice inválido.\n")
        except ValueError:
            print("Índice inválido.\n")

    def eliminar_estudiante(self):
        self.ver()
        try:
            index = int(input("Ingrese el índice del inscrito: "))
            inscrito = self.inscritos[index]
            estudiante_idx = int(input("Ingrese el ID del estudiante a eliminar: "))
            
            if estudiante_idx < 0 or estudiante_idx >= len(inscrito.estudiantes.entidades):
                print("ID de estudiante inválido.\n")
                return
            
            del inscrito.estudiantes.entidades[estudiante_idx]
            print("Estudiante eliminado exitosamente.\n")
        except (IndexError, ValueError):
            print("Índice inválido.\n")

    def agregar_estudiantes(self):
        self.ver()
        try:
            index = int(input("Ingrese el índice del curso al que desea agregar estudiantes: "))
            inscrito = self.inscritos[index]
            
            estudiantes_interface = IEstudiante()
            while True:
                estudiante = estudiantes_interface.insertar()
                inscrito.estudiantes.agregar(estudiante)
                
                otra = input("¿Desea agregar otro estudiante? (s/n): ")
                if otra.lower() != 's':
                    break
            
            print("Estudiantes agregados exitosamente.\n")
        except (IndexError, ValueError):
            print("Índice inválido.\n")
