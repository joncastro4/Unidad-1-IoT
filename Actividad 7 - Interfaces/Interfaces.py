import tkinter as tk
from ventanas_cursos import VentanasCursos
from ventanas_estudiantes import VentanasEstudiantes
from ventanas_inscritos import VentanasInscritos

<<<<<<< HEAD
def main():
    root = tk.Tk()
    root.title("Menú")
    root.geometry("200x200")
=======

>>>>>>> 8627105f3c5920eaa875b92e972f3fd598b85e1d

    def abrir_cursos():
        vc = VentanasCursos(root)
        vc.ventana_cursos()

    def abrir_estudiantes():
        ve = VentanasEstudiantes(root)
        ve.ventana_estudiantes()

    def abrir_inscritos():
        vi.ventana_inscritos()
        vi = VentanasInscritos(root)

    btn1 = tk.Button(root, text="Curso", command=abrir_cursos)
    btn1.pack(pady=5)

    btn2 = tk.Button(root, text="Estudiantes", command=abrir_estudiantes)
    btn2.pack(pady=5)

    btn3 = tk.Button(root, text="Inscritos", command=abrir_inscritos)
    btn3.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
