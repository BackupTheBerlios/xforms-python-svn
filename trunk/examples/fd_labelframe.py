#!/usr/bin/env python3
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class Fd_labelframe(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'Fd_labelframe', None, 0)

        xfl.fl_set_coordunit(xfl.FL_COORD_PIXEL)
        self.create_forms()
        xfl.fl_show_form(self.sampledemo, xfl.FL_PLACE_CENTERFREE, xfl.FL_FULLBORDER, 'sampledemo')

        while xfl.fl_do_forms():
            pass

        xfl.fl_finish()

    def create_forms(self):

        self.sampledemo = xfl.fl_bgn_form(xfl.FL_NO_BOX, 320, 250)

        self.ptrflobj0 = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 320, 250, '')
        xfl.fl_set_object_color(self.ptrflobj0, xfl.FL_COL1, xfl.FL_COL1)
        xfl.fl_set_object_lalign(self.ptrflobj0, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(self.ptrflobj0, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.ptrflobj0, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.ptrflobj0, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.ptrflobj0, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.ptrflobj0, xfl.FL_NoGravity, xfl.FL_NoGravity)
        self.mylblfrm = xfl.fl_add_labelframe(xfl.FL_EMBOSSED_FRAME, 20, 30, 270, 110, 'some\nframe')
        xfl.fl_set_object_boxtype(self.mylblfrm, xfl.FL_SHADOW_BOX)
        xfl.fl_set_object_color(self.mylblfrm, xfl.FL_BLACK, xfl.FL_COL1)
        xfl.fl_set_object_lalign(self.mylblfrm, xfl.FL_ALIGN_LEFT_TOP)
        xfl.fl_set_object_lstyle(self.mylblfrm, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.mylblfrm, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.mylblfrm, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.mylblfrm, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.mylblfrm, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_callback(self.mylblfrm, self.lframe_cb, 2)

        xfl.fl_end_form()

    def lframe_cb(self, pobj, data):
        pass


if __name__ == '__main__':
    print("***** fd_labelframe.py *****")
    ApplDemo = Fd_labelframe(len(sys.argv), sys.argv)

