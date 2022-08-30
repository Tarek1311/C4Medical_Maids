#!/usr/bin/venv python
from distutils.core import setup
from setuptools import find_packages
from app import app

setup(
    # Name of the package
    name=app,
    version='1.0.0',
    license='',
    description='Notre projet est une application de vente et location de matériels médical et paramédical',
    author='Tarek Khaldi',
    author_email='tarekkhaldi1311@gmail.com',
    url='https://github.com/Tarek1311/C4Medical_Maids.git/',
    packages=find_packages(include=['app', 'app.*']),
    keywords=[],
    python_requires='>=3.7, <4',
    install_requires=["pytest",
                      "dash==2.6.1",
                      "dash-bootstrap-components==1.2.1",
                      "requests==2.28.1",
                      "gunicorn==20.1.0",
                      "dash-auth==1.3.2"
                      ],
)