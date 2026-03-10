def cajero(pin, cuenta, opcion):
	if len(pin) == 4:
		if opcion == 0:
			print("Las opciones son:")
			print("1  Retiro")
			print("2  Deposito")
			print("3  Consulta (Consulta de saldo)")
			print("4 Cambio de moneda")
	else:
		print("Pin invalido")

poner_pin = str(input("Ingrese su pin de 4 digitos: "))
print("Ingrese su tipo de cuenta: Caja de Ahorro(1), Cuenta Corriente(2) o Extranjero(0)")
cuentatipo = int(input())
elegir = int(input("Ingresa una opcion (0 para help): "))
cajero(poner_pin, cuentatipo, elegir)