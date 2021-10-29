from app import appFlask, create_app, db
from app.models import Usuario

appFlask = create_app()

@appFlask.shell_context_processor
def make_shell_context():
    return {'db': db, 'Usuario': Usuario}