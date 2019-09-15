try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Simple Python web scrapper for filmweb TV series data',
    'author': 'TRogalski',
    'author_email': 'tomracc@yahoo.com',
    'version': '0.1',
    'install_requires': ['nose', 'bs4', 'requests'], # external dependencies (packages)
    'packages': ['webScrapper'],
    'scripts': [],
    'name': 'webScrapper'
}

setup(**config)
