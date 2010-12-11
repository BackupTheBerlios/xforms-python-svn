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
import xformslib as xfl



# Forms and Objects
class FD_form0(object):
    form0 = None
    vdata = None
    ldata = None
    timer = None
    restart = None
    report = None


class Fltimerprec(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.fdform0 = self.create_form_form0()
        # fill-in form initialization code
        self.fdform0.ldata = 2800.0
        self.start_timer(self.fdform0.timer, 0)
        # show the first form
        xfl.fl_show_form(self.fdform0.form0, xfl.FL_PLACE_CENTER, \
                xfl.FL_FULLBORDER, "Timer object precision")
        xfl.fl_do_forms()


    def exit_cb(self, obj, data):
        xfl.fl_finish()
        sys.exit(0)


    # timer expired
    def timer_cb(self, pobj, data):
        timerval = self.fdform0.ldata * 0.001
        end_sec, end_usec = xfl.fl_gettime()
        df = end_sec - self.start_sec + \
                (end_usec - self.start_usec) * 1.0e-6
        buf = "Timeout: %.3f  Actual: %.3f  DeltaE: %.3f" % \
                (timerval, df, df - timerval)
        xfl.fl_set_object_label(self.fdform0.report, buf)


    def start_timer(self, pobj, data):
        self.fdform0.ldata += 200.0
        numldata = self.fdform0.ldata / 1000
        buf = "Timer accuracy testing %.3f sec ..." % numldata
        xfl.fl_set_object_label(self.fdform0.report, buf)
        self.start_sec, self.start_usec = xfl.fl_gettime()
        xfl.fl_set_timer(self.fdform0.timer, numldata)


    # Form definition
    def create_form_form0(self):

        fdui = FD_form0()
        fdui.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 320, 130)

        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 320, 130, "")
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 210, 80, 90, 35,
                "Done")
        xfl.fl_set_object_callback(pobj, self.exit_cb, 0)
        fdui.restart = xfl.fl_add_button(xfl.FL_TOUCH_BUTTON, 110, 80, \
                90, 35, "Restart")
        xfl.fl_set_object_callback(fdui.restart, self.start_timer, 0)
        fdui.timer = xfl.fl_add_timer(xfl.FL_HIDDEN_TIMER, 10, 40, 100, 40, \
                "Timer")
        xfl.fl_set_object_callback(fdui.timer, self.timer_cb, 0)
        fdui.report = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 10, 20, 290, 50, "")

        xfl.fl_end_form()

        return fdui



if __name__ == '__main__':
    print ("********* timerprec.py *********")
    Fltimerprec(len(sys.argv), sys.argv)

