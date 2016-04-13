#!/usr/bin/env python3

import os
from setuptools import setup

readme_path = os.path.join(os.path.dirname(__file__), 'README.md')

try:
    import pypandoc
except ImportError:
    with open(readme_path) as fd:
        long_description = fd.read()
else:
    long_description = pypandoc.convert(readme_path, 'rst')

setup(
        name='powertop',
        version='0.2.2',
        description='Small wrapper to use PowerTOP in Python',
        long_description=long_description,
        author='Valentin Lorentz',
        author_email='valentin.lorentz+git@ens-lyon.org',
        url='https://github.com/ProgVal/python-powertop',
        packages=['powertop'],
        classifiers=[
            'Development Status :: 1 - Planning',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3',
            'Topic :: System :: Monitoring',
            ],
        )
