import json

class Cliente:
    def __init__(self, id_cliente=None, nombre=None, apellido_paterno=None, apellido_materno=None, direccion=None):
        self.modo_lista = all(arg is None for arg in (id_cliente, nombre, apellido_paterno, apellido_materno, direccion))

        if self.modo_lista:
            self.lista = []
        else:
            self.id_cliente = id_cliente
            self.nombre = nombre
            self.apellido_paterno = apellido_paterno
            self.apellido_materno = apellido_materno
            self.direccion = direccion

    def agregar_cliente(self, cliente):
        if cliente.modo_lista:
            raise ValueError("Una lista dentro de una lista? :^?")
        if self.modo_lista:
            self.lista.append(cliente)
        else:
            raise ValueError("Este objeto no está configurado como lista de clientes.")

    def eliminar_cliente(self, id_cliente):
        if self.modo_lista:
            self.lista = [cliente for cliente in self.lista if cliente.id_cliente != id_cliente]
        else:
            raise ValueError("Este objeto no está configurado como lista de clientes.")

    def modificar(self, cliente):
        if self.modo_lista:
            return False
        else:
            self.id_cliente = cliente.id_cliente
            self.nombre = cliente.nombre
            self.apellido_paterno = cliente.apellido_paterno
            self.apellido_materno = cliente.apellido_materno
            self.direccion = cliente.direccion
        return True

    def modificar_cliente(self, id_cliente, nuevo_cliente):
        if self.modo_lista:
            for i, cliente in enumerate(self.lista):
                if cliente.id_cliente == id_cliente:
                    self.lista[i] = nuevo_cliente
                    return
            raise ValueError(f"No se encontró un cliente con id {id_cliente}.")
        else:
            raise ValueError("Este objeto no está configurado como lista de clientes.")

    def mostrar(self, id_cliente=None):
        if self.modo_lista:
            if id_cliente is None:
                return [cliente.serializar() if isinstance(cliente, Cliente) else cliente for cliente in self.lista]
            for cliente in self.lista:
                if cliente.id_cliente == id_cliente:
                    return cliente.serializar()
            raise ValueError(f"Cliente con ID {id_cliente} no encontrada.")
        else:
            return self.serializar()

    def destruir(self):
        if self.modo_lista:
            self.lista = []
        else:
            self.id_cliente = None
            self.nombre = None
            self.apellido_paterno = None
            self.apellido_materno = None
            self.direccion = None

    def serializar(self):
        if self.modo_lista:
            return [cliente.serializar() for cliente in self.lista]
        else:
            return {
                "id_cliente": self.id_cliente,
                "nombre": self.nombre,
                "apellido_paterno": self.apellido_paterno,
                "apellido_materno": self.apellido_materno,
                "direccion": self.direccion
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
            self.lista = [Cliente(**cliente) for cliente in datos]
        else:
            new_cliente = Cliente(datos[0].get("id_cliente"), datos[0].get("nombre"), datos[0].get("apellido_paterno"), datos[0].get("apellido_materno"), datos[0].get("direccion"))
            return new_cliente

