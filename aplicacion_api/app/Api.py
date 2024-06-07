from flask import Flask, request, jsonify
from Calculadora import Calculadora
from flask_cors import CORS

app = Flask(__name__)
#CORS(app, resources={r"/*": {"origins": ["http://localhost:8081","http://ubuntu-tests:8081","http:servicio-web-calculadora"]}}, supports_credentials=True)
CORS(app)
calculadora = Calculadora()

@app.route('/sume', methods=['GET'])
def Sume():
    try:
        primerNumero = request.args.get('primerNumero', type=float)
        segundoNumero = request.args.get('segundoNumero', type=float)
        resultado = calculadora.Sume(primerNumero, segundoNumero)
        return jsonify({'resultado': resultado})
    except TypeError as e:
         return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor.'}), 500   
    

@app.route('/reste', methods=['GET'])
def Reste():
    try:
        primerNumero = request.args.get('primerNumero', type=float)
        segundoNumero = request.args.get('segundoNumero', type=float)
        resultado = calculadora.Reste(primerNumero, segundoNumero)
        return jsonify({'resultado': resultado})
    except TypeError as e:
         return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor.'}), 500   


@app.route('/multiplique', methods=['GET'])
def Multiplique():
    try:
        primerNumero = request.args.get('primerNumero', type=float)
        segundoNumero = request.args.get('segundoNumero', type=float)
        resultado = calculadora.Multiplique(primerNumero, segundoNumero)
        return jsonify({'resultado': resultado})
    except TypeError as e:
         return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor.'}), 500
    
@app.route('/divida', methods=['GET'])
def Divida():
    try:
        primerNumero = request.args.get('primerNumero', type=float)
        segundoNumero = request.args.get('segundoNumero', type=float)
        resultado = calculadora.Divida(primerNumero, segundoNumero)
        return jsonify({'resultado': resultado})
    except TypeError as e:
         return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor.'}), 500
    
@app.route('/calcule_potencia', methods=['GET'])
def CalculePotencia():
    try:
        base = request.args.get('base', type=float)
        exponente = request.args.get('exponente', type=float)
        resultado = calculadora.CalculePotencia(base, exponente)
        return jsonify({'resultado': resultado})
    except TypeError as e:
         return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor.'}), 500
    
@app.route('/calcule_raiz_cuadrada', methods=['GET'])
def CalculeRaizCuadrada():
    try:
        numero = request.args.get('numero', type=float)
        resultado = calculadora.CalculeRaizCuadrada(numero)
        return jsonify({'resultado': resultado})
    except TypeError as e:
         return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor.'}), 500
    
@app.route('/calcule_logaritmo_base_10', methods=['GET'])
def CalculeLogaritmoEnBase10():
    try:
        numero = request.args.get('numero', type=float)
        resultado = calculadora.CalculeLogaritmoEnBase10(numero)
        return jsonify({'resultado': resultado})
    except TypeError as e:
         return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Error interno del servidor.'}), 500  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
