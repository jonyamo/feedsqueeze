#!/usr/bin/env python

import os
import sys

from feedsqueeze import __title__, __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()
with open('HISTORY.rst') as f:
    history = f.read()

(vmajor, vminor) = sys.version_info[:2]

def get_requirements(file):
    if not os.path.exists(file):
        return []

    requirements = []
    with open(file) as f:
        for line in f.readlines():
            line = line.strip()
            if not line or line.startswith(('#', '-r')):
                continue
            requirements.append(line)

    return requirements

setup(
    name=__title__.lower(),
    version=__version__,
    description='Squeeze multiple feeds into one',
    long_description=readme + '\n\n' + history,
    author='Jon Yamokoski',
    author_email='code@jonyamo.us',
    url='https://github.com/jonyamo/feedsqueeze',
    license='BSD',
    packages=['feedsqueeze'],
    package_dir={'feedsqueeze': 'feedsqueeze'},
    include_package_data=True,
    zip_safe=False,
    install_requires=get_requirements('requirements/base.txt')
                    +get_requirements('requirements/base-py{0}{1}.txt'.format(vmajor,vminor)),
    test_suite='tests',
    tests_require=get_requirements('requirements/test.txt')
                 +get_requirements('requirements/test-py{0}{1}.txt'.format(vmajor,vminor)),
    entry_points={
        'console_scripts': [
            'feedsqueeze=feedsqueeze.cli:main'
        ]
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ]
)

