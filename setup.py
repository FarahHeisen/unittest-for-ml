from setuptools import setup

with open("requirements.txt", "r") as requirements_file:
    requirements = requirements_file.read().split()

with open("requirements-dev.txt", "r") as requirements_dev_file:
    requirements_dev = requirements_dev_file.read().split()

setup(
    name='kata-dataframe',
    version='0.1.0',
    packages=["kata-dataframe"],
    package_dir={"kata-dataframe": "dataframe"},
    url='',
    license='',
    author='SkoolAI',
    author_email='',
    description='DOJO : mise en place d\'une CI, d\' un setup, ...',
    install_requires=[requirements, requirements_dev]
)
