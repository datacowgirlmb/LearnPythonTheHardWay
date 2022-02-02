try:
	from setuptools import setuptools
except ImportError:
	from distutils.core import setuptools

config = {
	'description': 'An exmaplef from LPTHW Exercise 46',
	'author': 'Maggie Butler',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'datacowgirlmb@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex46']
	'scripts': [],
	'name': 'projectname'
}

setup(**config)