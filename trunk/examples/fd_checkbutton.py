#!/usr/bin/env python3
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class Fd_checkbutton(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'Fd_checkbutton', None, 0)

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
        self.chkbutton = xfl.fl_add_checkbutton(xfl.FL_INOUT_BUTTON, 50, 30, 240, 100, 'button')
        xfl.fl_set_object_boxtype(self.chkbutton, xfl.FL_NO_BOX)
        xfl.fl_set_button_mouse_buttons(self.chkbutton, 14)
        xfl.fl_set_button(self.chkbutton, 1)
        xfl.fl_set_object_color(self.chkbutton, xfl.FL_COL1, xfl.FL_YELLOW)
        xfl.fl_set_object_lalign(self.chkbutton, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(self.chkbutton, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.chkbutton, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.chkbutton, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.chkbutton, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.chkbutton, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.chkbutton, 't', 1)
        xfl.fl_set_object_callback(self.chkbutton, self.buttoncb, 123)

        xfl.fl_end_form()

    def buttoncb(self, pobj, data):
        pass


if __name__ == '__main__':
    print("***** fd_checkbutton.py *****")
    ApplDemo = Fd_checkbutton(len(sys.argv), sys.argv)

	
