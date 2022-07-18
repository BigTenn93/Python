from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "password123"

@app.route("/")
def start_html():
    session['counter'] = 1
    print("start")
    return render_template("start.html")

@app.route("/count1", methods=['POST'])
def click():
    verify(1)
    print("next1")
    return render_template("next1.html", num=session['counter'])

@app.route("/count2", methods=['POST'])
def double_click():
    verify(2)
    print("next2")
    return render_template("next2.html", num=session['counter'])

@app.route("/number", methods=['POST'])
def add_in_number():
    verify(int(request.form['number']))
    print("next3")
    return render_template("next3.html", num=session['counter'])

@app.route("/destroy_session", methods=['POST'])
def delete():
    print("redirect")
    return redirect('/')

def verify(i):
    if 'counter' in session:
        session['counter'] +=i
    else:
        session['counter'] = 1

if __name__ == "__main__":
    app.run(debug=True)