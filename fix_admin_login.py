"""Create or reset an Atelier Home administrator account.
Run from the project root with: .venv\\Scripts\\python.exe fix_admin_login.py
Password input is visible while typing to avoid confusion with hidden getpass input.
"""
from getpass import getpass
from app import create_app, db
from app.models import User

app = create_app()
with app.app_context():
    email = input('Admin email: ').strip().lower()
    name = input('Admin full name: ').strip()
    if not email or '@' not in email or not name:
        raise SystemExit('Please enter a valid email and name.')

    # Use visible input for password so the user can see that typing works.
    password = input('New password (minimum 12 characters; input will be visible): ')
    confirm = input('Type the same password again: ')
    if len(password) < 12:
        raise SystemExit('Password must be at least 12 characters. Nothing was changed.')
    if password != confirm:
        raise SystemExit('Passwords do not match. Nothing was changed.')

    user = User.query.filter_by(email=email).first()
    if user is None:
        user = User(email=email, full_name=name, is_admin=True)
        db.session.add(user)
        message = 'Administrator account created.'
    else:
        user.full_name = name
        user.is_admin = True
        message = 'Existing account updated as administrator and password reset.'

    user.set_password(password)
    db.session.commit()
    print('\nSUCCESS:', message)
    print('Now open http://127.0.0.1:5000/login and use the email/password you just entered.')
    print('For security, change this password later if anyone else could see your screen.')
