import json
import os
from menu import Menu
from estudiante import Estudiante

class main_estudiante(Menu):
    def __init__(self):
        super().__init__()
    
    def set(self):
        nombre = input("Introduce el nombre del estudiante: ")
        ap_paterno = input("Introduce el apellido paterno: ")
        ap_materno = input("Introduce el apellido materno: ")
        curp = input("Introduce la CURP: ")
        telefono = input("Introduce el teléfono: ")

        nuevo = Estudiante(nombre, ap_paterno, ap_materno, curp, telefono)
        return nuevo

if __name__ == "__main__":
    data_actual = Estudiante()
    file_path = "estudiantes.json"
    if os.path.exists(file_path):
        data_actual.read_json(file_path)
    print("Contenido actual de Estudiante:")
    print(data_actual.to_dictionary())

    main_estudiante = main_estudiante()
    main_estudiante.crud_menu(data_actual, file_path)