import json
import os
from menu import Menu
from inscrito import Inscrito
from main_curso import main_curso
from main_estudiante import main_estudiante
from estudiante import Estudiante

class main_inscrito(Menu):
    def __init__(self):
        super().__init__()
    
    def set(self):
        curso_actual = main_curso()
        curso = curso_actual.set()

        numero_estudiantes = int(input("¿Cuántos estudiantes deseas inscribir?"))
        estudiante_actual = main_estudiante()
        if numero_estudiantes == 1:
            estudiante = estudiante_actual.set()
        else:
            estudiante = Estudiante()
            #estudiante.is_collection = True
            for _ in range(numero_estudiantes):
                nuevo_estudiante = estudiante_actual.set()
                estudiante.create(nuevo_estudiante)
        nuevo = Inscrito(estudiante, curso)
        return nuevo
    
if __name__ == "__main__":
    data_actual = Inscrito()
    file_path = "inscrito.json"
    #print(file_path)
    #print(data_actual)
    if os.path.exists(file_path):
        data_actual = data_actual.read_json(file_path)
    print("Contenido actual de Inscrito:")
    #print(data_actual)
    print(data_actual.to_dictionary())

    main_inscrito = main_inscrito()
    main_inscrito.crud_menu(data_actual, file_path)