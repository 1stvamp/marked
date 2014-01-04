"""Installer for marked
"""

from setuptools import setup, find_packages

setup(
    name='marked',
    description='',
    long_description=open('README.rst').read(),
    provides=['marked'],
    version='1.0.0',
    author='Wes Mason',
    author_email='wes@1stvamp.org',
    url='https://github.com/1stvamp/marked.py',
    install_requires=[
        'BeautifulSoup >= 3.0',
        'markgen >= 0.9'
    ],
    packages=find_packages(exclude=['marked_tests']),
    package_data={},
    include_package_data=True,
    license='BSD'
)
