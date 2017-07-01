from wtforms import Form
from wtforms import StringField,TextField
from wtforms.fields.html5 import EmailField

from wtforms import validators

class Session(Form):
	username=StringField('username')
	password=StringField('passwd')

	
class Usuario(Form):
	Nombre=StringField('Nombre')
	Passwd=StringField('Passwd')
