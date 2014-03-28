# tests.utils_tests
# Testing for the utilities of the gtcal
#
# Author:   Benjamin Bengfort <bb830@georgetown.edu>
# Created:  Thu Mar 27 21:57:51 2014 -0400
#
# Copyright (C) 2014 Georgetown University
# For license information, see LICENSE.txt
#
# ID: utils_tests.py [] bb830@georgetown.edu $

"""
Testing for the utilities of the gtcal
"""

##########################################################################
## Imports
##########################################################################

import os
import tempfile
import unittest

from gtcal.utils import *

##########################################################################
## Test Cases
##########################################################################

class UtilsTests(unittest.TestCase):

    def setUp(self):
        self.tempdir  = tempfile.mkdtemp()
        self.testpath = os.path.join(self.tempdir, "red/fox/gt/cal/calendar.csv")

    def tearDown(self):
        if os.path.exists(self.testpath):
            os.path.remove(self.testpath)

    @unittest.skip
    def test_makepath(self):
        """
        Check that makepath makes directories
        """
        path = makepath(self.testpath)
        self.assertTrue(os.path.exists(os.path.dirname(path)))
