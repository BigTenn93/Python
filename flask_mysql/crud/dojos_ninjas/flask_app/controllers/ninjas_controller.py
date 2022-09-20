from crypt import methods
from time import clock_settime
from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/ninjas/new')
def new_ninja_form():
    all_dojos = Dojo.get_all()
    return render_template('ninja_new.html', all_dojos = all_dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    Ninja.create(request.form)
    return redirect('/')