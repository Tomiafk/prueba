# Zona de Definiciones

# Retiro
def retiro(opcion):
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


# Deposito
def deposito(opcion):
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

#