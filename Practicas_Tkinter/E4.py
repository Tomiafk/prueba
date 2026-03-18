import tkinter as tk

def mostrar():
    nombre = entrada.get()
    print(nombre)

ventana = tk.Tk()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Mostrar", command=mostrar)
boton.pack()

ventana.mainloop()
