#!/usr/bin/env python3
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class Fd_input(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'Fd_input', None, 0)

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
        self.pinput = xfl.fl_add_input(xfl.FL_SECRET_INPUT, 100, 60, 170, 30, 'MyInput')
        xfl.fl_set_object_boxtype(self.pinput, xfl.FL_DOWN_BOX)
        xfl.fl_set_object_color(self.pinput, xfl.FL_INDIANRED, xfl.FL_BISQUE)
        xfl.fl_set_object_lalign(self.pinput, xfl.FL_ALIGN_LEFT)
        xfl.fl_set_object_lstyle(self.pinput, 14)
        xfl.fl_set_object_lsize(self.pinput, xfl.FL_MEDIUM_SIZE)
        xfl.fl_set_object_lcol(self.pinput, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.pinput, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.pinput, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_callback(self.pinput, self.inputcb, 5)
        xfl.fl_set_object_return(self.pinput, xfl.FL_RETURN_END_CHANGED)

        xfl.fl_end_form()

    def inputcb(self, pobj, data):
        pass


if __name__ == '__main__':
    print("***** fd_input.py *****")
    ApplDemo = Fd_input(len(sys.argv), sys.argv)

