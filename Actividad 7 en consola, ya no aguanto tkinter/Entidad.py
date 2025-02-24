import json
import os
from pymongo import MongoClient

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
    
    def transformar_json(self, ruta):
        with open(ruta + ".json", 'w') as file:
            json.dump(self.diccionario(), file, indent=2)
    def to_json(self, directory, file_name):
            if not os.path.exists(directory):
                os.makedirs(directory)

            file_path = os.path.join(directory, file_name)
            with open(file_path, "w", encoding="utf-8") as json_file:
                json.dump([item.to_dict() for item in self.entidades], json_file, ensure_ascii=False, indent=4)
    
    
    def guardar_en_mongodb(self, database_name="universidad", collection_name="inscripciones"):

        mongo_uri = "mongodb+srv://myAtlasDBUser:absdefg@myatlasclusteredu.hhf3j.mongodb.net/?retryWrites=true&w=majority"

        try:
            client = MongoClient(mongo_uri)
            db = client[database_name]
            collection = db[collection_name] 

            datos_json = [item.diccionario() for item in self.entidades]

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