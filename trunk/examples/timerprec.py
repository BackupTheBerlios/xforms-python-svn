#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  timerprec.c XForms demo, with some adaptations.
#
#  timerprec.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Test the accuracy of timer
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc


# Forms and Objects
class FD_form0(object):
    form0 = None
    vdata = None
    ldata = None
    timer = None
    restart = None
    report = None



def exit_cb(ob, data):
    xf.fl_finish()
    sys.exit(0)


# timer expired

def timer_cb(ob, data):
    timerval = fdform0.ldata * 0.001
    end_sec, end_usec = xf.fl_gettime()
    df = end_sec.value - start_sec.value + \
        (end_usec.value - start_usec.value) * 1.0e-6
    buf = "Timeout: %.3f  Actual: %.3f  DeltaE: %.3f" % \
          (timerval, df, df - timerval)
    xf.fl_set_object_label(fdform0.report, buf)


def start_timer(ob, data):
    global start_sec, start_usec

    fdform0.ldata += 200.0
    numldata = fdform0.ldata / 1000
    buf = "Timer accuracy testing %.3f sec ..." % numldata
    xf.fl_set_object_label(fdform0.report, buf)
    start_sec, start_usec = xf.fl_gettime()
    xf.fl_set_timer(fdform0.timer, numldata)



def main(lsysargv, sysargv):
    global fdform0

    xf.fl_initialize(lsysargv, sysargv, 0, 0, 0)
    fdform0 = create_form_form0()
    # fill-in form initialization code
    fdform0.ldata = 2800.0
    start_timer(fdform0.timer, 0)
    # show the first form
    xf.fl_show_form(fdform0.form0, xfc.FL_PLACE_CENTER, xfc.FL_FULLBORDER,
                    "Timer object precision")
    xf.fl_do_forms()
    return 0



# Form definition file

def create_form_form0():
    #global fdui

    fdui = FD_form0()
    fdui.form0 = xf.fl_bgn_form(xfc.FL_NO_BOX, 320, 130)
    obj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 320, 130, "")
    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 210, 80, 90, 35,
                           "Done")
    xf.fl_set_object_callback(obj, exit_cb, 0)
    fdui.restart = xf.fl_add_button(xfc.FL_TOUCH_BUTTON, 110, 80, 90, 35,
                              "Restart")
    xf.fl_set_object_callback(fdui.restart, start_timer, 0)
    fdui.timer = xf.fl_add_timer(xfc.FL_HIDDEN_TIMER, 10, 40, 100, 40,
                              "Timer")
    xf.fl_set_object_callback(fdui.timer, timer_cb, 0)
    fdui.report = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 10, 20, 290, 50, "")
    xf.fl_end_form()
    return fdui



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

