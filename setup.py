import os
import sys
from setuptools import setup, find_packages

milkman = __import__("milkman")

if sys.version_info >= (3,):
    extra_kwargs = {"use_2to3": True}
else:
    extra_kwargs = {}

setup(
    name="milkman",
    version=milkman.get_version(),
    description="Testing Django without all the fixtures",
    author="Wilkes Joiner, Chuck Collins, Patrick Altman",
    author_email="chuck.collins@gmail.com",
    license="BSD",
    url="http://github.com/ccollins/milkman/",
    keywords="django testing mock stub",
    packages=find_packages(exclude=["tests.*", "tests"]),
    include_package_data=True,
    install_requires=[
        "docutils>=0.3",
    ],
    zip_safe=False,
)
