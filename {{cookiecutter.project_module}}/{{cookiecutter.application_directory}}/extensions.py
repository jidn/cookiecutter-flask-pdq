"""Extensions module. Each extension instance is here."""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def register_extensions(app):
    """Register flask extensions with app."""
    db.init_app(app)
    migrate.init_app(app, db)
