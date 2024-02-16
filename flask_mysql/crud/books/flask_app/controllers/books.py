from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/book')
def book():
    books=Book.get_all()
    return render_template('book.html',books = books)

@app.route('/create/book', methods=['post'])
def new_book():
    Book.save(request.form)
    return redirect('/book')

@app.route('/show/book/<int:id>')
def show_book(id):
    data = {
        "id":id
    }
    return render_template('show_book.html',book=Book.get_by_id(data),unfavorited_authors=Author.unfavorited_authors(data))

@app.route('/join/author',methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/show/book/{request.form['book_id']}")