from flask import Flask, request, jsonify
from scraping import consultar_patente_chile

app = Flask(__name__)

@app.route("/consulta", methods=["GET"])
def consulta():
    patente = request.args.get("patente", "").upper()

    if not patente:
        return jsonify({"error": "❗ Debes proporcionar una patente."}), 400

    resultado = consultar_patente_chile(patente)
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(debug=True)
    