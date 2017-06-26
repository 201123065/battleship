from nodoLista import nodoLista

class Lista():
	def __init__(self):
		self.cabeza=None
	def cargar(self,Usuario,tiros, acertados,fallados, victoria,damage):
		hijo = nodoLista()
		hijo.tiros=tiros
		hijo.acertados=acertados
		hijo.fallados=fallados
		hijo.victoria=victoria
		self.damage=damage
		if self.cabeza==None:
