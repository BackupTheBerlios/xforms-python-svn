#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" unit-test for functions in flbitmap.py

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

import xformslib as xfl


class Test_fl_add_bitmap(unittest.TestCase):

    def setUp(self):
        """invoked before each test."""
        self.statusmsg = ""
        self.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 800, 600)

    def tearDown(self):
        """invoked after each test."""
        xfl.fl_end_form()
        print(self.statusmsg)

    def test_fl_add_bitmap_ok(self):
        # test should NOT fail
        self.statusmsg = "%s: should NOT fail." % sys._getframe().f_code.co_name
        bitobj = xfl.fl_add_bitmap(xfl.FL_NORMAL_BITMAP, 200, 250, 120, 120, \
                "My Bitmap")

    def test_fl_add_bitmap_fail1(self):
        # failing: 1st arg out-of-range value
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        bitobj = xfl.fl_add_bitmap(150, 200, 250, 120, 120, \
                "My Bitmap")

    def test_fl_add_bitmap_fail2(self):
        # failing: 5th arg missing
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        bitobj = xfl.fl_add_bitmap(xfl.FL_NORMAL_BITMAP, 200, 250, 120, \
                "My Bitmap")

    def test_fl_add_bitmap_fail3(self):
        # failing: 3rd arg of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        bitobj = xfl.fl_add_bitmap(xfl.FL_NORMAL_BITMAP, 200, "bingo", 120, \
                120, "My Bitmap")


class Test_fl_set_bitmap_data(unittest.TestCase):

    def setUp(self):
        """invoked before each test."""
        self.statusmsg = ""
        self.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 800, 600)
        self.bitobj = xfl.fl_add_bitmap(xfl.FL_NORMAL_BITMAP, 200, \
                250, 120, 120, "My Bitmap")

    def tearDown(self):
        """invoked after each test."""
        xfl.fl_end_form()
        print(self.statusmsg)

    def test_fl_set_bitmap_data_ok(self):
        # test should NOT fail
        self.statusmsg = "%s: should NOT fail." % sys._getframe().f_code.co_name
        w = 6
        h = 6
        xbmdata = "\xa0\x99\x98\x97\x96\x95\x94\x93\x92\x91\x90\x89" \
                  "\x88\x87\x86\x85\x84\x83\x82\x81\x80\x79\x78\x77" \
                  "\x76\x75\x74\x73\x72\x71\x70\x69\x68\x67\x66\x65"
        xfl.fl_set_bitmap_data(self.bitobj, w, h, xbmdata)

    def test_fl_set_bitmap_data_fail1(self):
        # failing: 1st arg of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        w = 6
        h = 6
        xbmdata = "\xa0\x99\x98\x97\x96\x95\x94\x93\x92\x91\x90\x89" \
                  "\x88\x87\x86\x85\x84\x83\x82\x81\x80\x79\x78\x77" \
                  "\x76\x75\x74\x73\x72\x71\x70\x69\x68\x67\x66\x65"
        xfl.fl_set_bitmap_data(w, w, h, xbmdata)

    def test_fl_set_bitmap_data_fail2(self):
        # failing: 2nd arg missing
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        w = 6
        h = 6
        xbmdata = "\xa0\x99\x98\x97\x96\x95\x94\x93\x92\x91\x90\x89" \
                  "\x88\x87\x86\x85\x84\x83\x82\x81\x80\x79\x78\x77" \
                  "\x76\x75\x74\x73\x72\x71\x70\x69\x68\x67\x66\x65"
        xfl.fl_set_bitmap_data(self.bitobj, h, xbmdata)

    def test_fl_set_bitmap_data_fail3(self):
        # test should fail: params not matching
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        w = 2
        h = 3
        xbmdata = "\xa0\x99\x98\x97"
        xfl.fl_set_bitmap_data(self.bitobj, w, h, xbmdata)


class Test_fl_set_bitmap_file(unittest.TestCase):

    def setUp(self):
        """invoked before each test."""
        self.statusmsg = ""
        self.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 800, 600)
        self.bitobj = xfl.fl_add_bitmap(xfl.FL_NORMAL_BITMAP, 200, \
                250, 120, 120, "My Bitmap")

    def tearDown(self):
        """invoked after each test."""
        xfl.fl_end_form()
        print(self.statusmsg)

    def test_fl_set_bitmap_file_ok(self):
        # test should NOT fail
        self.statusmsg = "%s: should NOT fail." % sys._getframe().f_code.co_name
        xbmfile = "prova.xbm"
        xfl.fl_set_bitmap_file(self.bitobj, xbmfile)

    def test_fl_set_bitmap_file_fail1(self):
        # failing: 1st arg of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xfl.fl_set_bitmap_file(self.bitobj, 102)

    def test_fl_set_bitmap_file_fail2(self):
        # failing: 1st and 2nd args of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xfl.fl_set_bitmap_file(102, self.bitobj)

    def test_fl_set_bitmap_file_fail3(self):
        # failing: 2nd arg missing
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xfl.fl_set_bitmap_file(self.bitobj)




if __name__ == '__main__':
    xfl.fl_initialize(len(sys.argv), sys.argv, "Bitmap", 0, 0)
    unittest.main()
    xfl.fl_finish()
