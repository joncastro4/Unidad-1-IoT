import json
import os
from menu import Menu
from curso import Curso

class main_curso(Menu):
    def __init__(self):
        super().__init__()
    
    def set(self):
        nombre_curso = input("Introduce el nombre del curso: ")
        cuatrimestre = int(input("Introduce el cuatrimestre: "))
        profesor = input("Introduce el profesor: ")
        carrera = input("Introduce la carrera: ")
        creditos = int(input("Introduce los créditos: "))

        nuevo = Curso(nombre_curso, cuatrimestre, profesor, carrera, creditos)
        return nuevo

if __name__ == "__main__":
    data_actual = Curso()
    file_path = "cursos.json"
    if os.path.exists(file_path):
        data_actual.read_json(file_path)
    print("Contenido actual de Cursos:")
    print(data_actual.to_dictionary())

    main_curso = main_curso()
    main_curso.crud_menu(data_actual, file_path)