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
import xformslib as xfl



# Forms and Objects
class FD_form(object):
    form = None
    timer_id = 0
    vdata = None
    ldata = 0
    timer = None
    restart = None
    report = None


class Fltimeoutprec(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.fd_form = self.create_form_form()
        # fill-in form initialization code
        self.fd_form.ldata = 800
        self.start_timer(self.fd_form.report, 0)
        # show the first form
        xfl.fl_show_form(self.fd_form.form, xfl.FL_PLACE_CENTER, \
                xfl.FL_FULLBORDER, "Timeout precision")
        xfl.fl_do_forms()


    def exit_cb(self, pobj, data):
        xfl.fl_finish()
        sys.exit(0)


    # timer expired
    def timer_cb(self, idt, data):
        timerval =  1.0e-3 * self.fd_form.ldata
        self.fd_form.timer_id = 0
        end_sec, end_usec = xfl.fl_gettime()
        df = end_sec - self.start_sec + 1.0e-6 * (end_usec - self.start_usec)
        buf = "Timeout: %.3f  Actual: %.3f  DeltaE: %.3f" % \
                (timerval, df, df - timerval)
        xfl.fl_set_object_label(self.fd_form.report, buf)


    def start_timer(self, pobj, data):
        if self.fd_form.timer_id:
            xfl.fl_remove_timeout(self.fd_form.timer_id)
        self.fd_form.ldata += 200
        buf = "Timer accuracy testing %.3f sec ..." % \
                float(self.fd_form.ldata * 0.001)
        xfl.fl_set_object_label(self.fd_form.report, buf)
        self.start_sec, self.start_usec = xfl.fl_gettime()
        self.fd_form.timer_id = xfl.fl_add_timeout(self.fd_form.ldata, \
                self.timer_cb, 0)


    def create_form_form(self):
        fdui = FD_form()
        fdui.form = xfl.fl_bgn_form(xfl.FL_NO_BOX, 320, 130)
        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 320, 130, "")
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 210, 80, 90, 35, "Done")
        xfl.fl_set_object_callback(pobj, self.exit_cb, 0)
        fdui.restart = xfl.fl_add_button(xfl.FL_TOUCH_BUTTON, 110, 80, \
                90, 35, "Restart")
        xfl.fl_set_object_callback(fdui.restart, self.start_timer, 0)
        fdui.report = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 10, 20, 290, 50,"")
        xfl.fl_end_form()
        return fdui



if __name__ == '__main__':
    print ("********* timeoutprec.py *********")
    Fltimeoutprec(len(sys.argv), sys.argv)

