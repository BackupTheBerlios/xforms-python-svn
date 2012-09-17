#!/usr/bin/env python3
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class Fd_formbrowser(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'Fd_formbrowser', None, 0)

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
        self.pformbrwsr = xfl.fl_add_formbrowser(xfl.FL_NORMAL_FORMBROWSER, 40, 40, 250, 180, 'A normal formbrowser')
        xfl.fl_set_object_boxtype(self.pformbrwsr, xfl.FL_OVAL3D_DOWNBOX)
        xfl.fl_set_object_color(self.pformbrwsr, xfl.FL_COL1, xfl.FL_COL1)
        xfl.fl_set_object_lalign(self.pformbrwsr, xfl.FL_ALIGN_BOTTOM)
        xfl.fl_set_object_lstyle(self.pformbrwsr, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.pformbrwsr, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.pformbrwsr, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.pformbrwsr, xfl.FL_RESIZE_NONE)
        xfl.fl_set_object_gravity(self.pformbrwsr, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.pformbrwsr, 'n', 1)
        xfl.fl_set_object_callback(self.pformbrwsr, self.formbrwsr_cb, 99)

        xfl.fl_end_form()

    def formbrwsr_cb(self, pobj, data):
        pass


if __name__ == '__main__':
    print("***** fd_formbrowser.py *****")
    ApplDemo = Fd_formbrowser(len(sys.argv), sys.argv)

