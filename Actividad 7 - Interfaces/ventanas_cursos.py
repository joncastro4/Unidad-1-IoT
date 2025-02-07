import tkinter as tk

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

        # Aquí podrías agregar un widget de texto o una tabla para mostrar los cursos
        text_cursos = tk.Text(ventana)
        text_cursos.pack(pady=20, fill=tk.BOTH, expand=True)

        # Simulación de datos de cursos
        cursos = [
            {"id": 1, "nombre": "Curso 1", "descripcion": "Descripción 1", "fecha_inicio": "2023-01-01", "fecha_fin": "2023-12-31", "profesor": "Profesor 1"},
            {"id": 2, "nombre": "Curso 2", "descripcion": "Descripción 2", "fecha_inicio": "2023-02-01", "fecha_fin": "2023-11-30", "profesor": "Profesor 2"},
        ]

        for curso in cursos:
            text_cursos.insert(tk.END, f"ID: {curso['id']}\n")
            text_cursos.insert(tk.END, f"Nombre: {curso['nombre']}\n")
            text_cursos.insert(tk.END, f"Descripción: {curso['descripcion']}\n")
            text_cursos.insert(tk.END, f"Fecha de inicio: {curso['fecha_inicio']}\n")
            text_cursos.insert(tk.END, f"Fecha de fin: {curso['fecha_fin']}\n")
            text_cursos.insert(tk.END, f"Profesor: {curso['profesor']}\n")
            text_cursos.insert(tk.END, "-" * 50 + "\n")
