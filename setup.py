try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '',
    'author': 'Alex Gerdom',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': '',
    'version': '0.1',
    'install_requires': [],
    'packages': ['tkinterwidgets'],
    'scripts': [],
    'name': 'tkinterwidgets'
}

setup(**config)

