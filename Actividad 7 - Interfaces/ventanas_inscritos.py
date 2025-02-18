import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
from Inscrito import Inscrito

class VentanasInscritos():
    def __init__(self, root, inscritos = None):
        self.root = root

        if inscritos is None:
            self.isJson = True
            self.inscritos = Inscrito()
            self.inscritos.json_a_objeto(self.inscritos.obtener_json())
        elif inscritos is not None:
            self.isJson = False
            self.inscritos = inscritos

    def ventana_inscritos(self):
        ventana_inscrito = tk.Toplevel(self.root)
        ventana_inscrito.title("Inscritos")
        ventana_inscrito.geometry("200x300")

        tk.Button(ventana_inscrito, text="Insertar", command=self.ventana_insertar).pack(pady=10)
        tk.Button(ventana_inscrito, text="Ver", command=self.ventana_ver).pack(pady=10)
        tk.Button(ventana_inscrito, text="Modificar", command=self.ventana_modificar).pack(pady=10)
        tk.Button(ventana_inscrito, text="Eliminar", command=self.ventana_eliminar).pack(pady=10)
        tk.Button(ventana_inscrito, text="Menú", command=ventana_inscrito.destroy).pack(pady=10)

    def ventana_insertar(self): 
        ventana = tk.Toplevel(self.root)
        ventana.title("Insertar inscrito")
        ventana.geometry("400x400")

        tk.Button(ventana, text="Curso", command=self.vc.ventana_insertar).pack(pady=10)
        tk.Button(ventana, text="Estudiante", command=self.ve.ventana_insertar).pack(pady=10)

    def ventana_ver(self):
        ventana = tk.Toplevel()
        ventana.title("Ver inscritos")
        ventana.geometry("1050x600")

        inscritos = self.inscritos.ver()

        if not inscritos:
            tk.Label(ventana, text="No hay inscritos").pack(pady=10)
            return

        curI = 0
        for inscrito in inscritos:
            curso = inscrito.curso
            estudiantes = inscrito.estudiantes if isinstance(inscrito.estudiantes, list) else [inscrito.estudiantes]

            tree_curso = ttk.Treeview(ventana, columns=("ID", "Nombre", "Descripcion", "Fecha Inicio", "Fecha Fin", "Profesor"), show="headings", height=1)
            tree_curso.pack(fill="x", padx=10, pady=5)

            tree_curso.heading("ID", text="ID")
            tree_curso.column("ID", width=50, anchor="center")

            tree_curso.heading("Nombre", text="Nombre")
            tree_curso.column("Nombre", width=200, anchor="center")

            tree_curso.heading("Descripcion", text="Descripcion")
            tree_curso.column("Descripcion", width=200, anchor="center")

            tree_curso.heading("Fecha Inicio", text="Fecha Inicio")
            tree_curso.column("Fecha Inicio", width=200, anchor="center")

            tree_curso.heading("Fecha Fin", text="Fecha Fin")
            tree_curso.column("Fecha Fin", width=200, anchor="center")

            tree_curso.heading("Profesor", text="Profesor")
            tree_curso.column("Profesor", width=200, anchor="center")

            tree_curso.insert("", "end", values=(curI, curso.nombre, curso.descripcion, curso.fecha_inicio, curso.fecha_fin, curso.profesor))

            frame_estudiantes = tk.Frame(ventana)
            frame_estudiantes.pack(fill="x", padx=10, pady=5)

            tree_estudiantes = ttk.Treeview(frame_estudiantes, columns=("ID", "Nombre", "Apellido Paterno", "Apellido Materno", "Fecha Nacimiento", "Teléfono"), show="headings", height=10)
            tree_estudiantes.pack(side="left", fill="both", expand=True)

            scrollbar_estudiantes = ttk.Scrollbar(frame_estudiantes, orient="vertical", command=tree_estudiantes.yview)
            scrollbar_estudiantes.pack(side="right", fill="y")
            tree_estudiantes.configure(yscrollcommand=scrollbar_estudiantes.set)

            tree_estudiantes.heading("ID", text="ID")
            tree_estudiantes.column("ID", width=50, anchor="center")

            tree_estudiantes.heading("Nombre", text="Nombre")
            tree_estudiantes.column("Nombre", width=200, anchor="center")

            tree_estudiantes.heading("Apellido Paterno", text="Apellido Paterno")
            tree_estudiantes.column("Apellido Paterno", width=200, anchor="center")

            tree_estudiantes.heading("Apellido Materno", text="Apellido Materno")
            tree_estudiantes.column("Apellido Materno", width=200, anchor="center")

            tree_estudiantes.heading("Fecha Nacimiento", text="Fecha Nacimiento")
            tree_estudiantes.column("Fecha Nacimiento", width=200, anchor="center")

            tree_estudiantes.heading("Teléfono", text="Teléfono")
            tree_estudiantes.column("Teléfono", width=200, anchor="center")


            for estudiante in estudiantes:
                estudiante_diccionario = estudiante.diccionario()
                print(estudiante_diccionario)

                estI = 0
                for est in estudiante_diccionario:
                    tree_estudiantes.insert("", "end", values=(estI, est["nombre"], est["apellido_paterno"], est["apellido_materno"], est["fecha_nacimiento"], est["telefono"]))
                    estI += 1

            ttk.Separator(ventana, orient="horizontal").pack(fill="x", pady=10)
            curI += 1
    
    def ventana_modificar(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Modificar inscrito")
        ventana.geometry("400x400")

        tk.Button(ventana, text="Curso").pack(pady=10)
        tk.Button(ventana, text="Estudiante").pack(pady=10)
    
    def ventana_eliminar(self): 
        ventana = tk.Toplevel(self.root)
        ventana.title("Eliminar inscrito")
        ventana.geometry("400x400")

        tk.Button(ventana, text="Curso").pack(pady=10)
        tk.Button(ventana, text="Estudiante").pack(pady=10)