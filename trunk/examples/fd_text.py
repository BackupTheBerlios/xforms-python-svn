#!/usr/bin/env python3
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class Fd_text(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'Fd_text', None, 0)

        xfl.fl_set_coordunit(xfl.FL_COORD_PIXEL)
        self.create_forms()
        xfl.fl_show_form(self.sampleform, xfl.FL_PLACE_CENTERFREE, xfl.FL_FULLBORDER, 'sampleform')

        while xfl.fl_do_forms():
            pass

        xfl.fl_finish()

    def create_forms(self):

        self.sampleform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 320, 250)

        self.ptrflobj0 = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 320, 250, '')
        xfl.fl_set_object_color(self.ptrflobj0, xfl.FL_COL1, xfl.FL_COL1)
        xfl.fl_set_object_lalign(self.ptrflobj0, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(self.ptrflobj0, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.ptrflobj0, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.ptrflobj0, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.ptrflobj0, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.ptrflobj0, xfl.FL_NoGravity, xfl.FL_NoGravity)
        self.ptext = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 40, 40, 240, 110, 'My name is text,\nspecial agent Text from the Earth')
        xfl.fl_set_object_boxtype(self.ptext, xfl.FL_DOWN_BOX)
        xfl.fl_set_object_color(self.ptext, xfl.FL_COL1, xfl.FL_MCOL)
        xfl.fl_set_object_lalign(self.ptext, xfl.FL_ALIGN_RIGHT_TOP|xfl.FL_ALIGN_INSIDE)
        xfl.fl_set_object_lstyle(self.ptext, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.ptext, 11)
        xfl.fl_set_object_lcol(self.ptext, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.ptext, xfl.FL_RESIZE_X)
        xfl.fl_set_object_gravity(self.ptext, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.ptext, 'T', 1)
        xfl.fl_set_object_callback(self.ptext, self.textcb, 0)

        xfl.fl_end_form()

    def textcb(self, pobj, data):
        pass


if __name__ == '__main__':
    print("***** fd_text.py *****")
    ApplDemo = Fd_text(len(sys.argv), sys.argv)

