import json
import os

class Menu():
    def __init__(self):
        self.data_actual = None
        self.file_path = ""

    def crud_menu(self, data_actual, file_path):
        while True:
            print("\nMenú de Operaciones")
            print("1. Crear")
            print("2. Leer")
            print("3. Actualizar")
            print("4. Eliminar")
            print("5. Volver al menú principal")
            operation = input("Escoge una opción: ")

            if operation == '1':
                self.crear(data_actual, file_path)
            elif operation == '2':
                self.leer(data_actual, file_path)
            elif operation == '3':
                self.actualizar(data_actual, file_path)
            elif operation == '4':
                self.eliminar(data_actual, file_path)
            elif operation == '5':
                break
            else:
                print("Opción no válida, por favor intenta nuevamente.")

    def crear(self, data_actual, file_path):
        nuevo = self.set() 
        data_actual.create(nuevo)
        #aquí debo decidir, si lo mandó a llamar main_inscrito
        data_actual.to_json(file_path)
        print("hizo data_actual.to_json(file_path)")
        print(data_actual)

    def leer(self, data_actual, file_path):
        print("Contenido actual:")
        data_actual.read_json(file_path)
        print(data_actual.to_dictionary())

    def actualizar(self, data_actual, file_path):
        index = int(input("Introduce el índice del elemento a actualizar: "))
        if 0 <= index < len(data_actual.collection):
            nuevo = self.set() 
            data_actual.update(index, nuevo)
            data_actual.to_json(file_path)
        else:
            print("Índice fuera de rango.")

    def eliminar(self, data_actual, file_path):
        index = int(input("Introduce el índice del elemento a eliminar: "))
        if 0 <= index < len(data_actual.collection):
            print(f"Elemento a eliminar:\n{data_actual.collection[index].to_dictionary()}")
            confirm = input("¿Estás seguro? (s/n): ")
            if confirm.lower() == 's':
                data_actual.delete(index)
                data_actual.to_json(file_path)
                print("Elemento eliminado.")
            else:
                print("Operación cancelada.")
        else:
            print("Índice fuera de rango.")

