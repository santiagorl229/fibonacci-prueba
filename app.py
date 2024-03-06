from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import time

app = Flask(__name__)

# Configuración para el envío de correos electrónicos
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USERNAME'] = 'santiagorl229@gmail.com'
# app.config['MAIL_PASSWORD'] = 'Santiago1960*'
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False

# mail = Mail(app)

from flask import Flask, request, jsonify
import time

app = Flask(__name__)

class Fibonacci:
    def generar_serie(self, semilla_x, semilla_y, cantidad_numeros):
        serie = [semilla_x, semilla_y] #Se genera el inicio de la secuencia
        for _ in range(cantidad_numeros): #En este ciclo for se inicia la cantidad de iteraciones de la serie fibonacci
            nuevo_numero = serie[-1] + serie[-2] # -1 el ultimo valor es decir el valor de x y -2 el valor de y
            serie.append(nuevo_numero)#Vamos agregando con la funcion append los valores de la sumatoria de la serie
        return serie[::-1]  # Invertimos la serie para que esté en orden descendente

@app.route('/serie_fibonacci', methods=['GET'])
def serie_fibonacci():
    hora_actual = time.localtime()
    hora_en_secuencia = str(hora_actual.tm_hour) +':'+str(hora_actual.tm_min)+ ':'+str(hora_actual.tm_sec)

    semilla_x = (hora_actual.tm_min) % 10 #Con el modulo obtenemos el primer valor de izquierda a derecha de los minutos
    semilla_y = (hora_actual.tm_min) // 10 # El primer valor de derecha a izquierda
    cantidad_numeros = hora_actual.tm_sec # Se obtiene la cantidad de numeros 
    if cantidad_numeros == 0:
        return jsonify({'mensaje': 'No se debe mostrar ningún número.'})
    else:
        fibonacci = Fibonacci()
        serie_fibonacci = fibonacci.generar_serie(semilla_x, semilla_y, cantidad_numeros)
        # Envío de correo electrónico
        # msg = Message('Serie Fibonacci Generada', sender='santiagorl229@gmail.com', recipients=['santiagorl229@gmail.com'])
        # msg.body = f'La serie Fibonacci generada es: {serie_fibonacci}'
        # mail.send(msg)
        
        return jsonify({'serie_fibonacci': serie_fibonacci, 'hora_generacion': hora_en_secuencia})

if __name__ == '__main__':
    app.run(debug=True)