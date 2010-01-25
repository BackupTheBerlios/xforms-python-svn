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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.fltimer import *
from xformslib.flmisc import *
from xformslib.xfdata import *



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

        fl_initialize(lsysargv, sysargv, 0, 0, 0)
        self.fdform0 = self.create_form_form0()
        # fill-in form initialization code
        self.fdform0.ldata = 2800.0
        self.start_timer(self.fdform0.timer, 0)
        # show the first form
        fl_show_form(self.fdform0.form0, FL_PLACE_CENTER, FL_FULLBORDER,
                        "Timer object precision")
        fl_do_forms()


    def exit_cb(self, obj, data):
        fl_finish()
        sys.exit(0)


    # timer expired
    def timer_cb(self, pobj, data):
        timerval = self.fdform0.ldata * 0.001
        end_sec, end_usec = fl_gettime()
        df = end_sec - self.start_sec + \
                (end_usec - self.start_usec) * 1.0e-6
        buf = "Timeout: %.3f  Actual: %.3f  DeltaE: %.3f" % \
                (timerval, df, df - timerval)
        fl_set_object_label(self.fdform0.report, buf)


    def start_timer(self, pobj, data):
        self.fdform0.ldata += 200.0
        numldata = self.fdform0.ldata / 1000
        buf = "Timer accuracy testing %.3f sec ..." % numldata
        fl_set_object_label(self.fdform0.report, buf)
        self.start_sec, self.start_usec = fl_gettime()
        fl_set_timer(self.fdform0.timer, numldata)


    # Form definition
    def create_form_form0(self):

        fdui = FD_form0()
        fdui.form0 = fl_bgn_form(FL_NO_BOX, 320, 130)

        pobj = fl_add_box(FL_UP_BOX, 0, 0, 320, 130, "")
        pobj = fl_add_button(FL_NORMAL_BUTTON, 210, 80, 90, 35,
                           "Done")
        fl_set_object_callback(pobj, self.exit_cb, 0)

        fdui.restart = fl_add_button(FL_TOUCH_BUTTON, 110, 80, 90, 35,
                                      "Restart")
        fl_set_object_callback(fdui.restart, self.start_timer, 0)

        fdui.timer = fl_add_timer(FL_HIDDEN_TIMER, 10, 40, 100, 40,
                                  "Timer")
        fl_set_object_callback(fdui.timer, self.timer_cb, 0)

        fdui.report = fl_add_text(FL_NORMAL_TEXT, 10, 20, 290, 50, "")

        fl_end_form()

        return fdui




if __name__ == '__main__':
    Fltimerprec(len(sys.argv), sys.argv)

