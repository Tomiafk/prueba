import tkinter as tk

def saludo():
    print("Hola!")

ventana = tk.Tk()

boton = tk.Button(ventana, text="Presionar", command=saludo)
boton.pack()

ventana.mainloop()
