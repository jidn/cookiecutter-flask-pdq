import logging

LOGGER = logging.getLogger()

if __name__ == "__main__":
    print("Running post hook")
    LOGGER.warning("Unable to create latest, best .gitignore")
    # TODO https://github.com/github/gitignore/blob/master/Python.gitignore
