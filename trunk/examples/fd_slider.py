#!/usr/bin/env python
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class My_slider(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'My_slider', None, 0)

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
        self.pslider = xfl.fl_add_slider(xfl.FL_HOR_NICE_SLIDER, 60, 50, 220, 40, 'my slider\nin the sky')
        xfl.fl_set_object_boxtype(self.pslider, xfl.FL_DOWN_BOX)
        xfl.fl_set_slider_bounds(self.pslider, 1, 15)
        xfl.fl_set_slider_value(self.pslider, 1)
        xfl.fl_set_slider_increment(self.pslider, 0.15, 0.25)
        xfl.fl_set_slider_size(self.pslider, 0.15)
        xfl.fl_set_slider_step(self.pslider, 2)
        xfl.fl_set_object_color(self.pslider, xfl.FL_DARKKHAKI, xfl.FL_AQUAMARINE)
        xfl.fl_set_object_lalign(self.pslider, xfl.FL_ALIGN_BOTTOM)
        xfl.fl_set_object_lstyle(self.pslider, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.pslider, xfl.FL_TINY_SIZE)
        xfl.fl_set_object_lcol(self.pslider, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.pslider, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.pslider, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.pslider, 'i', 1)
        xfl.fl_set_object_callback(self.pslider, self.slidecb, 0)
        xfl.fl_set_object_return(self.pslider, xfl.FL_RETURN_CHANGED|xfl.FL_RETURN_END)

        xfl.fl_end_form()

    def slidecb(self, pobj, data):
        pass


if __name__ == '__main__':
    ApplDemo = My_slider(len(sys.argv), sys.argv)