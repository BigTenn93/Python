import datetime
from flask import flash
from flask_app import app, DATABASE
from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for row in results:
            recipes.append(row)
        return recipes

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM recipes WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_name(cls,data):
        query = "SELECT * FROM recipes WHERE name=%(name)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls,data):
        query = "INSERT INTO recipes (name, description, instructions, under_30, date_made) VALUES (%(name)s, %(description)s, %(instruction)s, %(under_30)s, %(date_made)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "update RECIPES set (%(name)s, %(description)s, %(instruction)s, %(under_30)s, %(date_made)s WHERE %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        today = datetime.today().strftime("%Y-%m-%d")
        recipe_in_db = Recipe.get_by_name(recipe)
        if recipe_in_db:
            flash("Recipe name already used")
            is_valid = False
        if len(recipe["name"]) < 3:
            flash("Name must be at least 3 characters")
            is_valid = False
        if len(recipe["description"]) < 3:
            flash("Description must be at least 3 characters")
            is_valid = False
        if len(recipe["instructions"]) < 3:
            flash("Instructions must be at least 3 characters")
            is_valid = False
        if not recipe["date_made"]:
            flash("Please enter a date")
            is_valid = False
        if recipe["date_made"] > today:
            flash("Please choose current/past date")
            is_valid = False