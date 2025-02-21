from producto import Producto
import os

class ProductoInterface:
    def __init__(self, productos=None):
        self.modo_archivo = productos is None
        self.productos = productos if productos else Producto()
        if self.modo_archivo:
            self.cargar_productos()

    def cargar_productos(self):
        self.productos.cargar("productos.json")

    def guardar_productos(self):
        if self.modo_archivo:
            self.productos.guardar("productos.json")

    def nuevo_producto(self):
        id_producto = int(input("ID del Producto: "))
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        marca = input("Marca: ")
        contenido = input("Contenido: ")
        return Producto(id_producto, nombre, precio, marca, contenido)

    def menu_productos(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("=== Menú Productos ===")
            print("1. Agregar Producto")
            print("2. Mostrar Productos")
            print("3. Eliminar Producto")
            print("4. Modificar Producto")
            print("5. Destruir Todos")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.productos.agregar_producto(self.nuevo_producto())
                if self.modo_archivo:
                    self.guardar_productos()
            elif opcion == "2":
                print(self.productos.mostrar())
            elif opcion == "3":
                id_producto = int(input("ID del producto a eliminar: "))
                self.productos.eliminar_producto(id_producto)
            elif opcion == "4":
                id_producto = int(input("ID del producto a modificar: "))
                self.productos.modificar_producto(id_producto, self.nuevo_producto())
            elif opcion == "5":
                self.productos.destruir()
                if self.modo_archivo:
                    self.guardar_productos()
                print("Todos los productos fueron eliminados.")
            elif opcion == "6":
                self.guardar_productos()
                print("Productos guardados exitosamente.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    prod = ProductoInterface(productos=[])
    prod.menu_productos()
