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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.xfdata import *




class Flobjpos(object):

    def __init__(self, lsysargv, sysargv):

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        pform = fl_bgn_form(FL_DOWN_BOX, 400, 200)
        self.pbut = fl_add_button(FL_NORMAL_BUTTON, 10, 60, 70, 35, "Exit")  # 140 160
        fl_set_object_resize(self.pbut, FL_RESIZE_NONE)
        pobj = fl_add_button(FL_TOUCH_BUTTON, 330, 150, 50, 30, "Move")
        fl_set_object_resize(pobj, FL_RESIZE_NONE)
        fl_set_object_gravity(pobj, FL_SouthEast, FL_SouthEast )
        fl_set_object_callback(pobj, self.move_cb, 0)   # but
        fl_end_form()

        fl_show_form(pform, FL_PLACE_MOUSE | FL_FREE_SIZE, \
                     FL_FULLBORDER, "ObjPos")

        fl_do_forms()


    def move_cb(self, pobj, data):

        dx = 8
        dy = 8
        x, y, w, h = fl_get_object_geometry(self.pbut)

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

        fl_set_object_position(self.pbut, x, y)




if __name__ == '__main__':
    Flobjpos(len(sys.argv), sys.argv)

