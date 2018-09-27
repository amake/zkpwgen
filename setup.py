from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='zkpwgen',
    version='1.0',
    description='Generate random passwords of full-width Japanese characters',
    long_description=long_description,
    url='https://github.com/amake/zkpwgen',
    author='Aaron Madlon-Kay',
    author_email='aaron@madlon-kay.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Security',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='password generator full-width japanese',
    py_modules=['zkpwgen'],
    entry_points={
        'console_scripts': [
            'zkpwgen=zkpwgen:main',
        ],
    },
)
