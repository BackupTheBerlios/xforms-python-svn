#!/usr/bin/env python3
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class Fd_valslider(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'Fd_valslider', None, 0)

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
        self.pvalslider = xfl.fl_add_valslider(xfl.FL_HOR_SLIDER, 10, 40, 290, 30, 'Horizontal way')
        xfl.fl_set_object_boxtype(self.pvalslider, xfl.FL_UP_BOX)
        xfl.fl_set_slider_bounds(self.pvalslider, 1, 25)
        xfl.fl_set_slider_value(self.pvalslider, 1)
        xfl.fl_set_slider_increment(self.pvalslider, 0.4, 0.5)
        xfl.fl_set_slider_size(self.pvalslider, 0.20)
        xfl.fl_set_slider_step(self.pvalslider, 1)
        xfl.fl_set_slider_precision(self.pvalslider, 3)
        xfl.fl_set_object_color(self.pvalslider, xfl.FL_COL1, xfl.FL_COL1)
        xfl.fl_set_object_lalign(self.pvalslider, xfl.FL_ALIGN_BOTTOM)
        xfl.fl_set_object_lstyle(self.pvalslider, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.pvalslider, xfl.FL_TINY_SIZE)
        xfl.fl_set_object_lcol(self.pvalslider, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.pvalslider, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.pvalslider, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.pvalslider, 'H', 1)
        xfl.fl_set_object_callback(self.pvalslider, self.slidercb, 4)
        xfl.fl_set_object_return(self.pvalslider, xfl.FL_RETURN_CHANGED|xfl.FL_RETURN_END)

        xfl.fl_end_form()

    def slidercb(self, pobj, data):
        pass


if __name__ == '__main__':
    print("***** fd_valslider.py *****")
    ApplDemo = Fd_valslider(len(sys.argv), sys.argv)

