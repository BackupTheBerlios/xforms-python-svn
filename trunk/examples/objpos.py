#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  objpos.c XForms demo, with some adaptations.
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
from xformslib import library as xf
from xformslib import xfdata as xfc



def move_cb(ob, data):

    dx = 8
    dy = 8

    #xf.fl_get_object_geometry(but, x, y, w, h)
    x, y, w, h = xf.fl_get_object_geometry(but)

    xlimitup = x.value + w.value + dx
    xlimitdown = x.value + dx
    ylimitup = y.value + h.value + dy
    ylimitdown = y.value + dy
    if (xlimitdown < 0):
        dx = -dx
    if (xlimitup >= but[0].form[0].w):
        dx = -(dx*32)
    if (ylimitdown < 0):
        dy = -dy
    if (ylimitup >= but[0].form[0].h):
        dy = -(dy*16)
    x.value += dx
    y.value += dy

    xf.fl_set_object_position(but, x.value, y.value)
    #xf.fl_set_object_position(but, x, y)




def main(lsysargv, sysargv):
    global but

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    form = xf.fl_bgn_form(xfc.FL_DOWN_BOX, 400, 200)
    but = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 10, 60, 70, 35, "Exit")  # 140 160
    xf.fl_set_object_resize(but, xfc.FL_RESIZE_NONE)
    obj = xf.fl_add_button(xfc.FL_TOUCH_BUTTON, 330, 150, 50, 30, "Move")
    xf.fl_set_object_resize(obj, xfc.FL_RESIZE_NONE)
    xf.fl_set_object_gravity(obj, xfc.FL_SouthEast, xfc.FL_SouthEast )
    xf.fl_set_object_callback(obj,move_cb, 0)   # but
    xf.fl_end_form()

    xf.fl_show_form(form, xfc.FL_PLACE_MOUSE | xfc.FL_FREE_SIZE, \
                    xfc.FL_FULLBORDER, "ObjPos")

    xf.fl_do_forms()

    return 0


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
