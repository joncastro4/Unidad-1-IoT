import json
import os
from clase import Clase
from curso import Curso
from estudiante import Estudiante
from inscrito import Inscrito

def main():
    dataActual = None
    file_path = ""

    while True:
        print("Menú Principal")
        print("1. Estudiante")
        print("2. Curso")
        print("3. Inscrito")
        print("4. Salir")
        choice = input("Escoge una opción: ")

        if choice == '1':
            dataActual = Estudiante()
            file_path = "estudiantes.json"
            if os.path.exists(file_path):
                dataActual.read_json(file_path)
            print("Contenido actual de Estudiante:")
            print(dataActual.to_dictionary())
        elif choice == '2':
            dataActual = Curso()
            file_path = "cursos.json"
            if os.path.exists(file_path):
                dataActual.read_json(file_path)
            print("Contenido actual de Curso:")
            print(dataActual.to_dictionary())
        elif choice == '3':
            dataActual = Inscrito()
            file_path = "inscrito.json"
            if os.path.exists(file_path):
                dataActual.read_json(file_path)
            print("Contenido actual de Inscrito:")
            print(dataActual.to_dictionary())
        elif choice == '4':
            break
        else:
            print("Opción no válida, por favor intenta nuevamente.")
            continue

        while True:
            print("\nMenú de Operaciones")
            print("1. Crear")
            print("2. Leer")
            print("3. Actualizar")
            print("4. Eliminar")
            print("5. Volver al menú principal")
            operation = input("Escoge una opción: ")

            if operation == '1':
                if isinstance(dataActual, Estudiante):
                    try:
                        nombre = input("Introduce el nombre del estudiante: ")
                        ap_paterno = input("Introduce el apellido paterno: ")
                        ap_materno = input("Introduce el apellido materno: ")
                        curp = input("Introduce la CURP: ")
                        telefono = input("Introduce el teléfono: ")

                        nuevo = Estudiante(nombre, ap_paterno, ap_materno, curp, telefono)
                        dataActual.create(nuevo)
                        dataActual.to_json(file_path)
                    except ValueError as e:
                        print(f"Error: {e}")
                elif isinstance(dataActual, Curso):
                    try:
                        nombre_curso = input("Introduce el nombre del curso: ")
                        cuatrimestre = int(input("Introduce el cuatrimestre: "))
                        profesor = input("Introduce el profesor: ")
                        carrera = input("Introduce la carrera: ")
                        creditos = int(input("Introduce los créditos: "))

                        nuevo = Curso(nombre_curso, cuatrimestre, profesor, carrera, creditos)
                        dataActual.create(nuevo)
                        dataActual.to_json(file_path)
                    except ValueError as e:
                        print(f"Error: {e}")
                elif isinstance(dataActual, Inscrito):
                    try:
                        curso_nombre = input("Introduce el nombre del curso: ")
                        cuatrimestre = int(input("Introduce el cuatrimestre: "))
                        profesor = input("Introduce el profesor: ")
                        carrera = input("Introduce la carrera: ")
                        creditos = int(input("Introduce los créditos: "))
                        curso = Curso(curso_nombre, cuatrimestre, profesor, carrera, creditos)

                        numero_estudiantes = int(input("¿Cuántos estudiantes deseas inscribir? "))
                        estudiantes = Estudiante()
                        for _ in range(numero_estudiantes):
                            nombre = input("Introduce el nombre del estudiante: ")
                            apellido_paterno = input("Introduce el apellido paterno: ")
                            apellido_materno = input("Introduce el apellido materno: ")
                            matricula = input("Introduce la matrícula: ")
                            telefono = input("Introduce el teléfono: ")
                            estudiante = Estudiante(nombre, apellido_paterno, apellido_materno, matricula, telefono)
                            estudiantes.create(estudiante)

                        nuevo = Inscrito(estudiantes, curso)
                        dataActual.create(nuevo)
                        dataActual.to_json(file_path)
                    except ValueError as e:
                        print(f"Error: {e}")
            elif operation == '2':
                print("Contenido actual:")
                dataActual.read_json(file_path)
                print(dataActual.to_dictionary())
            elif operation == '3':
                if isinstance(dataActual, Estudiante):
                    try:
                        index = int(input("Introduce el índice del estudiante a actualizar: "))
                        if 0 <= index < len(dataActual.collection):
                            nombre = input("Introduce el nuevo nombre del estudiante: ")
                            ap_paterno = input("Introduce el nuevo apellido paterno: ")
                            ap_materno = input("Introduce el nuevo apellido materno: ")
                            curp = input("Introduce la nueva CURP: ")
                            telefono = input("Introduce el nuevo teléfono: ")

                            nuevo = Estudiante(nombre, ap_paterno, ap_materno, curp, telefono)
                            dataActual.update(index, nuevo)
                            dataActual.to_json(file_path)
                        else:
                            print("Índice fuera de rango.")
                    except ValueError as e:
                        print(f"Error: {e}")
                elif isinstance(dataActual, Curso):
                    try:
                        index = int(input("Introduce el índice del curso a actualizar: "))
                        if 0 <= index < len(dataActual.collection):
                            nombre_curso = input("Introduce el nuevo nombre del curso: ")
                            cuatrimestre = int(input("Introduce el nuevo cuatrimestre: "))
                            profesor = input("Introduce el nuevo profesor: ")
                            carrera = input("Introduce la nueva carrera: ")
                            creditos = int(input("Introduce los nuevos créditos: "))

                            nuevo = Curso(nombre_curso, cuatrimestre, profesor, carrera, creditos)
                            dataActual.update(index, nuevo)
                            dataActual.to_json(file_path)
                        else:
                            print("Índice fuera de rango.")
                    except ValueError as e:
                        print(f"Error: {e}")
                elif isinstance(dataActual, Inscrito):
                    try:
                        index = int(input("Introduce el índice del inscrito a actualizar: "))
                        if 0 <= index < len(dataActual.collection):
                            curso_nombre = input("Introduce el nuevo nombre del curso: ")
                            cuatrimestre = int(input("Introduce el nuevo cuatrimestre: "))
                            profesor = input("Introduce el nuevo profesor: ")
                            carrera = input("Introduce la nueva carrera: ")
                            creditos = int(input("Introduce los nuevos créditos: "))
                            curso = Curso(curso_nombre, cuatrimestre, profesor, carrera, creditos)

                            numero_estudiantes = int(input("¿Cuántos estudiantes deseas actualizar? "))
                            estudiantes = Estudiante()
                            for _ in range(numero_estudiantes):
                                nombre = input("Introduce el nombre del estudiante: ")
                                apellido_paterno = input("Introduce el apellido paterno: ")
                                apellido_materno = input("Introduce el apellido materno: ")
                                matricula = input("Introduce la matrícula: ")
                                telefono = input("Introduce el teléfono: ")
                                estudiante = Estudiante(nombre, apellido_paterno, apellido_materno, matricula, telefono)
                                estudiantes.create(estudiante)

                            nuevo = Inscrito(estudiantes, curso)
                            dataActual.update(index, nuevo)
                            dataActual.to_json(file_path)
                        else:
                            print("Índice fuera de rango.")
                    except ValueError as e:
                        print(f"Error: {e}")
            elif operation == '4':
                index = int(input("Introduce el índice del elemento a eliminar: "))
                if 0 <= index < len(dataActual.collection):
                    print(f"Elemento a eliminar:\n{dataActual.collection[index].to_dictionary()}")
                    confirm = input("¿Estás seguro? (s/n): ")
                    if confirm.lower() == 's':
                        dataActual.delete(index)
                        dataActual.to_json(file_path)
                        print("Elemento eliminado.")
                    else:
                        print("Operación cancelada.")
                else:
                    print("Índice fuera de rango.")
            elif operation == '5':
                break
            else:
                print("Opción no válida, por favor intenta nuevamente.")

if __name__ == "__main__":
    main()