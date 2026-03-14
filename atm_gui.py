#contains tkinter window 
#buttons 
#entries 
#layout  
#interface
import tkinter as tk
from banco_final import saldo_bs

def start_gui():

    window = tk.Tk()
    window.title("Banco del Tigre ATM")
    window.geometry("400x400")

    titulo = tk.Label(window, text="Banco del Tigre", font=("Arial",18))
    titulo.pack(pady=20)

    def ver_saldo():
        saldo_label.config(text="Saldo: " + str(saldo_bs) + " Bs")

    def abrir_retiro():

        retiro_window = tk.Toplevel(window)
        retiro_window.title("Retiro")

        label = tk.Label(retiro_window,text="Monto a retirar")
        label.pack()

        entrada = tk.Entry(retiro_window)
        entrada.pack()

        def retirar():
            monto = float(entrada.get())
            resultado.config(text="Retiro simulado: " + str(monto))

        boton = tk.Button(retiro_window,text="Retirar",command=retirar)
        boton.pack()

        resultado = tk.Label(retiro_window,text="")
        resultado.pack()

    boton_retirar = tk.Button(window,text="Retirar",width=20,command=abrir_retiro)
    boton_retirar.pack(pady=10)

    boton_saldo = tk.Button(window,text="Consultar saldo",width=20,command=ver_saldo)
    boton_saldo.pack(pady=10)

    saldo_label = tk.Label(window,text="")
    saldo_label.pack(pady=20)

    boton_salir = tk.Button(window,text="Salir",command=window.destroy)
    boton_salir.pack(pady=10)

    window.mainloop()