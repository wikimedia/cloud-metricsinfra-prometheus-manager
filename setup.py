from os import path

from setuptools import find_packages, setup

current_directory = path.dirname(path.abspath(__file__))

setup(
    name='prometheus-manager',
    version='0.0.1',
    packages=find_packages('prometheus_manager'),
    install_requires=[
        line.strip() for line in open(path.join(current_directory, 'requirements.txt'), 'r')
    ],
    scripts=[
        'scripts/pm-interactive',
        'scripts/pm-migrate',
    ],
)
