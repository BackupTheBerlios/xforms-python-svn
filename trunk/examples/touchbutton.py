#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  touchbutton.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a touch buttons.
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc


val = 0


def main(lsysargv, sysarg):
    global pvalobj

    xf.fl_initialize(lsysargv, sysarg, "FormDemo", 0, 0)

    pform = xf.fl_bgn_form(xfc.FL_UP_BOX, 360, 140)

    pobj = xf.fl_add_button(xfc.FL_TOUCH_BUTTON, 50, 30, 40, 30, "@<<")
    xf.fl_set_object_boxtype(pobj, xfc.FL_FRAME_BOX)
    xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_INDIANRED)
    xf.fl_set_object_callback(pobj, show_val, -5)
    xf.fl_set_button_shortcut(pobj, "1", 0)

    pobj = xf.fl_add_button(xfc.FL_TOUCH_BUTTON, 90, 30, 40, 30, "@<")
    xf.fl_set_object_boxtype(pobj, xfc.FL_FRAME_BOX)
    xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_INDIANRED)
    xf.fl_set_object_callback(pobj, show_val, -1)
    xf.fl_set_button_shortcut(pobj, "2",  0)

    pvalobj = xf.fl_add_box(xfc.FL_BORDER_BOX, 130, 30, 100, 30, "")
    xf.fl_set_object_color(pvalobj, xfc.FL_LEFT_BCOL, xfc.FL_LEFT_BCOL)

    pobj = xf.fl_add_button(xfc.FL_TOUCH_BUTTON, 230, 30, 40, 30, "@>")
    xf.fl_set_object_boxtype(pobj, xfc.FL_FRAME_BOX)
    xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_INDIANRED)
    xf.fl_set_object_callback(pobj, show_val, 1)
    xf.fl_set_button_shortcut(pobj, "3", 0)

    pobj = xf.fl_add_button(xfc.FL_TOUCH_BUTTON, 270, 30, 40, 30, "@>>")
    xf.fl_set_object_boxtype(pobj, xfc.FL_FRAME_BOX)
    xf.fl_set_object_callback(pobj, show_val, 5)
    xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_INDIANRED)
    xf.fl_set_button_shortcut(pobj, "4", 0)

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 220, 90, 100, 30, "Exit")

    xf.fl_end_form()

    xf.fl_show_form(pform, xfc.FL_PLACE_CENTER, xfc.FL_NOBORDER, "Touch Buttons")

    xf.fl_do_forms()
    xf.fl_finish()

    return 0



def show_val(pob, delta):
    global val 

    val += delta
    strng = "%d" % val
    xf.fl_set_object_label(pvalobj, strng)



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

