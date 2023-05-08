from flask import Flask
from flask_migrate import Migrate

from .users.routes import users
from .users.models import User
from .appointments.models import Appointment
from .appointments.routes import appointments
from .auth.routes import auth
from .dashboard.routes import dashboard
from .db import db
from .conf import login_manager

migrate = Migrate()

DB_USER = "postgres"
DB_PASS = "root"
DB_NAME = "appointments"
DB_HOST = "localhost"

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    with app.app_context():

        app.register_blueprint(users)
        app.register_blueprint(auth)
        app.register_blueprint(dashboard)
        app.register_blueprint(appointments)

        return app