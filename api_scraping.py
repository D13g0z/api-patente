from flask import Flask, request, jsonify
from scraping import obtener_datos  # Esta función debe hacer el scraping real

app = Flask(__name__)

@app.route('/consulta', methods=['GET'])
def consulta():
    patente = request.args.get('patente')
    resultado = obtener_datos(patente)  # Aquí se ejecuta el scraping
    return jsonify({'resultado': resultado})