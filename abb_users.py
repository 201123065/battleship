from nodo_users import User
from cad_a_int import cadena_a_entero
class ABB_USERS():
	def __init__(self):
		self.raiz=None
	def Agregar(self,nombre,passwd,login):
		usuario =User(nombre,passwd,login,None,None,None)
		if self.raiz==None:
			self.raiz=usuario
		else:
			temporal = self.raiz
			while temporal!=None:
				if temporal.nombre>usuario.nombre:
					temporal=temporal.izq
				elif temporal.nombre<usuario.nombre:
					temporal=temporal.der
				else:
					return "este usuario ya existe"
			temporal=usuario
			return "agregado satisfactoriamente"; 
	def Modificar(self,nombre,nuevo_nombre):
		tmp = self.raiz



TMP   usuario
AAB		AAA
AAA		AAB