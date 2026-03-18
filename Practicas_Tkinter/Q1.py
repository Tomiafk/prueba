import tkinter as tk

saldo_bs = 1000

# FUNCIONES
def consultar():
    resultado.config(text="Saldo: " + str(saldo_bs) + " Bs")

def depositar():
    global saldo_bs
    monto = float(entrada.get())
    saldo_bs = saldo_bs + monto
    resultado.config(text="Deposito realizado")

def retirar():
    global saldo_bs
    monto = float(entrada.get())
    
    if monto <= saldo_bs:
        saldo_bs = saldo_bs - monto
        resultado.config(text="Retiro realizado")
    else:
        resultado.config(text="Saldo insuficiente")

# VENTANA
ventana = tk.Tk()
ventana.title("Banco del Tigre")
ventana.geometry("300x250")

titulo = tk.Label(ventana, text="Cajero Automatico")
titulo.pack()

entrada = tk.Entry(ventana)
entrada.pack()

btn_deposito = tk.Button(ventana, text="Depositar", command=depositar)
btn_deposito.pack()

btn_retiro = tk.Button(ventana, text="Retirar", command=retirar)
btn_retiro.pack()

btn_consulta = tk.Button(ventana, text="Consultar saldo", command=consultar)
btn_consulta.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()
