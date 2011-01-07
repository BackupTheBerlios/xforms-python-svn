#!/usr/bin/env python
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class Fd_bitmapbutton(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'Fd_bitmapbutton', None, 0)

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
        self.pbmbutton = xfl.fl_add_bitmapbutton(xfl.FL_NORMAL_BUTTON, 50, 40, 220, 90, 'xbmbutton')
        xfl.fl_set_object_boxtype(self.pbmbutton, xfl.FL_UP_BOX)
        xfl.fl_set_button_mouse_buttons(self.pbmbutton, 27)
        xfl.fl_set_bitmapbutton_file(self.pbmbutton, '././bm1.xbm')
        xfl.fl_set_object_color(self.pbmbutton, xfl.FL_COL1, xfl.FL_BLUE)
        xfl.fl_set_object_lalign(self.pbmbutton, xfl.FL_ALIGN_BOTTOM)
        xfl.fl_set_object_lstyle(self.pbmbutton, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.pbmbutton, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.pbmbutton, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.pbmbutton, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.pbmbutton, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.pbmbutton, 'm', 1)
        xfl.fl_set_object_callback(self.pbmbutton, self.buttoncb, 999)

        xfl.fl_end_form()

    def buttoncb(self, pobj, data):
        pass


if __name__ == '__main__':
    print("***** fd_bitmapbutton.py *****")
    ApplDemo = Fd_bitmapbutton(len(sys.argv), sys.argv)

