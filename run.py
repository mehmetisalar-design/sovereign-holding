import click
from app import create_app, db
from app.models import User
app = create_app()

@app.cli.command('create-admin')
def create_admin():
    """Interactively create the first administrator; no default password is created."""
    email=click.prompt('Administrator email').strip().lower()
    name=click.prompt('Administrator full name').strip()
    password=click.prompt('Password', hide_input=True, confirmation_prompt=True)
    if len(password) < 12: raise click.ClickException('Use a password of at least 12 characters.')
    if User.query.filter_by(email=email).first(): raise click.ClickException('An account with that email already exists.')
    user=User(email=email,full_name=name,is_admin=True); user.set_password(password); db.session.add(user); db.session.commit()
    click.echo('Administrator created. Store the password securely.')

if __name__ == '__main__':
    app.run(debug=False)
