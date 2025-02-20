import json
from cliente import Cliente
from producto import Producto

class Venta:
    def __init__(self, id_venta=None, cliente=None):
        self.modo_lista = all(arg is None for arg in (id_venta, cliente))
        if self.modo_lista:
            self.ventas = []
        else:
            self.id_venta = id_venta
            self.cliente = cliente
            self.productos = Producto()  # Inicializa como lista de productos
            self.total = 0

    def agregar_venta(self, venta):
        if venta.modo_lista:
            raise ValueError("Una lista dentro de una lista? :^?")
        if self.modo_lista:
            if any(v.id_venta == venta.id_venta for v in self.ventas):
                raise ValueError(f"Ya existe una venta con ID {venta.id_venta}.")
            self.ventas.append(venta)
        else:
            raise ValueError("Este objeto no está configurado como lista de ventas.")

    def agregar_producto(self, producto, id_venta=None):
        if not isinstance(producto, Producto):
            raise ValueError("El producto debe ser un objeto de la clase Producto.")

        if self.modo_lista:
            for venta in self.ventas:
                if venta.id_venta == id_venta:
                    venta.productos.agregar_producto(producto)
                    venta.total = venta.calcular_total()
                    return f"Producto agregado a la venta con ID {id_venta}."
            raise ValueError(f"Venta con ID {id_venta} no encontrada.")
        else:
            self.productos.agregar_producto(producto)
            self.total = self.calcular_total()
            return "Producto agregado a la venta única."

    def mostrar_venta(self, id_venta=None):
        if self.modo_lista:
            if id_venta is None:
                return [venta.serializar() for venta in self.ventas]
            for venta in self.ventas:
                if venta.id_venta == id_venta:
                    return venta.serializar()
            raise ValueError(f"Venta con ID {id_venta} no encontrada.")
        else:
            return self.serializar()

    def destruir_venta(self, id_venta=None):
        if self.modo_lista:
            if id_venta is None:
                self.ventas = []
                return "Todas las ventas han sido eliminadas."
            for venta in self.ventas:
                if venta.id_venta == id_venta:
                    self.ventas.remove(venta)
                    return f"Venta con ID {id_venta} eliminada correctamente."
            raise ValueError(f"Venta con ID {id_venta} no encontrada.")
        else:
            self.productos.destruir()
            self.total = 0
            return "Venta única destruida correctamente."

    def calcular_total(self, id_venta=None):
        if self.modo_lista:
            for venta in self.ventas:
                if venta.id_venta == id_venta:
                    return sum(p.precio for p in venta.productos.lista)
            raise ValueError(f"Venta con ID {id_venta} no encontrada.")
        else:
            return sum(p.precio for p in self.productos.lista)

    def serializar(self):
        if self.modo_lista:
            return [venta.serializar() for venta in self.ventas]
        else:
            return {
                "id_venta": self.id_venta,
                "cliente": self.cliente.serializar() if isinstance(self.cliente, Cliente) else self.cliente,
                "productos": self.productos.serializar(),  # Serializa la lista de productos
                "total": self.total
            }

    def guardar(self, archivo):
        datos = self.serializar()
        with open(archivo, "w", encoding="utf-8") as f:
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
            self.ventas = [Venta(
                id_venta=venta.get("id_venta"),
                cliente=Cliente(**venta.get("cliente"))
            ) for venta in datos]
            for venta, data in zip(self.ventas, datos):
                venta.productos = Producto()
                venta.productos.convertir(data.get("productos"))
                for detalle in venta.productos.lista:
                    venta.productos.agregar_producto(Producto(**detalle))
                venta.total = data.get("total", 0)
        else:
            new_venta = Venta(datos[0].get("id_venta"), datos[0].get("cliente", {}))
            new_prod = datos[0].get("productos", [])
            for prod in new_prod:
                new_venta.agregar_producto(prod)
            return new_venta
