__author__ = "Mac"
__date__ = "$Jun 12, 2017 11:41:07 AM$"

from flask import flasksk, request

app = Flask("ejemploJunio")

@app.route('/metodo2',methods=['POST']) 
def h():
    parametroPython = str(request.form['p'])
    parametroPython2 = str(request.form['pa'])
    return "parametro = " + parametroPython

@app.route('/hola') 
def he():
    return "hola Mundo" 

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')