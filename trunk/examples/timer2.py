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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.fltimer import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *




class Fltimer2(object):
    def __init__(self, lsysargv, sysargv):
        self.TIME = 5
        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.makeforms()
        fl_show_form(self.pform1, FL_PLACE_CENTER, FL_NOBORDER, \
                        "Timer")
        fl_set_timer(self.ptim, self.TIME)
        fl_do_forms()


    def timer1_expired(self, pobj, q):
        fl_deactivate_form(self.pform1)
        fl_set_timer(self.ptim2, 10)
        fl_show_form(self.pform2, FL_PLACE_MOUSE, \
                    FL_TRANSIENT, "Q")


    def nothing(self, pobj, q):
        pass


    def continue_cb(self, pobj, q):
        fl_hide_form(self.pform2)
        fl_activate_form(self.pform1)
        fl_set_timer(self.ptim, self.TIME)
        fl_set_object_callback(self.ptim, self.nothing, 0)


    def done_cb(self, pobj, a):
        fl_finish()
        sys.exit(0)


    def makeforms(self):
        self.pform1 = fl_bgn_form(FL_UP_BOX, 400, 400)

        pobj = fl_add_button(FL_NORMAL_BUTTON, 140, 160, 120, 80, "Push Me")
        fl_set_object_callback(pobj, self.done_cb, 0)

        self.ptim = fl_add_timer(FL_VALUE_TIMER, 200, 40, 90, 50, "Time Left")
        fl_set_object_callback(self.ptim, self.timer1_expired, 0)
        fl_set_object_lcol(self.ptim, FL_BLACK)

        fl_end_form()

        self.pform2 = fl_bgn_form(FL_UP_BOX, 320, 120)

        fl_add_box(FL_NO_BOX, 160, 40, 0, 0, "You were too late")

        pobj = fl_add_button(FL_NORMAL_BUTTON, 100, 70, 120, 30, "Try Again")
        fl_set_object_callback(pobj, self.continue_cb, 0)

        self.ptim2 = fl_add_timer(FL_HIDDEN_TIMER, 0, 0, 1, 2, "")
        fl_set_object_callback(self.ptim2, self.continue_cb, 0)
        fl_end_form()





if __name__ == '__main__':
    Fltimer2(len(sys.argv), sys.argv)

