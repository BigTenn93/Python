from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def checkerboard():
    print("checkerboard")
    return render_template('checkerboard.html')

@app.route('/eightBYfour')          # The "@" decorator associates this route with the function immediately following
def checkerboard8_4():
    print("checkerboard8_4")
    return render_template('checkerboard8_4.html')

@app.route('/Skol')          # The "@" decorator associates this route with the function immediately following
def checkerboardSkol():
    print("checkerboardSkol")
    return render_template('checkerboardSkol.html')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

