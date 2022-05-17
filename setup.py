from setuptools import setup

with open("requirements.txt", "r") as requirements_file:
    requirements = requirements_file.read().split()

with open("requirements-dev.txt", "r") as requirements_dev_file:
    requirements_dev = requirements_dev_file.read().split()

setup(
    name='unittest-for-ml',
    version='0.1.0',
    packages=["unittest-for-ml"],
    package_dir={"unittest-for-ml": "dataframe"},
    url='',
    license='',
    author='Engie',
    author_email='',
    description='DOJO : unittests for ML',
    install_requires=[requirements, requirements_dev]
)
