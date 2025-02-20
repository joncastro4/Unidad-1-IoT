import json

class Clase:
    def __init__(self):
        self.collection = []
        self.is_single_object = False

    def create(self, obj):
        self.collection.append(obj)
        return f"Agregada: {obj}"

    def update(self, index, new_single_object):
        if 0 <= index < len(self.collection):
            self.collection[index] = new_single_object
            return f"Modificada:\n{new_single_object}"
        return "Fuera de rango."

    def delete(self, index):
        if 0 <= index < len(self.collection):
            old_single_object = self.collection.pop(index)
            return f"Eliminada:\n{old_single_object}"
        return "Índice fuera de rango."

# --------------------------------------------------------------------------------------------			

    def to_json(self, path):
        if not path.endswith(".json"):
            path += ".json"
        with open(path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.to_dictionary(), ensure_ascii=False, indent=2))

    def read_json(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return self.to_object(data)
        
# --------------------------------------------------------------------------------------------			
        
    def get_class(self, data):
        from inscrito import Inscrito, Estudiante, Curso
        if isinstance(data, list):
            if all('nombre_curso' in item for item in data):
                return Curso
            elif all('nombre' in item for item in data):
                return Estudiante
            elif all('curso' in item and 'estudiantes' in item for item in data):
                return Inscrito
        elif isinstance(data, dict):
            if 'nombre_curso' in data:
                return Curso
            elif 'nombre' in data:
                return Estudiante
            elif 'curso' in data and 'estudiantes' in data:
                return Inscrito
        raise ValueError("Clase desconocida")

# --------------------------------------------------------------------------------------------	
  

    def to_object(self, data):
        self_class = self.get_class(data)
        from inscrito import Inscrito

        if isinstance(data, dict):
            if self_class is Inscrito:
                return self._process_inscrito(data)
            else:
                obj = self_class(**data)
                return obj
        elif isinstance(data, list):
            if self_class is Inscrito:
                inscrito_coleccion = self_class()
                for item in data:
                    inscrito_coleccion.create(self._process_inscrito(item))
                return inscrito_coleccion
            else:
                self.collection = [self_class(**item) for item in data]
                return self
        else:
            raise ValueError("Formato JSON inválido.")

    def _process_inscrito(self, data):
        curso_data = data.get("curso")
        estudiantes_data = data.get("estudiantes", [])

        curso_class = self.get_class({"nombre_curso": ""})
        estudiante_class = self.get_class([{"nombre": ""}])

        curso = curso_class(**curso_data) if curso_data else None

        estudiantes_coleccion = estudiante_class()
        for estudiante_data in estudiantes_data:
            estudiante = estudiante_class(**estudiante_data)
            estudiantes_coleccion.create(estudiante)

        inscrito_class = self.get_class({"curso": {}, "estudiantes": []})
        return inscrito_class(estudiantes_coleccion, curso)