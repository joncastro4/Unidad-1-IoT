from interfaz_curso import ICurso
from interfaz_estudiante import IEstudiante
from interfaz_inscrito import IInscrito
import pymongo

class Menu:
    def mostrar_menu(self):
        while True:
            print("\n1. Curso")
            print("2. Estudiantes")
            print("3. Inscritos")
            print("4. Salir")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                curso = ICurso()
                curso.menu()
            elif opcion == "2":
                estudiante = IEstudiante()
                estudiante.menu()
            elif opcion == "3":
                inscrito = IInscrito()
                inscrito.menu()
            elif opcion == "4":
                print("Saliendo")
                break
            else:
                print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()