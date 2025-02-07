import tkinter as tk

class VentanasCursos:
    @staticmethod
    def ventana():
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
    def ventana_modificiar():
        ventana = tk.Toplevel()
        ventana.title("Agregar Curso")
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
                input_nombre.get(),
                input_descripcion.get(),
                input_fecha_inicio.get(),
                input_fecha_fin.get(),
                input_profesor.get(),
            ),
        )
        btn_guardar.pack(pady=20)

    def ventana_eliminar(self):
        ventana = tk.Toplevel()
        ventana.title("Agregar Curso")
        ventana.geometry("500x500")

        label_id = tk.Label(ventana, text="ID:")
        label_id.pack(pady=5)

        input_id = tk.Entry(ventana)
        input_id.pack(pady=5)

        btn_guardar = tk.Button(
            ventana,
            text="Guardar",
            command=lambda: print(input_id.get()),
        )
        btn_guardar.pack(pady=20)

    def ventana_ver(self):
        ventana = tk.Toplevel()
        ventana.title("Agregar Curso")
        ventana.geometry("500x500")