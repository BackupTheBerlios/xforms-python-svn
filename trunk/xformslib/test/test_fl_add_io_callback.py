#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" unit-test for functions in flbasic.py module

    For every function I have created use-cases tests:
    - one supposed to be working correctly;
    - some supposed to fail, but be promptly intercepted by
    xforms-python's error handling routines; or without
    being intercepted, so error handling is left to upstream
    XForms C functions.
"""

import sys
import os
sys.path.append('..')
import unittest

from xformslib import flbasic, flxbasic, xfdata


class Test_fl_add_io_callback(unittest.TestCase):
    def setUp(self):
        """invoked before each test."""
        self.fdesc = None

    def tearDown(self):
        """invoked after each test."""
        pass

    def iocb(num, vdata):
        print "file opened %s", vdata

    def test_00_fl_add_io_callback_ok(self):
        # test_00 should NOT fail
        self.fdesc = os.open('./stubfile.txt', os.O_RDONLY)
        flbasic.fl_add_io_callback(self.fdesc, xfdata.FL_READ, self.iocb, 
                                   "Good morning")
        os.close(self.fdesc)

    def test_01_fl_add_io_callback_fail(self):
        # test_01 should fail
        self.fdesc = os.open('./stubfile.txt', os.O_RDONLY)
        # should fail on the 2nd param.
        flbasic.fl_add_io_callback(self.fdesc, 12500, self.iocb, None)
        os.close(self.fdesc)

    def test_02_fl_add_io_callback_fail(self):
        # test_02 should fail
        self.fdesc = os.open('./stubfile.txt', os.O_RDONLY)
        # should fail on the 3rd param.
        flbasic.fl_add_io_callback(self.fdesc, xfdata.FL_READ, None, 12)
        os.close(self.fdesc)

    def test_03_fl_add_io_callback_fail(self):
        # test_03 should fail
        self.fdesc = "some strange value"
        # should fail on the 1st param.
        flbasic.fl_add_io_callback(self.fdesc, xfdata.FL_READ, self.iocb, None)


if __name__ == '__main__':
    print "%s : test_00 should NOT fail " \
        "- test_01, test_02, test_03 should fail.\n" % __file__
    flxbasic.fl_initialize(len(sys.argv), sys.argv, "test", 0, 0)
    unittest.main()
    flxbasic.fl_finish()
