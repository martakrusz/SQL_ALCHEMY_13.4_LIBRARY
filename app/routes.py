from flask import request, render_template, redirect, url_for
from app import app, db
from app import services
from forms import BookForm


@app.route("/", methods=["GET", "POST"])
def show_library():
    error=""
    book_form = BookForm()

    if request.method == "POST":
        if book_form.validate_on_submit(): 
            services.add_book(book_form)
            return redirect(url_for('show_library'))
            
    books_list = services.load()
    return render_template("homepage.html", form = book_form, books = books_list, error=error)


@app.route("/borrow", methods=["GET", "POST"])
def borrow_book():
    if request.method == "POST":
        book_title = request.args.get('book_title')
        services.borrow_book(book_title)
    return redirect(url_for('show_library'))

@app.route("/return", methods=["GET", "POST"])
def return_book():
    if request.method == "POST":
        book_title = request.args.get('book_title')
        services.return_book(book_title)
    return redirect(url_for('show_library'))


@app.route("/delete", methods=["GET", "POST"])
def delete_book():
    if request.method == "POST":
        book_title = request.args.get('book_title')
        services.delete_book(book_title)
    return redirect(url_for('show_library'))

@app.route("/<int:title_id>", methods=["GET", "POST"])
def one_book():
    book_title = request.args.get('book_title')
    if request.method == "POST":
        book_title = request.args.get('book_title')
        services.load(book_title)
    return render_template('book_details.html')