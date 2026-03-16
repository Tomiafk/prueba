
import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Banco del Tigre")
ventana.geometry("400x300")

# Texto bienvenida
titulo = tk.Label(ventana, text="Bienvenido al Banco del Tigre", font=("Arial",16))
titulo.pack(pady=20)

# Funcion iniciar
def iniciar():

    # Nueva ventana para el PIN
    ventana_pin = tk.Toplevel(ventana)
    ventana_pin.title("Ingreso de PIN")
    ventana_pin.geometry("400x300")

    texto_pin = tk.Label(ventana_pin, text="Ingrese su PIN de 4 digitos")
    texto_pin.pack(pady=20)

    entrada_pin = tk.Entry(ventana_pin, show="*", width=20)
    entrada_pin.pack(pady=10)

    def verificar_pin():
        pin = entrada_pin.get()

        if len(pin) == 4 and pin.isdigit():
            messagebox.showinfo("Correcto", "PIN valido")
        else:
            messagebox.showerror("Error", "PIN invalido")

    boton_ingresar = tk.Button(ventana_pin, text="Ingresar", command=verificar_pin)
    boton_ingresar.pack(pady=10)

# Funcion cancelar
def cancelar():
    respuesta = messagebox.askyesno("Confirmar", "¿Esta seguro que desea cancelar?")
    
    if respuesta:
        ventana.destroy()

# Botones
boton_iniciar = tk.Button(ventana, text="1 - Iniciar", width=20, command=iniciar)
boton_iniciar.pack(pady=10)

boton_cancelar = tk.Button(ventana, text="0 - Cancelar", width=20, command=cancelar)
boton_cancelar.pack(pady=10)

ventana.mainloop()
