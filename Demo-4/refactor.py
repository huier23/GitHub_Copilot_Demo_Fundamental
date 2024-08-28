from flask import Flask, request, jsonify

app = Flask(__name__)

store = []
port = 3000

@app.route('/store', methods=['GET'])
def get_store():
    return jsonify(store), 200

@app.route('/store', methods=['POST'])
def add_to_store():
    item = request.get_json()
    store.append(item)
    return "success", 200

if __name__ == '__main__':
    app.run(port=port)