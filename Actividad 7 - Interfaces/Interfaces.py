import tkinter as tk
from ventanas_cursos import VentanasCursos as VC



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