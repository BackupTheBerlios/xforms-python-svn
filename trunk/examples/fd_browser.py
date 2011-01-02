#!/usr/bin/env python
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class My_browser(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'My_browser', None, 0)

        xfl.fl_set_coordunit(xfl.FL_COORD_PIXEL)
        self.create_forms()
        xfl.fl_show_form(self.sample, xfl.FL_PLACE_CENTERFREE, xfl.FL_FULLBORDER, 'sample')

        while xfl.fl_do_forms():
            pass

        xfl.fl_finish()

    def create_forms(self):

        self.sample = xfl.fl_bgn_form(xfl.FL_NO_BOX, 320, 250)

        self.ptrflobj0 = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 320, 250, '')
        xfl.fl_set_object_color(self.ptrflobj0, xfl.FL_COL1, xfl.FL_COL1)
        xfl.fl_set_object_lalign(self.ptrflobj0, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(self.ptrflobj0, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.ptrflobj0, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.ptrflobj0, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.ptrflobj0, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.ptrflobj0, xfl.FL_NoGravity, xfl.FL_NoGravity)
        self.pbrowser = xfl.fl_add_browser(xfl.FL_NORMAL_BROWSER, 20, 40, 280, 160, 'My Browser with\na lot of text')
        xfl.fl_set_object_boxtype(self.pbrowser, xfl.FL_DOWN_BOX)
        xfl.fl_set_browser_hscrollbar(self.pbrowser, xfl.FL_ON)
        xfl.fl_set_browser_vscrollbar(self.pbrowser, xfl.FL_ON)
        xfl.fl_set_object_color(self.pbrowser, xfl.FL_WHITE, xfl.FL_YELLOW)
        xfl.fl_set_object_lalign(self.pbrowser, xfl.FL_ALIGN_BOTTOM)
        xfl.fl_set_object_lstyle(self.pbrowser, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.pbrowser, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.pbrowser, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.pbrowser, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.pbrowser, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.pbrowser, 'l', 1)
        xfl.fl_set_object_callback(self.pbrowser, self.browsercb, 33)
        xfl.fl_set_object_return(self.pbrowser, xfl.FL_RETURN_END_CHANGED|xfl.FL_RETURN_SELECTION|xfl.FL_RETURN_DESELECTION)

        xfl.fl_end_form()

    def browsercb(self, pobj, data):
        pass


if __name__ == '__main__':
    ApplDemo = My_browser(len(sys.argv), sys.argv)