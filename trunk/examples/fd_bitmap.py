#!/usr/bin/env python
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class My_bitmap(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'My_bitmap', None, 0)

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
        self.bitmapname = xfl.fl_add_bitmap(xfl.FL_NORMAL_BITMAP, 40, 30, 250, 100, 'bitmap')
        xfl.fl_set_object_boxtype(self.bitmapname, xfl.FL_NO_BOX)
        xfl.fl_set_bitmap_file(self.bitmapname, './bm2.xbm')
        xfl.fl_set_object_color(self.bitmapname, xfl.FL_COL1, xfl.FL_COL1)
        xfl.fl_set_object_lalign(self.bitmapname, xfl.FL_ALIGN_BOTTOM)
        xfl.fl_set_object_lstyle(self.bitmapname, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.bitmapname, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.bitmapname, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.bitmapname, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.bitmapname, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.bitmapname, 'b', 1)
        xfl.fl_set_object_callback(self.bitmapname, self.bitmapcb, 2)

        xfl.fl_end_form()

    def bitmapcb(self, pobj, data):
        pass


if __name__ == '__main__':
    ApplDemo = My_bitmap(len(sys.argv), sys.argv)