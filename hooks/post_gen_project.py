import logging
import pathlib
import urllib.request

LOGGER = logging.getLogger()

if __name__ == "__main__":
    print("Running post hook")
    filename, headers = urllib.request.urlretrieve(
        "https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore",
        pathlib.Path.cwd().joinpath(".gitignore"),
    )
