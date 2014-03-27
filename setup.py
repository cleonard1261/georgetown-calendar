#!/usr/bin/env python
# setup
# Setup script for gtcal
#
# Author:   Benjamin Bengfort <bb830@georgetown.edu>
# Created:  Thu Mar 27 16:46:11 2014 -0400
#
# Copyright (C) 2014 Georgetown University
# For license information, see LICENSE.txt
#
# ID: setup.py [] bb830@georgetown.edu $

"""
Setup script for gtcal
"""

##########################################################################
## Imports
##########################################################################

try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    raise ImportError("Could not import \"setuptools\"."
                      "Please install the setuptools package.")

##########################################################################
## Package Information
##########################################################################

packages = find_packages(where=".", exclude=("tests", "bin", "docs", "fixtures",))
requires = []

with open('requirements.txt', 'r') as reqfile:
    for line in reqfile:
        requires.append(line.strip())

classifiers = (
    # TODO: Add classifiers
    # See: https://pypi.python.org/pypi?%3Aaction=list_classifiers
)

config = {
    "name": "GtCal",
    "version": "0.1",
    "description": "A simple command line calendar",
    "author": "Benjamin Bengfort",
    "author_email": "bb830@georgetown.edu",
    "url": "https://github.com/bbengfort/gtcal",
    "packages": packages,
    "install_requires": requires,
    "classifiers": classifiers,
    "zip_safe": False,
    "scripts": ["scripts/gtcal",],
}

##########################################################################
## Run setup script
##########################################################################

if __name__ == '__main__':
    setup(**config)
