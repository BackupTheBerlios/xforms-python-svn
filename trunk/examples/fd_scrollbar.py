#!/usr/bin/env python3
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class Fd_scrollbar(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'Fd_scrollbar', None, 0)

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
        self.pscrollbar = xfl.fl_add_scrollbar(xfl.FL_HOR_PLAIN_SCROLLBAR, 40, 40, 250, 50, 'A common scrollbar')
        xfl.fl_set_object_boxtype(self.pscrollbar, xfl.FL_DOWN_BOX)
        xfl.fl_set_scrollbar_bounds(self.pscrollbar, 1, 5)
        xfl.fl_set_scrollbar_value(self.pscrollbar, 1)
        xfl.fl_set_scrollbar_increment(self.pscrollbar, 0.5, 0.05)
        xfl.fl_set_scrollbar_size(self.pscrollbar, 0.20)
        xfl.fl_set_scrollbar_step(self.pscrollbar, 1.000)
        xfl.fl_set_object_color(self.pscrollbar, xfl.FL_COL1, xfl.FL_COL1)
        xfl.fl_set_object_lalign(self.pscrollbar, xfl.FL_ALIGN_BOTTOM)
        xfl.fl_set_object_lstyle(self.pscrollbar, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.pscrollbar, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.pscrollbar, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.pscrollbar, xfl.FL_RESIZE_X)
        xfl.fl_set_object_gravity(self.pscrollbar, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.pscrollbar, 'r', 1)
        xfl.fl_set_object_callback(self.pscrollbar, self.scrollbarcb, 3)
        xfl.fl_set_object_return(self.pscrollbar, xfl.FL_RETURN_END_CHANGED)

        xfl.fl_end_form()

    def scrollbarcb(self, pobj, data):
        pass


if __name__ == '__main__':
    print("***** fd_scrollbar.py *****")
    ApplDemo = Fd_scrollbar(len(sys.argv), sys.argv)

