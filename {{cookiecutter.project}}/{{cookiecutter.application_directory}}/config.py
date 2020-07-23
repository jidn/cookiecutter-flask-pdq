import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base configuration"""
{% if cookiecutter.use_postgresql == 'yes' %}
    user = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PASSWORD"]
    hostname = os.environ["POSTGRES_HOSTNAME"]
    database = os.environ["POSTGRES_DB"]
    port = os.environ["POSTGRES_PORT"]

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{user}:{password}@{hostname}:{port}/{database}"
    )
{% endif %}
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfigProduction(Config):
    """Production configuration"""


class ConfigDevelopment(Config):
    """Development configuration"""


class ConfigTesting(Config):
    """Testing configuration"""

    TESTING = True
