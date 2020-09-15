from app import db
from datetime import datetime


subs = db.Table('subs',
    db.Column('book_id', db.Integer, db.ForeignKey('title.book_id')),
    db.Column('author_id', db.Integer, db.ForeignKey('author.author_id'))
)


class Title(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, unique=True)
    borrowed = db.relationship('Borrowed', backref='book')

    def __str__(self):
        return f"<Title {self.title}>"

class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(200), index=True)
    many_authors = db.relationship('Title', secondary=subs, backref=db.backref('many_authors', lazy = 'dynamic'))

    def __str__(self):
        return f"<Author {self.author}>"

class Borrowed(db.Model):
    borrowed_id = db.Column(db.Integer, primary_key=True)
    borrowed_date = db.Column(db.Date, index=True, default=datetime.today())
    book_borrowed_id = db.relationship(db.Integer, db.ForeignKey('title.book_id'))

    def __str__(self):
        return f"<Borrowed {self.borrowed_id} {self.book_borrowed_id}>"

db.create_all()
