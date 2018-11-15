from setuptools import setup, find_packages

setup(
        name="gsionpackage",
        version="0.1.0",
        packages=find_packages(exclude=['*test']),
        author="Gareth Sion Jones",
        author_email="garethsion@googlemail.com",
        install_requires=['numpy','scipy']
    )

