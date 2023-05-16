from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")
    
    db.init_app(app)
    migrate.init_app(app, db)

    # Model Imports
    from app.models.inventory import Inventory

    # Register Blueprints
    from .routes import inventory_bp
    app.register_blueprint(inventory_bp)
    from .routes import hello_world_bp
    app.register_blueprint(hello_world_bp)

    CORS(app)
    return app

my_app = create_app