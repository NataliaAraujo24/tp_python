def validarVacios(dato):
	if(dato == ""):
		return True
	else:
		return False
def validarSoloNumeros(dato):
	print(dato)
	dato = str(dato)
	for caracter in dato:
		if(not(caracter.isdigit())):
			if(ord(caracter)!=46):
				return True
	return False
def validarSoloNumerosEnteros(dato):
	dato = str(dato)
	for caracter in dato:
		if(not(caracter.isdigit())):
			return True
	return False
