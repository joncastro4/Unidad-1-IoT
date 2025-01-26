class Entidad:
    def __init__(self):
        self.entidades = []

    def agregar(self, entidad):
        self.entidades.append(entidad)
        return f"Entidad agregada: {entidad}"

    def ver(self):
        return self.entidades

    def modificar(self, index, nueva_entidad):
        if 0 <= index < len(self.entidades):
            self.entidades[index] = nueva_entidad
            return f"Entidad modificada: {nueva_entidad}"
        return "Índice fuera de rango."

    def eliminar(self, index):
        if 0 <= index < len(self.entidades):
            entidad_eliminada = self.entidades.pop(index)
            return f"Entidad eliminada: {entidad_eliminada}"
        return "Índice fuera de rango."