import datetime

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from db import db, ma
from db.models.books import Book, book_schema, books_schema


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)


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


@app.route('/get/<pk>', methods=['GET'])
def book_detail(pk):
    book = Book.query.get_or_404(pk)
    return book_schema.jsonify(book)


@app.route('/edit/<pk>', methods=['PUT'])
def update_book(pk):
    book = Book.query.get_or_404(pk)

    name = request.json['name']
    author = request.json['author']

    book.name = name
    book.author = author

    db.session.commit()
    return book_schema.jsonify(book)


@app.route('/delete/<pk>', methods=['DELETE'])
def delete_book(pk):
    book = Book.query.get_or_404(pk)
    db.session.delete(book)

    db.session.commit()
    return book_schema.jsonify(book)


if __name__ == '__main__':
    app.run(debug=True)

