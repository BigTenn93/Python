from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import bcrypt, DATABASE
from flask import flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).querry_db(query,data)

    @classmethod
    def get_one_email(cls,data:dict) -> object:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def get_one(cls,data:dict) -> object:
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0])
        return False

    @staticmethod
    def is_valid(form_data):
        is_valid = True
        if len(form_data['first_name']) < 2:
            flash("First Name must be at least 2 characters", 'err_user_first_name')
            is_valid = False

        if len(form_data['last_name']) < 2:
            flash("Last Name must be at least 2 characters", 'err_user_last_name')
            is_valid = False

        if len(form_data['email']) < 5:
            flash("Email is required", 'err_user_email')
            is_valid = False
        elif not EMAIL_REGEX.match(form_data['email']):
            flash("Invalid email address", 'err_user_email')
            is_valid = False
        else:
            potential_user = User.get_one_email({'email': form_data['email']})
            if potential_user:
                flash("Email is already being used", 'err_user_email')

        if len(form_data['password']) < 8:
            flash("Password must be at least 8 characters", 'err_user_password')
            is_valid = False

        if len(form_data['password_confirm']) < 8:
            flash("Passwords do not match", 'err_user_password_confirm')
            is_valid = False
        elif form_data['password_confirm'] != form_data['password']:
            flash("Passwords do not match", 'err_user_password_confirm')
            is_valid = False
        return is_valid

    @staticmethod
    def is_valid_login(form_data):
        is_valid = True

        if len (form_data['email']) < 5:
            flash("Email is required", 'err_user_email_login')

        elif not EMAIL_REGEX.match(form_data['email']):
            flash("Invalid email address", 'err_user_email_login')
            is_valid = False

        if len(form_data['password']) < 8:
            flash("Password must be at least 8 characters", 'err_user_password_login')
            is_valid = False

        else:
            potential_user = User.get_one_email({'email': form_data['email']})
            if not potential_user:
                is_valid = False
                flash("No User Found", 'err_user_password_login')
            elif not bcrypt.check_password_hash(potential_user.password, form_data['password']):
                is_valid = False
                flash('Incorrect Password', 'err_user_password_login')
            else:
                session['uuid'] = potential_user.id

            return is_valid