from flask import Flask
from flask import request
from flask import render_template


import form
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
	sesion = form.Session(request.form)
	if request.method=='POST':
		print sesion.username.data
		print sesion.password.data
	return render_template('index.html',usuario="mau",form=sesion)

@app.route('/prueba')
def prueba():
	return "esto es para ver si si"

@app.route('/grafica')
def grafica():
	print "siiiiii"
	return "grap"

if __name__=='__main__':
	app.run(debug=False,host='0.0.0.0')