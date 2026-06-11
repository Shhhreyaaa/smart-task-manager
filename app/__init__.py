import os
from flask import Flask
from dotenv import load_dotenv

from app.config import Config
from app.extensions import db, login_manager, csrf

# Load environment configurations from local .env
load_dotenv()


def create_app(config_class=Config):
    """Flask application factory."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Ensure the database instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # Bind extensions
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
