from producto import Producto

class TestProducto:
    @staticmethod
    def ejecutar():
        print("=== Iniciando pruebas de la clase Producto ===\n")

        productos = Producto()
        productos.agregar_producto(Producto(101, "Nitro", 10.99, "Adonis", 100))
        productos.guardar("productos.json")
        productos.cargar("productos.json")

        print("Productos cargados desde archivo:")
        print(productos.mostrar())

        print("Agregando otro producto...")
        productos.agregar_producto(Producto(102, "Boostane", 10.99, "Laravel", 100))
        productos.guardar("productos.json")

        el_solo_producto = Producto(9, "", 10, "", "")
        el_solo_producto = el_solo_producto.cargar("productos.json")

        print("Cargando producto único:")
        print(el_solo_producto.mostrar())

if __name__ == "__main__":
    TestProducto.ejecutar()
