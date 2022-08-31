#!/usr/bin/venv python
from setuptools import find_packages, setup

setup(
    name='C4Medical_Maids',
    version='1.0.0',
    description='Notre projet est une application de vente et location de matériels médical et paramédical',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author='Tarek Khaldi',
    author_email='tarekkhaldi1311@gmail.com',
    url='https://github.com/Tarek1311/C4Medical_Maids.git/',
    packages=find_packages(include=['app', 'app.*']),
    include_package_data=True,
    python_requires='>=3.7, <4',
    install_requires=["pytest",
                      "dash==2.6.1",
                      "dash-bootstrap-components==1.2.1",
                      "requests==2.28.1",
                      "gunicorn==20.1.0",
                      "dash-auth==1.3.2"
                      ],
    entry_points={"console_scripts": ["C4Medical_Maids = app.__main__:C4Medical_Maids"]},
)
