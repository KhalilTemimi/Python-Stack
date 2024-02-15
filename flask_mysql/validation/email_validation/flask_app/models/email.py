from flask import flash
import re
from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL('emails_schema').query_db( query, data )
    
    @classmethod
    def get_all(cls):
        query="select * from emails;"
        results=connectToMySQL("emails_schema").query_db(query)
        emails=[]
        for row in results:
            emails.append(cls(row))
        return emails 
    
    @classmethod
    def show_last(cls):
        query = "SELECT * FROM emails ORDER BY created_at DESC LIMIT 1;"
        results = connectToMySQL('emails_schema').query_db( query)
        return (results[0])
    
    @classmethod
    def destroy(cls,data):
        query = "delete from emails where id = %(id)s"
        return connectToMySQL("emails_schema").query_db(query,data)

    
    @staticmethod
    def validate_entry(email):
        is_valid = True 
        query = "select * from emails where email = %(email)s;"
        results = connectToMySQL("emails_schema").query_db(query,email)
        if len(results)>=1:
            flash("Email adress exist already")
            is_valid = False
        if not EMAIL_REGEX.match(email['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid