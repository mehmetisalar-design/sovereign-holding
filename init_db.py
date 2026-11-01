"""Initialize the local database and sample catalog."""
from app import create_app, db

app = create_app()
with app.app_context():
    db.create_all()
    print("Database initialized. Sample catalog is created automatically on a fresh database.")
