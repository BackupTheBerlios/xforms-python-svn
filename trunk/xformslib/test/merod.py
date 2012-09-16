#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" unit-test for functions in flbrowser.py

    For every function I have created one use-cases test supposed to fail,
    but be promptly intercepted by xforms-python's error handling routines;
    or without being intercepted, so error handling is left to upstream XForms C functions.
"""

import sys
import os
import random
import ctypes
sys.path.append('..')
import unittest

import xformslib as xfl

def provide_casual_params():
    randlist = [1, 'Hello', 0, 15.0, xfl.FL_OBJECT, 's', 254, xfl.FL_BLUE, \
            xfl.FL_INPUTVALIDATOR, 1001, 'E.U.', 4.5, 'Label', xfl.FL_FORM, \
            15899, '88', xfl.KEY_list, ctypes.POINTER(xfl.FL_OBJECT), 0.1, \
            ctypes.POINTER(xfl.FL_FORM)(), [0,1,2,3], {'a':0, 'b':1}]
    random.seed()
    nargs = random.randint(0, 8)        # max 7 args
    argstoret = []
    if not nargs:
        return None, None
    else:       # some args
        for idx in range(0, nargs):
            posn = random.randint(0, len(randlist)-1)
            singarg = randlist[posn]
            argstoret.append(singarg)
        return argstoret


class Test_flbrowser(unittest.TestCase):
    def setUp(self):
        """invoked before each test."""
        pass

    def tearDown(self):
        """invoked after each test."""
        pass

    def test_fl_add_browser(self):
        """fl_add_browser(browsertype, xpos, ypos, width, height, label)"""
        xfl.fl_add_browser(77.1234, )

    def test_fl_clear_browser(self):
        """fl_clear_browser(ptr_flobject)"""
        xfl.fl_clear_browser(149, 1.0, 4, )

    def test_fl_add_browser_line(self):
        """fl_add_browser_line(ptr_flobject, newtext)"""
        xfl.fl_add_browser_line(Hello, 15899, None, Label, E.U., 149, )

    def test_fl_addto_browser(self):
        """fl_addto_browser(ptr_flobject, newtext)"""
        xfl.fl_addto_browser([0, 1, 2, 3], Label, [0, 1, 2, 3], None, 15899, {'a': 0, 'b': 1}, )

    def test_fl_addto_browser_chars(self):
        """fl_addto_browser_chars(ptr_flobject, addedtext)"""
        xfl.fl_addto_browser_chars(0.1, 1, 4, 149, E.U., 254, iop, [0, 1, 2, 3], )

    def test_fl_insert_browser_line(self):
        """fl_insert_browser_line(ptr_flobject, linenum, newtext)"""
        xfl.fl_insert_browser_line([5, 5], [5, 5], None, Label, 154, 4, 154, 1001, )

    def test_fl_delete_browser_line(self):
        """fl_delete_browser_line(ptr_flobject, linenum)"""
        xfl.fl_delete_browser_line([1, 2, 4, 7, 33554432, 67108864, 134217728], )

    def test_fl_replace_browser_line(self):
        """fl_replace_browser_line(ptr_flobject, linenum, newtext)"""
        xfl.fl_replace_browser_line(254, E.U., )

    def test_fl_get_browser_line(self):
        """fl_get_browser_line(ptr_flobject, linenum) -> linetext"""
        xfl.fl_get_browser_line(4.5, 15899, [0, 1, 2, 3], )

    def test_fl_load_browser(self):
        """fl_load_browser(ptr_flobject, filename) -> result"""
        xfl.fl_load_browser([0, 1, 2, 3], 1.0, {'a': 0, 'b': 1}, [1, 2, 4, 7, 33554432, 67108864, 134217728], )

    def test_fl_select_browser_line(self):
        """fl_select_browser_line(ptr_flobject, linenum)"""
        xfl.fl_select_browser_line(0.1, 1, )

    def test_fl_deselect_browser_line(self):
        """fl_deselect_browser_line(ptr_flobject, linenum)"""
        xfl.fl_deselect_browser_line(Hello, 1001, {'a': 0, 'b': 1}, Label, 1001, Hello, )

    def test_fl_deselect_browser(self):
        """fl_deselect_browser(ptr_flobject)"""
        xfl.fl_deselect_browser(149, 15899, [5, 5], O, O, 4, [0, 1, 2, 3], [0, 1, 2, 3], )

    def test_fl_isselected_browser_line(self):
        """fl_isselected_browser_line(ptr_flobject, linenum) -> yesno"""
        xfl.fl_isselected_browser_line(1001, 1.0, 149, E.U., 4.5, )

    def test_fl_get_browser_topline(self):
        """fl_get_browser_topline(ptr_flobject) -> linenum"""
        xfl.fl_get_browser_topline(15899, 4.5, 4, )

    def test_fl_get_browser(self):
        """fl_get_browser(ptr_flobject) -> linenum"""
        xfl.fl_get_browser(E.U., 154, 149, 1, E.U., [5, 5], Label, berries, )

    def test_fl_get_browser_maxline(self):
        """fl_get_browser_maxline(ptr_flobject) -> numlines"""
        xfl.fl_get_browser_maxline(None)

    def test_fl_get_browser_screenlines(self):
        """fl_get_browser_screenlines(ptr_flobject) -> numlines"""
        xfl.fl_get_browser_screenlines(berries, 0, Hello, 149, iop, )

    def test_fl_set_browser_topline(self):
        """fl_set_browser_topline(ptr_flobject, linenum)"""
        xfl.fl_set_browser_topline(s, 254, 149, {'a': 0, 'b': 1}, E.U., )

    def test_fl_set_browser_bottomline(self):
        """fl_set_browser_bottomline(ptr_flobject, linenum)"""
        xfl.fl_set_browser_bottomline(77.1234, )

    def test_fl_set_browser_fontsize(self):
        """fl_set_browser_fontsize(ptr_flobject, size)"""
        xfl.fl_set_browser_fontsize(4, )

    def test_fl_set_browser_fontstyle(self):
        """fl_set_browser_fontstyle(ptr_flobject, style)"""
        xfl.fl_set_browser_fontstyle(Hello, aabbccddee, Hello, 4.5, s, 77.1234, )

    def test_fl_set_browser_specialkey(self):
        """fl_set_browser_specialkey(ptr_flobject, specialkey)"""
        xfl.fl_set_browser_specialkey(s, 0.1, 88, [5, 5], )

    def test_fl_set_browser_vscrollbar(self):
        """fl_set_browser_vscrollbar(ptr_flobject, howscroll)"""
        xfl.fl_set_browser_vscrollbar(None, [5, 5], O, 1.0, )

    def test_fl_set_browser_hscrollbar(self):
        """fl_set_browser_hscrollbar(ptr_flobject, howscroll)"""
        xfl.fl_set_browser_hscrollbar(154, 149, 0.1, O, 149, 88, aabbccddee, )

    def test_fl_set_browser_line_selectable(self):
        """fl_set_browser_line_selectable(ptr_flobject, linenum, yesno)"""
        xfl.fl_set_browser_line_selectable(None)

    def test_fl_get_browser_dimension(self):
        """fl_get_browser_dimension(ptr_flobject) -> xpos, ypos, width, height"""
        xfl.fl_get_browser_dimension(None)

    def test_fl_set_browser_dblclick_callback(self):
        """fl_set_browser_dblclick_callback(ptr_flobject, pyfn_CallbackPtr, numdata)"""
        xfl.fl_set_browser_dblclick_callback(None, 4.5, aabbccddee, Label, )

    def test_fl_get_browser_xoffset(self):
        """fl_get_browser_xoffset(ptr_flobject) -> numpixels"""
        xfl.fl_get_browser_xoffset(254, )

    def test_fl_get_browser_rel_xoffset(self):
        """fl_get_browser_rel_xoffset(ptr_flobject) -> roffset"""
        xfl.fl_get_browser_rel_xoffset(15.0, O, 1, )

    def test_fl_set_browser_xoffset(self):
        """fl_set_browser_xoffset(ptr_flobject, numpixels)"""
        xfl.fl_set_browser_xoffset(None, E.U., None, Hello, [1, 2, 4, 7, 33554432, 67108864, 134217728], [0, 1, 2, 3], )

    def test_fl_set_browser_rel_xoffset(self):
        """fl_set_browser_rel_xoffset(ptr_flobject, roffset)"""
        xfl.fl_set_browser_rel_xoffset(88, iop, 1001, iop, )

    def test_fl_get_browser_yoffset(self):
        """fl_get_browser_yoffset(ptr_flobject) -> numpixels"""
        xfl.fl_get_browser_yoffset(None, 0, 1.0, )

    def test_fl_get_browser_rel_yoffset(self):
        """fl_get_browser_rel_yoffset(ptr_flobject) -> roffset"""
        xfl.fl_get_browser_rel_yoffset(None, 4, 254, Label, None, E.U., aabbccddee, Hello, )

    def test_fl_set_browser_yoffset(self):
        """fl_set_browser_yoffset(ptr_flobject, numpixels)"""
        xfl.fl_set_browser_yoffset(4.5, [1, 2, 4, 7, 33554432, 67108864, 134217728], 4, 254, None, Label, iop, 15899, )

    def test_fl_set_browser_rel_yoffset(self):
        """fl_set_browser_rel_yoffset(ptr_flobject, roffset)"""
        xfl.fl_set_browser_rel_yoffset([1, 2, 4, 7, 33554432, 67108864, 134217728], iop, 1.0, [1, 2, 4, 7, 33554432, 67108864, 134217728], 88, 154, )

    def test_fl_set_browser_scrollbarsize(self):
        """fl_set_browser_scrollbarsize(ptr_flobject, height, width)"""
        xfl.fl_set_browser_scrollbarsize([1, 2, 4, 7, 33554432, 67108864, 134217728], [1, 2, 4, 7, 33554432, 67108864, 134217728], 88, 149, 0.1, None, 1001, s, )

    def test_fl_show_browser_line(self):
        """fl_show_browser_line(ptr_flobject, linenum)"""
        xfl.fl_show_browser_line(15.0, 1, None, [5, 5], 0.1, [5, 5], Hello, 4, )

    def test_fl_set_browser_hscroll_callback(self):
        """fl_set_browser_hscroll_callback(ptr_flobject, pyfn_BrowserScrollCb,
        userdata)"""
        xfl.fl_set_browser_hscroll_callback(1.0, 77.1234, )

    def test_fl_set_browser_vscroll_callback(self):
        """fl_set_browser_vscroll_callback(ptr_flobject, pyfn_BrowserScrollCb,
        userdata)"""
        xfl.fl_set_browser_vscroll_callback(None, [5, 5], 149, )

    def test_fl_get_browser_line_yoffset(self):
        """fl_get_browser_line_yoffset(ptr_flobject, linenum) -> offset"""
        xfl.fl_get_browser_line_yoffset(None, 4.5, {'a': 0, 'b': 1}, )

    def test_fl_get_browser_hscroll_callback(self):
        """fl_get_browser_hscroll_callback(ptr_flobject) -> BrowserScrollCb"""
        xfl.fl_get_browser_hscroll_callback(iop, berries, [1, 2, 4, 7, 33554432, 67108864, 134217728], aabbccddee, 0, )

    def test_fl_get_browser_vscroll_callback(self):
        """fl_get_browser_vscroll_callback(ptr_flobject) -> BrowserScrollCb"""
        xfl.fl_get_browser_vscroll_callback(4.5, [1, 2, 4, 7, 33554432, 67108864, 134217728], )

    def test_fl_get_browser_scrollbar_repeat(self):
        """fl_get_browser_scrollbar_repeat(ptr_flobject) -> tdelay"""
        xfl.fl_get_browser_scrollbar_repeat(4.5, (0, 0), 15899, )

    def test_fl_set_browser_scrollbar_repeat(self):
        """fl_set_browser_scrollbar_repeat(ptr_flobject, tdelay)"""
        xfl.fl_set_browser_scrollbar_repeat([0, 1, 2, 3], None, [1, 2, 4, 7, 33554432, 67108864, 134217728], {'a': 0, 'b': 1}, [1, 2, 4, 7, 33554432, 67108864, 134217728], )


if __name__ == '__main__':
    xfl.fl_initialize(len(sys.argv), sys.argv, "flbrowser", 0, 0)
    unittest.main()
    xfl.fl_finish()
