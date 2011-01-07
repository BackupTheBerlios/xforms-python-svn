#!/usr/bin/env python
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class Fd_counter(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'Fd_counter', None, 0)

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
        self.pcounter = xfl.fl_add_counter(xfl.FL_NORMAL_COUNTER, 30, 50, 260, 70, 'My counter')
        xfl.fl_set_object_boxtype(self.pcounter, xfl.FL_FLAT_BOX)
        xfl.fl_set_counter_bounds(self.pcounter, -1000.0000, 1000.0000)
        xfl.fl_set_counter_value(self.pcounter, 100.0000)
        xfl.fl_set_object_color(self.pcounter, xfl.FL_WHEAT, xfl.FL_DARKGOLDENROD)
        xfl.fl_set_object_lalign(self.pcounter, xfl.FL_ALIGN_BOTTOM)
        xfl.fl_set_object_lstyle(self.pcounter, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.pcounter, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.pcounter, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.pcounter, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.pcounter, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.pcounter, 'M', 1)
        xfl.fl_set_object_callback(self.pcounter, self.countercb, 6)
        xfl.fl_set_object_return(self.pcounter, xfl.FL_RETURN_END_CHANGED)

        xfl.fl_end_form()

    def countercb(self, pobj, data):
        pass


if __name__ == '__main__':
    print("***** fd_counter.py *****")
    ApplDemo = Fd_counter(len(sys.argv), sys.argv)

