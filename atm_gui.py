import tkinter as tk
<<<<<<< HEAD
from banco_final import retirar_gui, depositar_gui, obtener_saldos

# WINDOW

ventana = tk.Tk()
ventana.title("Banco El Tigre ATM")
ventana.geometry("100x900")
ventana.configure(bg="#FFD100") # Amarillo

# VARIABLES
=======
from banco_final import retirar_gui, depositar_gui, obtener_saldos,convertir_gui
estado = "inicio"
cuenta = ""
#ventana ////

ventana = tk.Tk()
ventana.title("Banco El Tigre ATM")
ventana.geometry("1200x900")
ventana.configure(bg="#FFD100")   #yellow tigre rawr logo

# variables para empezar/////
>>>>>>> 3524fdca18db8b8b2759fa221db0c2c910c31dd3

numero_ingresado = ""
estado = "inicio"

<<<<<<< HEAD
# SCREEN
=======
#SCREEN ///////////////////////////////////// 
#to fix screen size problem prueba 1
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight() 
ancho_ventana = int(ancho_pantalla * 0.8)
alto_ventana = int(alto_pantalla * 0.8)   
>>>>>>> 3524fdca18db8b8b2759fa221db0c2c910c31dd3

#centered in the middle 
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)

ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
pantalla = tk.Label(ventana,text="Bienvenido\nBanco El Tigre",bg="black",fg="#FFD100",font=("helvetica",20,"bold"),width=40,height=10,justify="left",anchor="nw",padx=15,pady=15)

pantalla.pack(pady=20)

<<<<<<< HEAD
# TIGER LOGO

=======
#TIGER LOGO//////////////////////////////////
#anticrasheo
>>>>>>> 3524fdca18db8b8b2759fa221db0c2c910c31dd3
try:
    logo = tk.PhotoImage(file="tigre_logo.png")
    logo_label = tk.Label(ventana,image=logo,bg="#FFD100")
    logo_label.pack()
except:
    pass

<<<<<<< HEAD
# ENTRY DISPLAY
=======
#ENTRY DISPLAY 
>>>>>>> 3524fdca18db8b8b2759fa221db0c2c910c31dd3

entrada = tk.Label(ventana,text="",bg="white",fg="black",font=("Courier",16),width=20)

entrada.pack(pady=10)

# FUNCTIONS
<<<<<<< HEAD
=======

>>>>>>> 3524fdca18db8b8b2759fa221db0c2c910c31dd3
def presionar(num):
    global numero_ingresado
    numero_ingresado += str(num)
    entrada.config(text=numero_ingresado)


def limpiar():
    global numero_ingresado
    numero_ingresado = ""
    entrada.config(text="")


def aceptar():

    global numero_ingresado
    global estado
    global operacion
    global moneda
    global cuenta
    global moneda_origen
    global moneda_destino

<<<<<<< HEAD
    # START
=======
    # INICIO
>>>>>>> 3524fdca18db8b8b2759fa221db0c2c910c31dd3
    if estado == "inicio":

        pantalla.config(text="Seleccione tipo de cuenta:\n\n""1 Ahorro\n""2 Corriente\n""3 Extranjero")

        estado = "cuenta"
        limpiar()
        return

    # CUENTA
    if estado == "cuenta":

        if numero_ingresado == "1":
            cuenta = "ahorro"

        elif numero_ingresado == "2":
            cuenta = "corriente"

        elif numero_ingresado == "3":
            cuenta = "extranjero"

        pantalla.config(text="Opciones:\n""1 Retiro\n""2 Deposito\n""3 Consulta\n""4 Cambio\n""5 Salir")

        estado = "menu"
        limpiar()
        return

<<<<<<< HEAD

    #  MENU
=======
    # MENU
>>>>>>> 3524fdca18db8b8b2759fa221db0c2c910c31dd3
    if estado == "menu":

        if numero_ingresado == "1":

            operacion = "retiro"

            pantalla.config(text="Seleccione moneda\n\n""1 Bs\n2 USD\n3 GBP\n4 EUR")

            estado = "moneda"

        elif numero_ingresado == "2":

            operacion = "deposito"

            pantalla.config(text="Seleccione moneda\n\n""1 Bs\n2 USD\n3 GBP\n4 EUR")

            estado = "moneda"

        elif numero_ingresado == "3":

            saldos = obtener_saldos()

            pantalla.config(text=f"BS: {saldos['bs']}\n"f"USD: {saldos['usd']}\n"f"GBP: {saldos['libras']}\n"f"EUR: {saldos['euro']}\n\n""1 Otra\n2 Salir")

            estado = "otra"

        elif numero_ingresado == "4":

            operacion = "cambio"

            pantalla.config(text="Moneda origen:\n\n""1 Bs\n2 USD\n3 GBP\n4 EUR")

            estado = "moneda_origen"

        elif numero_ingresado == "5":

            pantalla.config(text="Gracias por usar\nBanco El Tigre")

            ventana.after(3000, reiniciar)

            estado = "fin"

        limpiar()
        return

    # MONEDA ORIGEN
    if estado == "moneda_origen":

<<<<<<< HEAD
    # MONEDA
=======
        if numero_ingresado == "1":
            moneda_origen = "bs"
        elif numero_ingresado == "2":
            moneda_origen = "usd"
        elif numero_ingresado == "3":
            moneda_origen = "libras"
        elif numero_ingresado == "4":
            moneda_origen = "euro"

        pantalla.config(text="Moneda destino:\n\n""1 Bs\n2 USD\n3 GBP\n4 EUR")

        estado = "moneda_destino"
        limpiar()
        return

    # MONEDA DESTINO
    if estado == "moneda_destino":

        if numero_ingresado == "1":
            moneda_destino = "bs"
        elif numero_ingresado == "2":
            moneda_destino = "usd"
        elif numero_ingresado == "3":
            moneda_destino = "libras"
        elif numero_ingresado == "4":
            moneda_destino = "euro"

        pantalla.config(text="Ingrese monto a convertir:")

        estado = "monto_cambio"
        limpiar()
        return

    # MONTO CAMBIO
    if estado == "monto_cambio":

        monto = float(numero_ingresado)

        mensaje = convertir_gui(moneda_origen, moneda_destino, monto)

        pantalla.config(text=
        mensaje + "\n\n""Otra transaccion?\n""1 Si\n2 No")

        estado = "otra"
        limpiar()
        return

    # MONEDA NORMAL
>>>>>>> 3524fdca18db8b8b2759fa221db0c2c910c31dd3
    if estado == "moneda":

        if numero_ingresado == "1":
            moneda = "bs"
        elif numero_ingresado == "2":
            moneda = "usd"
        elif numero_ingresado == "3":
            moneda = "libras"
        elif numero_ingresado == "4":
            moneda = "euro"

        pantalla.config(text="Ingrese monto:")

        estado = "monto"
        limpiar()
        return

<<<<<<< HEAD

    # MONTO
=======
    # MONTO NORMAL
>>>>>>> 3524fdca18db8b8b2759fa221db0c2c910c31dd3
    if estado == "monto":

        monto = float(numero_ingresado)

        if operacion == "retiro":
            mensaje = retirar_gui(moneda, monto)

        elif operacion == "deposito":
            mensaje = depositar_gui(moneda, monto)

        pantalla.config(text=mensaje + "\n\n""Otra transaccion?\n""1 Si\n2 No")

        estado = "otra"
        limpiar()
        return

<<<<<<< HEAD

    # OTRA TRANSACCION
=======
    # OTRA
>>>>>>> 3524fdca18db8b8b2759fa221db0c2c910c31dd3
    if estado == "otra":

        if numero_ingresado == "1":

            pantalla.config(text="Opciones:\n""1 Retiro\n2 Deposito\n3 Consulta\n4 Cambio\n5 Salir")
            estado = "menu"

        elif numero_ingresado == "2":

            pantalla.config(text="Gracias por usar\nBanco El Tigre")

            ventana.after(3000, reiniciar)

            estado = "fin"

        limpiar()

<<<<<<< HEAD
# KEYPAD
=======
#KEYPAD /////////////////////////////////////////////
>>>>>>> 3524fdca18db8b8b2759fa221db0c2c910c31dd3

frame_teclado = tk.Frame(ventana,bg="#FFD100")
frame_teclado.pack()
#use of tuplas>?? check.....
numeros = [
(1,0,0),(2,0,1),(3,0,2),
(4,1,0),(5,1,1),(6,1,2),
(7,2,0),(8,2,1),(9,2,2),
(0,3,1)
]

for (num,r,c) in numeros:

    boton = tk.Button(frame_teclado,text=num,width=6,height=2,bg="black",fg="#FFD100",command=lambda n=num: presionar(n))

    boton.grid(row=r,column=c,padx=5,pady=5)


<<<<<<< HEAD
# CONTROL BUTTONS
=======
#buttones aceptar y borrar //////////////////////
>>>>>>> 3524fdca18db8b8b2759fa221db0c2c910c31dd3

tk.Button(ventana,text="Aceptar",bg="black",fg="#FFD100",width=15,command=aceptar).pack(pady=10)

tk.Button(ventana,text="Borrar",bg="black",fg="#FFD100",width=15,command=limpiar).pack()

#START SCREEN 

<<<<<<< HEAD
# START SCREEN FRAME

start_frame = tk.Frame(ventana, bg="#FFD100")
start_frame.pack(pady=20)

# Load logo
logo = tk.PhotoImage(file="tigre_logo.png")

logo_label = tk.Label(start_frame, image=logo, bg="#FFD100")
logo_label.pack(side="left", padx=10)  
logo_label.image = logo

texto_inicio = tk.Label(
    start_frame,
    text="Banco El Tigre\n\nPresione Aceptar\npara comenzar",
    bg="black",
    fg="#FFD100",
    font=("Courier New",18,"bold"),
    width=20,
    height=6,
    justify="left"
)

texto_inicio.pack(side="right")

# RUN
=======
pantalla.config(text="Banco El Tigre\n\n""Presione Aceptar\n""para comenzar")

#para reniciar y hacerlo correr 
>>>>>>> 3524fdca18db8b8b2759fa221db0c2c910c31dd3
def reiniciar():

    global estado

    estado = "inicio"

    pantalla.config(text="Banco El Tigre\n\n""Presione Aceptar\n""para comenzar")

    limpiar()
ventana.mainloop()