from cliente import Cliente
from venta import Venta

class TestVenta:
    @staticmethod
    def ejecutar():
        print("=== Iniciando pruebas de la clase Venta ===\n")

        clientes = Cliente()
        clientes.agregar_cliente(Cliente(1, "Erick", "Rangel", "Vazquez", "Sol de Oriente"))

        ventas = Venta()
        ventas.agregar_venta(Venta(1, clientes.mostrar(1)))
        ventas.guardar("ventas.json")
        ventas.cargar("ventas.json")

        print("Ventas cargadas desde archivo:")
        print(ventas.mostrar_venta())

        print("Agregando otra venta...")
        ventas.agregar_venta(Venta(2, clientes.mostrar(1)))
        ventas.guardar("ventas.json")

        el_solo_venta = Venta(9, clientes.mostrar(1))
        el_solo_venta = el_solo_venta.cargar("ventas.json")

        print("Cargando venta única:")
        print(el_solo_venta.mostrar_venta())

if __name__ == "__main__":
    TestVenta.ejecutar()
