#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  timer2.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# A demo showing the use of timer objects.
# note there is only one fl_do_form().
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc


TIME = 5


def timer1_expired(ob, q):
    xf.fl_deactivate_form(form1)
    xf.fl_set_timer(tim2, 10)
    xf.fl_show_form(form2, xfc.FL_PLACE_MOUSE, \
                    xfc.FL_TRANSIENT, "Q")


def nothing(ob, q):
    pass



def continue_cb(ob, q):
    xf.fl_hide_form(form2)
    xf.fl_activate_form(form1)
    xf.fl_set_timer(tim, TIME)
    xf.fl_set_object_callback(tim, nothing, 0)



def done_cb(ob, a):
    xf.fl_finish()
    sys.exit(0)



def makeforms():
    global form1, tim, form2, tim2

    form1 = xf.fl_bgn_form(xfc.FL_UP_BOX, 400, 400)

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 140, 160, 120, 80, "Push Me")
    xf.fl_set_object_callback(obj, done_cb, 0)

    tim = xf.fl_add_timer(xfc.FL_VALUE_TIMER, 200, 40, 90, 50, "Time Left")
    xf.fl_set_object_callback(tim, timer1_expired, 0)
    xf.fl_set_object_lcol(tim, xfc.FL_BLACK)

    xf.fl_end_form()

    form2 = xf.fl_bgn_form(xfc.FL_UP_BOX, 320, 120)

    xf.fl_add_box(xfc.FL_NO_BOX, 160, 40, 0, 0, "You were too late")

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 100, 70, 120, 30, "Try Again")
    xf.fl_set_object_callback(obj, continue_cb, 0)

    tim2 = xf.fl_add_timer(xfc.FL_HIDDEN_TIMER, 0, 0, 1, 2, "")
    xf.fl_set_object_callback(tim2, continue_cb, 0)
    xf.fl_end_form()



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    makeforms()
    xf.fl_show_form(form1, xfc.FL_PLACE_CENTER, xfc.FL_NOBORDER, "Timer")
    xf.fl_set_timer(tim, TIME)
    xf.fl_do_forms()
    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

