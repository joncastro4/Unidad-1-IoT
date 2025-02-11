import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
from Estudiante import Estudiante

class VentanasEstudiantes:
    def __init__(self, root):
        self.root = root
        self.estudiantes = Estudiante()
        json = self.estudiantes.obtener_json()
        self.estudiantes.json_a_objeto(json)

    def ventana_estudiantes(self):
        ventana_estudiante = tk.Toplevel(self.root)
        ventana_estudiante.title("Estudiantes")
        ventana_estudiante.geometry("200x300")

        tk.Button(ventana_estudiante, text="Insertar", command=self.ventana_insertar).pack(pady=10)
        tk.Button(ventana_estudiante, text="Ver", command=self.ventana_ver).pack(pady=10)
        tk.Button(ventana_estudiante, text="Modificar", command=self.ventana_modificar).pack(pady=10)
        tk.Button(ventana_estudiante, text="Eliminar", command=self.ventana_eliminar).pack(pady=10)
        tk.Button(ventana_estudiante, text="Menú", command=ventana_estudiante.destroy).pack(pady=10)

    def ventana_insertar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar estudiante")
        ventana.geometry("500x500")

        tk.Label(ventana, text="Nombre:").pack(pady=10)
        input_nombre = tk.Entry(ventana).pack(pady=5)

        tk.Label(ventana, text="Apellido paterno:").pack(pady=10)
        input_apellido_paterno = tk.Entry(ventana).pack(pady=5)

        tk.Label(ventana, text="Apellido Materno:").pack(pady=10)
        input_apellido_materno = tk.Entry(ventana).pack(pady=5)

        tk.Label(ventana, text="Fecha de nacimiento:").pack(pady=10)
        input_fecha_nacimiento = tk.Entry(ventana).pack(pady=5)

        tk.Label(ventana, text="Telefono:").pack(pady=10)
        input_telefono = tk.Entry(ventana).pack(pady=5)

        def agregar_estudiante():
            nombre = input_nombre.get()
            apellido_paterno = input_apellido_paterno.get()
            apellido_materno = input_apellido_materno.get()
            fecha_nacimiento = input_fecha_nacimiento.get()
            telefono = input_telefono.get()

            if not nombre or not apellido_paterno or not apellido_materno or not fecha_nacimiento or not telefono:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
            
            if not re.match(r"^[a-zA-Z0-9\sáéíóúÁÉÍÓÚüÜñÑ]+$", nombre):
                messagebox.showerror("Error", "El nombre solo puede contener letras, números, espacios y acentos")
                return
            
            if not re.match(r"^[a-zA-Z0-9\sáéíóúÁÉÍÓÚüÜñÑ]+$", apellido_paterno):
                messagebox.showerror("Error", "El apellido paterno solo puede contener letras, números, espacios y acentos")
                return
            
            if not re.match(r"^[a-zA-Z0-9\sáéíóúÁÉÍÓÚüÜñÑ]+$", apellido_materno):
                messagebox.showerror("Error", "El apellido materno solo puede contener letras, números, espacios y acentos")
                return
            
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", fecha_nacimiento):
                messagebox.showerror("Error", "La fecha de nacimiento debe estar en formato YYYY-MM-DD")
                return
            
            if not re.match(r"^\d{10}$", telefono):
                messagebox.showerror("Error", "El teléfono debe contener 10 dígitos")
                return
            
            if self.estudiantes.agregar(Estudiante(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono)):
                self.estudiantes.transformar_json("estudiante")
                messagebox.showinfo("Información", "Estudiante agregado correctamente")
            else:
                messagebox.showerror("Error", "Error al agregar el estudiante")

        tk.Button(ventana, text="Guardar", command=agregar_estudiante).pack(pady=20)

    def ventana_modificar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Modificar Estudiante")
        ventana.geometry("500x500")

        tk.Label(ventana, text="ID:").pack(pady=5)
        input_id = tk.Entry(ventana)
        input_id.pack(pady=5)

        tk.Label(ventana, text="Nombre:").pack(pady=10)
        input_nombre = tk.Entry(ventana)
        input_nombre.pack(pady=5)

        tk.Label(ventana, text="Apellido paterno:").pack(pady=10)
        input_apellido_paterno = tk.Entry(ventana)
        input_apellido_paterno.pack(pady=5)

        tk.Label(ventana, text="Apellido Materno:").pack(pady=10)
        input_apellido_materno = tk.Entry(ventana)
        input_apellido_materno.pack(pady=5)

        tk.Label(ventana, text="Fecha de nacimiento:").pack(pady=10)
        input_fecha_nacimiento = tk.Entry(ventana)
        input_fecha_nacimiento.pack(pady=5)

        tk.Label(ventana, text="Telefono:").pack(pady=10)
        input_telefono = tk.Entry(ventana)
        input_telefono.pack(pady=5)

        def modificar_estudiante():
            index = input_id.get()
            
            nombre = input_nombre.get()
            apellido_paterno = input_apellido_paterno.get()
            apellido_materno = input_apellido_materno.get()
            fecha_nacimiento = input_fecha_nacimiento.get()
            telefono = input_telefono.get()

            if not index.isdigit():
                messagebox.showerror("Error", "El ID debe ser un número entero")
                return

            if not all([nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono]):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]+$", nombre):
                messagebox.showerror("Error", "El nombre solo puede contener letras y espacios")
                return

            if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]+$", apellido_paterno):
                messagebox.showerror("Error", "El apellido paterno solo puede contener letras y espacios")
                return

            if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]+$", apellido_materno):
                messagebox.showerror("Error", "El apellido materno solo puede contener letras y espacios")
                return

            if not re.match(r"^\d{4}-\d{2}-\d{2}$", fecha_nacimiento):
                messagebox.showerror("Error", "La fecha de nacimiento debe estar en formato YYYY-MM-DD")
                return

            if not re.match(r"^\d{10}$", telefono):
                messagebox.showerror("Error", "El teléfono debe contener exactamente 10 dígitos numéricos")
                return

            if not self.estudiantes.modificar(int(index), Estudiante(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono)):
                messagebox.showerror("Error", "ID no encontrado")
                return
            
            self.estudiantes.transformar_json("estudiante")
            messagebox.showinfo("Información", "Estudiante modificado correctamente")
        
        btn_guardar = tk.Button(ventana, text="Guardar", command=modificar_estudiante)
        btn_guardar.pack(pady=20)

    def ventana_eliminar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Eliminar Estudiante")
        ventana.geometry("500x500")

        tk.Label(ventana, text="ID:").pack(pady=5)
        input_id = tk.Entry(ventana).pack(pady=5)

        def eliminar_estudiante():
            estudiante_id = input_id.get()

            if not estudiante_id.isdigit():
                messagebox.showerror("Error", "El ID debe ser un número entero")
                return

            if self.estudiantes.eliminar(int(estudiante_id)):
                self.estudiantes.transformar_json("estudiante")
                messagebox.showinfo("Información", "Estudiante eliminado correctamente")
            else:
                messagebox.showerror("Error", "Estudiante no encontrado")

        btn_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_estudiante)
        btn_eliminar.pack(pady=20)

    def ventana_ver(self):
        ventana = tk.Toplevel()
        ventana.title("Ver Estudiantes")
        ventana.geometry("1050x600")

        estudiantes = self.estudiantes.ver()
        
        if not estudiantes:
            tk.Label(ventana, text="No hay estudiantes registrados").pack(pady=10)
            return
        
        frame = tk.Frame(ventana)
        frame.pack(pady=10, fill=tk.BOTH, expand=True)

        cols = ("ID", "Nombre", "Apellido Paterno", "Apellido Materno", "Fecha nacimiento", "Teléfono")
        tree = ttk.Treeview(frame, columns=cols, show="headings")
        
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=200 if col != "ID" else 50, anchor="center")
        
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        tree.pack(side="left", fill=tk.BOTH, expand=True)

        for idx, estudiante in enumerate(estudiantes):
            tree.insert("", "end", values=(idx, estudiante.nombre, estudiante.apellido_paterno, estudiante.apellido_materno, estudiante.fecha_nacimiento, estudiante.telefono))