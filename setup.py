#!/usr/bin/env python3

import os
from setuptools import setup

setup(
        name='powertop',
        version='0.2',
        description='Small wrapper to use PowerTOP in Python',
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
