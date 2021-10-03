import datetime

from db import db, ma


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


