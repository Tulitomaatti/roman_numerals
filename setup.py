try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description': 'Roman numeral to/from converter scripts',
    'author' : 'E Lampsijärvi',
    'url' : 'none',
    'download_url' : 'none',
    'author_email' : 'eetu.lampsijarvi@helsinki.fi',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages': ['roman_numerals'],
    'scripts': [],
    'name': 'roman_numerals'
]

setup(**config)
