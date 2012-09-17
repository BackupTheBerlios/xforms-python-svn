#!/usr/bin/env python3
# Forms definition originally created with XForms fdesign.
# Converted by fd2python.py to be used with xforms-python.

import sys
import xformslib as xfl

class Fd_xyplot(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 'Fd_xyplot', None, 0)

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
        self.pxyplot = xfl.fl_add_xyplot(xfl.FL_SQUARE_XYPLOT, 30, 40, 260, 160, 'myxyplot')
        xfl.fl_set_object_boxtype(self.pxyplot, xfl.FL_FLAT_BOX)
        xfl.fl_set_xyplot_xgrid(self.pxyplot, xfl.FL_GRID_MAJOR)
        xfl.fl_set_xyplot_ygrid(self.pxyplot, xfl.FL_GRID_MAJOR)
        xfl.fl_set_xyplot_grid_linestyle(self.pxyplot, xfl.FL_DOTDASH)
        xfl.fl_set_object_color(self.pxyplot, xfl.FL_COL1, xfl.FL_BLACK)
        xfl.fl_set_object_lalign(self.pxyplot, xfl.FL_ALIGN_BOTTOM)
        xfl.fl_set_object_lstyle(self.pxyplot, xfl.FL_NORMAL_STYLE)
        xfl.fl_set_object_lsize(self.pxyplot, xfl.FL_TINY_SIZE)
        xfl.fl_set_object_lcol(self.pxyplot, xfl.FL_BLACK)
        xfl.fl_set_object_resize(self.pxyplot, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_gravity(self.pxyplot, xfl.FL_NoGravity, xfl.FL_NoGravity)
        xfl.fl_set_object_shortcut(self.pxyplot, 'x', 1)
        xfl.fl_set_object_callback(self.pxyplot, self.xyplot_cb, 2)

        xfl.fl_end_form()

    def xyplot_cb(self, pobj, data):
        pass


if __name__ == '__main__':
    print("***** fd_xyplot.py *****")
    ApplDemo = Fd_xyplot(len(sys.argv), sys.argv)

