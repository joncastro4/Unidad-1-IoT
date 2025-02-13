import tkinter as tk
from ventanas_cursos import VentanasCursos
from ventanas_estudiantes import VentanasEstudiantes
from ventanas_inscritos import VentanasInscritos

def main():
    root = tk.Tk()
    root.title("Menú")
    root.geometry("200x200")

    vc = VentanasCursos(root)
    ve = VentanasEstudiantes(root)
    vi = VentanasInscritos(root)

    btn1 = tk.Button(root, text="Curso", command=vc.ventana_cursos)
    btn1.pack(pady=5)

    btn2 = tk.Button(root, text="Estudiantes", command=ve.ventana_estudiantes)
    btn2.pack(pady=5)

    btn3 = tk.Button(root, text="Inscritos", command=vi.ventana_inscritos)
    btn3.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
