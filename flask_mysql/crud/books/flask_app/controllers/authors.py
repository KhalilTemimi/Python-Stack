from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def home():
    authors=Author.get_all()
    return render_template('author.html',authors =authors)

@app.route('/create/author', methods=['post'])
def new_author():
    Author.save(request.form)
    return redirect('/')

@app.route('/show/author/<int:id>')
def show_author(id):
    data = {
        "id": id
    }
    return render_template('show_author.html',author=Author.get_by_id(data),unfavorited_books=Book.unfavorited_books(data))

@app.route('/join/book',methods=['post'])
def join_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/show/author/{request.form['author_id']}")