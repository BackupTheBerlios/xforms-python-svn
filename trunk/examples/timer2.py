#!/usr/bin/env python3

#  This file is part of xforms-python, and it has been ported from
#  timer2.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# A demo showing the use of timer objects.
# note there is only one xfl.fl_do_form().
#

import sys
#sys.path.append("..")
import xformslib as xfl



class Fltimer2(object):
    def __init__(self, lsysargv, sysargv):
        self.TIME = 5
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.makeforms()
        xfl.fl_show_form(self.pform1, xfl.FL_PLACE_CENTER, \
                xfl.FL_NOBORDER, "Timer")
        xfl.fl_set_timer(self.ptim, self.TIME)
        xfl.fl_do_forms()


    def timer1_expired(self, pobj, q):
        xfl.fl_deactivate_form(self.pform1)
        xfl.fl_set_timer(self.ptim2, 10)
        xfl.fl_show_form(self.pform2, xfl.FL_PLACE_MOUSE, \
                xfl.FL_TRANSIENT, "Q")


    def nothing(self, pobj, q):
        pass


    def continue_cb(self, pobj, q):
        xfl.fl_hide_form(self.pform2)
        xfl.fl_activate_form(self.pform1)
        xfl.fl_set_timer(self.ptim, self.TIME)
        xfl.fl_set_object_callback(self.ptim, self.nothing, 0)


    def done_cb(self, pobj, a):
        xfl.fl_finish()
        sys.exit(0)


    def makeforms(self):
        self.pform1 = xfl.fl_bgn_form(xfl.FL_UP_BOX, 400, 400)

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 140, 160, \
                120, 80, "Push Me")
        xfl.fl_set_object_callback(pobj, self.done_cb, 0)

        self.ptim = xfl.fl_add_timer(xfl.FL_VALUE_TIMER, 200, 40, \
                90, 50, "Time Left")
        xfl.fl_set_object_callback(self.ptim, self.timer1_expired, 0)
        xfl.fl_set_object_lcol(self.ptim, xfl.FL_BLACK)

        xfl.fl_end_form()

        self.pform2 = xfl.fl_bgn_form(xfl.FL_UP_BOX, 320, 120)

        xfl.fl_add_box(xfl.FL_NO_BOX, 160, 40, 0, 0, "You were too late")

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 100, 70, 120, 30, \
                "Try Again")
        xfl.fl_set_object_callback(pobj, self.continue_cb, 0)

        self.ptim2 = xfl.fl_add_timer(xfl.FL_HIDDEN_TIMER, 0, 0, 1, 2, "")
        xfl.fl_set_object_callback(self.ptim2, self.continue_cb, 0)
        xfl.fl_end_form()



if __name__ == '__main__':
    print ("********* timer2.py *********")
    Fltimer2(len(sys.argv), sys.argv)

