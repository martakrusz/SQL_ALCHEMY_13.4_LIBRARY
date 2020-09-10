from app import db
from datatime import datatime

class Title(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, unique=True)
    borrowed = db.relationship('Borrowed', backref='book', lazy='dynamic')

    def __str__(self):
        return f"<Title {self.title}>"

class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(200), index=True)
    many_authors = db.relationship(     )

    def __str__(self):
        return f"<Author {self.author}>"

