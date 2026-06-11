from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db


class User(db.Model, UserMixin):
    """User model for storing registration details and authentication keys."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(120), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    profile_picture = db.Column(db.String(256), nullable=True)
    
    # Metadata timestamps and state flags
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    # Relationships
    # backref='owner' dynamically attaches an '.owner' attribute to the Task model
    # cascade='all, delete-orphan' ensures tasks are deleted if their user is deleted
    tasks = db.relationship('Task', backref='owner', lazy='dynamic', cascade='all, delete-orphan')

    def set_password(self, password):
        """Generates and sets a secure password hash."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks raw input password against stored secure hash."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Task(db.Model):
    """Task model for representing action items assigned to users."""
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default='Pending', nullable=False)
    priority = db.Column(db.String(20), default='Medium', nullable=False)
    due_date = db.Column(db.Date, nullable=True)
    category = db.Column(db.String(50), nullable=True)
    
    # Metadata timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Foreign key constraint linking to Users
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    # Database level check constraints to validate exact values for status and priority
    __table_args__ = (
        db.CheckConstraint(status.in_(['Pending', 'In Progress', 'Completed']), name='check_task_status'),
        db.CheckConstraint(priority.in_(['Low', 'Medium', 'High']), name='check_task_priority'),
    )

    def __repr__(self):
        return f'<Task {self.title}>'
