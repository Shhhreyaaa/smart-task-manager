import os
from pathlib import Path

# Resolve the project root folder directory
BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    """Application configuration definitions."""
    # Loaded from environment variables with fallback defaults
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-development-secret-key-12345')
    
    # Database configuration defaults to SQLite in instance/ folder
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        f"sqlite:///{BASE_DIR / 'instance' / 'tasks.db'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
