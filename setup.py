from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='python_module_quickstart',
    version='0.0.1',
    description='A skeleton module for easy, clean python code',
    long_description=readme,
    author='Dan Busbridge',
    author_email='dan.busbridge@gmail.com',
    url='https://github.com/dbusbridge/python_module_quickstart',
    packages=find_packages(exclude=('tests', 'docs'))
)
