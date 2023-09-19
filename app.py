from flask import Flask
from flask_restful import Api
from application.controller import *

# Configuration for the app
app = Flask(__name__)
api = Api(app)

# Add routes for API resources
api.add_resource(Senti, '/api/sentiment/')


if __name__ == "__main__":
    app.debug=True
    app.run()