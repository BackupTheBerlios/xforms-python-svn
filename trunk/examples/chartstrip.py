#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  chartstrip.c XForms demo, with some adaptations.
#
#  chartstrip.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# A demo of a moving chart
#

import sys, math
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc


func = 1
x = 0.0
step = 0.15



def set_function(obj, arg):
    global func
    func = arg
    xf.fl_clear_chart(pchartobj)
    x = 0.0


def set_step(obj, arg):
    global step
    step = xf.fl_get_slider_value(pstepobj)



def next_step():
    global x
    res = 0.0

    if func == 1:
        res = math.sin(x)
    elif func == 2:
        res = math.sin(2 * x) * math.cos(x)
    elif func == 3:
        res = math.sin(2 * x) + math.cos(x)
    elif func == 4:
        res = math.sin(3 * x) + math.cos(x)
    elif func == 5:
        res = math.sin(x) * math.sin(x) + math.cos(x)
    elif func == 6:
        res = math.sin(x) * math.sin(x) * math.sin(x)

    x += 0.2 * step
    return res



def idle_cb(xev, d):
    xf.fl_insert_chart_value(pchartobj, 1, next_step(), "", 1)
    return 0



def add_value(xev, a):
    xf.fl_insert_chart_value(pchartobj, 1, next_step(), "", 1)



def main(lsysargv, sysargv):

    xf.fl_flip_yorigin()
    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    create_form_form()
    xf.fl_set_chart_bounds(pchartobj, -1.5, 1.5)
    xf.fl_set_chart_maxnumb(pchartobj, 80)
    xf.fl_set_chart_autosize(pchartobj, 0)
    xf.fl_set_button(psinobj, 1)
    xf.fl_set_slider_value(pstepobj, 0.5)
    xf.fl_set_slider_bounds(pstepobj, 0.0, 1.0)

    xf.fl_show_form(pform, xfc.FL_PLACE_CENTER | xfc.FL_FREE_SIZE, \
                    xfc.FL_TRANSIENT, "StripChart")

    while True:
        xf.fl_insert_chart_value(pchartobj, 1, next_step(), "", 1)
        pobj = xf.fl_check_forms()
        if xf.fl_is_same_object(pobj, pexitbut):
            break

    xf.fl_finish()
    return 0



def create_form_form():
    global pform, pchartobj, pstepobj, psinobj, pexitbut

    pform = xf.fl_bgn_form(xfc.FL_NO_BOX, 490, 320)

    xf.fl_add_box(xfc.FL_BORDER_BOX, 0, 0, 490, 320, "")

    pchartobj = xf.fl_add_chart(xfc.FL_LINE_CHART, 20, 160, 390, 140, "")
    xf.fl_set_object_dblbuffer(pchartobj, 1)

    xf.fl_bgn_group()

    psinobj = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 30, 120, 170, 30,
                                    "sin(x)")
    xf.fl_set_object_boxtype(psinobj, xfc.FL_BORDER_BOX)
    xf.fl_set_object_callback(psinobj, set_function, 1)

    pobj = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 30, 90, 170, 30,
                                 "sin(2x)*cos(x)")
    xf.fl_set_object_boxtype(pobj, xfc.FL_BORDER_BOX)
    xf.fl_set_object_callback(pobj, set_function, 2)

    pobj = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 30, 60, 170, 30,
                                 "sin(2x)+cos(x)")
    xf.fl_set_object_boxtype(pobj, xfc.FL_BORDER_BOX)
    xf.fl_set_object_callback(pobj, set_function, 3)

    pobj = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 240, 120, 160, 30,
                                 "sin(3x)+cos(x)")
    xf.fl_set_object_boxtype(pobj, xfc.FL_BORDER_BOX)
    xf.fl_set_object_callback(pobj, set_function, 4)

    pobj = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 240, 90, 160, 30,
                                 "sin(x)^2 + cos(x)")
    xf.fl_set_object_boxtype(pobj, xfc.FL_BORDER_BOX)
    xf.fl_set_object_callback(pobj, set_function, 5)

    pobj = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 240, 60, 160, 30,
                                 "sin(x)^3")
    xf.fl_set_object_boxtype(pobj, xfc.FL_BORDER_BOX)
    xf.fl_set_object_callback(pobj, set_function, 6)

    xf.fl_end_group()

    pexitbut = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 150, 20, 140, 30, \
                                "Exit")
    xf.fl_set_object_boxtype(pexitbut, xfc.FL_BORDER_BOX)

    pstepobj = xf.fl_add_valslider(xfc.FL_VERT_SLIDER, 430, 20, 40, 280, "")
    xf.fl_set_object_boxtype(pstepobj, xfc.FL_BORDER_BOX)
    xf.fl_set_object_callback(pstepobj, set_step, 0)

    xf.fl_end_form()




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

