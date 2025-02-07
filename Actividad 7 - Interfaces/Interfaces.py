import tkinter as tk
from ventanas_cursos import VentanasCursos as VC

def ventana_cursos():
    ventana_curso = tk.Toplevel(root)
    ventana_curso.title("Cursos")
    ventana_curso.geometry("200x300")
    
    btn_insertar = tk.Button(ventana_curso, text="Insertar", command=VC.ventana_insertar)
    btn_insertar.pack(pady=10)

    btn_buscar = tk.Button(ventana_curso, text="Buscar", command=VC.ventana_ver)
    btn_buscar.pack(pady=10)

    btn_modificar = tk.Button(ventana_curso, text="Modificar", command=VC.ventana_modificar)
    btn_modificar.pack(pady=10)

    btn_eliminar = tk.Button(ventana_curso, text="Eliminar", command=VC.ventana_eliminar)
    btn_eliminar.pack(pady=10)

    btn_cerrar = tk.Button(ventana_curso, text="Menú", command=ventana_curso.destroy)
    btn_cerrar.pack(pady=10)

root = tk.Tk()
root.title("Menú")
root.geometry("200x200")

btn1 = tk.Button(root, text="Curso", command=ventana_cursos)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Estudiantes")
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Inscritos")
btn3.pack(pady=5)

root.mainloop()