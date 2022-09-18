from flask import Flask, render_template, request, redirect, session
from user_model import User # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Users, CRUD, Modularized!'  # Return the string 'Hello World!' as a response

@app.route('/users')
def users():
    User.get_all()
    return render_template("read_all.html")

@app.route('/create', methods=['POST'])
def create():
    print(request.form)
    first_name = request.form['']
    last_name = request.form['']
    email = request.form['']
    return redirect('/new_list')

@app.route('/new_list')
def new_list():
    return render_template("read_all.html")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

