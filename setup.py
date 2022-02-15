import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="logsnag",
    version='0.0.1',
    description="LogSnag API Wrapper",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/logsnag/logsnag.py",
    author="Shayan Taslim",
    author_email="shayan@logsnag.com",
    license="MIT",
    python_requires='>=3.6',
    packages=["logsnag"],
    include_package_data=True,
    install_requires=["requests"],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
