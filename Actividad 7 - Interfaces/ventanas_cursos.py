import tkinter as tk
from Curso import Curso

class VentanasCursos:
    def __init__(self, root):
        self.root = root
        self.cursos = Curso()
        self.cursos.obtener_json()

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
            cur = Curso(
                input_nombre.get(),
                input_descripcion.get(),
                input_fecha_inicio.get(),
                input_fecha_fin.get(),
                input_profesor.get()
            )

            json = self.cursos.obtener_json()

            self.cursos.json_a_objeto(json)

            cursos = self.cursos.agregar(cur)

            self.cursos.transformar_json("curso")

        btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_curso)
        btn_agregar.pack(pady=20)

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
            nuevo_curso = Curso(
                input_nombre.get(),
                input_descripcion.get(),
                input_fecha_inicio.get(),
                input_fecha_fin.get(),
                input_profesor.get()
            )

            json = self.cursos.obtener_json()
            self.cursos.json_a_objeto(json)

            self.cursos.modificar(index, nuevo_curso)

            self.cursos.transformar_json("curso")

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
            
            self.cursos.eliminar(int(curso))

        btn_eliminar = tk.Button(
            ventana,
            text="Eliminar",
            command=eliminar_curso
        )
        btn_eliminar.pack(pady=20)

    def ventana_ver(self):
        ventana = tk.Toplevel()
        ventana.title("Ver Cursos")
        ventana.geometry("500x500")

        text_area = tk.Text(ventana)
        text_area.pack(pady=20, fill=tk.BOTH, expand=True)

        cursos = self.cursos.obtener_json()

        if not cursos:
            text_area.insert(tk.END, "No hay cursos disponibles.\n")
            return
        
        cursosI = 0
        for curso in cursos:
            text_area.insert(tk.END, f"Id de curso {cursosI}:\n")
            text_area.insert(tk.END, f"Nombre: {curso.get('nombre', 'Desconocido')}\n")
            text_area.insert(tk.END, f"Descripción: {curso.get('descripcion', 'No disponible')}\n")
            text_area.insert(tk.END, f"Fecha de inicio: {curso.get('fecha_inicio', 'No disponible')}\n")
            text_area.insert(tk.END, f"Fecha de fin: {curso.get('fecha_fin', 'No disponible')}\n")
            text_area.insert(tk.END, f"Profesor: {curso.get('profesor', 'No disponible')}\n")
            text_area.insert(tk.END, "----------------------------------------------------------\n")
            cursosI += 1
