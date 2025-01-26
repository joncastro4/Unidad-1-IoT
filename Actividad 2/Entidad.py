class Entidad:
    def __init__(self):
        self.entidades = []

    def agregar(self, entidad):
        self.entidades.append(entidad)
        if hasattr(self, "entidades"):
            return True
        return False

    def eliminar(self, i):
        if hasattr(self, "entidades") and 0 <= i < len(self.entidades):
            del self.entidades[i]
            return f"Entidad eliminada"
        return f"Índice no válido o no existen entidades"

    def modificar(self, i, entidad_modificada):
        if hasattr(self, "entidades") and 0 <= i < len(self.entidades):
            self.entidades[i] = entidad_modificada
            return f"Entidad modificada"

    def ver(self):
        if not hasattr(self, "entidades") or not self.entidades:
            return ["No hay entidades disponibles"]
        return [str(entidad) for entidad in self.entidades]
