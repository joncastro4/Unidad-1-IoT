import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Curso import Curso

class VentanasCursos:
    def __init__(self, root, cursos=None):
        self.root = root
        
        if cursos is None:
            self.isJson = True
            self.cursos = Curso()
            self.cursos.json_a_objeto(self.cursos.obtener_json())
        else:
            self.isJson = False
            self.cursos = cursos

    def ventana_cursos(self):
        ventana_curso = tk.Toplevel(self.root)
        ventana_curso.overrideredirect(True)
        ventana_curso.title("Cursos")
        ventana_curso.geometry("200x300")

        tk.Button(ventana_curso, text="Insertar", command=self.ventana_insertar).pack(pady=10)
        tk.Button(ventana_curso, text="Ver", command=self.ventana_ver).pack(pady=10)
        tk.Button(ventana_curso, text="Modificar", command=self.ventana_modificar).pack(pady=10)
        tk.Button(ventana_curso, text="Eliminar", command=self.ventana_eliminar).pack(pady=10)
        
        def cerrar():
            if self.isJson:
                self.cursos.transformar_json("curso")
            ventana_curso.destroy()

        tk.Button(ventana_curso, text="Menú", command=cerrar).pack(pady=10)

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

            if self.cursos.agregar(Curso(nombre, descripcion, fecha_inicio, fecha_fin, profesor)):
                messagebox.showinfo("Información", "Curso agregado correctamente")
            else:
                messagebox.showerror("Error", "Error al agregar el curso")

        tk.Button(ventana, text="Guardar", command=agregar_curso).pack(pady=20)

    def ventana_ver(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Ver Cursos")
        ventana.geometry("1050x600")

        if not self.cursos.ver():
            tk.Label(ventana, text="No hay cursos").pack(pady=10)
        else:
            frame = tk.Frame(ventana)
            frame.pack(pady=10, fill=tk.BOTH, expand=True)

            cols = ("ID", "Nombre", "Descripción", "Fecha inicio", "Fecha fin", "Profesor")
            tree = ttk.Treeview(frame, columns=cols, show="headings")
            
            for col in cols:
                tree.heading(col, text=col)
                tree.column(col, width=200, anchor="center")
            
            scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.pack(side="right", fill="y")
            tree.pack(side="left", fill=tk.BOTH, expand=True)
            
            for i, curso in enumerate(self.cursos.ver()):
                tree.insert("", "end", values=(i, curso.nombre, curso.descripcion, curso.fecha_inicio, curso.fecha_fin, curso.profesor))

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
            index = input_id.get()
            if not index.isdigit():
                messagebox.showerror("Error", "El ID debe ser un número entero")
                return
            index = int(index)

            nombre = input_nombre.get()
            descripcion = input_descripcion.get()
            fecha_inicio = input_fecha_inicio.get()
            fecha_fin = input_fecha_fin.get()
            profesor = input_profesor.get()

            if not nombre or not descripcion or not fecha_inicio or not fecha_fin or not profesor:
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return

            if self.cursos.modificar(index, Curso(nombre, descripcion, fecha_inicio, fecha_fin, profesor)):
                messagebox.showinfo("Información", "Curso modificado correctamente")
            else:
                messagebox.showerror("Error", "El curso no se pudo modificar")

        tk.Button(ventana, text="Guardar", command=modificar_curso).pack(pady=20)

    def ventana_eliminar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Eliminar Curso")
        ventana.geometry("500x500")

        tk.Label(ventana, text="ID:").pack(pady=5)
        input_id = tk.Entry(ventana)
        input_id.pack(pady=5)

        def eliminar_curso():
            curso = input_id.get()
            if not curso.isdigit():
                messagebox.showerror("Error", "El ID debe ser un número entero")
                return

            if self.cursos.eliminar(int(curso)):
                messagebox.showinfo("Información", "Curso eliminado correctamente")
            else:
                messagebox.showerror("Error", "Curso no encontrado")

<<<<<<< HEAD
        tk.Button(ventana, text="Eliminar", command=eliminar_curso).pack(pady=20)
=======
        cursos = tk.Text(ventana)
        cursos.pack(pady=20, fill=tk.BOTH, expand=True)

        cursos = c.obtener_json()

        for curso in cursos:
            cursos.insert(tk.END, f"ID: {curso['id']}\n")
            cursos.insert(tk.END, f"Nombre: {curso['nombre']}\n")
            cursos.insert(tk.END, f"Descripción: {curso['descripcion']}\n")
            cursos.insert(tk.END, f"Fecha de inicio: {curso['fecha_inicio']}\n")
            cursos.insert(tk.END, f"Fecha de fin: {curso['fecha_fin']}\n")
            cursos.insert(tk.END, f"Profesor: {curso['profesor']}\n")
            cursos.insert(tk.END, "-" * 50 + "\n")

    def ventana_cursos(self):
        ventana_curso = tk.Toplevel(root)
        ventana_curso.title("Cursos")
        ventana_curso.geometry("200x300")

        cursos = c.Curso()
        
        tk.Button(ventana_curso, text="Insertar", command=self.ventana_insertar).pack(pady=10)
        tk.Button(ventana_curso, text="Ver", command=self.ventana_ver).pack(pady=10)
        tk.Button(ventana_curso, text="Modificar", command=self.ventana_modificar).pack(pady=10)
        tk.Button(ventana_curso, text="Eliminar", commands=self.ventana_eliminar).pack(pady=10)
        tk.Button(ventana_curso, text="Menú", command=ventana_curso.destroy).pack(pady=10)
>>>>>>> 8627105f3c5920eaa875b92e972f3fd598b85e1d
