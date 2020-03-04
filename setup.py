#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='boom',
    version="master",
    description='Boom you have been pre-committed',
    long_description=readme,
    license='MIT',
    author='HBS Online',
    author_email='hbxdev@myhbx.org',
    url='https://github.com/kofi/boom',
    download_url='https://github.com/kofi/boom',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'lint_diffs'
    ],
    classifiers=[
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    scripts=['scripts/boom'],
    keywords=['pre-commit', 'hooks', 'python'],
)
