#!/usr/bin/env python
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class Fd_thumbwheel(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'Fd_thumbwheel', None, 0)

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
        self.pthumbwheel = xfl.fl_add_thumbwheel(xfl.FL_VERT_THUMBWHEEL, 140, 30, 40, 160, 'A thumbwheel')
        xfl.fl_set_object_boxtype(self.pthumbwheel, xfl.FL_RSHADOW_BOX)
        xfl.fl_set_thumbwheel_bounds(self.pthumbwheel, 10, 100)
        xfl.fl_set_thumbwheel_value(self.pthumbwheel, 15)
        xfl.fl_set_thumbwheel_step(self.pthumbwheel, 0.05)
        xfl.fl_set_object_color(self.pthumbwheel, xfl.FL_DODGERBLUE, xfl.FL_COL1)
        xfl.fl_set_object_lalign(self.pthumbwheel, xfl.FL_ALIGN_BOTTOM)
        xfl.fl_set_object_lstyle(self.pthumbwheel, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.pthumbwheel, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.pthumbwheel, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.pthumbwheel, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.pthumbwheel, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.pthumbwheel, 'w', 1)
        xfl.fl_set_object_callback(self.pthumbwheel, self.twheelcb, 5)
        xfl.fl_set_object_return(self.pthumbwheel, xfl.FL_RETURN_ALWAYS)

        xfl.fl_end_form()

    def twheelcb(self, pobj, data):
        pass


if __name__ == '__main__':
    ApplDemo = Fd_thumbwheel(len(sys.argv), sys.argv)