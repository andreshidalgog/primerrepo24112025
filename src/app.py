from flask import Flask, render_template, request

app = Flask(__name__)


def validar_rut(rut: str) -> bool:
    # Convertido de la función VB: eliminar puntos y guiones, pasar a mayúsculas
    rut = rut.replace('.', '').replace('-', '').upper()

    # Verificar que haya al menos número + dígito verificador
    if len(rut) < 2:
        return False

    numero = rut[:-1]
    dv = rut[-1]

    suma = 0
    multiplicador = 2

    # Recorrer los dígitos de derecha a izquierda
    for ch in reversed(numero):
        if not ch.isdigit():
            return False
        suma += int(ch) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    resto = suma % 11

    if resto == 1:
        dv_esperado = 'K'
    elif resto == 0:
        dv_esperado = '0'
    else:
        dv_esperado = str(11 - resto)

    return dv_esperado == dv


@app.route('/')
def index():
    return render_template('rut.html', resultado=None, rut='')


@app.route('/rut', methods=['GET', 'POST'])
def rut():
    # Permite POST (form) y GET (consulta directa ?rut=...)
    if request.method == 'POST':
        rut_value = request.form.get('rut', '')
        valido = validar_rut(rut_value)
        return render_template('rut.html', resultado=valido, rut=rut_value)

    rut_value = request.args.get('rut', '')
    if rut_value:
        valido = validar_rut(rut_value)
        return render_template('rut.html', resultado=valido, rut=rut_value)
    return render_template('rut.html', resultado=None, rut='')


if __name__ == '__main__':
    # Ejecutar en el puerto 3000 y escuchar en todas las interfaces para Codespaces
    app.run(host='0.0.0.0', port=3000, debug=True)
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Servidor activo ✅</h1><p>Bienvenido a tu primera app con Flask 🚀</p>'

@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre')
    return render_template('saludo.html', nombre=nombre)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
