from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'main.login'  # Указываем путь к маршруту login в Blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login.init_app(app)

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    with app.app_context():
        db.create_all()

    return app
