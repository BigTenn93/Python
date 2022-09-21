from crypt import methods
from flask import Flask, render_template, redirect, request, session
from flask_app import app, bcrypt
from flask_app.models import user_model

@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect('/')
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')

@app.route('/user/create', methods=['POST'])
def create_user():
    is_valid = user_model.User.is_valid(request.form)

    if is_valid == False:
        return redirect('/')

        hash_pw = bcrypt.generate_password_hash(request.form['password'])
        data = {
            **request.form,
            'password': hash_pw
        }
        id = user_model.User.create(data)
        return redirect('/')

@app.route('/user/login', methods=['POST'])
def login():
    is_valid = user_model.User.is_valid_login(request.form)

    if not is_valid:
        return redirect('/')

    return redirect('/')