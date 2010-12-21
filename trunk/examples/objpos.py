#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  objpos.c XForms demo, with some adaptations and modifications.
#
#  objpos.c was written by M. Overmars and T.C. Zhao
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This is a crazy demo showing the "use" of changing
# fields in objects.
#

import sys
#sys.path.append("..")
import xformslib as xfl


class Flobjpos(object):

    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        pform = xfl.fl_bgn_form(xfl.FL_DOWN_BOX, 400, 200)
        self.pbut = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 10, 60, \
                70, 35, "Exit")  # 140 160
        xfl.fl_set_object_resize(self.pbut, xfl.FL_RESIZE_NONE)
        pobj = xfl.fl_add_button(xfl.FL_TOUCH_BUTTON, 330, 150, 50, 30, "Move")
        xfl.fl_set_object_resize(pobj, xfl.FL_RESIZE_NONE)
        xfl.fl_set_object_gravity(pobj, xfl.FL_SouthEast, xfl.FL_SouthEast )
        xfl.fl_set_object_callback(pobj, self.move_cb, 0)   # but
        xfl.fl_end_form()
        xfl.fl_show_form(pform, xfl.FL_PLACE_MOUSE | xfl.FL_FREE_SIZE, \
                 xfl.FL_FULLBORDER, "ObjPos")
        xfl.fl_do_forms()


    def move_cb(self, pobj, data):

        dx = 8
        dy = 8
        x, y, w, h = xfl.fl_get_object_geometry(self.pbut)

        xlimitup = x + w + dx
        xlimitdown = x + dx
        ylimitup = y + h + dy
        ylimitdown = y + dy
        if (xlimitdown < 0):
            dx = -dx
        if (xlimitup >= self.pbut.contents.form.contents.w):
            dx = -(dx*32)
        if (ylimitdown < 0):
            dy = -dy
        if (ylimitup >= self.pbut.contents.form.contents.h):
            dy = -(dy*16)
        x += dx
        y += dy

        xfl.fl_set_object_position(self.pbut, x, y)



if __name__ == '__main__':
    print ("********* objpos.py *********")
    Flobjpos(len(sys.argv), sys.argv)

