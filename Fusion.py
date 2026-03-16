import tkinter as tk
from tkinter import messagebox

from banco_final import retirar_gui, depositar_gui, obtener_saldos

ventana = tk.Tk()
ventana.title("Banco del Tigre")
ventana.geometry("400x300")

# Texto bienvenida
titulo = tk.Label(ventana, text="Bienvenido al Banco del Tigre", font=("Arial",16))
titulo.pack(pady=20)

# Funcion iniciar
def iniciar():

    # --- AQUI VA TODO EL CODIGO DEL PIN ---
    ventana_pin = tk.Toplevel(ventana)
    ventana_pin.title("Ingreso de PIN")
    ventana_pin.geometry("400x400")

    texto_pin = tk.Label(ventana_pin, text="Ingrese su PIN de 4 digitos")
    texto_pin.pack(pady=10)

    pin_var = tk.StringVar()
    pin_correcto = "1234"
    intentos = {"contador":0}

    pantalla_pin = tk.Entry(ventana_pin, textvariable=pin_var, show="*", justify="center", font=("Arial",18))
    pantalla_pin.pack(pady=10)

    def presionar(numero):
        if len(pin_var.get()) < 4:
            pin_var.set(pin_var.get() + str(numero))

    def borrar():
        pin_var.set("")

    def verificar_pin():
        pin = pin_var.get()

        if pin == pin_correcto:
            messagebox.showinfo("Correcto", "PIN valido")
            ventana_pin.destroy()
            tipo_cuenta()


        else:
            intentos["contador"] += 1
            messagebox.showerror("Error", "PIN incorrecto")

            if intentos["contador"] >= 3:
                messagebox.showerror("Bloqueado", "Tarjeta bloqueada")

                ventana_pin.destroy()   # cierra ventana PIN
                ventana.destroy()       # cierra programa 

            borrar()

    frame_teclado = tk.Frame(ventana_pin)
    frame_teclado.pack()

    numeros = [
        (1,0,0),(2,0,1),(3,0,2),
        (4,1,0),(5,1,1),(6,1,2),
        (7,2,0),(8,2,1),(9,2,2),
        (0,3,1)
    ]

    for num,fila,col in numeros:
        boton = tk.Button(frame_teclado,text=num,width=5,height=2,
                          command=lambda n=num: presionar(n))
        boton.grid(row=fila,column=col,padx=5,pady=5)

    boton_borrar = tk.Button(frame_teclado,text="Borrar",command=borrar)
    boton_borrar.grid(row=3,column=0,padx=5,pady=5)

    boton_ingresar = tk.Button(frame_teclado,text="Ingresar",command=verificar_pin)
    boton_ingresar.grid(row=3,column=2,padx=5,pady=5)

def menu_cajero():

    ventana_menu = tk.Toplevel(ventana)
    ventana_menu.title("Banco del Tigre - Cajero")
    ventana_menu.geometry("500x400")

    titulo = tk.Label(ventana_menu, text="Seleccione una operación", font=("Arial",14))
    titulo.pack(pady=20)

    frame_menu = tk.Frame(ventana_menu)
    frame_menu.pack()

    # Botones lado izquierdo
    boton_retiro = tk.Button(frame_menu, text="Retiro", width=20, height=2, command=retiro_gui)
    boton_retiro.grid(row=0, column=0, padx=20, pady=10)

    boton_consulta = tk.Button(frame_menu, text="Consulta de saldo", width=20, height=2, command=consulta_gui)
    boton_consulta.grid(row=1, column=0, padx=20, pady=10)

    boton_info = tk.Button(frame_menu, text="Información de cuenta", width=20, height=2, command=info_cuenta_gui)
    boton_info.grid(row=2, column=0, padx=20, pady=10)

    # Botones lado derecho
    boton_deposito = tk.Button(frame_menu, text="Depósito", width=20, height=2, command=deposito_gui)
    boton_deposito.grid(row=0, column=1, padx=20, pady=10)
    
    boton_cambio = tk.Button(frame_menu, text="Cambio de moneda", width=20, height=2, command=cambio_moneda_gui)
    boton_cambio.grid(row=1, column=1, padx=20, pady=10)

    boton_salir = tk.Button(frame_menu, text="Salir", width=20, height=2, command=ventana.destroy)
    boton_salir.grid(row=2, column=1, padx=20, pady=10)
def tipo_cuenta():

    ventana_cuenta = tk.Toplevel(ventana)
    ventana_cuenta.title("Tipo de cuenta")
    ventana_cuenta.geometry("400x300")

    titulo = tk.Label(ventana_cuenta, text="Seleccione su tipo de cuenta", font=("Arial",14))
    titulo.pack(pady=20)

    def seleccionar(tipo):
        global cuenta
        cuenta = tipo
        ventana_cuenta.destroy()
        menu_cajero()

    boton_ahorro = tk.Button(ventana_cuenta,
                             text="Caja de Ahorro",
                             width=20,
                             height=2,
                             command=lambda: seleccionar(1))
    boton_ahorro.pack(pady=10)

    boton_corriente = tk.Button(ventana_cuenta,
                                text="Cuenta Corriente",
                                width=20,
                                height=2,
                                command=lambda: seleccionar(2))
    boton_corriente.pack(pady=10)

    boton_extranjero = tk.Button(ventana_cuenta,
                                 text="Extranjero",
                                 width=20,
                                 height=2,
                                 command=lambda: seleccionar(0))
    boton_extranjero.pack(pady=10)
def retiro_gui():

    ventana_retiro = tk.Toplevel(ventana)
    ventana_retiro.title("Retiro")

    tk.Label(ventana_retiro,text="Moneda (bs/usd/libras/euro)").pack()

    moneda_entry = tk.Entry(ventana_retiro)
    moneda_entry.pack()

    tk.Label(ventana_retiro,text="Monto").pack()

    monto_entry = tk.Entry(ventana_retiro)
    monto_entry.pack()

    def ejecutar():

        moneda = moneda_entry.get()
        try:
            monto = float(monto_entry.get())

            if monto <= 0:
                messagebox.showerror("Error","Invalido")
                return

        except:
            messagebox.showerror("Error","Invalido")
            return

        mensaje = retirar_gui(moneda,monto)

        messagebox.showinfo("Resultado",mensaje)


    tk.Button(ventana_retiro,text="Retirar",command=ejecutar).pack()
def deposito_gui():

    ventana_deposito = tk.Toplevel(ventana)
    ventana_deposito.title("Deposito")

    tk.Label(ventana_deposito,text="Moneda (bs/usd/libras/euro)").pack()

    moneda_entry = tk.Entry(ventana_deposito)
    moneda_entry.pack()

    tk.Label(ventana_deposito,text="Monto").pack()

    monto_entry = tk.Entry(ventana_deposito)
    monto_entry.pack()

    def ejecutar():
        
        moneda = moneda_entry.get()

        try:
            monto = float(monto_entry.get())

            if monto <= 0:
                messagebox.showerror("Error","Invalido")
                return

        except:
            messagebox.showerror("Error","Invalido")
            return

        mensaje = retirar_gui(moneda,monto)

        messagebox.showinfo("Resultado",mensaje)


    tk.Button(ventana_deposito,text="Depositar",command=ejecutar).pack()
def consulta_gui():

    saldos = obtener_saldos()

    mensaje = (
        f"Bolivianos: {saldos['bs']}\n"
        f"Dolares: {saldos['usd']}\n"
        f"Libras: {saldos['libras']}\n"
        f"Euro: {saldos['euro']}"
    )

    messagebox.showinfo("Saldos",mensaje)
def info_cuenta_gui():

    if cuenta == 1:
        tipo = "Caja de ahorro"
    elif cuenta == 2:
        tipo = "Cuenta corriente"
    else:
        tipo = "Extranjero"

    messagebox.showinfo(
        "Cuenta",
        f"Banco del Tigre\nTipo de cuenta: {tipo}"
    )
def cambio_moneda_gui():

    ventana_cambio = tk.Toplevel(ventana)
    ventana_cambio.title("Cambio de moneda")
    ventana_cambio.geometry("300x250")

    tk.Label(ventana_cambio, text="Moneda origen (bs/usd/libras/euro)").pack(pady=5)
    moneda_origen = tk.Entry(ventana_cambio)
    moneda_origen.pack()

    tk.Label(ventana_cambio, text="Moneda destino (bs/usd/libras/euro)").pack(pady=5)
    moneda_destino = tk.Entry(ventana_cambio)
    moneda_destino.pack()

    tk.Label(ventana_cambio, text="Monto").pack(pady=5)
    monto_entry = tk.Entry(ventana_cambio)
    monto_entry.pack()

    def ejecutar():

        origen = moneda_origen.get().lower()
        destino = moneda_destino.get().lower()
        monto_texto = monto_entry.get()

        monedas_validas = ["bs","usd","libras","euro"]

        # validar monedas
        if origen not in monedas_validas or destino not in monedas_validas:
            messagebox.showerror("Error","Invalido")
            return

        # validar monto
        try:
            monto = float(monto_texto)

            if monto <= 0:
                messagebox.showerror("Error","Invalido")
                return

        except:
            messagebox.showerror("Error","Invalido")
            return

        messagebox.showinfo("Cambio realizado",
                            f"Se cambiaron {monto} {origen} a {destino}")

    tk.Button(ventana_cambio,text="Cambiar",command=ejecutar).pack(pady=10)

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
