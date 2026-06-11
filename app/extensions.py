from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

# Instantiate SQLAlchemy ORM
db = SQLAlchemy()

# Instantiate Flask-Login session manager
login_manager = LoginManager()

# Instantiate CSRF protection for forms validation safety
csrf = CSRFProtect()
