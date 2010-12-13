#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" unit-test for functions in flbitmap.py

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


class Test_fl_add_bitmap(unittest.TestCase):

    def setUp(self):
        #invoked before each test
        self.statusmsg = ""
        self.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 800, 600)

    def tearDown(self):
        #invoked after each test
        xfl.fl_end_form()
        print(self.statusmsg)

    def test_fl_add_bitmap__ok(self):
        # test should NOT fail
        self.statusmsg = "%s: should NOT fail." % \
                sys._getframe().f_code.co_name
        bitobj = xfl.fl_add_bitmap(xfl.FL_NORMAL_BITMAP, 200, 250, \
                120, 120, "My Bitmap")

    def test_fl_add_bitmap__fail1(self):
        # failing: 1st arg out-of-range value
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        bitobj = xfl.fl_add_bitmap(150, 200, 250, 120, 120, \
                "My Bitmap")

    def test_fl_add_bitmap__fail2(self):
        # failing: 5th arg missing
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        bitobj = xfl.fl_add_bitmap(xfl.FL_NORMAL_BITMAP, 200, 250, \
                120, "My Bitmap")

    def test_fl_add_bitmap__fail3(self):
        # failing: 3rd arg of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        bitobj = xfl.fl_add_bitmap(xfl.FL_NORMAL_BITMAP, 200, "bingo", \
                120, 120, "My Bitmap")


class Test_fl_set_bitmap_data(unittest.TestCase):

    def setUp(self):
        #invoked before each test
        self.statusmsg = ""
        self.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 800, 600)
        self.bitobj = xfl.fl_add_bitmap(xfl.FL_NORMAL_BITMAP, 200, \
                250, 120, 120, "My Bitmap")

    def tearDown(self):
        #invoked after each test
        xfl.fl_end_form()
        print(self.statusmsg)

    def test_fl_set_bitmap_data__ok(self):
        # test should NOT fail
        self.statusmsg = "%s: should NOT fail." % \
                sys._getframe().f_code.co_name
        w = 6
        h = 6
        xbmdata = [0xa0, 0x99, 0x98, 0x97, 0x96, 0x95, 0x94, 0x93,
                   0x92, 0x91, 0x90, 0x89, 0x88, 0x87, 0x86, 0x85,
                   0x84, 0x83, 0x82, 0x81, 0x80, 0x79, 0x78, 0x77,
                   0x76, 0x75, 0x74, 0x73, 0x72, 0x71, 0x70, 0x69,
                   0x68, 0x67, 0x66, 0x65]
        xfl.fl_set_bitmap_data(self.bitobj, w, h, xbmdata)

    def test_fl_set_bitmap_data__fail1(self):
        # failing: 1st arg of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        w = 6
        h = 6
        xbmdata = [0xa0, 0x99, 0x98, 0x97, 0x96, 0x95, 0x94, 0x93,
                   0x92, 0x91, 0x90, 0x89, 0x88, 0x87, 0x86, 0x85,
                   0x84, 0x83, 0x82, 0x81, 0x80, 0x79, 0x78, 0x77,
                   0x76, 0x75, 0x74, 0x73, 0x72, 0x71, 0x70, 0x69,
                   0x68, 0x67, 0x66, 0x65]
        xfl.fl_set_bitmap_data(w, w, h, xbmdata)

    def test_fl_set_bitmap_data__fail2(self):
        # failing: 2nd arg missing
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        w = 6
        h = 6
        xbmdata = [0xa0, 0x99, 0x98, 0x97, 0x96, 0x95, 0x94, 0x93,
                   0x92, 0x91, 0x90, 0x89, 0x88, 0x87, 0x86, 0x85,
                   0x84, 0x83, 0x82, 0x81, 0x80, 0x79, 0x78, 0x77,
                   0x76, 0x75, 0x74, 0x73, 0x72, 0x71, 0x70, 0x69,
                   0x68, 0x67, 0x66, 0x65]
        xfl.fl_set_bitmap_data(self.bitobj, h, xbmdata)

    def test_fl_set_bitmap_data__fail3(self):
        # failing: 4th arg of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        w = 2
        h = 3
        xfl.fl_set_bitmap_data(self.bitobj, w, h, 10)


class Test_fl_set_bitmap_file(unittest.TestCase):

    def setUp(self):
        #invoked before each test
        self.statusmsg = ""
        self.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 800, 600)
        self.bitobj = xfl.fl_add_bitmap(xfl.FL_NORMAL_BITMAP, 200, \
                250, 120, 120, "My Bitmap")

    def tearDown(self):
        #invoked after each test
        xfl.fl_end_form()
        print(self.statusmsg)

    def test_fl_set_bitmap_file__ok(self):
        # test should NOT fail
        self.statusmsg = "%s: should NOT fail." % \
                sys._getframe().f_code.co_name
        xbmfile = "prova.xbm"
        xfl.fl_set_bitmap_file(self.bitobj, xbmfile)

    def test_fl_set_bitmap_file__fail1(self):
        # failing: 2nd arg of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xfl.fl_set_bitmap_file(self.bitobj, 102)

    def test_fl_set_bitmap_file__fail2(self):
        # failing: 1st and 2nd args of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xfl.fl_set_bitmap_file(102, self.bitobj)

    def test_fl_set_bitmap_file__fail3(self):
        # failing: 2nd arg missing
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xfl.fl_set_bitmap_file(self.bitobj)


class Test_fl_read_bitmapfile(unittest.TestCase):

    def setUp(self):
        #invoked before each test
        self.statusmsg = ""
        self.win0 = xfl.fl_default_win()
        self.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 800, 600)

    def tearDown(self):
        #invoked after each test
        xfl.fl_end_form()
        print(self.statusmsg)

    def test_fl_read_bitmapfile__ok(self):
        # test should NOT fail
        self.statusmsg = "%s: should NOT fail." % \
                sys._getframe().f_code.co_name
        xbmfile = "prova.xbm"
        pixm, w, h, hotx, hoty = xfl.fl_read_bitmapfile(self.win0, xbmfile)

    def test_fl_read_bitmapfile__fail1(self):
        # failing: 2nd arg of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        pixm, w, h, hotx, hoty = xfl.fl_read_bitmapfile(self.win0, self.win0)

    def test_fl_read_bitmapfile__fail2(self):
        # failing: 1st and 2nd args of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xbmfile = "prova.xbm"
        pixm, w, h, hotx, hoty = xfl.fl_read_bitmapfile(xbmfile, self.win0)

    def test_fl_read_bitmapfile__fail3(self):
        # failing: 1st arg missing
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xbmfile = "prova.xbm"
        pixm, w, h, hotx, hoty = xfl.fl_read_bitmapfile(xbmfile)


class Test_fl_create_from_bitmapdata(unittest.TestCase):

    def setUp(self):
        #invoked before each test
        self.statusmsg = ""
        self.win0 = xfl.fl_default_win()
        self.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 800, 600)

    def tearDown(self):
        #invoked after each test
        xfl.fl_end_form()
        print(self.statusmsg)

    def test_fl_create_from_bitmapdata__ok(self):
        # test should NOT fail
        self.statusmsg = "%s: should NOT fail." % \
                sys._getframe().f_code.co_name
        xbmdata = "\x45\x46\x47\x48\x49\x25\x26\x27\x28\x29\x05\x06\x07" \
                  "\x08\x09\x60\x61\x62\x63\x64\x68\x86\xaa\xab\xac\xad"
        pixm = xfl.fl_create_from_bitmapdata(self.win0, xbmdata, 15, 15)

    def test_fl_create_from_bitmapdata__fail1(self):
        # failing: 2nd arg of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        pixm = xfl.fl_create_from_bitmapdata(self.win0, self.form0, 15, 15)

    def test_fl_create_from_bitmapdata__fail2(self):
        # failing: 1st and 2nd args of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xbmdata = "\x45\x46\x47\x48\x49\x25\x26\x27\x28\x29\x05\x06\x07" \
                  "\x08\x09\x60\x61\x62\x63\x64\x68\x86\xaa\xab\xac\xad"
        pixm = xfl.fl_create_from_bitmapdata(xbmdata, self.win0, 15, 15)

    def test_fl_create_from_bitmapdata__fail3(self):
        # failing: 2st arg missing
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        pixm = xfl.fl_create_from_bitmapdata(self.win0, 15, 15)


class Test_fl_add_pixmap(unittest.TestCase):

    def setUp(self):
        #invoked before each test
        self.statusmsg = ""
        self.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 800, 600)

    def tearDown(self):
        #invoked after each test
        xfl.fl_end_form()
        print(self.statusmsg)

    def test_fl_add_pixmap__ok(self):
        # test should NOT fail
        self.statusmsg = "%s: should NOT fail." % \
                sys._getframe().f_code.co_name
        pxmtobj = xfl.fl_add_pixmap(xfl.FL_NORMAL_PIXMAP, 200, 250, \
                120, 120, "My pixmap")

    def test_fl_add_pixmap__fail1(self):
        # failing: 1st arg out-of-range value
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        pxmobj = xfl.fl_add_pixmap(150, 200, 250, 120, 120, \
                "My pixmap")

    def test_fl_add_pixmap__fail2(self):
        # failing: 5th arg missing
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        pxmobj = xfl.fl_add_pixmap(xfl.FL_NORMAL_PIXMAP, 200, 250, \
                120, "My pixmap")

    def test_fl_add_pixmap__fail3(self):
        # failing: 3rd arg of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        bitobj = xfl.fl_add_pixmap(xfl.FL_NORMAL_PIXMAP, 200, "bingo", \
                120, 120, "My pixmap")


class Test_fl_set_pixmap_data(unittest.TestCase):

    def setUp(self):
        #invoked before each test
        self.statusmsg = ""
        self.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 800, 600)
        self.pxmobj = xfl.fl_add_pixmapbutton(xfl.FL_NORMAL_PIXMAP, 200, \
                250, 120, 120, "My pixmap")
        self.xpmdatalist = ["25 25 2 1", " 	c #000000000000", \
                ".	c #FFFFFFFFFFFF", "    .           .        ", \
                "    .     .     .        ", " .......  .  .......     ", \
                " .      . .  .      .    ", " ..    ..    ..    ..    ", \
                "  ......  .   ......     ", " .        .  .           ", \
                " .......  .  .......     ", " .      . .  .      .    ", \
                " ..    ..    ..    ..    ", "  ......  .   ......     ",
                " .        .  .           ", " .......  .  .......     ",
                " .      . .  .      .    ", " ..    ..    ..    ..    ",
                "  ......  .   ......     ", " .        .  .           ",
                " .......  .  .......     ", " .      . .  .      .    ",
                " ..    ..    ..    ..    ", "  ......  .   ......     ",
                " .        .  .           ", " ....     .   ...        ",
                "    .           .        ", "    .           .        "]

    def tearDown(self):
        #invoked after each test
        xfl.fl_end_form()
        print(self.statusmsg)

    """def test_fl_set_pixmap_data__ok(self):
        # test should NOT fail
        self.statusmsg = "%s: should NOT fail." % \
                sys._getframe().f_code.co_name
        xfl.fl_set_pixmap_data(self.pxmobj, self.xpmdatalist)"""

    def test_fl_set_pixmap_data__fail1(self):
        # failing: 1st arg of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xfl.fl_set_pixmap_data(self.form0, self.xpmdatalist)

    def test_fl_set_pixmap_data__fail2(self):
        # failing: 2nd arg missing
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xfl.fl_set_pixmap_data(self.pxmobj)

    def test_fl_set_pixmap_data__fail3(self):
        # failing: 1st and 2nd of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xfl.fl_set_pixmap_data(self.xpmdatalist, self.pxmobj)


class Test_fl_set_pixmap_file(unittest.TestCase):
    def setUp(self):
        #invoked before each test
        self.statusmsg = ""
        self.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 800, 600)
        self.pxmobj0 = xfl.fl_add_pixmap(xfl.FL_NORMAL_PIXMAP, 200, \
                250, 120, 120, "My Pixmap")

    def tearDown(self):
        #invoked after each test
        xfl.fl_end_form()
        print(self.statusmsg)

    """def test_fl_set_pixmap_file__ok(self):
        # test should NOT fail
        self.statusmsg = "%s: should NOT fail." % \
                sys._getframe().f_code.co_name
        xpmfile = "./prova.xpm"
        xfl.fl_set_pixmap_file(self.pxmobj0, xpmfile)"""

    def test_fl_set_pixmap_file__fail1(self):
        # failing: 2nd arg of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xfl.fl_set_pixmap_file(self.pxmobj0, 102)

    def test_fl_set_pixmap_file__fail2(self):
        # failing: 1st and 2nd args of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xfl.fl_set_pixmap_file(102, self.pxmobj0)

    def test_fl_set_pixmap_file__fail3(self):
        # failing: 2nd arg missing
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xfl.fl_set_pixmap_file(self.pxmobj0)


class Test_fl_set_pixmap_align(unittest.TestCase):
    def setUp(self):
        #invoked before each test
        self.statusmsg = ""
        self.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 800, 600)
        self.pxmobj0 = xfl.fl_add_pixmap(xfl.FL_NORMAL_PIXMAP, 200, \
                250, 120, 120, "My Pixmap")

    def tearDown(self):
        #invoked after each test
        xfl.fl_end_form()
        print(self.statusmsg)

    def test_fl_set_pixmap_align__ok(self):
        # test should NOT fail
        self.statusmsg = "%s: should NOT fail." % \
                sys._getframe().f_code.co_name
        xfl.fl_set_pixmap_align(self.pxmobj0, xfl.FL_ALIGN_BOTTOM, 2, 2)

    def test_fl_set_pixmap_align__fail1(self):
        # failing: 2nd arg of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xfl.fl_set_pixmap_align(self.pxmobj0, 199, 2, 2)

    def test_fl_set_pixmap_align__fail2(self):
        # failing: 1st and 2nd args of unfit type
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xfl.fl_set_pixmap_align(102, self.pxmobj0, 2, 2)

    def test_fl_set_pixmap_align__fail3(self):
        # failing: 4th arg missing
        self.statusmsg = "%s: should fail." % sys._getframe().f_code.co_name
        xfl.fl_set_pixmap_align(self.pxmobj0, xfl.FL_ALIGN_TOP, 2)




if __name__ == '__main__':
    xfl.fl_initialize(len(sys.argv), sys.argv, "flbitmap", 0, 0)
    unittest.main()
    xfl.fl_finish()
