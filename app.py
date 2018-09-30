from flask import Flask, render_template, request
# Habilitar solo para probar en la raspberry
# import RPi.GPIO as GPIO 

APP = Flask(__name__)

def contact():
    if "nose" in request.data:
        print("Noseee")

@APP.route('/')
def index():
    """Ruta principal
    
    Returns:
        LED -- Encendido/apagado
    """


    print("Print request form", request.form)
    if "Right" in request.form:
        print("Derechaaa")
    elif "Up" in request.form:
        print("Arribaaa")
    return render_template('home.html')


if __name__ == '__main__':
    APP.run(host='0.0.0.0', debug=True)
