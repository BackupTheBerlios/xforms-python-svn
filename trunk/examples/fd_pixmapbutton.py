#!/usr/bin/env python
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class Fd_pixmapbutton(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'Fd_pixmapbutton', None, 0)

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
        self.ppxmbutton = xfl.fl_add_pixmapbutton(xfl.FL_TOUCH_BUTTON, 40, 50, 230, 90, 'mypixmapbtn')
        xfl.fl_set_object_boxtype(self.ppxmbutton, xfl.FL_ROUNDED_BOX)
        xfl.fl_set_button_mouse_buttons(self.ppxmbutton, 29)
        xfl.fl_set_pixmapbutton_align(self.ppxmbutton, xfl.FL_ALIGN_TOP|xfl.FL_ALIGN_INSIDE, 3, 3)
        xfl.fl_set_object_helper(self.ppxmbutton, 'my image')
        xfl.fl_set_pixmapbutton_file(self.ppxmbutton, './crab45.xpm')
        xfl.fl_set_pixmapbutton_focus_file(self.ppxmbutton, './crab.xpm')
        xfl.fl_set_object_color(self.ppxmbutton, xfl.FL_COL1, xfl.FL_COL1)
        xfl.fl_set_object_lalign(self.ppxmbutton, xfl.FL_ALIGN_BOTTOM)
        xfl.fl_set_object_lstyle(self.ppxmbutton, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.ppxmbutton, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.ppxmbutton, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.ppxmbutton, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.ppxmbutton, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.ppxmbutton, 'b', 1)
        xfl.fl_set_object_callback(self.ppxmbutton, self.buttoncb, 5)
        xfl.fl_set_object_return(self.ppxmbutton, xfl.FL_RETURN_CHANGED)

        xfl.fl_end_form()

    def buttoncb(self, pobj, data):
        pass


if __name__ == '__main__':
    print("***** fd_pixmapbutton.py *****")
    ApplDemo = Fd_pixmapbutton(len(sys.argv), sys.argv)

