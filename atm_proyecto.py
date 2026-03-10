# Cajero automatico atm
import math
import tkinter
def cajero(iniciar):
	if iniciar == 1:
		pin = int(input("Ingrese su pin de 4 digitos: "))
		pin = str(pin)
		if len(pin) == 4:
			print("Ingrese su tipo de cuenta: Caja de Ahorro(1), Cuenta Corriente(2) o Extranjero(0)")
			cuenta = int(input())
			saldo_bs = 1000
			saldo_dol = 0
			saldo_libras = 0
			saldo_euro = 0
			while True:
				opcion = int(input("Ingresa una opcion (0 para help): "))
				if opcion == 0:
					print("Las opciones son:")
					print("1  Retiro")
					print("2  Deposito")
					print("3  Consulta (Consulta de saldo)")
					print("4  Cambio de moneda")
					print("5  Informacion de cuenta")
					print("6  Salir")

				# Retiro
				elif opcion == 1:
					print("Retiro en:")
					print("1. Bolivianos")
					print("2. Dolares")
					print("3. Libras esterlinas")
					print("4. Euro")
					op_retiro = int(input())
					saldo_a_retirar = float(input("Ingresa saldo a retirar: "))
					if op_retiro == 1:
						saldo_bs = saldo_bs - saldo_a_retirar
					elif op_retiro == 2:
						saldo_dol = saldo_dol - saldo_a_retirar
					elif op_retiro == 3:
						saldo_libras = saldo_libras - saldo_a_retirar
					elif op_retiro == 4:
						saldo_euro = saldo_euro - saldo_a_retirar
					else:
						print("Opcion no valida")

					# Confirmacion salir
					print("Desea hacer otra transaccion? ")
					print("Y o N")
					fin_trans = input()
					if fin_trans == "N":
						print("Esta seguro? ")
						fin = input()
						if fin == "Y":
							print("Muchas gracias por usar nuestro servicio :3")
							break
						elif fin == "N":
							print("")
						else:
							print("Opcion no valida")
					elif fin_trans == "Y":
						print("")
					else:
						print("Opcion no valida")	

				# Deposito
				elif opcion == 2:
					print("Deposito en:")
					print("1. Bolivianos")
					print("2. Dolares")
					print("3. Libras esterlinas")
					print("4. Euro")
					op_deposito = int(input())
					saldo_a_depositar = float(input("Ingresa saldo a depositar: "))
					if op_deposito == 1:
						saldo_bs = saldo_bs + saldo_a_depositar
					elif op_deposito == 2:
						saldo_dol = saldo_dol + saldo_a_depositar
					elif op_deposito == 3:
						saldo_libras = saldo_libras + saldo_a_depositar
					elif op_deposito == 4:
						saldo_euro = saldo_euro + saldo_a_depositar
					else:
						print("Opcion no valida")
					# Confirmacion Salir		
					print("Desea hacer otra transaccion? ")
					print("Y o N")
					fin_trans = input()
					if fin_trans == "N":
						print("Esta seguro? ")
						fin = input()
						if fin == "Y":
							print("Muchas gracias por usar nuestro servicio :3")
							break
						elif fin == "N":
							print("")
						else:
							print("Opcion no valida")
					elif fin_trans == "Y":
						print("")
					else:
						print("Opcion no valida")

				# Consulta de saldo		
				elif opcion == 3:
					print("Tu saldo en Bolivianos es: ", round(saldo_bs, 2))
					print("Tu saldo en Dolares es: ", round(saldo_dol, 2))
					print("Tu saldo en Libras esterlinas es: ", round(saldo_libras, 2))
					print("Tu saldo en Euro es: ", round(saldo_euro, 2))

					# Confirmacion Salir		
					print("Desea hacer otra transaccion? ")
					print("Y o N")
					fin_trans = input()
					if fin_trans == "N":
						print("Esta seguro? ")
						fin = input()
						if fin == "Y":
							print("Muchas gracias por usar nuestro servicio :3")
							break
						elif fin == "N":
							print("")
						else:
							print("Opcion no valida")
					elif fin_trans == "Y":
						print("")
					else:
						print("Opcion no valida")

				# Cambio de moneda
				elif opcion == 4:
					print("Selecciona la moneda:")
					print("1. Bolivianos")
					print("2. Dolares")
					print("3. Libras esterlinas")
					print("4. Euro")
					tipo_moneda = int(input())
					if tipo_moneda == 1:
						print("Selecciona el tipo de cambio: ")
						print("1. Dolares")
						print("2. Libras esterlinas")
						print("3. Euro")
						tipo_cambio = int(input())
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
						tipo_cambio = int(input())
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
								saldo_dol = round((monto_convertir / 1.16), 2)
							else:
								print("Opcion no valida")
						else:
							print("Sin saldo suficiente")
					elif tipo_moneda == 3:
						print("Selecciona el tipo de cambio: ")
						print("1. Bolivianos")
						print("2. Dolares")
						print("3. Euro")
						tipo_cambio = int(input())
						monto_convertir = float(input("Ingresa monto a convertir: "))
						if monto_convertir <= saldo_libras:
							if tipo_cambio == 1:
								saldo_libras = saldo_libras - monto_convertir
								saldo_bs = round((monto_convertir * 9.20), 2)
							elif tipo_cambio == 2:
								saldo_dol = saldo_libras - monto_convertir
								saldo_libras = round((monto_convertir * 1.33), 2)
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
						tipo_cambio = int(input())
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

					# Confirmacion Salir		
					print("Desea hacer otra transaccion? ")
					print("Y o N")
					fin_trans = input()
					if fin_trans == "N":
						print("Esta seguro? ")
						fin = input()
						if fin == "Y":
							print("Muchas gracias por usar nuestro servicio :3")
							break
						elif fin == "N":
							print("")
						else:
							print("Opcion no valida")
					elif fin_trans == "Y":
						print("")
					else:
						print("Opcion no valida")

				# Informacion de la cuenta
				elif opcion == 5:
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

					elif pin_revelar == "N":
						print("")
					else:
						print("Opcion no valida")

					# Confirmacion Salir		
					print("Desea hacer otra transaccion? ")
					print("Y o N")
					fin_trans = input()
					if fin_trans == "N":
						print("Esta seguro? ")
						fin = input()
						if fin == "Y":
							print("Muchas gracias por usar nuestro servicio :3")
							break
						elif fin == "N":
							print("")
						else:
							print("Opcion no valida")
					elif fin_trans == "Y":
						print("")
					else:
						print("Opcion no valida")

				# Salir
				elif opcion == 6:
					print("Esta seguro de que desea salir?" )
					print("Y o N")
					seguro_salir = input()
					if seguro_salir == "Y":
						print("Muchas gracias por usar nuestro servicio :3")
						break
					elif seguro_salir == "N":
						print("")
					else:
						print("Opcion no valida")


		else:
			print("Pin invalido")
			
	elif iniciar == 0:
		return
	else:
		print("Opcion invalida")

print("Bienvenido al Banco del Tigre")
print("Presione 1 para iniciar")
print("Presiona 0 para cancelar")
iniciar = int(input())
cajero(iniciar)