from setuptools import setup

setup(
    name='prometheus-manager',
    version='0.0.1',
    packages=['prometheus_manager'],
    install_requires=[
        # debian buster has flask 1.0.2
        'flask==1.0.2',
    ],
)
