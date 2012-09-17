#!/usr/bin/env python3
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class Fd_spinner(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'Fd_spinner', None, 0)

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
        self.pspinner = xfl.fl_add_spinner(xfl.FL_FLOAT_SPINNER, 90, 20, 220, 120, 'My spinner')
        xfl.fl_set_object_boxtype(self.pspinner, xfl.FL_NO_BOX)
        xfl.fl_set_spinner_bounds(self.pspinner, -100.0000, 100.0000)
        xfl.fl_set_spinner_value(self.pspinner, 10.0000)
        xfl.fl_set_spinner_precision(self.pspinner, 4)
        xfl.fl_set_object_color(self.pspinner, xfl.FL_COL1, xfl.FL_MCOL)
        xfl.fl_set_object_lalign(self.pspinner, xfl.FL_ALIGN_LEFT)
        xfl.fl_set_object_lstyle(self.pspinner, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.pspinner, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.pspinner, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.pspinner, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.pspinner, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.pspinner, 'p', 1)
        xfl.fl_set_object_callback(self.pspinner, self.spinnercb, 0)
        xfl.fl_set_object_return(self.pspinner, xfl.FL_RETURN_END_CHANGED)

        xfl.fl_end_form()

    def spinnercb(self, pobj, data):
        pass


if __name__ == '__main__':
    print("***** fd_spinner.py *****")
    ApplDemo = Fd_spinner(len(sys.argv), sys.argv)

