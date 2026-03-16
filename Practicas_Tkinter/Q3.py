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
    boton_retiro = tk.Button(frame_menu, text="Retiro", width=20, height=2)
    boton_retiro.grid(row=0, column=0, padx=20, pady=10)

    boton_consulta = tk.Button(frame_menu, text="Consulta de saldo", width=20, height=2)
    boton_consulta.grid(row=1, column=0, padx=20, pady=10)

    boton_info = tk.Button(frame_menu, text="Información de cuenta", width=20, height=2)
    boton_info.grid(row=2, column=0, padx=20, pady=10)

    # Botones lado derecho
    boton_deposito = tk.Button(frame_menu, text="Depósito", width=20, height=2)
    boton_deposito.grid(row=0, column=1, padx=20, pady=10)

    boton_cambio = tk.Button(frame_menu, text="Cambio de moneda", width=20, height=2)
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
