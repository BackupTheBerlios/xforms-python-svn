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
import xformslib as xfl



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
        xfl.fl_set_border_width(-2)
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.fd_timerform = self.create_form_timerform()
        # fill-in form initialization code
        xfl.fl_set_timer(self.fd_timerform.timer, self.T)
        xfl.fl_set_button(self.fd_timerform.down, 1)
        # show the first form
        xfl.fl_show_form(self.fd_timerform.timerform, xfl.FL_PLACE_CENTER, \
                xfl.FL_FULLBORDER, "timerform")
        xfl.fl_do_forms()


    # callbacks for form timer form
    def suspend_resume(self, pobj, data):
        if data:
            xfl.fl_resume_timer(self.fd_timerform.timer)
        else:
            xfl.fl_suspend_timer(self.fd_timerform.timer)


    def reset(self, pobj, data):
        xfl.fl_set_timer(self.fd_timerform.timer, self.T)


    def timer_direction(self, pobj, data):
        xfl.fl_set_timer_countup(self.fd_timerform.timer, data)


    def expired(self, pobj, data):
        if xfl.fl_show_question("Expired!\n\nQuit?", 0) == 1:
            xfl.fl_finish()
            sys.exit(0)
        else:
            xfl.fl_set_timer(self.fd_timerform.timer, self.T)


    def create_form_timerform(self):
        fdui = FD_timerform()
        fdui.timerform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 290, 210)
        xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 290, 210, "")
        xfl.fl_add_frame(xfl.FL_UP_FRAME, 0, 0, 290, 94, "")
        xfl.fl_add_frame(xfl.FL_UP_FRAME, 0, 100, 330, 190, "")
        xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 100, 170, 80, 30, "Done")
        fdui.timer = xfl.fl_add_timer(xfl.FL_VALUE_TIMER, 20, 30, 
                180, 40, "Timer")
        xfl.fl_set_object_boxtype(fdui.timer, xfl.FL_UP_BOX)
        xfl.fl_set_object_lsize(fdui.timer, xfl.FL_MEDIUM_SIZE)
        xfl.fl_set_object_lalign(fdui.timer, xfl.FL_ALIGN_TOP)
        xfl.fl_set_object_lstyle(fdui.timer, xfl.FL_TIMES_STYLE)
        xfl.fl_set_object_callback(fdui.timer, self.expired, 0)
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 20, 120, 80, 30, \
                "Suspend")
        xfl.fl_set_object_callback(pobj, self.suspend_resume, 0)
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 100, 120, 80, 30, \
                "Resume")
        xfl.fl_set_object_callback(pobj, self.suspend_resume, 1)
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 180, 120, 80, 30, \
                "Reset")
        xfl.fl_set_object_callback(pobj, self.reset, 0)
        fdui.down = xfl.fl_add_checkbutton(xfl.FL_RADIO_BUTTON, 210, 20, 
                70, 30, "Down")
        xfl.fl_set_object_shortcut(fdui.down, "D#D", 1)
        xfl.fl_set_object_callback(fdui.down, self.timer_direction, 0)
        fdui.down = xfl.fl_add_checkbutton(xfl.FL_RADIO_BUTTON, 210, 50, \
                70, 30, "Up")
        xfl.fl_set_object_shortcut(fdui.down, "U#U", 1 )
        xfl.fl_set_object_callback(fdui.down, self.timer_direction, 1)
        xfl.fl_end_form()
        return fdui



if __name__ == '__main__':
    print ("********* timer.py *********")
    Fltimer(len(sys.argv), sys.argv)

