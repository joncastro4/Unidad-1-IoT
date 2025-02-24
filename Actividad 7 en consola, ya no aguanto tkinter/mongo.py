import json
import os
from pymongo import MongoClient


class Lista:
    def __init__(self):
        self.items = []

    def __str__(self):
        return "\n".join([str(item) for item in self.items])

    def agregar(self, item):
        self.items.append(item)

    def editar(self, indice, nuevo_item):
        if 0 <= indice < len(self.items):
            self.items[indice] = nuevo_item
        else:
            return None

    def eliminar(self, indice):
        if 0 <= indice < len(self.items):
            del self.items[indice]
        else:
            return None
    
    def to_json(self, directory, file_name):
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, file_name)
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump([item.to_dict() for item in self.items], json_file, ensure_ascii=False, indent=4)
            
    def from_json(self, directory="output", file_name="default.json", obj_class=None):
        file_path = os.path.join(directory, file_name)

        if not os.path.exists(file_path):
            print(f"El archivo {file_path} no existe.")
            return None

        if os.path.getsize(file_path) == 0:
            print(f"El archivo {file_path} está vacío.")
            return None

        try:
            with open(file_path, "r", encoding="utf-8") as json_file:
                items_dicts = json.load(json_file)
        except json.JSONDecodeError as e:
            print(f"Error al decodificar el archivo JSON: {e}")
            return None

        if isinstance(items_dicts, list):
            return self.convertir_a_objetos(items_dicts, obj_class)  
        else:
            return None

    def convertir_a_objetos(self, items_dicts, obj_class):
        for item_dict in items_dicts:
            # Convertir el campo 'curso' de dict a Curso
            if 'curso' in item_dict:
                from curso import Curso 
                item_dict['curso'] = Curso(**item_dict['curso'])
        
            # Convertir la lista de estudiantes de dicts a Estudiante
            if 'estudiantes' in item_dict:
                from estudiante import Estudiante 
                estudiantes = Estudiante()  # Crear una lista de estudiantes
                if isinstance(item_dict['estudiantes'], list):  # Verificar si es una lista
                    for est_dict in item_dict['estudiantes']:
                        if isinstance(est_dict, dict):  # Verificar si es un diccionario
                            estudiantes.agregar(Estudiante(**est_dict))
                        else:
                            print(f"Advertencia: Se encontró un estudiante no válido: {est_dict}")
                else:
                    print(f"Advertencia: El campo 'estudiantes' no es una lista: {item_dict['estudiantes']}")
                item_dict['estudiantes'] = estudiantes
        
            # Crear el objeto Inscripcion
            self.agregar(obj_class(**item_dict))
        return self 
    
    def guardar_en_mongodb(self, database_name="universidad", collection_name="inscripciones"):

        mongo_uri = "mongodb+srv://myAtlasDBUser:sssabsdefg@myatlasclusteredu.hhf3j.mongodb.net/?retryWrites=true&w=majority"

        try:
            client = MongoClient(mongo_uri)
            db = client[database_name]
            collection = db[collection_name] 

            datos_json = [item.to_dict() for item in self.items]

            if datos_json:
                collection.insert_many(datos_json)
                print(f"{len(datos_json)} documentos guardados en MongoDB Atlas en la colección '{collection_name}'")
            else:
                print("No hay datos para guardar en MongoDB")

        except Exception as e:
            print(f"Error al conectar a MongoDB Atlas: {e}")
            self.to_json("outputCopia", f"{collection_name}_temporal.json")
          
        finally:
            client.close()
    
    def verificar_conexion_mongodb(self, database_name="universidad", collection_name="inscripciones"):
        mongo_uri = "mongodb+srv://myAtlasDBUser:absdefg@myatlasclusteredu.hhf3j.mongodb.net/?retryWrites=true&w=majority"

        if not mongo_uri:
            print("Error: No se encontró la URI de MongoDB en el archivo .env")
            return False

        archivo_temporal = os.path.join("outputCopia", f"{collection_name}_temporal.json")
        print(f"Buscando archivo: {archivo_temporal}")

        try:
            with MongoClient(mongo_uri) as client:
                client.server_info()
                print("Conexión a MongoDB Atlas exitosa.")

                if os.path.exists(archivo_temporal):
                    with open(archivo_temporal, "r") as f:
                        datos_json = json.load(f)

                    if datos_json:
                        db = client[database_name]
                        collection = db[collection_name]

                        collection.insert_many(datos_json)
                        print(f"{len(datos_json)} documentos recuperados y guardados en MongoDB Atlas, reemplazando los anteriores.")

                        try:
                            os.remove(archivo_temporal)
                            print(f"Archivo temporal '{archivo_temporal}' eliminado correctamente.")
                        except Exception as e:
                            print(f"Advertencia: No se pudo eliminar el archivo temporal '{archivo_temporal}': {e}")

            return True

        except Exception as e:
            print(f"❌ Error al conectar a MongoDB Atlas: {e}")
            return False