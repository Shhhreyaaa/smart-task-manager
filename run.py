from app import create_app

# Instantiate the application using the factory pattern
app = create_app()

if __name__ == '__main__':
    # Start the local development server in debug mode
    app.run(debug=True)
