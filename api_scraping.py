from flask import Flask, request, jsonify
from scraping import consultar_patente_chile  # ✅ nombre correcto de la función

app = Flask(__name__)

@app.route("/consultar", methods=["GET"])
def consultar():
    patente = request.args.get("patente")
    if not patente:
        return jsonify({"error": "Falta el parámetro 'patente'"}), 400

    resultado = consultar_patente_chile(patente)
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
