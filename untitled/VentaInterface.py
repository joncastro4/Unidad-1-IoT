from venta import Venta
import os

class VentaInterface:
    def __init__(self, clientes=None, productos=None, ventas=None):
        self.modo_archivo = ventas is not None and clientes is None and productos is None
        self.ventas = ventas or Venta()
        self.clientes = clientes
        self.productos = productos
        if self.modo_archivo:
            self.cargar_ventas()

    def cargar_ventas(self):
        self.ventas.cargar("ventas.json")

    def guardar_ventas(self):
        if self.modo_archivo:
            self.ventas.guardar("ventas.json")

    def nueva_venta(self):
        id_venta = int(input("ID de la Venta: "))
        id_cliente = int(input("ID del Cliente: "))
        cliente = self.clientes.mostrar(id_cliente) if self.clientes else None
        if cliente:
            self.ventas.agregar_venta(Venta(id_venta, cliente))
            if self.modo_archivo:
                self.guardar_ventas()
        else:
            print("Cliente no encontrado.")

    def agregar_producto_a_venta(self):
        id_venta = int(input("ID de la Venta: "))
        id_producto = int(input("ID del Producto: "))
        producto = self.productos.mostrar(id_producto) if self.productos else None
        if producto:
            print(self.ventas.agregar_producto(producto, id_venta))
        else:
            print("Producto no encontrado.")

    def mostrar_todas_las_ventas(self):
        print(self.ventas.mostrar_venta())

    def menu_ventas(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("=== Menú Ventas ===")
            print("1. Agregar Venta")
            print("2. Agregar Producto a Venta")
            print("3. Mostrar Ventas")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.nueva_venta()
            elif opcion == "2":
                self.agregar_producto_a_venta()
            elif opcion == "3":
                self.mostrar_todas_las_ventas()
            elif opcion == "4":
                self.guardar_ventas()
                print("Ventas guardadas exitosamente.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")


if __name__ == "__main__":
    prod = VentaInterface(ventas=[])
    prod.menu_ventas()
