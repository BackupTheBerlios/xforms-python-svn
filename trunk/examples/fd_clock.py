#!/usr/bin/env python3
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class Fd_clock(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'Fd_clock', None, 0)

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
        self.pclock = xfl.fl_add_clock(xfl.FL_ANALOG_CLOCK, 50, 40, 230, 100, 'mygoodlabel')
        xfl.fl_set_object_boxtype(self.pclock, xfl.FL_UP_BOX)
        xfl.fl_set_object_color(self.pclock, xfl.FL_INACTIVE, xfl.FL_BOTTOM_BCOL)
        xfl.fl_set_object_lalign(self.pclock, xfl.FL_ALIGN_TOP)
        xfl.fl_set_object_lstyle(self.pclock, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.pclock, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.pclock, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.pclock, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.pclock, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.pclock, 'g', 1)
        xfl.fl_set_object_callback(self.pclock, self.clockcb, 88)

        xfl.fl_end_form()

    def clockcb(self, pobj, data):
        pass


if __name__ == '__main__':
    print("***** fd_clock.py *****")
    ApplDemo = Fd_clock(len(sys.argv), sys.argv)

