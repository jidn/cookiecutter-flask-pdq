from flask import Flask
from .extensions import register_extensions


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(
        f"{{cookiecutter.application_directory}}.config.Config{config_name.capitalize()}"
    )
    register_extensions(app)

    @app.route("/")
    def hello_world():
        return "Hello, World!"

    return app
