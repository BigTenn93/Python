from ast import Return
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
from env import KEY
app.secret_key = KEY

@app.route("/")
def survey():
    return render_template("survey.html")

@app.route("/process", methods=["POST"])
def submit():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/info")

@app.route("/info")
def info():
    return render_template('/info.html')

@app.route("/back")
def restart():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)