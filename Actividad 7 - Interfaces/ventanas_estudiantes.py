import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Estudiante import Estudiante

class VentanasEstudiantes:
    def __init__(self, root, estudiantes=None):
        self.root = root
        
        if estudiantes is None:
            self.isJson = True
            self.estudiantes = Estudiante()
            self.estudiantes.json_a_objeto(self.estudiantes.obtener_json())
        else:
            self.isJson = False
            self.estudiantes = estudiantes

    def ventana_estudiantes(self):
        ventana_estudiante = tk.Toplevel(self.root)
        ventana_estudiante.overrideredirect(True)
        ventana_estudiante.title("Estudiantes")
        ventana_estudiante.geometry("200x300")

        tk.Button(ventana_estudiante, text="Insertar", command=self.ventana_insertar).pack(pady=10)
        tk.Button(ventana_estudiante, text="Ver", command=self.ventana_ver).pack(pady=10)
        tk.Button(ventana_estudiante, text="Modificar", command=self.ventana_modificar).pack(pady=10)
        tk.Button(ventana_estudiante, text="Eliminar", command=self.ventana_eliminar).pack(pady=10)
        
        def cerrar():
            if self.isJson:
                self.estudiantes.transformar_json("estudiante")
            ventana_estudiante.destroy()
        
        tk.Button(ventana_estudiante, text="Menú", command=cerrar).pack(pady=10)

    def ventana_insertar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Estudiante")
        ventana.geometry("500x500")

        tk.Label(ventana, text="Nombre:").pack(pady=5)
        input_nombre = tk.Entry(ventana)
        input_nombre.pack(pady=5)

        tk.Label(ventana, text="Apellido Paterno:").pack(pady=5)
        input_apellido_paterno = tk.Entry(ventana)
        input_apellido_paterno.pack(pady=5)

        tk.Label(ventana, text="Apellido Materno:").pack(pady=5)
        input_apellido_materno = tk.Entry(ventana)
        input_apellido_materno.pack(pady=5)

        tk.Label(ventana, text="Fecha de Nacimiento:").pack(pady=5)
        input_fecha_nacimiento = tk.Entry(ventana)
        input_fecha_nacimiento.pack(pady=5)

        tk.Label(ventana, text="Teléfono:").pack(pady=5)
        input_telefono = tk.Entry(ventana)
        input_telefono.pack(pady=5)

        def agregar_estudiante():
            nombre = input_nombre.get()
            apellido_paterno = input_apellido_paterno.get()
            apellido_materno = input_apellido_materno.get()
            fecha_nacimiento = input_fecha_nacimiento.get()
            telefono = input_telefono.get()

            if not nombre or not apellido_paterno or not apellido_materno or not fecha_nacimiento or not telefono:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            if self.estudiantes.agregar(Estudiante(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono)):
                messagebox.showinfo("Información", "Estudiante agregado correctamente")
            else:
                messagebox.showerror("Error", "Error al agregar el estudiante")

        tk.Button(ventana, text="Guardar", command=agregar_estudiante).pack(pady=20)

    def ventana_ver(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Ver Estudiantes")
        ventana.geometry("1050x600")

        if not self.estudiantes.ver():
            tk.Label(ventana, text="No hay estudiantes").pack(pady=10)
        else:
            frame = tk.Frame(ventana)
            frame.pack(pady=10, fill=tk.BOTH, expand=True)

            cols = ("ID", "Nombre", "Apellido Paterno", "Apellido Materno", "Fecha de Nacimiento", "Teléfono")
            tree = ttk.Treeview(frame, columns=cols, show="headings")
            
            for col in cols:
                tree.heading(col, text=col)
                tree.column(col, width=200, anchor="center")
            
            scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.pack(side="right", fill="y")
            tree.pack(side="left", fill=tk.BOTH, expand=True)
            
            for i, estudiante in enumerate(self.estudiantes.ver()):
                tree.insert("", "end", values=(i, estudiante.nombre, estudiante.apellido_paterno, estudiante.apellido_materno, estudiante.fecha_nacimiento, estudiante.telefono))

    def ventana_modificar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Modificar Estudiante")
        ventana.geometry("500x500")

        tk.Label(ventana, text="ID:").pack(pady=5)
        input_id = tk.Entry(ventana)
        input_id.pack(pady=5)

        tk.Label(ventana, text="Nombre:").pack(pady=5)
        input_nombre = tk.Entry(ventana)
        input_nombre.pack(pady=5)

        tk.Label(ventana, text="Apellido Paterno:").pack(pady=5)
        input_apellido_paterno = tk.Entry(ventana)
        input_apellido_paterno.pack(pady=5)

        tk.Label(ventana, text="Apellido Materno:").pack(pady=5)
        input_apellido_materno = tk.Entry(ventana)
        input_apellido_materno.pack(pady=5)

        tk.Label(ventana, text="Fecha de Nacimiento:").pack(pady=5)
        input_fecha_nacimiento = tk.Entry(ventana)
        input_fecha_nacimiento.pack(pady=5)

        tk.Label(ventana, text="Teléfono:").pack(pady=5)
        input_telefono = tk.Entry(ventana)
        input_telefono.pack(pady=5)

        def modificar_estudiante():
            index = input_id.get()
            if not index.isdigit():
                messagebox.showerror("Error", "El ID debe ser un número entero")
                return
            index = int(index)

            nombre = input_nombre.get()
            apellido_paterno = input_apellido_paterno.get()
            apellido_materno = input_apellido_materno.get()
            fecha_nacimiento = input_fecha_nacimiento.get()
            telefono = input_telefono.get()

            if not nombre or not apellido_paterno or not apellido_materno or not fecha_nacimiento or not telefono:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            if self.estudiantes.modificar(index, Estudiante(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, telefono)):
                messagebox.showinfo("Información", "Estudiante modificado correctamente")
            else:
                messagebox.showerror("Error", "El estudiante no se pudo modificar")

        tk.Button(ventana, text="Guardar", command=modificar_estudiante).pack(pady=20)

    def ventana_eliminar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Eliminar Estudiante")
        ventana.geometry("500x500")

        tk.Label(ventana, text="ID:").pack(pady=5)
        input_id = tk.Entry(ventana)
        input_id.pack(pady=5)

        def eliminar_estudiante():
            estudiante = input_id.get()
            if not estudiante.isdigit():
                messagebox.showerror("Error", "El ID debe ser un número entero")
                return

            if self.estudiantes.eliminar(int(estudiante)):
                messagebox.showinfo("Información", "Estudiante eliminado correctamente")
            else:
                messagebox.showerror("Error", "Estudiante no encontrado")

        tk.Button(ventana, text="Eliminar", command=eliminar_estudiante).pack(pady=20)
1