from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api/sanxo_store', methods=['GET'])
def obtener_negocio():
    with open('prueba_api.json', 'r', encoding='utf-8') as f:
        datos = json.load(f)
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
