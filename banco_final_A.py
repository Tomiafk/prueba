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
    try:
        op_retiro = int(input())
    except:
        print("Opcion invalida")
        return
    while True:
        saldo_a_retirar = int(input("Ingresa saldo a retirar: "))
        if saldo_a_retirar <= 0:
            print("Monto no valido")
            continue
        if op_retiro == 1:
            if saldo_a_retirar > saldo_bs:
                print("Saldo Insuficiente")
            else:
                saldo_bs = saldo_bs - saldo_a_retirar
                print("Transaccion exitosa")
                
                print("Revisar consulta de saldo")
                break
            
        elif op_retiro == 2:
            if saldo_a_retirar > saldo_dol:
                print("Saldo Insuficiente")
            else:
                saldo_dol = saldo_dol - saldo_a_retirar
                print("Transaccion exitosa")
                print("Saldo actual:")
                break
        elif op_retiro == 3:
            if saldo_a_retirar > saldo_libras:
                print("Saldo Insuficiente")
            else:
                saldo_libras = saldo_libras - saldo_a_retirar
                print("Transaccion exitosa")
                print("Revisar consulta de saldo")
                break
        elif op_retiro == 4:
            if saldo_a_retirar > saldo_euro:
                print("Saldo Insuficiente")
            else:
                saldo_euro = saldo_euro - saldo_a_retirar
                print("Transaccion exitosa")
                print("Revisar consulta de saldo")
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
    
    while True:
        try:
            op_deposito = int(input())

            if 1 <= op_deposito <= 4:
                break
            else:
                print("Opcion invalida")

        except:
            print("Entrada invalida")


    while True:
        try:
            saldo_a_depositar = int(input("Ingresa saldo a depositar: "))

            if saldo_a_depositar <= 0:
                print("Monto invalido")
                continue

            if saldo_a_depositar % 10 != 0:
                print("Solo montos en decenas (10, 20, 30...)")
                continue

            break

        except:
            print("Entrada invalida")
 
    while True:
        if saldo_a_depositar <= 0:
            print("Opcion no valida")
        if op_deposito == 1:
            saldo_bs = saldo_bs + saldo_a_depositar
            print("Transaccion exitosa")
            print("Saldo actual: ", saldo_bs)
            break
        elif op_deposito == 2:
            saldo_dol = saldo_dol + saldo_a_depositar
            print("Transaccion exitosa")
            print("Saldo actual: ", saldo_dol)
            break
        elif op_deposito == 3:
            saldo_libras = saldo_libras + saldo_a_depositar
            print("Transaccion exitosa")
            print("Saldo actual: ", saldo_dol)
            break
        elif op_deposito == 4:
            saldo_euro = saldo_euro + saldo_a_depositar
            print("Transaccion exitosa")
            print("Saldo actual: ", saldo_euro)
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
    while True:
        try:
            tipo_moneda = int(input())

            if 1 <= tipo_moneda <= 4:
                break
            else:
                print("Opcion invalida")

        except:
            print("Entrada invalida")

   
    if tipo_moneda == 1:
        print("Selecciona el tipo de cambio: ")
        print("1. Dolares")
        print("2. Libras esterlinas")
        print("3. Euro")
        while True:
            try:
                tipo_cambio = int(input())

                if 1 <= tipo_cambio <= 3:
                    break
                else:
                    print("Opcion invalida")

            except:
                print("Entrada invalida")

        while True:
            try:
                monto_convertir = int(input("Ingresa monto a convertir: "))

                if monto_convertir <= 0:
                    print("Monto invalido")
                    continue
                if monto_convertir % 10 != 0:
                    print("Solo se permiten montos en decenas y centenas (10, 20, 30, 100...)")
                    continue

                break

            except:
                print("Entrada invalida")

        if monto_convertir <= saldo_bs:
            if tipo_cambio == 1:
                saldo_bs = saldo_bs - monto_convertir
                saldo_dol += round((monto_convertir / 6.96), 2)
                print("Transaccion exitosa")
                print("Revisar consulta de saldo")
            elif tipo_cambio == 2:
                saldo_bs = saldo_bs - monto_convertir
                saldo_libras += round((monto_convertir / 9.20), 2)
                print("Transaccion exitosa")
                print("Revisar consulta de saldo")
            elif tipo_cambio == 3:
                saldo_bs = saldo_bs - monto_convertir
                saldo_euro += round((monto_convertir / 7.99), 2)
                print("Transaccion exitosa")
                print("Revisar consulta de saldo")
            else:
                print("Opcion no valida")
        else:
            print("Sin saldo suficiente")
    elif tipo_moneda == 2:
        print("Selecciona el tipo de cambio: ")
        print("1. Bolivianos")
        print("2. Libras esterlinas")
        print("3. Euro")
        while True:
            try:
                tipo_cambio = int(input())

                if 1 <= tipo_cambio <= 3:
                    break
                else:
                    print("Opcion invalida")

            except:
                print("Entrada invalida")

        while True:
            try:
                monto_convertir = int(input("Ingresa monto a convertir: "))

                if monto_convertir <= 0:
                    print("Monto invalido")
                    continue
                if monto_convertir % 10 != 0:
                    print("Solo se permiten montos en decenas y centenas (10, 20, 30, 100...)")
                    continue

                break

            except:
                print("Entrada invalida")

        if monto_convertir <= saldo_dol:
            if tipo_cambio == 1:
                saldo_dol = saldo_dol - monto_convertir
                saldo_bs += round((monto_convertir * 6.96) ,2)
                print("Transaccion exitosa")
                print("Revisar consulta de saldo")
            elif tipo_cambio == 2:
                saldo_dol = saldo_dol - monto_convertir
                saldo_libras += round((monto_convertir / 1.33), 2)
                print("Transaccion exitosa")
                print("Revisar consulta de saldo")
            elif tipo_cambio == 3:
                saldo_dol = saldo_dol - monto_convertir
                saldo_euro += round((monto_convertir / 1.16), 2)
                print("Transaccion exitosa")
                print("Revisar consulta de saldo")
            else:
                print("Opcion no valida")
        else:
            print("Sin saldo suficiente")
            
    elif tipo_moneda == 3:
        print("Selecciona el tipo de cambio: ")
        print("1. Bolivianos")
        print("2. Dolares")
        print("3. Euro")
        while True:
            try:
                tipo_cambio = int(input())

                if 1 <= tipo_cambio <= 3:
                    break
                else:
                    print("Opcion invalida")

            except:
                print("Entrada invalida")

        while True:
            try:
                monto_convertir = int(input("Ingresa monto a convertir: "))

                if monto_convertir <= 0:
                    print("Monto invalido")
                    continue
                if monto_convertir % 10 != 0:
                    print("Solo se permiten montos en decenas y centenas (10, 20, 30, 100...)")
                    continue

                break

            except:
                print("Entrada invalida")

        if monto_convertir <= saldo_libras:
            if tipo_cambio == 1:
                saldo_libras = saldo_libras - monto_convertir
                saldo_bs += round((monto_convertir * 9.20), 2)
                print("Transaccion exitosa")
                print("Revisar consulta de saldo")
            elif tipo_cambio == 2:
                saldo_libras = saldo_libras - monto_convertir
                saldo_dol += round((monto_convertir * 1.33), 2)
                print("Transaccion exitosa")
                print("Revisar consulta de saldo")
            elif tipo_cambio == 3:
                saldo_libras = saldo_libras - monto_convertir
                saldo_euro += round((monto_convertir * 1.15), 2)
                print("Transaccion exitosa")
                print("Revisar consulta de saldo")
            else:
                print("Opcion no valida")
        else:
            print("Sin saldo suficiente")

    elif tipo_moneda == 4:
        print("Selecciona el tipo de cambio: ")
        print("1. Bolivianos")
        print("2. Dolares")
        print("3. Libras esterlinas")
        while True:
            try:
                tipo_cambio = int(input())

                if 1 <= tipo_cambio <= 3:
                    break
                else:
                    print("Opcion invalida")

            except:
                print("Entrada invalida")

        while True:
            try:
                monto_convertir = int(input("Ingresa monto a convertir: "))

                if monto_convertir <= 0:
                    print("Monto invalido")
                    continue
                if monto_convertir % 10 != 0:
                    print("Solo se permiten montos en decenas y centenas (10, 20, 30, 100...)")
                    continue

                break

            except:
                print("Entrada invalida")

        if monto_convertir <= saldo_euro:
            if tipo_cambio == 1:
                saldo_euro = saldo_euro - monto_convertir
                saldo_bs += round((monto_convertir * 7.99), 2)
                print("Transaccion exitosa")
                print("Revisar consulta de saldo")
            elif tipo_cambio == 2:
                saldo_euro = saldo_euro - monto_convertir
                saldo_dol += round((monto_convertir * 1.16), 2)
                print("Transaccion exitosa")
                print("Revisar consulta de saldo")
            elif tipo_cambio == 3:
                saldo_euro = saldo_euro - monto_convertir
                saldo_libras += round((monto_convertir / 1.15), 2)
                print("Transaccion exitosa")
                print("Revisar consulta de saldo")
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
        elif seguro_salir == "N":
            return False
        else:
            print("Opcion no valida")
        

# Confirmacion salir
def confirmacion_salir():
    while True:
        print("Desea hacer otra transaccion?")
        print("Y o N")
        fin_trans = input()

        if fin_trans == "Y":
            return False

        elif fin_trans == "N":
            while True:
                print("Esta seguro?")
                print("Y o N")
                fin = input()

                if fin == "Y":
                    print("Muchas gracias por usar nuestro servicio :3")
                    return True
                
                elif fin == "N":
                    break
                else:
                    print("Opcion no valida")

        else:
            print("Opcion no valida")

#pin

def cajero_fin(iniciar):
    global pin, cuenta
    while True:
        if iniciar == 1: 
            intentos = 3

            while intentos > 0:
                pin = input("Ingrese su pin de 4 digitos: ")

                try:
                    int(pin)

                    if len(pin) == 4:
                        print("PIN correcto")
                        while True:
                            print("Ingrese su tipo de cuenta:")
                            print("Caja de Ahorro (1)")
                            print("Cuenta Corriente (2)")
                            print("Extranjero (0)")

                            try:
                                cuenta = int(input())

                                if cuenta in (0, 1, 2):
                                    break
                                else:
                                    print("Opcion invalida")

                            except:
                                print("Entrada invalida")

                       
                        break
                    else:
                        print("Pin invalido")

                except:
                    print("Pin invalido")

                intentos -= 1

                if intentos == 0:
                    print("Demasiados intentos fallidos")
                    print("Usted no es propietario de esta cuenta")
                    return


            while True:
                try:
                    opcion = int(input("Ingresa una opcion (0 para help): "))
                except:
                    print("Entrada invalida")
                    continue
                
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
            try:
                iniciar = int(input())
            except:
                print("Entrada invalida")
                return

# -------- FUNCIONES PARA GUI --------

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


# -------- ORIGINAL CODE --------

pin = ""
cuenta = 0

if __name__ == "__main__":
    print("Bienvenido al Banco del Tigre")
    print("Presione 1 para iniciar")
    print("Presiona 0 para cancelar")

    while True:
        try:
            iniciar = int(input())
            if iniciar == 1 or iniciar == 0:
                break
            else:
                print("Opcion invalida")
        except:
            print("Entrada invalida")

    cajero_fin(iniciar)

