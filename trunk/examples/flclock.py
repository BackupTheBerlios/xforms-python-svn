#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  flclock.c XForms demo, with some adaptations.
#
#  flclock.c was written by M. Overmars and T.C. Zhao.
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Built-in xforms clock
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc


fclock = None


def exit_cb(ob, q):
    xf.fl_finish()
    sys.exit(0)


def create_form_clock():
    global fclock

    if fclock:
        return

    fclock = xf.fl_bgn_form(xfc.FL_NO_BOX, 500, 350)
    obj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 500, 350, "")

    obj = xf.fl_add_clock(xfc.FL_DIGITAL_CLOCK, 185, 20, 150, 35, "")
    xf.fl_set_object_boxtype(obj, xfc.FL_ROUNDED_BOX)
    xf.fl_set_object_color(obj, xfc.FL_COL1, xfc.FL_BLACK)
    xf.fl_set_object_lsize(obj, xfc.FL_MEDIUM_SIZE)
    xf.fl_set_object_lstyle(obj, xfc.FL_BOLD_STYLE)

    obj = xf.fl_add_clock(xfc.FL_ANALOG_CLOCK, 30, 70, 220, 200, "")
    xf.fl_set_object_boxtype(obj, xfc.FL_UP_BOX)

    obj = xf.fl_add_clock(xfc.FL_ANALOG_CLOCK, 260, 70, 220, 200, "")
    xf.fl_set_object_boxtype(obj, xfc.FL_OVAL3D_UPBOX)

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 375, 300, 110, 35, "Exit")
    xf.fl_set_object_callback(obj, exit_cb, 0)

    xf.fl_end_form()

    xf.fl_scale_form(fclock, 0.7, 0.7)



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0,  0)

    create_form_clock()
    xf.fl_show_form(fclock, xfc.FL_PLACE_CENTER, xfc.FL_TRANSIENT, "clocks")

    xf.fl_do_forms()
    xf.fl_finish()
    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
