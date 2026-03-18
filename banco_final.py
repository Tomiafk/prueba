import random
import tkinter

saldo_bs = 1000
saldo_dol = 0
saldo_libras = 0
saldo_euro = 0 

# Zona de Definiciones

# Retiro
def retiro(opcion):
    global saldo_bs, saldo_dol, saldo_libras, saldo_euro
    print("Retiro en:")
    print("1. Bolivianos")
    print("2. Dolares")
    print("3. Libras esterlinas")
    print("4. Euro")
    op_retiro = float(input())
    while True:
        saldo_a_retirar = float(input("Ingresa saldo a retirar: "))
        if saldo_a_retirar <= 0:
            print("Monto no valido")
        if op_retiro == 1:
            if saldo_a_retirar > saldo_bs:
                print("Saldo Insuficiente")
                print("Saldo actual:", saldo_bs)
            else:
                saldo_bs = saldo_bs - saldo_a_retirar
                print("Saldo actual:", saldo_bs)
                break
        elif op_retiro == 2:
            if saldo_a_retirar > saldo_dol:
                print("Saldo Insuficiente")
            else:
                saldo_dol = saldo_dol - saldo_a_retirar
                break
        elif op_retiro == 3:
            if saldo_a_retirar > saldo_libras:
                print("Saldo Insuficiente")
            else:
                saldo_libras = saldo_libras - saldo_a_retirar
                break
        elif op_retiro == 4:
            if saldo_a_retirar > saldo_euro:
                print("Saldo Insuficiente")
            else:
                saldo_euro = saldo_euro - saldo_a_retirar
                break
        else:
            print("Opcion no valida")
    return confirmacion_salir()

# Deposito
def deposito(opcion):
    global saldo_bs, saldo_dol, saldo_libras, saldo_euro
    print("Deposito en:")
    print("1. Bolivianos")
    print("2. Dolares")
    print("3. Libras esterlinas")
    print("4. Euro")
    op_deposito = float(input())
    while True:
        saldo_a_depositar = float(input("Ingresa saldo a depositar: "))
        if saldo_a_depositar <= 0:
            print("Opcion no valida")
        if op_deposito == 1:
            saldo_bs = saldo_bs + saldo_a_depositar
            break
        elif op_deposito == 2:
            saldo_dol = saldo_dol + saldo_a_depositar
            break
        elif op_deposito == 3:
            saldo_libras = saldo_libras + saldo_a_depositar
            break
        elif op_deposito == 4:
            saldo_euro = saldo_euro + saldo_a_depositar
            break
        else:
            print("Opcion no valida")
    return confirmacion_salir()

# Consulta de Saldo
def consulta_saldo(opcion):
    global saldo_bs, saldo_dol, saldo_libras, saldo_euro
    print("Tu saldo en Bolivianos es: ", round(saldo_bs, 2))
    print("Tu saldo en Dolares es: ", round(saldo_dol, 2))
    print("Tu saldo en Libras esterlinas es: ", round(saldo_libras, 2))
    print("Tu saldo en Euro es: ", round(saldo_euro, 2))
    return confirmacion_salir()

# Cambio de moneda
def cambio_moneda(opcion):
    global saldo_bs, saldo_dol, saldo_libras, saldo_euro
    print("Selecciona la moneda:")
    print("1. Bolivianos")
    print("2. Dolares")
    print("3. Libras esterlinas")
    print("4. Euro")
    tipo_moneda = float(input())
    if tipo_moneda == 1:
        print("Selecciona el tipo de cambio: ")
        print("1. Dolares")
        print("2. Libras esterlinas")
        print("3. Euro")
        tipo_cambio = float(input())
        monto_convertir = float(input("Ingresa monto a convertir: "))
        if monto_convertir <= saldo_bs:
            if tipo_cambio == 1:
                saldo_bs = saldo_bs - monto_convertir
                saldo_dol = round((monto_convertir / 6.96), 2)
            elif tipo_cambio == 2:
                saldo_bs = saldo_bs - monto_convertir
                saldo_libras = round((monto_convertir / 9.20), 2)
            elif tipo_cambio == 3:
                saldo_bs = saldo_bs - monto_convertir
                saldo_euro = round((monto_convertir / 7.99), 2)
            else:
                print("Opcion no valida")
        else:
            print("Sin saldo suficiente")
    elif tipo_moneda == 2:
        print("Selecciona el tipo de cambio: ")
        print("1. Bolivianos")
        print("2. Libras esterlinas")
        print("3. Euro")
        tipo_cambio = float(input())
        monto_convertir = float(input("Ingresa monto a convertir: "))
        if monto_convertir <= saldo_dol:
            if tipo_cambio == 1:
                saldo_dol = saldo_dol - monto_convertir
                saldo_bs = round((monto_convertir * 6.96) ,2)
            elif tipo_cambio == 2:
                saldo_dol = saldo_dol - monto_convertir
                saldo_libras = round((monto_convertir / 1.33), 2)
            elif tipo_cambio == 3:
                saldo_dol = saldo_dol - monto_convertir
                saldo_euro = round((monto_convertir / 1.16), 2)
            else:
                print("Opcion no valida")
        else:
            print("Sin saldo suficiente")
    elif tipo_moneda == 3:
        print("Selecciona el tipo de cambio: ")
        print("1. Bolivianos")
        print("2. Dolares")
        print("3. Euro")
        tipo_cambio = float(input())
        monto_convertir = float(input("Ingresa monto a convertir: "))
        if monto_convertir <= saldo_libras:
            if tipo_cambio == 1:
                saldo_libras = saldo_libras - monto_convertir
                saldo_bs = round((monto_convertir * 9.20), 2)
            elif tipo_cambio == 2:
                saldo_libras = saldo_libras - monto_convertir
                saldo_dol = round((monto_convertir * 1.33), 2)
            elif tipo_cambio == 3:
                saldo_libras = saldo_libras - monto_convertir
                saldo_euro = round((monto_convertir * 1.15), 2)
            else:
                print("Opcion no valida")
        else:
            print("Sin saldo suficiente")

    elif tipo_moneda == 4:
        print("Selecciona el tipo de cambio: ")
        print("1. Bolivianos")
        print("2. Dolares")
        print("3. Libras esterlinas")
        tipo_cambio = float(input())
        monto_convertir = float(input("Ingresa monto a convertir: "))
        if monto_convertir <= saldo_euro:
            if tipo_cambio == 1:
                saldo_euro = saldo_euro - monto_convertir
                saldo_bs = round((monto_convertir * 7.99), 2)
            elif tipo_cambio == 2:
                saldo_euro = saldo_euro - monto_convertir
                saldo_dol = round((monto_convertir * 1.16), 2)
            elif tipo_cambio == 3:
                saldo_euro = saldo_euro - monto_convertir
                saldo_libras = round((monto_convertir / 1.15), 2)
            else:
                print("Opcion no valida")
        else:
            print("Sin saldo suficiente")
    return confirmacion_salir()



# Informacion de la cuenta
def info_cuenta(opcion):
    global saldo_bs, saldo_dol, saldo_libras, saldo_euro
    while True:
        print("Informacion de tu cuenta: ")
        print("Banco del Tigre")
        print("Pin: ****")
        if cuenta == 1:
            print("Tipo de cuenta: Caja de Ahorro")
        elif cuenta == 2:
            print("Tipo de cuenta: Cuenta Corriente")
        elif cuenta == 0:
            print("Tipo de cuenta: Extranjero")

        print("Desea revelar el pin? ")
        print("Y o N")

        pin_revelar = input()
        if pin_revelar == "Y":
            print("Informacion de tu cuenta: ")
            print("Banco del Tigre")
            print("Pin: ",pin)
            if cuenta == 1:
                print("Tipo de cuenta: Caja de Ahorro")
            elif cuenta == 2:
                print("Tipo de cuenta: Cuenta Corriente")
            elif cuenta == 0:
                print("Tipo de cuenta: Extranjero")
            break

        elif pin_revelar == "N":
            print("")
            break
        else:
            print("Opcion no valida")
    return confirmacion_salir()

# Salir
def salir(opcion):
    while True:
        print("Esta seguro de que desea salir?" )
        print("Y o N")
        seguro_salir = input()
        if seguro_salir == "Y":
            print("Muchas gracias por usar nuestro servicio :3")
            return True
            break
        elif seguro_salir == "N":
            return False
            break
        else:
            print("Opcion no valida")
            print("Esta seguro? ")
            print("Y o N")
            saalir_fin = input()

# Confirmacion salir
def confirmacion_salir():
    while True:
        print("Desea hacer otra transaccion? ")
        print("Y o N")
        fin_trans = input()
        if fin_trans == "N":
            print("Esta seguro? ")
            fin = input()
            if fin == "Y":
                print("Muchas gracias por usar nuestro servicio :3")
                return True
                break
            elif fin == "N":
                return False
                break
            else:
                print("Opcion no valida")
        elif fin_trans == "Y":
            print("")
            break
        else:
            print("Opcion no valida")




def cajero_fin(iniciar):
    global pin, cuenta
    while True:
        if iniciar == 1:
            pin = input("Ingrese su pin de 4 digitos: ")
            pin = str(pin)
            if len(pin) == 4:
                print("Ingrese su tipo de cuenta: Caja de Ahorro(1), Cuenta Corriente(2) o Extranjero(3)")
                cuenta = float(input())
                if cuenta == 3 or cuenta == 2 or cuenta == 1:    
                    while True:
                        opcion = float(input("Ingresa una opcion (0 para help): "))
                        if opcion == 0:
                            print("Las opciones son:")
                            print("1  Retiro")
                            print("2  Deposito")
                            print("3  Consulta (Consulta de saldo)")
                            print("4  Cambio de moneda")
                            print("5  Informacion de cuenta")
                            print("6  Salir")
                        elif opcion == 1:
                            if retiro(opcion):
                                return

                        elif opcion == 2:
                            if deposito(opcion):
                                return
                           
                        elif opcion == 3:
                            if consulta_saldo(opcion):
                                return

                        elif opcion == 4:
                            if cambio_moneda(opcion):
                                return
                            
                        elif opcion == 5:
                            if info_cuenta(opcion):
                                return
                            
                        elif opcion == 6:
                            if salir(opcion):
                                return
                        else:
                            print("Opcion no valida")
                else:
                    print("Cuenta no valida")
            else:
                print("Pin invalido")
                print("Usted no es el propietario de esta cuenta")
                break

        elif iniciar == 0:
            print("Esta seguro? ")
            print("Y o N")
            saalir_fin = input()
            if saalir_fin == "Y":
                print("Muchas gracias por usar nuestro servicio :3")
                break
            elif saalir_fin == "N":
                print("Bienvenido al Banco del Tigre")
                print("Presione 1 para iniciar")
                print("Presiona 0 para cancelar")
                iniciar = float(input())

            else:
                print("Opcion no valida")
        else:
            print("opcion invalida")
            iniciar = float(input())

# FUNCIONES PARA GUI

def obtener_saldos():
    return {
        "bs": saldo_bs,
        "usd": saldo_dol,
        "libras": saldo_libras,
        "euro": saldo_euro
    }


def retirar_gui(moneda, monto):
    global saldo_bs, saldo_dol, saldo_libras, saldo_euro

    if monto < 0:
        return "Monto no valido"

    if moneda == "bs":
        if monto > saldo_bs:
            return "Saldo insuficiente"
        saldo_bs -= monto

    elif moneda == "usd":
        if monto > saldo_dol:
            return "Saldo insuficiente"
        saldo_dol -= monto

    elif moneda == "libras":
        if monto > saldo_libras:
            return "Saldo insuficiente"
        saldo_libras -= monto

    elif moneda == "euro":
        if monto > saldo_euro:
            return "Saldo insuficiente"
        saldo_euro -= monto

    return "Retiro exitoso"


def depositar_gui(moneda, monto):
    global saldo_bs, saldo_dol, saldo_libras, saldo_euro

    if monto < 0:
        return "Monto no valido"

    if moneda == "bs":
        saldo_bs += monto

    elif moneda == "usd":
        saldo_dol += monto

    elif moneda == "libras":
        saldo_libras += monto

    elif moneda == "euro":
        saldo_euro += monto

    return "Deposito exitoso"


# ORIGINAL CODE

pin = ""
cuenta = 0

if __name__ == "__main__":
    print("Bienvenido al Banco del Tigre")
    print("Presione 1 para iniciar")
    print("Presiona 0 para cancelar")
    iniciar =float(input())
    cajero_fin(iniciar)
