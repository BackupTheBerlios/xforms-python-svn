#!/usr/bin/env python
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class My_canvas(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'My_canvas', None, 0)

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
        self.pcanvas = xfl.fl_add_canvas(xfl.FL_NORMAL_CANVAS, 60, 60, 210, 120, 'My canvas')
        xfl.fl_set_object_boxtype(self.pcanvas, xfl.FL_RFLAT_BOX)
        xfl.fl_set_object_color(self.pcanvas, xfl.FL_COL1, xfl.FL_BLACK)
        xfl.fl_set_object_lalign(self.pcanvas, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(self.pcanvas, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.pcanvas, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.pcanvas, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.pcanvas, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.pcanvas, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.pcanvas, 'c', 1)
        xfl.fl_set_object_callback(self.pcanvas, self.canvascb, 4)

        xfl.fl_end_form()

    def canvascb(self, pobj, data):
        pass


if __name__ == '__main__':
    ApplDemo = My_canvas(len(sys.argv), sys.argv)