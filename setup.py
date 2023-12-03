#!/usr/bin/env python

from setuptools import setup

setup(name='supervisor-syslog',
    version='0.1.0',
    description='supervisor event handler for syslogging',
    py_modules=['supervisor_syslog'],
    setup_requires=['pytest-runner'],
    python_requires='>=3.*',
    install_requires=['PyYAML>=3.0'],
    tests_require=['pytest'],
    entry_points={'console_scripts': ['supervisor-syslog=supervisor_syslog:handler']}
    )

