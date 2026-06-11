from flask import Blueprint, render_template

# Define the main blueprint for landing and routing
main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Simple root welcome landing page to verify the project skeleton setup."""
    return render_template('index.html')
