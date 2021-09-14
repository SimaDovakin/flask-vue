import datetime

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    author = db.Column(db.String(80), nullable=False, unique=True)
    creted_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, name, author):
        self.name = name
        self.author = author

@app.route('/', methods=['GET'])
def ping():
    return jsonify({'Ping': 'Pong', 'Hello': 'World'})


if __name__ == '__main__':
    app.run(debug=True)

