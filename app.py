from flask import Flask, render_template, request
# Habilitar solo para probar en la raspberry
# import RPi.GPIO as GPIO
import servo

APP = Flask(__name__)

@APP.route('/')
def index():
    """Ruta principal

    Returns:
        LED -- Encendido/apagado
    """
    return render_template('home.html')


@APP.route('/right', methods=['POST'])
def right():
    """Ruta principal

    Returns:
        LED -- Encendido/apagado
    """
    servo.correr()

    print("Derecha")
    return render_template('home.html')


@APP.route('/center', methods=["POST"])
def center():
    """Ruta principal

    Returns:
        LED -- Encendido/apagado
    """
    print("CENTROO")
    return render_template('home.html')


@APP.route('/left', methods=["POST"])
def left():
    """Ruta principal

    Returns:
        LED -- Encendido/apagado
    """
    print("IZQUIERDA")
    return 'I'


if __name__ == '__main__':
    APP.run(host='0.0.0.0', debug=True)
