from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route("/")
def welcome():
    return "Welcome to the Playground"

@app.route("/play")          # The "@" decorator associates this route with the function immediately following
def boxes():
    return render_template("index.html", Num=3)

@app.route("/play/int(x)")
def more_boxes(Num):
    return render_template("index.html", Num=Num)

@app.route("/play/<int:num>/<string:color>")
def box_color(Num,color):
    return render_template("index.html", Num=Num, color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

