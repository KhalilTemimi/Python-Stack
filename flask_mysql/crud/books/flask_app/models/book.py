from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    def __init__(self, data):
        self.id=data['id']
        self.title=data['title']
        self.number_of_pages=data['number_of_pages']
        self.created_at=['created_at']
        self.updated_at=['updated_at']
        self.authors_who_favorited = []

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO books ( title , number_of_pages) VALUES ( %(title)s , %(number_of_pages)s);"
        return connectToMySQL('books_schema').query_db( query, data )
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def get_by_id(cls,data):
        query = """SELECT * FROM books LEFT JOIN favories ON books.id = favories.book_id 
                    LEFT JOIN users ON users.id = favories.user_id WHERE books.id = %(id)s;"""
        results = connectToMySQL('books_schema').query_db(query,data)
        
        book = cls(results[0])
        for row in results:
            if row['users.id'] == None:
                break
            data = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "updated_at": row['users.updated_at'],
                "created_at": row['users.created_at'],
            }
            book.authors_who_favorited.append(author.Author(data))
            print(book)
        return book

    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favories WHERE user_id = %(id)s );"
        results = connectToMySQL('books_schema').query_db(query,data)
        books = []
        for row in results:
            books.append(cls(row))
        print(books)
        return books
