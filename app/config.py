import os


class Config:
    """Application configuration definitions."""
    # Loaded from environment variables with fallback defaults
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-development-secret-key-12345')
    
    # Database configuration defaults to SQLite inside the app instance/ folder
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'sqlite:///tasks.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
