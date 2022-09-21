from setuptools import setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="C4Medical_Maids",
    version="1.0.0",
    description="Notre projet est une application de vente et location de matériels médical et paramédical",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Tarek Khaldi",
    author_email="tarekkhaldi1311@gmail.com",
    url="https://github.com/Tarek1311/C4Medical_Maids.git/",
    include_package_data=True,
    python_requires=">=3.7, <4",
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={"console_scripts": ["run = app.app:run"]},
)
