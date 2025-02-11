import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
from Curso import Curso

class VentanasCursos:
    def __init__(self, root):
        self.root = root
        self.cursos = Curso()
        json = self.cursos.obtener_json()
        self.cursos.json_a_objeto(json)

    def ventana_cursos(self):
        ventana_curso = tk.Toplevel(self.root)
        ventana_curso.title("Cursos")
        ventana_curso.geometry("200x300")

        tk.Button(ventana_curso, text="Insertar", command=self.ventana_insertar).pack(pady=10)
        tk.Button(ventana_curso, text="Ver", command=self.ventana_ver).pack(pady=10)
        tk.Button(ventana_curso, text="Modificar", command=self.ventana_modificar).pack(pady=10)
        tk.Button(ventana_curso, text="Eliminar", command=self.ventana_eliminar).pack(pady=10)
        tk.Button(ventana_curso, text="Menú", command=ventana_curso.destroy).pack(pady=10)

    def ventana_insertar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Curso")
        ventana.geometry("500x500")

        tk.Label(ventana, text="Nombre:").pack(pady=5)
        input_nombre = tk.Entry(ventana)
        input_nombre.pack(pady=5)

        tk.Label(ventana, text="Descripción:").pack(pady=5)
        input_descripcion = tk.Entry(ventana)
        input_descripcion.pack(pady=5)

        tk.Label(ventana, text="Fecha de inicio:").pack(pady=5)
        input_fecha_inicio = tk.Entry(ventana)
        input_fecha_inicio.pack(pady=5)

        tk.Label(ventana, text="Fecha de fin:").pack(pady=5)
        input_fecha_fin = tk.Entry(ventana)
        input_fecha_fin.pack(pady=5)

        tk.Label(ventana, text="Profesor:").pack(pady=5)
        input_profesor = tk.Entry(ventana)
        input_profesor.pack(pady=5)

        def agregar_curso():
            nombre = input_nombre.get()
            descripcion = input_descripcion.get()
            fecha_inicio = input_fecha_inicio.get()
            fecha_fin = input_fecha_fin.get()
            profesor = input_profesor.get()

            if not nombre or not descripcion or not fecha_inicio or not fecha_fin or not profesor:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            if not re.match(r"^[a-zA-Z0-9\sáéíóúÁÉÍÓÚüÜñÑ]+$", nombre):
                messagebox.showerror("Error", "El nombre solo puede contener letras, números, espacios y acentos")
                return

            if not re.match(r"^[a-zA-Z0-9\sáéíóúÁÉÍÓÚüÜñÑ.,!?()-]+$", descripcion):
                messagebox.showerror("Error", "La descripción contiene caracteres no permitidos")
                return

            if not re.match(r"^\d{4}-\d{2}-\d{2}$", fecha_inicio):
                messagebox.showerror("Error", "La fecha de inicio debe estar en formato YYYY-MM-DD")
                return

            if not re.match(r"^\d{4}-\d{2}-\d{2}$", fecha_fin):
                messagebox.showerror("Error", "La fecha de fin debe estar en formato YYYY-MM-DD")
                return

            if fecha_fin < fecha_inicio:
                messagebox.showerror("Error", "La fecha de fin no puede ser menor a la fecha de inicio")
                return

            if not re.match(r"^[a-zA-Z\sáéíóúÁÉÍÓÚüÜñÑ]+$", profesor):
                messagebox.showerror("Error", "El nombre del profesor solo puede contener letras, espacios y acentos")
                return

            if self.cursos.agregar(Curso(nombre, descripcion, fecha_inicio, fecha_fin, profesor)):
                self.cursos.transformar_json("curso")
                messagebox.showinfo("Información", "Curso agregado correctamente")
            else:
                messagebox.showerror("Error", "Error al agregar el curso")

        btn_guardar = tk.Button(
            ventana,
            text="Guardar",
            command=agregar_curso
        )
        btn_guardar.pack(pady=20)

    def ventana_modificar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Modificar Curso")
        ventana.geometry("500x500")

        tk.Label(ventana, text="ID:").pack(pady=5)
        input_id = tk.Entry(ventana)
        input_id.pack(pady=5)

        tk.Label(ventana, text="Nombre:").pack(pady=5)
        input_nombre = tk.Entry(ventana)
        input_nombre.pack(pady=5)

        tk.Label(ventana, text="Descripción:").pack(pady=5)
        input_descripcion = tk.Entry(ventana)
        input_descripcion.pack(pady=5)

        tk.Label(ventana, text="Fecha de inicio:").pack(pady=5)
        input_fecha_inicio = tk.Entry(ventana)
        input_fecha_inicio.pack(pady=5)

        tk.Label(ventana, text="Fecha de fin:").pack(pady=5)
        input_fecha_fin = tk.Entry(ventana)
        input_fecha_fin.pack(pady=5)

        tk.Label(ventana, text="Profesor:").pack(pady=5)
        input_profesor = tk.Entry(ventana)
        input_profesor.pack(pady=5)

        def modificar_curso():
            index = int(input_id.get())

            nombre = input_nombre.get()
            descripcion = input_descripcion.get()
            fecha_inicio = input_fecha_inicio.get()
            fecha_fin = input_fecha_fin.get()
            profesor = input_profesor.get()

            if not nombre or not descripcion or not fecha_inicio or not fecha_fin or not profesor:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            if not re.match(r"^[a-zA-Z0-9\sáéíóúÁÉÍÓÚüÜñÑ]+$", nombre):
                messagebox.showerror("Error", "El nombre solo puede contener letras, números, espacios y acentos")
                return

            if not re.match(r"^[a-zA-Z0-9\sáéíóúÁÉÍÓÚüÜñÑ.,!?()-]+$", descripcion):
                messagebox.showerror("Error", "La descripción contiene caracteres no permitidos")
                return

            if not re.match(r"^\d{4}-\d{2}-\d{2}$", fecha_inicio):
                messagebox.showerror("Error", "La fecha de inicio debe estar en formato YYYY-MM-DD")
                return

            if not re.match(r"^\d{4}-\d{2}-\d{2}$", fecha_fin):
                messagebox.showerror("Error", "La fecha de fin debe estar en formato YYYY-MM-DD")
                return

            if fecha_fin < fecha_inicio:
                messagebox.showerror("Error", "La fecha de fin no puede ser menor a la fecha de inicio")
                return

            if not re.match(r"^[a-zA-Z\sáéíóúÁÉÍÓÚüÜñÑ]+$", profesor):
                messagebox.showerror("Error", "El nombre del profesor solo puede contener letras, espacios y acentos")
                return
            
            if not self.cursos.modificar(index, Curso(nombre, descripcion, fecha_inicio, fecha_fin, profesor)):
                messagebox.showerror("Error", "ID no encontrado")
                return
            
            if self.cursos.modificar(index, Curso(nombre, descripcion, fecha_inicio, fecha_fin, profesor)):
                self.cursos.transformar_json("curso")
                messagebox.showinfo("Información", "Curso modificado correctamente")
            else:
                messagebox.showerror("Error", "El curso no se pudo modificar")

        btn_guardar = tk.Button(ventana, text="Guardar", command=modificar_curso)
        btn_guardar.pack(pady=20)

    def ventana_eliminar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Eliminar Curso")
        ventana.geometry("500x500")

        tk.Label(ventana, text="ID:").pack(pady=5)
        input_id = tk.Entry(ventana)
        input_id.pack(pady=5)

        def eliminar_curso():
            curso = input_id.get()

            if self.cursos.eliminar(int(curso)):
                self.cursos.transformar_json("curso")
                messagebox.showinfo("Información", "Curso eliminado correctamente")
            else:
                messagebox.showerror("Error", "Curso no encontrado")

        btn_eliminar = tk.Button(
            ventana,
            text="Eliminar",
            command=eliminar_curso
        )
        btn_eliminar.pack(pady=20)

    def ventana_ver(self):
        ventana = tk.Toplevel()
        ventana.title("Ver Cursos")
        ventana.geometry("1050x600")

        if not self.cursos.ver():
            label = tk.Label(ventana, text="No hay cursos")
            label.pack(pady=10)
        else:
            frame = tk.Frame(ventana)
            frame.pack(pady=10, fill=tk.BOTH, expand=True)

            cols = ("ID", "Nombre", "Descripción", "Fecha inicio", "Fecha fin", "Profesor")

            tree = ttk.Treeview(frame, columns=cols, show="headings")

            tree.heading("ID", text="ID")
            tree.heading("Nombre", text="Nombre")
            tree.heading("Descripción", text="Descripción")
            tree.heading("Fecha inicio", text="Fecha inicio")
            tree.heading("Fecha fin", text="Fecha fin")
            tree.heading("Profesor", text="Profesor")

            tree.column("ID", width=50, anchor="center")
            tree.column("Nombre", width=200, anchor="center")
            tree.column("Descripción", width=200, anchor="center")
            tree.column("Fecha inicio", width=200, anchor="center")
            tree.column("Fecha fin", width=200, anchor="center")
            tree.column("Profesor", width=200, anchor="center")
            
            scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            tree.configure(yscroll=scrollbar.set)

            scrollbar.pack(side="right", fill="y")
            tree.pack(side="left", fill=tk.BOTH, expand=True)

            curI = 0
            for curso in self.cursos.ver():
                tree.insert("", "end", values=[curI, curso.nombre, curso.descripcion, curso.fecha_inicio, curso.fecha_fin, curso.profesor])
                curI += 1
