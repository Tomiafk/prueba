import tkinter as tk
from banco_final import retirar_gui, depositar_gui, obtener_saldos,convertir_gui
estado = "inicio"
cuenta = ""
#ventana ////

ventana = tk.Tk() 
ventana.title("Banco El Tigre ATM")
#ventana.geometry("1200x900")
ventana.state("zoomed")  # pantalla completa
ventana.configure(bg="#FFD100")   #yellow tigre rawr logo

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

#ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")


pantalla = tk.Label(ventana,bg="black",fg="#FFD100",font=("helvetica",20,"bold"),width=40,height=8,justify="left",anchor="nw",padx=15,pady=15)


pantalla.pack(pady=20)

#TIGER LOGO//////////////////////////////////
#anticrasheo
import os
try:
    ruta = os.path.join(os.path.dirname(__file__), "tigre_logo.png")

    logo = tk.PhotoImage(file=ruta)
    logo = logo.subsample(2, 2)

    logo_label = tk.Label(ventana, image=logo, bg="#FFD100")
    logo_label.image = logo
    logo_label.pack(pady=10)


except:
    print("No se pudo cargar el logo")


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
    if numero_ingresado == "":
        pantalla.config(text="Opcion invalida")
        return


    # INICIO/////////////////////////////////////
    if estado == "inicio":

        if numero_ingresado == "1":
            pantalla.config(text="Seleccione cuenta:\n\n1 Caja de ahorros\n2 Cuenta Extranjera\n\n9 Volver")
            estado = "cuenta"

        elif numero_ingresado == "0":
            pantalla.config(text="Gracias por usar\nBanco El Tigre")
            ventana.after(2000, ventana.destroy)
            estado = "fin"

        else:
            pantalla.config(text="Opcion invalida\n\n1 Iniciar\n0 Salir")

        limpiar()
        return

    # CUENTA//////////////////////////////////////////

    if estado == "cuenta":

        if numero_ingresado == "1":
            cuenta = "cuenta1"

        elif numero_ingresado == "2":
            cuenta = "cuenta2"

        elif numero_ingresado == "9":
            pantalla.config(text="Banco El Tigre\n\n1 Iniciar\n0 Salir")
            estado = "inicio"
            limpiar()
            return

        else:
            pantalla.config(text="Opcion invalida\n\n1 Caja de ahorros\n2 Cuenta extranjera\n9 Volver")
            limpiar()
            return

        pantalla.config(text="Opciones:\n1 Retiro\n2 Deposito\n3 Consulta\n4 Cambio\n5 Salir\n9 Volver")
        estado = "menu"
        limpiar()
        return


    # MENU////////////////////////////////////
    if estado == "menu":

        if numero_ingresado == "1":
            operacion = "retiro"
            pantalla.config(text="Seleccione moneda\n\n1 Bs\n2 USD\n3 GBP\n4 EUR\n9 Volver")
            estado = "moneda"

        elif numero_ingresado == "2":
            operacion = "deposito"
            pantalla.config(text="Seleccione moneda\n\n1 Bs\n2 USD\n3 GBP\n4 EUR\n9 Volver")
            estado = "moneda"

        elif numero_ingresado == "3":
            saldos = obtener_saldos()
            pantalla.config(text=f"BS: {saldos['bs']}\n"f"USD: {saldos['usd']}\n"f"GBP: {saldos['libras']}\n"f"EUR: {saldos['euro']}\n\n""1 Otra\n2 Salir")
            estado = "otra"

        elif numero_ingresado == "4":
            operacion = "cambio"
            pantalla.config(text="Moneda origen:\n\n1 Bs\n2 USD\n3 GBP\n4 EUR\n9 Volver")
            estado = "moneda_origen"

        elif numero_ingresado == "5":
            pantalla.config(text="Gracias por usar\nBanco El Tigre")
            ventana.after(2000, ventana.destroy)
            estado = "fin"

        elif numero_ingresado == "9":
            pantalla.config(text="Seleccione cuenta:\n\n1 Caja de ahorros\n2 Cuenta Extranjera\n9 Volver")
            estado = "cuenta"

        else:
            pantalla.config(text="Opcion invalida\n\n1 Retiro\n2 Deposito\n3 Consulta\n4 Cambio\n5 Salir\n9 Volver")

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

        elif numero_ingresado == "9":
            pantalla.config(text="Opciones:\n1 Retiro\n2 Deposito\n3 Consulta\n4 Cambio\n5 Salir\n9 Volver")
            estado = "menu"
            limpiar()
            return

        else:
            pantalla.config(text="Opcion invalida\n\n1 Bs\n2 USD\n3 GBP\n4 EUR\n9 Volver")
            limpiar()
            return

        pantalla.config(text="Moneda destino:\n\n1 Bs\n2 USD\n3 GBP\n4 EUR\n9 Volver")
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

        elif numero_ingresado == "9":
            pantalla.config(text="Moneda origen:\n\n1 Bs\n2 USD\n3 GBP\n4 EUR\n9 Volver")
            estado = "moneda_origen"
            limpiar()
            return

        else:
            pantalla.config(text="Opcion invalida\n\n1 Bs\n2 USD\n3 GBP\n4 EUR\n9 Volver")
            limpiar()
            return

        pantalla.config(text="Ingrese monto:")
        estado = "monto_cambio"
        limpiar()
        return


    # MONTO CAMBIO
    if estado == "monto_cambio":
        try:
            monto = float(numero_ingresado)

            if monto <= 0:
                pantalla.config(text="Monto invalido")
                limpiar()
                return

        except:
            pantalla.config(text="Entrada invalida")
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

        elif numero_ingresado == "9":
            pantalla.config(text="Opciones:\n1 Retiro\n2 Deposito\n3 Consulta\n4 Cambio\n5 Salir\n9 Volver")
            estado = "menu"
            limpiar()
            return

        else:
            pantalla.config(text="Opcion invalida\n\n1 Bs\n2 USD\n3 GBP\n4 EUR\n9 Volver")
            limpiar()
            return
        pantalla.config(text="Ingrese monto:")
        estado = "monto"
        limpiar()
        return

    # MONTO NORMAL
    if estado == "monto":
        try:
            monto = float(numero_ingresado)
            if monto <= 0:
                pantalla.config(text="Monto invalido\n\nIntente otra vez")
                limpiar()
                return
        except:
            pantalla.config(text="Entrada invalida")
            limpiar()
            return

        if operacion == "retiro":
            mensaje = retirar_gui(moneda, monto)

        elif operacion == "deposito":
            mensaje = depositar_gui(moneda, monto)

        saldos = obtener_saldos()

        pantalla.config(text= mensaje + "\n\n" f"BS: {saldos['bs']}\n"
        f"USD: {saldos['usd']}\n" f"GBP: {saldos['libras']}\n"
        f"EUR: {saldos['euro']}\n\n""Otra transaccion?\n1 Si\n2 No")

        estado = "otra"
        limpiar()
        return

    # OTRA
    if estado == "otra":

        if numero_ingresado == "1":
            pantalla.config(text="Opciones:\n1 Retiro\n2 Deposito\n3 Consulta\n4 Cambio\n5 Salir\n9 Volver")
            estado = "menu"

        elif numero_ingresado == "2":
            pantalla.config(text="Gracias por usar\nBanco El Tigre")
            ventana.after(2000, ventana.destroy)
            estado = "fin"

        else:
            pantalla.config(text="Opcion invalida\n\n1 Si\n2 No")

        limpiar()
        return


#KEYPAD /////////////////////////////////////////////

frame_teclado = tk.Frame(ventana,bg="#FFD100")
frame_teclado.pack()
#use of tuplas>?? check.....
numeros = [(1,0,0),(2,0,1),(3,0,2),(4,1,0),(5,1,1),(6,1,2),(7,2,0),(8,2,1),(9,2,2),(0,3,1)]

for (num,r,c) in numeros:

    boton = tk.Button(frame_teclado,text=num,width=6,height=2,bg="black",fg="#FFD100",command=lambda n=num: presionar(n))

    boton.grid(row=r,column=c,padx=1,pady=5)


#buttones aceptar y borrar /////////////////////////

tk.Button(ventana,text="Aceptar",bg="black",fg="#FFD100",width=15,command=aceptar).pack(pady=10)

tk.Button(ventana,text="Borrar",bg="black",fg="#FFD100",width=15,command=limpiar).pack()

#START SCREEN 


pantalla.config(text="Bienvenido a ""Banco El Tigre\n\n""1 Iniciar\n""0 Salir\n\n""Presione Aceptar")


#para reniciar y hacerlo correr 
def reiniciar():

    global estado
    estado = "inicio"
    pantalla.config(text="Banco El Tigre\n\n""Presione Aceptar\n""para comenzar")
    pantalla.config(text="Banco El Tigre\n\n1 Iniciar\n0 Salir")


    limpiar()
ventana.mainloop()