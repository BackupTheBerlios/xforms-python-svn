#!/usr/bin/env python
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class My_pixmap_usedata(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'My_pixmap_usedata', None, 0)

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
        self.ppixmap = xfl.fl_add_pixmap(xfl.FL_NORMAL_PIXMAP, 40, 40, 240, 90, 'one\ndemo\npixmap')
        xfl.fl_set_object_boxtype(self.ppixmap, xfl.FL_FRAME_BOX)
        xfl.fl_set_pixmap_align(self.ppixmap, xfl.FL_ALIGN_RIGHT|xfl.FL_ALIGN_INSIDE, 3, 3)
        crab = ['28 28 6 2 ', '. c None      m white      s s_SkyBlue ', 'x c orange      m black      s s_orange ', '* c #ff72c2      m black      s s_#ff72c2 ', '+ c SteelBlue      m white      s s_SteelBlue ', 'G c black      m black      s s_black ', 'a c LightGrey      m white      s s_LightGrey ', '. . . . . . * * * * . . . . . . . . . * * * * . . . . . ', '. . . . + * x x * . . . . . . . . . . + * x x * . . . . ', '. . . + * x x * . . . . . . . . . . . . + * x x * . . . ', '. . + * x * . . . * . . . . . . . . . * . . + * x * . . ', '. . + * x * . . + * . . . . . . . . + * . . + * x * . . ', '. . + * x * . + * * . . . . . . . . + * * . + * x * . . ', '. . + * x * + * * . . . . . . . . . . + * * + * x * . . ', '. . + * x * * * . . . . . . . . . . . . + * * x x * . . ', '. . . + * x * . . + * . . . . . . + * . . + * x * . . . ', '. . . + * x . . + * . + * * . * * . + * . . + x * . . . ', '. . . . + x . . + * . + * * . * * . + * . . + x . . . . ', '. . . . + x . . . + * + * * * * * + * . . . + x . . . . ', '. . . . + * x . . + * * * * * * * * * . . + x * . . . . ', '. . . . . + * x * * * * x x x x x * * * * x * . . . . . ', '. . . . + + + * * x x x x x x x x x x x x * . . . . . . ', '. . + + * x x x x x x x x x x x x x x x x x x * x . . . ', '. + * x x a + * * x x x x x x x x x x x * * a G * x * . ', '+ * x . . . + * * x x x x x x x x x x x * * G . . . x * ', '. . . . . . + * * x x x x x x x x x x x * * . . . . . . ', '. . . . . + * * x x x x x x x x x x x x x * * . . . . . ', '. . . + * x x x * x x x x x x x x x x x * x x x * . . . ', '. . + * x a a + * * x x x x x x x x x * * a a a x * . . ', '. + * x G G G + * * x x x x x x x x x * * a G G G x * . ', '. + * G . . . + * x * x x x x x x x * x * a G . . . * . ', '. . . . . . + * x a * * * x x x * * * a x * G . . . . . ', '. . . . . + * x a G a a * * * * * a a G a x * G . . . . ', '. . . . . + x a G . G G a a a a a G G . G G x a G . . . ', '. . . . . + x a G . . . G G G G G . . . . . x a G . . . ']
        xfl.fl_set_pixmap_data(self.ppixmap, crab)
        xfl.fl_set_object_color(self.ppixmap, xfl.FL_COL1, xfl.FL_COL1)
        xfl.fl_set_object_lalign(self.ppixmap, xfl.FL_ALIGN_BOTTOM)
        xfl.fl_set_object_lstyle(self.ppixmap, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.ppixmap, xfl.FL_DEFAULT_SIZE)
        xfl.fl_set_object_lcol(self.ppixmap, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.ppixmap, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.ppixmap, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.ppixmap, 'm', 1)
        xfl.fl_set_object_callback(self.ppixmap, self.pmapcb, 0)

        xfl.fl_end_form()

    def pmapcb(self, pobj, data):
        pass


if __name__ == '__main__':
    ApplDemo = My_pixmap_usedata(len(sys.argv), sys.argv)