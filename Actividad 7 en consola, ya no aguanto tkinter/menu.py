from interfaz_curso import ICurso

class Menu:
  def mostrar_menu(self):
    while True:
      print("1. Curso")
      print("2. Estudiantes")
      print("3. Inscritos")
      print("4. Salir")
      
      opcion = input("Seleccione una opción: ")
      
      try:
        opcion = int(opcion)
      except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

      if opcion == 1:
        curso = ICurso()
        curso.menu()
      elif opcion == 2:
        print("Opción Estudiantes seleccionada.")
      elif opcion == 3:
        print("Opción Inscritos seleccionada.")
      elif opcion == 4:
        print("Saliendo del programa...")
        break
      else:
        print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()
