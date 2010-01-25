#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  timer.c XForms demo, with some adaptations.
#
#  timer.c was written by T.C. Zhao and M. Overmars (1997)
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# timer routine tester
#

import sys
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flmisc import *
from xformslib.flbutton import *
from xformslib.fltimer import *
from xformslib.flgoodies import *
from xformslib.xfdata import *



# Forms and Objects

class FD_timerform(object):
    timerform = None
    vdata = None
    ldata = None
    timer = None
    down = None



class Fltimer(object):
    def __init__(self, lsysargv, sysargv):

        self.T = 20
        fl_set_border_width(-2)

        fl_initialize(lsysargv, sysargv, "", 0, 0)
        self.fd_timerform = self.create_form_timerform()

        # fill-in form initialization code
        fl_set_timer(self.fd_timerform.timer, self.T)
        fl_set_button(self.fd_timerform.down, 1)

        # show the first form
        fl_show_form(self.fd_timerform.timerform, FL_PLACE_CENTER,
                     FL_FULLBORDER, "timerform")
        fl_do_forms()


    # callbacks for form timer form
    def suspend_resume(self, pobj, data):
        if data:
            fl_resume_timer(self.fd_timerform.timer)
        else:
            fl_suspend_timer(self.fd_timerform.timer)


    def reset(self, pobj, data):
        fl_set_timer(self.fd_timerform.timer, self.T)


    def timer_direction(self, pobj, data):
        fl_set_timer_countup(self.fd_timerform.timer, data)


    def expired(self, pobj, data):
        if fl_show_question("Expired!\n\nQuit?", 0) == 1:
            fl_finish()
            sys.exit(0)
        else:
            fl_set_timer(self.fd_timerform.timer, self.T)


    def create_form_timerform(self):
        fdui = FD_timerform()
        fdui.timerform = fl_bgn_form(FL_NO_BOX, 290, 210)
        fl_add_box(FL_UP_BOX, 0, 0, 290, 210, "")
        fl_add_frame(FL_UP_FRAME, 0, 0, 290, 94, "")
        fl_add_frame(FL_UP_FRAME, 0, 100, 330, 190, "")
        fl_add_button(FL_NORMAL_BUTTON, 100, 170, 80, 30, "Done")
        fdui.timer = fl_add_timer(FL_VALUE_TIMER, 20, 30, 
                                     180, 40, "Timer")
        fl_set_object_boxtype(fdui.timer, FL_UP_BOX)
        fl_set_object_lsize(fdui.timer, FL_MEDIUM_SIZE)
        fl_set_object_lalign(fdui.timer, FL_ALIGN_TOP)
        fl_set_object_lstyle(fdui.timer, FL_TIMES_STYLE)
        fl_set_object_callback(fdui.timer, self.expired, 0)
        pobj = fl_add_button(FL_NORMAL_BUTTON, 20, 120, 80, 30, \
                                "Suspend")
        fl_set_object_callback(pobj, self.suspend_resume, 0)
        pobj = fl_add_button(FL_NORMAL_BUTTON, 100, 120, 80, 30, \
                                "Resume")
        fl_set_object_callback(pobj, self.suspend_resume, 1)
        pobj = fl_add_button(FL_NORMAL_BUTTON, 180, 120, 80, 30, \
                                "Reset")
        fl_set_object_callback(pobj, self.reset, 0)
        fdui.down = fl_add_checkbutton(FL_RADIO_BUTTON, 210, 20, 
                                          70, 30, "Down")
        fl_set_object_shortcut(fdui.down, "D#D", 1)
        fl_set_object_callback(fdui.down, self.timer_direction, 0)
        fdui.down = fl_add_checkbutton(FL_RADIO_BUTTON, 210, 50, \
                                          70, 30, "Up")
        fl_set_object_shortcut(fdui.down, "U#U", 1 )
        fl_set_object_callback(fdui.down, self.timer_direction, 1)
        fl_end_form()
        return fdui




if __name__ == '__main__':
    Fltimer(len(sys.argv), sys.argv)

