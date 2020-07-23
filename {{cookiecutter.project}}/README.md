{{cookiecutter.project_name}}
{{ '=' * cookiecutter.project_name|length }}

{{cookiecutter.description}}

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20FPD-ff69b4.svg
     :target: https://github.com/jidn/cookiecutter-flask-postgresql-docker/
     :alt: Built with Cookiecutter FPD(Flask, PostgreSQL, Docker)
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style
{% if cookiecutter.open_source_license != "Not open source" %}

:License: {{cookiecutter.open_source_license}}
{% endif %}

## Python and flask setup

    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements/development.txt

Check if flask "Hello, World" is working.

    $ ./manage.py flask run
     * Environment: development
     * Debug mode: on
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!

When adding additional packages, don't forget to update the docker web image.

    $ manage.py docker compose build web

## Database

Initial

    $ manage.py flask db init

After making changes to the database models, create the migration and apply the migration.

    $ manage.py flask db migrate -m "Some message"
    $ manage.py flask db upgrade

## Docker images

There are three containers: web, db, and nginx

Initial creation commands

    ./manage.py compose web
    ./manage.py create-initial-db

Start and stop commands are:

    ./manage.py compose up -d
    ./manage.py compose down

Verify running

    docker ps

## Testing

    $ manage.py test

## Scenarios

Fill the database with customized data in separate environment from development and testing environments.

Example: Scenario `foo`

Copy and modify, if needed, the files `config\scenario.json` and `docker\scenario.yml` renaming to `scenario_foo.???`

File `scenarios/foo.py`

    import os
    from application.app import create_app
    from application.models import db, User

    app = create_app("developement")

    def run():
        print("Scenario {os.environ['APPLICATION_SCENARIO_NAME']}")
        with app.app_context():
            db.drop_all()
            db.create_all()

            # Load and commit any additional database items

Run the scenario

    $ ./manage.py scenario up foo


## Production

See configuration files that add gunicorn and nginx

    $ APPLICATION_CONFIG="production" ./manage.py compose build web
    $ APPLICATION_CONFIG="production" ./manage.py compose up -d

To view the logs of nginx

    $ APPLICATION_CONFIG="production" ./manage.py compose logs -f nginx

To connection to the nginx shell

    $ APPLICATION_CONFIG="production" ./manage.py compose exec nginx bash

## TODO

+ Turn into cookiecutter
+ git commit hooks https://github.com/sourcery-ai/python-best-practices-cookiecutter
+ sqlite3 or postgresql

## Source

Taken from [Flask project setup: TDD, Docker, Postgres and more](https://www.thedigitalcatonline.com/blog/2020/07/05/flask-project-setup-tdd-docker-postgres-and-more-part-1/) by Leonardo Giordani

Leonardo Giordani [Github](https://github.com/lgiordani/rentomatic)
