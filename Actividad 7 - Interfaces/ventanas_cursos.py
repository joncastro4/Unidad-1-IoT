import tkinter as tk
from Curso import Curso as c

class VentanasCursos:
    @staticmethod
    def ventana_insertar():
        ventana = tk.Toplevel()
        ventana.title("Agregar Curso")
        ventana.geometry("500x500")

        label_nombre = tk.Label(ventana, text="Nombre:")
        label_nombre.pack(pady=5)

        input_nombre = tk.Entry(ventana)
        input_nombre.pack(pady=5)

        label_descripcion = tk.Label(ventana, text="Descripción:")
        label_descripcion.pack(pady=5)

        input_descripcion = tk.Entry(ventana)
        input_descripcion.pack(pady=5)

        label_fecha_inicio = tk.Label(ventana, text="Fecha de inicio:")
        label_fecha_inicio.pack(pady=5)

        input_fecha_inicio = tk.Entry(ventana)
        input_fecha_inicio.pack(pady=5)

        label_fecha_fin = tk.Label(ventana, text="Fecha de fin:")
        label_fecha_fin.pack(pady=5)

        input_fecha_fin = tk.Entry(ventana)
        input_fecha_fin.pack(pady=5)

        label_profesor = tk.Label(ventana, text="Profesor:")
        label_profesor.pack(pady=5)

        input_profesor = tk.Entry(ventana)
        input_profesor.pack(pady=5)

        btn_guardar = tk.Button(
            ventana,
            text="Guardar",
            command=lambda: print(
                input_nombre.get(),
                input_descripcion.get(),
                input_fecha_inicio.get(),
                input_fecha_fin.get(),
                input_profesor.get(),
            ),
        )
        btn_guardar.pack(pady=20)

    @staticmethod
    def ventana_modificar():
        ventana = tk.Toplevel()
        ventana.title("Modificar Curso")
        ventana.geometry("500x500")

        label_id = tk.Label(ventana, text="ID:")
        label_id.pack(pady=5)

        input_id = tk.Entry(ventana)
        input_id.pack(pady=5)

        label_nombre = tk.Label(ventana, text="Nombre:")
        label_nombre.pack(pady=5)

        input_nombre = tk.Entry(ventana)
        input_nombre.pack(pady=5)

        label_descripcion = tk.Label(ventana, text="Descripción:")
        label_descripcion.pack(pady=5)

        input_descripcion = tk.Entry(ventana)
        input_descripcion.pack(pady=5)

        label_fecha_inicio = tk.Label(ventana, text="Fecha de inicio:")
        label_fecha_inicio.pack(pady=5)

        input_fecha_inicio = tk.Entry(ventana)
        input_fecha_inicio.pack(pady=5)

        label_fecha_fin = tk.Label(ventana, text="Fecha de fin:")
        label_fecha_fin.pack(pady=5)

        input_fecha_fin = tk.Entry(ventana)
        input_fecha_fin.pack(pady=5)

        label_profesor = tk.Label(ventana, text="Profesor:")
        label_profesor.pack(pady=5)

        input_profesor = tk.Entry(ventana)
        input_profesor.pack(pady=5)

        btn_guardar = tk.Button(
            ventana,
            text="Guardar",
            command=lambda: print(
                input_id.get(),
                input_nombre.get(),
                input_descripcion.get(),
                input_fecha_inicio.get(),
                input_fecha_fin.get(),
                input_profesor.get(),
            ),
        )
        btn_guardar.pack(pady=20)

    @staticmethod
    def ventana_eliminar():
        ventana = tk.Toplevel()
        ventana.title("Eliminar Curso")
        ventana.geometry("500x500")

        label_id = tk.Label(ventana, text="ID:")
        label_id.pack(pady=5)

        input_id = tk.Entry(ventana)
        input_id.pack(pady=5)

        btn_eliminar = tk.Button(
            ventana,
            text="Eliminar",
            command=lambda: print(f"Eliminar curso con ID: {input_id.get()}"),
        )
        btn_eliminar.pack(pady=20)

    @staticmethod
    def ventana_ver():
        ventana = tk.Toplevel()
        ventana.title("Ver Cursos")
        ventana.geometry("500x500")

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
