import datetime

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
ma = Marshmallow(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    author = db.Column(db.String(80), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, name, author):
        self.name = name
        self.author = author
        

class BookSchema(ma.Schema):
    class Meta():
        fields = ('id', 'name', 'author', 'created_at')


book_schema = BookSchema()
books_schema = BookSchema(many=True)


@app.route('/', methods=['GET'])
def main_page():
    all_books = Book.query.all()
    serialized_books = books_schema.dump(all_books)

    return jsonify(serialized_books)


@app.route('/create', methods=['POST'])
def created_book():
    name = request.json['name']
    author = request.json['author']

    book = Book(name, author)
    db.session.add(book)
    db.session.commit()

    return book_schema.jsonify(book)


if __name__ == '__main__':
    app.run(debug=True)

