from crypt import methods
from time import clock_settime
from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.dojo_model import Dojo

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    all_dojos = Dojo.get_all()
    return render_template('index.html', all_dojos = all_dojos)

@app.route('/dojos/<int:id>')
def one_dojo(id):
    one_dojo = Dojo.get_one_with_ninjas({'id':id})
    return render_template('one_dojo.html', one_dojo = one_dojo)

@app.route('/dojos/new')
def new_dojo_form():
    return render_template("dojos_new.html")

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/')

@app.route('/dojos/<int:id>/edit')
def edit_dojo_form(id):
    data = {
        'id':id
    }
    this_dojo = Dojo.get_one(data)
    return render_template("dojos_edit.html", this_dojo = this_dojo)

@app.route('/dojos/<int:id>/update', methods=['POST'])
def update_dojo(id):
    data = {
        **request.form, #quick way to copy the contents of request.form into this dictionary
        'id':id
    }
    Dojo.update(data)
    return redirect('/')

@app.route('/dojos/<int:id>/delete')
def delete_dojo(id):
    data = {
        'id':id
    }
    Dojo.delete(data)
    return redirect('/')