from flask_app import app
from flask_app.controllers import user_controller, controller_routes

if __name__=="_main_":
    app.run(debug=True)