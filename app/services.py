from app import models, db

def add_book(book_form):
    new_title = book_form.data["title"]
    title = models.Title(title = new_title)
    db.session.add(title)

    new_author_input = book_form.data["author"]
    new_author_list = new_author_input.split(sep=",")
    
    for i in new_author_list:
        author = models.Author.query.filter_by(author=i).first()
        if author is None:
            author = models.Author(author = i)
            db.session.add(author)
            db.session.commit()
        title.authors.append(author)
        db.session.commit()


def borrow_book(book_title):
    book = models.Title.query.filter_by(title=book_title).first()
    borrowed = models.Borrowed(book = book)
    db.session.add(borrowed)
    db.session.commit()

def delete_book(book_title):
    book = models.Title.query.filter_by(title=book_title).first()
    borrowed = models.Borrowed.query.filter_by(book_id=book.title_id).first()
    
    if borrowed is not None:
        db.session.delete(borrowed)
    db.session.delete(book)
    db.session.commit()

def load():
    books_list = []
    
    for title in models.Title.query.all():
        temp_book = {}
        temp_book["title"] = title.title
        all_authors = []
        for author in title.authors:
            all_authors.append(author.author)
        authors = ", ".join(all_authors)
        temp_book['authors'] = authors

        borrowed = models.Borrowed.query.filter_by(book_id=title.title_id).first()
        if borrowed is not None:
            temp_book['borrowed_date'] = borrowed.borrowed_date
        else:
            temp_book['borrowed_date'] = ""
        books_list.append(temp_book)
 
    return books_list