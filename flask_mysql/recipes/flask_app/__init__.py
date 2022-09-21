from flask import Flask
app = Flask(__name__)
app.secret_key = "hush"

DATABASE = "recipes_db"