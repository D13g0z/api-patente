import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/consulta', methods=['GET'])
def consulta():
    patente = request.args.get('patente')
    # lógica de scraping aquí
    return jsonify({'resultado': f'Consulta recibida para {patente}'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render define PORT
    app.run(host='0.0.0.0', port=port, debug=True)