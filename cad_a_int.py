
def cadena_a_entero(antiguo,nuevo):
	i=0
	# si el valor antiguo es mas largo
	if antiguo.len()>nuevo.len():
		while i < nuevo.len():
			if antiguo(i)>nuevo(i):
				return -1
				# el char en 
			elif antiguo(i)<nuevo(i):
				return 1
			i=i+1
		# retorno de -1 porque es mas corto el nuevo
		return -1
	# si el valor nuevo es mas largo
	elif antiguo.len()<nuevo.len():
		while i < antiguo.len():
			if antiguo(i)>nuevo(i):
				return -1
			elif antiguo(i)<nuevo(i):
				return 1
			i=i+1
		# retorno de 1 porque es mas corto el anterior
		return 1
	else:
		while i < antiguo.len():
			if antiguo(i)>nuevo(i):
				return -1
			elif antiguo(i)<nuevo(i):
				return 1
			i=i+1
		# retorno de 0 valores repetidos
		return 0
