from setuptools import find_packages, setup
from databricks_framework import __version__

setup(
    name="databricks_framework",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="databricks project to implement a common framework",
    author="Enrique Mora Alonso",
)
