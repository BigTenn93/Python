from flask import Flask, render_template, session, request, redirect
from dogs_model import Dog
app = Flask(__name__)

@app.route('/')
def index():
    all_dogs = Dog.get_all()