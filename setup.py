
from setuptools import setup, find_packages


DISTNAME = "myproj"
DESCRIPTION = (
    "Description of my amazing python project."
)
MAINTAINER = "Genevieve Buckley"
PYTHON_VERSION = (3, 10)

if __name__ == "__main__":
    setup(
        name=DISTNAME,
        description=DESCRIPTION,
        author=MAINTAINER,
        packages=find_packages(),
    )
