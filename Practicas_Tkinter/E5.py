import tkinter as tk

def saludar():
    nombre = entrada.get()
    etiqueta.config(text="Hola " + nombre)

ventana = tk.Tk()
ventana.title("Saludo")

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

ventana.mainloop()

