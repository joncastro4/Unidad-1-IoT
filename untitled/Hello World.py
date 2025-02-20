from ClienteInterface import ClienteInterface
from ProductoInterface import ProductoInterface
from VentaInterface import VentaInterface
import os
import subprocess

class Main:
    def __init__(self):
        self.cliente_interface = ClienteInterface(clientes=[])
        self.producto_interface = ProductoInterface(productos=[])
        self.venta_interface = VentaInterface(
            clientes=self.cliente_interface.clientes,
            productos=self.producto_interface.productos,
            ventas=[]
        )
        self.cargar_datos()

    def cargar_datos(self):
        self.cliente_interface.cargar_clientes()
        self.producto_interface.cargar_productos()
        self.venta_interface.cargar_ventas()

    def guardar_datos(self):
        self.cliente_interface.guardar_clientes()
        self.producto_interface.guardar_productos()
        self.venta_interface.guardar_ventas()

    def ejecutar(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("=== Menú Principal ===")
            print("1. Gestión de Clientes")
            print("2. Gestión de Productos")
            print("3. Gestión de Ventas")
            print("4. Salir")
            print("5. Ejecutar Pruebas")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.cliente_interface.menu_clientes()
            elif opcion == "2":
                self.producto_interface.menu_productos()
            elif opcion == "3":
                self.venta_interface.menu_ventas()
            elif opcion == "4":
                self.guardar_datos()
                print("Datos guardados. Saliendo...")
                break
            elif opcion == "5":
                print("Ejecutando pruebas...")
                subprocess.run(["python", "TestCliente.py"])
                subprocess.run(["python", "TestProducto.py"])
                subprocess.run(["python", "TestVenta.py"])
                print("Pruebas finalizadas.")
            else:
                print("Opción no válida. Intente de nuevo.")

            input("Presione Enter para continuar...")

if __name__ == "__main__":
    programa = Main()
    programa.ejecutar()
