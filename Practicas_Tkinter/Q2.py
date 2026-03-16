import tkinter as tk

ventana = tk.Tk()
ventana.title("Banco del Tigre")
ventana.geometry("400x300")

# Texto de bienvenida
titulo = tk.Label(ventana, text="Bienvenido al Banco del Tigre", font=("Arial",16))
titulo.pack(pady=40)

# Funcion iniciar
def iniciar():
    print("Inicio del cajero")

# Funcion cancelar
def cancelar():
    ventana.destroy()

# Boton iniciar
boton_iniciar = tk.Button(ventana, text="Iniciar", width=20, height=2, command=iniciar)
boton_iniciar.pack(pady=10)

# Boton cancelar
boton_cancelar = tk.Button(ventana, text="Cancelar", width=20, height=2, command=cancelar)
boton_cancelar.pack(pady=10)

ventana.mainloop()
