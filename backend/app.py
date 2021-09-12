from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({'Ping': 'Pong'})


if __name__ == '__main__':
    app.run(debug=True)

