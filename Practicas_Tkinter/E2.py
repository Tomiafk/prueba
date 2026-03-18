import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Frame")
ventana.geometry("300x200")

# Crear un frame con color de fondo
frame = tk.Frame(ventana, bg="lightblue", bd=5, relief="sunken")
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Agregar un botón dentro del frame
boton = tk.Button(frame, text="Botón en Frame")
boton.pack(pady=10)

ventana.mainloop()