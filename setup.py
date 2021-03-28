from setuptools import find_packages, setup
from cicd_lab2 import __version__

setup(
    name="cicd_lab2",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="Databricks Labs CICD Templates Sample Project",
    author="Yang",
)
