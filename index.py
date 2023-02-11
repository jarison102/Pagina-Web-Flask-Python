#de la linea 1 hasta las 6 es para empezar a iniciar el navegador
from flask import Flask,render_template
app = Flask(__name__)

"""
@app.route('/')#indicando con un decorardor una ruta
def principal():
    return "Bienvenido - a mi pagina "

@app.route('/contacto')
def contacto():
    return "bienvenido al contacto"
"""

@app.route('/')#llama la ruta raiz
def principal():#llame un metodo principal que retorna un template de index.html
    return render_template('index.html') #aca hacemos referencia al documento html que esta dentro de templates


@app.route('/lenguajes')
def mostrarlenguajes():
    misleguajes=("PHP","JavaScript","Rubt","Python","Java","Rust","React js")
    return render_template('lenguajes.html',lenguajes=misleguajes)#nombre de la tupla mislenguajes y por el que lo envio lenguajes


@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/Portafolio')
def Portafolio():
    return render_template('Portafolio.html')



if __name__ == '__main__':
    #con el port es para camibar el puesto del navegador
    app.run(debug=True,port=3000)#esto es para que la aplicacion se actualice cada vez que vea un camio

