from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import views

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

db      = SQLAlchemy()
migrate = Migrate()
csrf    = CSRFProtect()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/lab5'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app