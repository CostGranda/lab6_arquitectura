from flask import Flask, render_template, request
# Habilitar solo para probar en la raspberry
# import RPi.GPIO as GPIO
import servo

APP = Flask(__name__)

p = servo.setup() # Configuración
p.start(2.5) # Arranque

@APP.route('/')
def index():
    """Ruta Principal
    
    Returns:
        Template -- Página principal/home
    """
    return render_template('home.html')


@APP.route('/right', methods=['POST'])
def right():
    """Ruta principal

    Returns:
        LED -- Encendido/apagado
    """

    servo.right(p)
    p.stop()
    return render_template('home.html')


@APP.route('/center', methods=["POST"])
def center():
    """Ruta principal

    Returns:
        LED -- Encendido/apagado
    """
    servo.center(p)
    p.stop()
    return render_template('home.html')


@APP.route('/left', methods=["POST"])
def left():
    """Ruta principal

    Returns:
        LED -- Encendido/apagado
    """
    servo.left(p)
    p.stop()
    return render_template('home.html')


if __name__ == '__main__':
    APP.run(host='0.0.0.0', debug=True)

