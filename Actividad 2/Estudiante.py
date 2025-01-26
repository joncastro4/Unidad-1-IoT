from Entidad import Entidad

class Estudiante(Entidad):
  def __init__(self, nombre = None, apellido_paterno = None, apellido_materno = None, fecha_nacimiento = None, telefono = None):
    self.isObject = nombre and apellido_paterno and apellido_materno and fecha_nacimiento and telefono

    if self.isObject:
      self.nombre = nombre
      self.apellido_paterno = apellido_paterno
      self.apellido_materno = apellido_materno
      self.fecha_nacimiento = fecha_nacimiento
      self.telefono = telefono
    else:
      super().__init__()

  def __str__(self):
    if self.isObject:
      return f"Estudiante: {self.nombre}, Apellido Paterno: {self.apellido_paterno}, Apellido Materno: {self.apellido_materno}, Fecha de Nacimiento: {self.fecha_nacimiento}, Telefono: {self.telefono}"
    else:
      return f"Cantidad de estudiantes: {len(self.entidades)}"

if __name__ == "__main__":
  estudiantes = Estudiante(None, None, None, None, None)

  estudiante1 = Estudiante("Estudiante 1", "Apellido Paterno 1", "Apellido Materno 1", "1990-01-01", "1234567890")
  estudiante2 = Estudiante("Estudiante 2", "Apellido Paterno 2", "Apellido Materno 2", "1991-02-15", "9876543210")

  print(estudiantes.agregar(estudiante1))
  print(estudiantes.agregar(estudiante2))

  for estudiante in estudiantes.ver():
    print(estudiante)

  estudiante_modificado = Estudiante("Estudiante Modificado", "Apellido Paterno Modificado", "Apellido Materno Modificado", "1992-03-01", "5555555555")
  print(estudiantes.modificar(1, estudiante_modificado))

  for estudiante in estudiantes.ver():
    print(estudiante)

  print(estudiantes.eliminar(0))

  for estudiante in estudiantes.ver():
    print(estudiante)
