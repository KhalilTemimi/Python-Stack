from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    def __init__(self, data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.created_at=['created_at']
        self.updated_at=['updated_at']
        self.favorite_books =[]

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name) VALUES ( %(first_name)s , %(last_name)s);"
        return connectToMySQL('books_schema').query_db( query, data )
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('books_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def unfavorited_authors(cls,data):
        query = "SELECT * FROM users WHERE users.id NOT IN ( SELECT user_id FROM favories WHERE book_id = %(id)s );"
        authors = []
        results = connectToMySQL('books_schema').query_db(query,data)
        for row in results:
            authors.append(cls(row))
        return authors
    
    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favories (user_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL('books_schema').query_db(query,data);
    
    @classmethod
    def get_by_id(cls,data):
        query = """SELECT * FROM users LEFT JOIN favories ON users.id = favories.user_id 
                    LEFT JOIN books ON books.id = favories.book_id WHERE users.id = %(id)s;"""
        results = connectToMySQL('books_schema').query_db(query,data)
        author = cls(results[0])
        for row in results:
            if row['books.id'] == None:
                break
            data = {
                "id": row['books.id'],
                "title": row['title'],
                "number_of_pages": row['number_of_pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            author.favorite_books.append(book.Book(data))
        return author
