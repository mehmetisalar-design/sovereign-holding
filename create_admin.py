"""Secure interactive helper to create an administrator account."""
import getpass
from app import create_app, db
from app.models import User

app = create_app()
with app.app_context():
    email = input("Administrator email: ").strip().lower()
    name = input("Administrator full name: ").strip()
    password = getpass.getpass("Password (minimum 12 characters): ")
    confirm = getpass.getpass("Confirm password: ")
    if not email or "@" not in email or not name:
        raise SystemExit("Enter a valid email and name.")
    if len(password) < 12:
        raise SystemExit("Password must be at least 12 characters.")
    if password != confirm:
        raise SystemExit("Passwords do not match.")
    if User.query.filter_by(email=email).first():
        raise SystemExit("An account with this email already exists.")
    user = User(email=email, full_name=name, is_admin=True)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    print("Administrator created. Keep the password secure.")
