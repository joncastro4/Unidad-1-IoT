from cliente import Cliente

class TestCliente:
    @staticmethod
    def ejecutar():
        print("=== Iniciando pruebas de la clase Cliente ===\n")

        clientes = Cliente()
        clientes.agregar_cliente(Cliente(1, "Erick", "Rangel", "Vazquez", "Sol de Oriente"))
        clientes.guardar("clientes.json")
        clientes.cargar("clientes.json")

        print("Clientes cargados desde archivo:")
        print(clientes.mostrar())

        print("Agregando otro cliente...")
        clientes.agregar_cliente(Cliente(2, "Daniel", "Rangel", "Lopez", "Sol de Oriente"))
        clientes.guardar("clientes.json")

        el_solo_cliente = Cliente(9, "", "", "", "")
        el_solo_cliente = el_solo_cliente.cargar("clientes.json")

        print("Cargando cliente único:")
        print(el_solo_cliente.mostrar())

if __name__ == "__main__":
    TestCliente.ejecutar()
