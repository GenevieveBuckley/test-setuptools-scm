
from setuptools import setup, find_packages

from myproj._version import __version__, __version_tuple__

DISTNAME = "myproj"
DESCRIPTION = (
    "Description of my amazing python project."
)
MAINTAINER = "Genevieve Buckley"
PYTHON_VERSION = (3, 10)

if __name__ == "__main__":
    setup(
        name=DISTNAME,
        version=__version__,
        description=DESCRIPTION,
        author=MAINTAINER,
        packages=find_packages(),
    )
