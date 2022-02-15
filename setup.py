import pathlib
from setuptools import setup
from logsnag import __version__

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="logsnag",
    version=__version__,
    description="LogSnag API Wrapper",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/logsnag/logsnag.py",
    author="Shayan Taslim",
    author_email="shayan@logsnag.com",
    license="MIT",
    packages=["logsnag"],
    include_package_data=True,
    install_requires=["requests"],
)
