from flask_app.controllers import authors,books
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app import app


if __name__ == "__main__":
    app.run(debug=True)