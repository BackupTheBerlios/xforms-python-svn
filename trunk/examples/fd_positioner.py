#!/usr/bin/env python
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class Fd_positioner(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'Fd_positioner', None, 0)

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
        self.ppositn = xfl.fl_add_positioner(xfl.FL_OVERLAY_POSITIONER, 50, 50, 210, 140, 'My anonymous positioner')
        xfl.fl_set_object_boxtype(self.ppositn, xfl.FL_NO_BOX)
        xfl.fl_set_positioner_xbounds(self.ppositn, 1, 75)
        xfl.fl_set_positioner_ybounds(self.ppositn, 2, 150)
        xfl.fl_set_positioner_xvalue(self.ppositn, 50)
        xfl.fl_set_positioner_yvalue(self.ppositn, 50)
        xfl.fl_set_positioner_xstep(self.ppositn, 1)
        xfl.fl_set_positioner_ystep(self.ppositn, 2)
        xfl.fl_set_object_color(self.ppositn, xfl.FL_COL1, xfl.FL_RED)
        xfl.fl_set_object_lalign(self.ppositn, xfl.FL_ALIGN_BOTTOM)
        xfl.fl_set_object_lstyle(self.ppositn, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.ppositn, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.ppositn, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.ppositn, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.ppositn, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.ppositn, 'u', 1)
        xfl.fl_set_object_callback(self.ppositn, self.positncb, 0)
        xfl.fl_set_object_return(self.ppositn, xfl.FL_RETURN_END_CHANGED)

        xfl.fl_end_form()

    def positncb(self, pobj, data):
        pass


if __name__ == '__main__':
    print("***** fd_positioner.py *****")
    ApplDemo = Fd_positioner(len(sys.argv), sys.argv)

