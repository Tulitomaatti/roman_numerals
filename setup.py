# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    description='Roman numeral to/from converter scripts',
    author='Eetu Lampsijärvi',
    url='https://github.com/Tulitomaatti/romanum',
    download_url='none',
    author_email='eetu.lampsijarvi@helsinki.fi',
    version='0.1',
    install_requires=['nose'],
    packages=['romanum'],
    scripts=['bin/n2r', 'bin/r2n'],
    name='romanum'
)
