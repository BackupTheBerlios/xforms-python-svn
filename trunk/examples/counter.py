#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  counter.c XForms demo, with some adaptations.
#
#  counter.c was written by M. Overmars and T.C. Zhao.
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This is an example of the use of counters.
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc




co = [0, 0, 0]


def color_change(ob, data):

    c = [0, 0, 0]

    for i in range(0, 3):
        c[i] = xf.fl_get_counter_value(co[i])

    xf.fl_mapcolor(xfc.FL_FREE_COL1, c[0], c[1], c[2])
    xf.fl_redraw_object(result)



def create_form_form():
    global result, co, form

    form = xf.fl_bgn_form(xfc.FL_NO_BOX, 480, 200)

    obj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 480, 200, "")

    result = xf.fl_add_box(xfc.FL_DOWN_BOX, 310, 20, 150, 160, "")
    xf.fl_set_object_dblbuffer(result, 1)

    co[0] = xf.fl_add_counter(xfc.FL_NORMAL_COUNTER, 20, 20, 270, 30, \
                              "")
    xf.fl_set_object_color(co[0], xfc.FL_INDIANRED, xfc.FL_RED)
    xf.fl_set_object_callback(co[0], color_change, 0)

    co[1] = xf.fl_add_counter(xfc.FL_NORMAL_COUNTER, 20, 60, 270, 30, \
                              "")
    xf.fl_set_object_color(co[1], xfc.FL_PALEGREEN, xfc.FL_GREEN)
    xf.fl_set_object_callback(co[1], color_change, 0)

    co[2] = xf.fl_add_counter(xfc.FL_NORMAL_COUNTER, 20, 100, 270, 30, \
                              "")
    xf.fl_set_object_color(co[2], xfc.FL_SLATEBLUE, xfc.FL_BLUE)
    xf.fl_set_object_callback(co[2], color_change, 0)

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 100, 150, 110, 30, "Exit")

    xf.fl_end_form()



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    create_form_form()
    xf.fl_set_object_color(result, xfc.FL_FREE_COL1, xfc.FL_FREE_COL1)

    for i in range(0, 3):
        xf.fl_set_counter_bounds(co[i], 0.0, 255.0)
        xf.fl_set_counter_step(co[i], 1.0, 10.0)
        xf.fl_set_counter_precision(co[i], 0)
        xf.fl_set_counter_return(co[i], 1)

    xf.fl_call_object_callback(co[0])

    xf.fl_show_form(form, xfc.FL_PLACE_CENTER, xfc.FL_TRANSIENT, \
                    "Counter")

    xf.fl_do_forms()

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

