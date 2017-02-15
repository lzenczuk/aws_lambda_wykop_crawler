# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='aws_wykop_crawler',
    version='0.1.0',
    description='Wykop crawler app',
    long_description=readme,
    author='Lucjan Zenczuk',
    author_email='lucjan.zenczuk@gmail.com',
    url='https://github.com/lzenczuk/aws_wykop_crawler',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

