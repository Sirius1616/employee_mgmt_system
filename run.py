from app import create_app, db
from flask_migrate import Migrate
from app.models import User, Employee

# Create the Flask app instance
app = create_app()

# Set up Flask-Migrate for database migrations
migrate = Migrate(app, db)

# Shell context for Flask CLI
@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Employee': Employee
    }

if __name__ == "__main__":
    app.run(debug=True)
k