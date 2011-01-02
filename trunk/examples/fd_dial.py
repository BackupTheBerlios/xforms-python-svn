#!/usr/bin/env python
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class Fd_dial(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'Fd_dial', None, 0)

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
        self.pdial = xfl.fl_add_dial(xfl.FL_LINE_DIAL, 40, 30, 240, 120, 'A line dial')
        xfl.fl_set_object_boxtype(self.pdial, xfl.FL_FLAT_BOX)
        xfl.fl_set_dial_bounds(self.pdial, 1, 128)
        xfl.fl_set_dial_value(self.pdial, 2.5)
        xfl.fl_set_dial_step(self.pdial, 1)
        xfl.fl_set_dial_angles(self.pdial, 45, 270)
        xfl.fl_set_dial_direction(self.pdial, xfl.FL_DIAL_CCW)
        xfl.fl_set_object_color(self.pdial, xfl.FL_COL1, xfl.FL_RIGHT_BCOL)
        xfl.fl_set_object_lalign(self.pdial, xfl.FL_ALIGN_BOTTOM)
        xfl.fl_set_object_lstyle(self.pdial, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.pdial, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.pdial, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.pdial, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.pdial, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.pdial, 'd', 1)
        xfl.fl_set_object_callback(self.pdial, self.dialcb, 7)
        xfl.fl_set_object_return(self.pdial, xfl.FL_RETURN_CHANGED)

        xfl.fl_end_form()

    def dialcb(self, pobj, data):
        pass


if __name__ == '__main__':
    ApplDemo = Fd_dial(len(sys.argv), sys.argv)