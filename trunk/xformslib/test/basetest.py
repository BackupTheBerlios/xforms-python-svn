#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" unit-test common class for functions in fl_*.py

    For every function I have created use-cases tests:
    - one supposed to be working correctly;
    - some supposed to fail, but be promptly intercepted by xforms-python's
    error handling routines; or without being intercepted, so error handling
    is left to upstream XForms C functions.
"""

import sys
import os
sys.path.append('..')
import unittest

import xformslib as xfl


class Testskel(object):
    def notenoughparams(self):
        pass

    def toomuchparams(self):
        pass

    def notnumeric(self):
        pass

    def notstring(self):
        pass

    def not(self):
        pass









class Test_fl_add_io_callback(unittest.TestCase):
    def setUp(self):
        """invoked before each test."""
        self.statusmsg = ""
        self.fdesc = None

    def tearDown(self):
        """invoked after each test."""
        print(self.statusmsg)

    def iocb(self, num, vdata):
        message = "file opened %s" % vdata
        print(message)

    def test_fl_add_io_callback_ok(self):
        # test should NOT fail
        self.statusmsg = "%s: should NOT fail." % \
                sys._getframe().f_code.co_name
        self.fdesc = os.open('./stubfile.txt', os.O_RDONLY)
        xfl.fl_add_io_callback(self.fdesc, xfl.FL_READ, self.iocb, \
                "Good morning")
        os.close(self.fdesc)

    def test_fl_add_io_callback_fail1(self):
        # failing on the 2nd param.
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        self.fdesc = os.open('./stubfile.txt', os.O_RDONLY)
        xfl.fl_add_io_callback(self.fdesc, 12500, self.iocb, None)
        os.close(self.fdesc)

    def test_fl_add_io_callback_fail2(self):
        # failing on the 3rd param.
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        self.fdesc = os.open('./stubfile.txt', os.O_RDONLY)
        xfl.fl_add_io_callback(self.fdesc, xfl.FL_READ, None, 12)
        os.close(self.fdesc)

    def test_fl_add_io_callback_fail3(self):
        # failing on the 1st param.
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        self.fdesc = "some strange value"
        xfl.fl_add_io_callback(self.fdesc, xfl.FL_READ, self.iocb, None)


class Test_fl_remove_io_callback(unittest.TestCase):
    def setUp(self):
        """invoked before each test."""
        self.statusmsg = ""
        self.fdesc = None

    def tearDown(self):
        """invoked after each test."""
        print(self.statusmsg)

    def iocb(self, num, vdata):
        message = "file opened %s" % vdata
        print(message)

    def precondition(self):
        self.fdesc = os.open('./stubfile.txt', os.O_RDONLY)
        xfl.fl_add_io_callback(self.fdesc, xfl.FL_READ, self.iocb, \
                "Good morning")

    def test_fl_remove_io_callback_ok(self):
        # test should NOT fail
        self.statusmsg = "%s: should NOT fail." % \
                sys._getframe().f_code.co_name
        self.precondition()
        self.fdesc = os.open('./stubfile.txt', os.O_RDONLY)
        xfl.fl_remove_io_callback(self.fdesc, xfl.FL_READ, self.iocb)
        os.close(self.fdesc)

    def test_fl_remove_io_callback_fail1(self):
        # failing on the 2nd param.
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        self.precondition()
        self.fdesc = os.open('./stubfile.txt', os.O_RDONLY)
        xfl.fl_remove_io_callback(self.fdesc, 12500, self.iocb)
        os.close(self.fdesc)

    def test_fl_remove_io_callback_fail2(self):
        # failing on the 3rd param.
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        self.precondition()
        self.fdesc = os.open('./stubfile.txt', os.O_RDONLY)
        xfl.fl_remove_io_callback(self.fdesc, xfl.FL_READ, None)
        os.close(self.fdesc)

    def test_fl_remove_io_callback_fail3(self):
        # failing on the 1st param.
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        self.precondition()
        self.fdesc = "some strange value"
        xfl.fl_remove_io_callback(self.fdesc, xfl.FL_READ, self.iocb)



if __name__ == '__main__':
    xfl.fl_initialize(len(sys.argv), sys.argv, "flbasic", 0, 0)
    unittest.main()
    xfl.fl_finish()

