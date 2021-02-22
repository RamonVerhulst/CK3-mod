from setuptools import setup, find_packages
from os import path

setup(
    name='CK3mod',
    version='1.0',
    author='Ramon Verhulst',
    packages=find_packages(),
    scripts=[path.join('CK3mod', 'bin', 'copy_replace')],
)
