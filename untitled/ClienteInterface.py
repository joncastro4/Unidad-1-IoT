from cliente import Cliente
import os

class ClienteInterface:
    def __init__(self, clientes=None):
        self.modo_archivo = clientes is None
        self.clientes = clientes if clientes else Cliente()
        if self.modo_archivo:
            self.cargar_clientes()
    def cargar_clientes(self):
        self.clientes.cargar("clientes.json")

    def guardar_clientes(self):
        if self.modo_archivo:
            self.clientes.guardar("clientes.json")

    def solicitar_datos_cliente(self):
        id_cliente = int(input("ID del Cliente: "))
        nombre = input("Nombre: ")
        apellido_paterno = input("Apellido Paterno: ")
        apellido_materno = input("Apellido Materno: ")
        direccion = input("Dirección: ")
        return Cliente(id_cliente, nombre, apellido_paterno, apellido_materno, direccion)

    def solicitar_modificacion_cliente(self):
        id_cliente = int(input("ID del Cliente a modificar: "))
        nuevo_cliente = self.solicitar_datos_cliente()
        return id_cliente, nuevo_cliente

    def menu_clientes(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print("=== Menú Clientes ===")
            print("1. Agregar Cliente")
            print("2. Mostrar Clientes")
            print("3. Eliminar Cliente")
            print("4. Modificar Cliente")
            print("5. Destruir Clientes")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.clientes.agregar_cliente(self.solicitar_datos_cliente())
                self.guardar_clientes()
            elif opcion == "2":
                print(self.clientes.mostrar())
            elif opcion == "3":
                id_cliente = int(input("ID del Cliente a eliminar: "))
                self.clientes.eliminar_cliente(id_cliente)
                self.guardar_clientes()
            elif opcion == "4":
                id_cliente, nuevo_cliente = self.solicitar_modificacion_cliente()
                self.clientes.modificar_cliente(id_cliente, nuevo_cliente)
                self.guardar_clientes()
            elif opcion == "5":
                self.clientes.destruir()
                self.guardar_clientes()
                print("Todos los clientes fueron eliminados.")
            elif opcion == "6":
                self.guardar_clientes()
                print("Clientes guardados exitosamente.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    cli = ClienteInterface(clientes=[])
    cli.menu_clientes()
