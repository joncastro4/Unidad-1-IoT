import json

class Producto:
    def __init__(self, id_producto=None, nombre=None, precio=None, marca=None, contenido=None):
        self.modo_lista = all(arg is None for arg in (id_producto, nombre, precio, marca, contenido))

        if self.modo_lista:
            self.lista = []
        else:
            self.id_producto = id_producto
            self.nombre = nombre
            self.precio = precio
            self.marca = marca
            self.contenido = contenido

    def agregar_producto(self, producto):
        if producto.modo_lista:
            raise ValueError("Una lista dentro de una lista? :^?")
        if self.modo_lista:
            self.lista.append(producto)
        else:
            raise ValueError("Este objeto no está configurado como lista de productos.")


    def eliminar_producto(self, id_producto):
        if self.modo_lista:
            self.lista = [producto for producto in self.lista if producto.id_producto != id_producto]
        else:
            raise ValueError("Este objeto no está configurado como lista de productos.")

    def modificar(self, producto):
        if self.modo_lista:
            return False
        else:
            self.id_producto = producto.id_producto
            self.nombre = producto.nombre
            self.precio = producto.precio
            self.marca = producto.marca
            self.contenido = producto.contenido
        return True

    def modificar_producto(self, id_producto, nuevo_producto):
        if self.modo_lista:
            for i, producto in enumerate(self.lista):
                if producto.id_producto == id_producto:
                    self.lista[i] = nuevo_producto
                    return
            raise ValueError(f"No se encontró un producto con id {id_producto}.")
        else:
            raise ValueError("Este objeto no está configurado como lista de productos.")

    def mostrar(self, id_producto=None):
        if self.modo_lista:
            if id_producto is None:
                return [producto.serializar() if isinstance(producto, Producto) else producto for producto in self.lista]
            for producto in self.lista:
                if producto.id_producto == id_producto:
                    return producto.serializar()
            raise ValueError(f"Producto con ID {id_producto} no encontrada.")
        else:
            return self.serializar()

    def destruir(self):
        if self.modo_lista:
            self.lista = []
        else:
            self.id_producto = None
            self.nombre = None
            self.precio = None
            self.marca = None
            self.contenido = None

    def serializar(self):
        if self.modo_lista:
            return [producto.serializar() for producto in self.lista]
        else:
            return {
                "id_producto": self.id_producto,
                "nombre": self.nombre,
                "precio": self.precio,
                "marca": self.marca,
                "contenido": self.contenido
            }

    def guardar(self, archivo):
        datos = self.serializar()
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

    def cargar(self, archivo):
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            resultado = self.convertir(datos)
            if resultado:
                self.__dict__.update(resultado.__dict__)
                return self
        except FileNotFoundError:
            raise ValueError(f"No se encontró el archivo {archivo}.")

    def convertir(self, datos):
        if isinstance(datos, list) and self.modo_lista:
            self.lista = [Producto(**producto) for producto in datos]
        else:
            return Producto(
                datos[0].get("id_producto"),
                datos[0].get("nombre"),
                datos[0].get("precio"),
                datos[0].get("marca"),
                datos[0].get("contenido")
            )

