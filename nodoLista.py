class nodoLista():
	def __init__(self,usuario=None, tiros=None,acertados=None,fallados=None,victoria=None,damage=None,siguiente=None,anterior=None):
		self.tiros = tiros
		self.acertados=acertados
		self.fallados=fallados
		self.victoria=victoria
		self.damage=damage
		self.siguiente=siguiente
		self.anterior = anterior
