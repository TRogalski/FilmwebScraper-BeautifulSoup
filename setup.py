try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Simple Python web scrapper',
    'author': 'TRogalski',
    'url': 'TODO',
    'download_url': 'TODO',
    'author_email': 'TODO',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['WebScrapper'],
    'scripts': [],
    'name': 'WebScrapper'
}

setup(**config)
