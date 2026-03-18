import tkinter as tk
#from banco_final import retirar_gui, depositar_gui, obtener_saldos,convertir_gui
estado = "inicio"
cuenta = ""


#ventana ////

ventana = tk.Tk() 
ventana.title("Banco El Tigre ATM")
ventana.geometry("1000x900")
ventana.configure(bg="#FFD100")   #yellow tigre rawr logo



def regresar():
    global estado

    if estado == "menu":
        pantalla.config(text="Seleccione tipo de cuenta:\n\n1 Ahorro\n2 Corriente\n3 Extranjero")
        estado = "cuenta"

    elif estado in ["moneda", "moneda_origen"]:
        pantalla.config(text="Opciones:\n1 Retiro\n2 Deposito\n3 Consulta\n4 Cambio\n5 Salir")
        estado = "menu"

    elif estado in ["monto", "monto_cambio", "moneda_destino"]:
        pantalla.config(text="Seleccione moneda\n\n1 Bs\n2 USD\n3 GBP\n4 EUR")
        estado = "moneda"

    elif estado == "cuenta":
        pantalla.config(text="Bienvenido al Banco del Tigre\n\n1 Iniciar\n0 Salir")
        estado = "inicio"

    limpiar()

#Botones
frame_top = tk.Frame(ventana, bg="#FFD100")
frame_top.place(x=10, y=10)  # esquina izquierda arriba
tk.Button(
    frame_top,
    text="⬅ Regresar",
    bg="black",
    fg="#FFD100",
    command=regresar
).pack(side="left", padx=5)


# variables para empezar/////

numero_ingresado = ""
estado = "inicio"

#SCREEN ///////////////////////////////////// 
#to fix screen size problem prueba 1
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight() 
ancho_ventana = int(ancho_pantalla * 0.8)
alto_ventana = int(alto_pantalla * 0.8)   

#centered in the middle 
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)

ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
pantalla = tk.Label(ventana,text="Bienvenido\nBanco El Tigre",bg="black",fg="#FFD100",font=("helvetica",20,"bold"),width=40,height=8,justify="left",anchor="nw",padx=15,pady=15)

pantalla.pack(pady=20)

#TIGER LOGO//////////////////////////////////
#anticrasheo
try:
    logo = tk.PhotoImage(file="tigre_logo.png")
    logo_label = tk.Label(ventana,image=logo,bg="#FFD100")
    logo_label.pack()
except:
    pass

#ENTRY DISPLAY 

entrada = tk.Label(ventana,text="",bg="white",fg="black",font=("Courier",16),width=20)

entrada.pack(pady=10)

# FUNCTIONS///////////////////////

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

    # INICIO//////////////////////////////////////////
    if estado == "inicio":
        
        if numero_ingresado == "1":
            pantalla.config(text="Seleccione tipo de cuenta:\n\n1 Ahorro\n2 Corriente\n3 Extranjero")
            estado = "cuenta"
            limpiar()
            return

        elif numero_ingresado == "0":
            pantalla.config(text="Gracias por usar\nBanco El Tigre")
            ventana.after(3000, reiniciar)
            estado = "fin"
            limpiar()
            return

        else:
            pantalla.config(text="Opcion invalida\n\n1 Iniciar\n0 Salir")
            limpiar()
            return



    # CUENTA//////////////////////////////////////////
    if estado == "cuenta":

        if numero_ingresado == "1":
            cuenta = "ahorro"

        elif numero_ingresado == "2":
            cuenta = "corriente"

        else:
            pantalla.config(text="Opcion invalida\n\nSeleccione tipo de cuenta:\n1 Ahorro\n2 Corriente")
            limpiar()
            return

        pantalla.config(text="Opciones:\n1 Retiro\n2 Deposito\n3 Consulta\n4 Cambio\n5 Salir")
        estado = "menu"
        limpiar()
        return

<<<<<<< HEAD


    # MENU
=======
    # MENU////////////////////////////////////
>>>>>>> Andres
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
    
    else:
        pantalla.config(text="Opcion invalida\n\n1 Retiro\n2 Deposito\n3 Consulta\n4 Cambio\n5 Salir")
        limpiar()
        return

    # MONEDA ORIGEN
    if estado == "moneda_origen":

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

        #monto = float(numero_ingresado)
        try:
            monto = float(numero_ingresado)

            if monto <= 0:
                pantalla.config(text="Monto invalido\nIngrese monto:")
                limpiar()
                return

        except:
            pantalla.config(text="Entrada invalida\nIngrese monto:")
            limpiar()
            return


        mensaje = convertir_gui(moneda_origen, moneda_destino, monto)

        pantalla.config(text=
        mensaje + "\n\n""Otra transaccion?\n""1 Si\n2 No")

        estado = "otra"
        limpiar()
        return

    # MONEDA NORMAL
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

    # MONTO NORMAL
    if estado == "monto":
        try:
            monto = float(numero_ingresado)

            if monto <= 0:
                pantalla.config(text="Monto invalido\nIngrese monto:")
                limpiar()
                return

        except:
            pantalla.config(text="Entrada invalida\nIngrese monto:")
            limpiar()
            return

        if operacion == "retiro":
            mensaje = retirar_gui(moneda, monto)

        elif operacion == "deposito":
            mensaje = depositar_gui(moneda, monto)

        pantalla.config(text=mensaje + "\n\n""Otra transaccion?\n""1 Si\n2 No")

        estado = "otra"
        limpiar()
        return

    # OTRA
    if estado == "otra":

        if numero_ingresado == "1":

            pantalla.config(text="Opciones:\n""1 Retiro\n2 Deposito\n3 Consulta\n4 Cambio\n5 Salir")
            estado = "menu"

        elif numero_ingresado == "2":

            pantalla.config(text="Gracias por usar\nBanco El Tigre")

            ventana.after(3000, reiniciar)

            estado = "fin"

        limpiar()

#KEYPAD /////////////////////////////////////////////

frame_teclado = tk.Frame(ventana,bg="#FFD100")
frame_teclado.pack()
#use of tuplas>?? check.....
numeros = [(1,0,0),(2,0,1),(3,0,2),(4,1,0),(5,1,1),(6,1,2),(7,2,0),(8,2,1),(9,2,2),(0,3,1)]

for (num,r,c) in numeros:

    boton = tk.Button(frame_teclado,text=num,width=6,height=2,bg="black",fg="#FFD100",command=lambda n=num: presionar(n))

    boton.grid(row=r,column=c,padx=5,pady=5)


#buttones aceptar y borrar /////////////////////////

tk.Button(ventana,text="Aceptar",bg="black",fg="#FFD100",width=15,command=aceptar).pack(pady=10)

tk.Button(ventana,text="Borrar",bg="black",fg="#FFD100",width=15,command=limpiar).pack()

#START SCREEN 

#pantalla.config(text="Banco El Tigre\n\n""Presione Aceptar\n""para comenzar")
pantalla.config(text="Bienvenido al Banco del Tigre\n\n1 Iniciar\n0 Salir")
estado = "inicio"

#para reniciar y hacerlo correr 
def reiniciar():
    global estado
    estado = "inicio"
<<<<<<< HEAD
    pantalla.config(text="Bienvenido al Banco del Tigre\n\n1 Iniciar\n0 Salir")
=======
    pantalla.config(text="Banco El Tigre\n\n""Presione Aceptar\n""para comenzar")

>>>>>>> Andres
    limpiar()

ventana.mainloop()