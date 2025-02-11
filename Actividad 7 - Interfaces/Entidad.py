import json

class Entidad:
    def __init__(self):
        self.entidades = []

    def agregar(self, entidad):
        self.entidades.append(entidad)
        return True

    def ver(self):
        return self.entidades

    def modificar(self, index, nueva_entidad):
        if 0 <= index < len(self.entidades):
            self.entidades[index] = nueva_entidad
            return True
        return False

    def eliminar(self, index):
        if 0 <= index < len(self.entidades):
            entidad_eliminada = self.entidades.pop(index)
            return True
        return False
    
    def transformar_json(self, ruta):
        with open(ruta + ".json", 'w') as file:
            json.dump(self.diccionario(), file, indent=2)