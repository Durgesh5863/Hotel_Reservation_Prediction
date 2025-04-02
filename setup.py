from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "MLOPS-PROJECT-1",
    version="0.1",
    author="Durgesh Babu P",
    packages=find_packages(),
    install_requires=requirements,
)