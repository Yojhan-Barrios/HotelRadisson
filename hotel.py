from app import appFlask, db
from app.models import Usuario

@appFlask.shell_context_processor
def make_shell_context():
    return {'db': db, 'Usuario': Usuario}