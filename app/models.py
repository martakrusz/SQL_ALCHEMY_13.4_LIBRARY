from app import db
from datetime import datetime


tilte_author = db.Table('tilte_author',
    db.Column('title_id', db.Integer, db.ForeignKey('title.title_id')),
    db.Column('author_id', db.Integer, db.ForeignKey('author.author_id'))
)


class Title(db.Model):
    title_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, unique=True)
    borrowed = db.relationship('Borrowed', backref = 'book')
    returned = db.relationship('Returned', backref = 'book')

    def __str__(self):
        return f"<Title {self.title}>"

class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(200), index=True)
    authors = db.relationship('Title', secondary=tilte_author, backref=db.backref('authors', lazy = 'dynamic'))

    def __str__(self):
        return f"<Author {self.author}>"


class Borrowed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrowed_date = db.Column(db.Date, index=True, default=datetime.today())
    book_id = db.Column(db.Integer, db.ForeignKey('title.title_id'))

    def __str__(self):
        return f"<Borrowed {self.id} {self.book_id}>"

class Returned(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    returned_date = db.Column(db.Date, index=True, default=datetime.today())
    book_id = db.Column(db.Integer, db.ForeignKey('title.title_id'))

    def __str__(self):
        return f"<Returned {self.id} {self.book_id}>"

db.create_all()