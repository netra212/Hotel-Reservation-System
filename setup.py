# This File is used for the project management. 
from setuptools import setup,find_packages
with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name = "hotel reservation system",
    version = "1.0.0",
    description = "This project will classify either the booking will be cancel or not.", 
    author = "Netra Khatri",
    packages = find_packages(include=["src", "src.*"]),
    install_requires = requirements
)
