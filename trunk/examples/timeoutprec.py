#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  timeoutprec.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Test the accuracy of timeouts
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



# Forms and Objects

class FD_form(object):
    form = None
    timer_id = 0
    vdata = None
    ldata = 0
    timer = None
    restart = None
    report = None


def exit_cb(pobj, data):
    xf.fl_finish()
    sys.exit(0)



# timer expired

def timer_cb(idt, data):

    timerval =  1.0e-3 * fd_form.ldata

    fd_form.timer_id = 0

    end_sec, end_usec = xf.fl_gettime()

    df = end_sec.value - start_sec.value + 1.0e-6 * (end_usec.value - start_usec.value)

    buf = "Timeout: %.3f  Actual: %.3f  DeltaE: %.3f" % \
          (timerval, df, df - timerval)

    xf.fl_set_object_label(fd_form.report, buf)



def start_timer(pobj, data):
    global start_sec, start_usec

    if fd_form.timer_id:
        xf.fl_remove_timeout(fd_form.timer_id)

    fd_form.ldata += 200
    buf = "Timer accuracy testing %.3f sec ..." % float(fd_form.ldata * 0.001)
    xf.fl_set_object_label(fd_form.report, buf)
    start_sec, start_usec = xf.fl_gettime()
    fd_form.timer_id = xf.fl_add_timeout(fd_form.ldata, timer_cb, 0)



def main(lsysargv, sysargv):
    global fd_form

    xf.fl_initialize(lsysargv, sysargv, 0, 0, 0)
    fd_form = create_form_form()

    # fill-in form initialization code

    fd_form.ldata = 800
    start_timer(fd_form.report, 0)

    # show the first form

    xf.fl_show_form(fd_form.form, xfc.FL_PLACE_CENTER, \
                    xfc.FL_FULLBORDER, "Timeout precision")
    xf.fl_do_forms()

    return 0




def create_form_form():

    fdui = FD_form()

    fdui.form = xf.fl_bgn_form(xfc.FL_NO_BOX, 320, 130)

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 320, 130, "")

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 210, 80, 90, 35, "Done")
    xf.fl_set_object_callback(pobj, exit_cb, 0)

    fdui.restart = xf.fl_add_button(xfc.FL_TOUCH_BUTTON, 110, 80, \
                                    90, 35, "Restart")
    xf.fl_set_object_callback(fdui.restart, start_timer, 0)

    fdui.report = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 10, 20, 290, 50,"")

    xf.fl_end_form()

    return fdui




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

