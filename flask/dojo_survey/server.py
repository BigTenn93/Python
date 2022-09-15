from xml.etree.ElementTree import Comment
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'abc123'

@app.route("/")
def survey():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def submit():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/info")

@app.route("/info")
def info():
    name = session['name']
    location = session['location']
    language = session['language']
    comment = session['comment']
    return render_template('/info.html', name = name, location = location, language = language, comment = comment)

@app.route("/clear_session")
def clear_sesion():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)