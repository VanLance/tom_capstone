from flask import Flask, request, jsonify
from flask_sqlaclehmy import SQLAlchemy
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    app.config['Secret Key'] = 'your-secret-key-here'



    return app
