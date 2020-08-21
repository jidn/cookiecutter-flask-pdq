import os

from {{cookiecutter.application_directory}}.app import create_app

app = create_app(os.environ["FLASK_CONFIG"])

# Now you can run the development server with
# $ FLASK_CONFIG="development" flask run
