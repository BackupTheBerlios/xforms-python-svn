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
from xformslib import library as xf
from xformslib import xfdata as xfc



# Forms and Objects

class FD_timerform(object):
    timerform = None
    vdata = None
    ldata = None
    timer = None
    down = None

T = 20


# callbacks for form timer form

def suspend_resume(pobj, data):

    if data:
	xf.fl_resume_timer(fd_timerform.timer)
    else:
	xf.fl_suspend_timer(fd_timerform.timer)


def reset(pobj, data):
    xf.fl_set_timer(fd_timerform.timer, T)


def timer_direction(pobj, data):
    xf.fl_set_timer_countup(fd_timerform.timer, data)


def expired(pobj, data):

    if xf.fl_show_question("Expired!\n\nQuit?", 0) == 1:
    	xf.fl_finish()
	sys.exit(0)
    else:
        xf.fl_set_timer(fd_timerform.timer, T)


def create_form_timerform():

    fdui = FD_timerform()

    fdui.timerform = xf.fl_bgn_form(xfc.FL_NO_BOX, 290, 210)
    xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 290, 210, "")
    xf.fl_add_frame(xfc.FL_UP_FRAME, 0, 0, 290, 94, "")
    xf.fl_add_frame(xfc.FL_UP_FRAME, 0, 100, 330, 190, "")
    xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 100, 170, 80, 30, "Done")

    fdui.timer = xf.fl_add_timer(xfc.FL_VALUE_TIMER, 20, 30, 
                                 180, 40, "Timer")
    xf.fl_set_object_boxtype(fdui.timer, xfc.FL_UP_BOX)
    xf.fl_set_object_lsize(fdui.timer, xfc.FL_MEDIUM_SIZE)
    xf.fl_set_object_lalign(fdui.timer, xfc.FL_ALIGN_TOP)
    xf.fl_set_object_lstyle(fdui.timer, xfc.FL_TIMES_STYLE)
    xf.fl_set_object_callback(fdui.timer, expired, 0)

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 20, 120, 80, 30, "Suspend")
    xf.fl_set_object_callback(pobj, suspend_resume, 0)

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 100, 120, 80, 30, "Resume")
    xf.fl_set_object_callback(pobj, suspend_resume, 1)

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 180, 120, 80, 30, "Reset")
    xf.fl_set_object_callback(pobj, reset, 0)

    fdui.down = xf.fl_add_checkbutton(xfc.FL_RADIO_BUTTON, 210, 20, 
                                      70, 30, "Down")
    xf.fl_set_object_shortcut(fdui.down, "D#D", 1)
    xf.fl_set_object_callback(fdui.down, timer_direction, 0)

    fdui.down = xf.fl_add_checkbutton(xfc.FL_RADIO_BUTTON, 210, 50, 70, 30, "Up")
    xf.fl_set_object_shortcut(fdui.down, "U#U", 1 )
    xf.fl_set_object_callback(fdui.down, timer_direction, 1)

    xf.fl_end_form()

    return fdui




def main(lsysargv, sysargv):
    global fd_timerform

    xf.fl_set_border_width(-2)

    xf.fl_initialize(lsysargv, sysargv, "", 0, 0)
    fd_timerform = create_form_timerform()

    # fill-in form initialization code

    xf.fl_set_timer(fd_timerform.timer, T)
    xf.fl_set_button(fd_timerform.down, 1)

    # show the first form

    xf.fl_show_form(fd_timerform.timerform, xfc.FL_PLACE_CENTER,
                    xfc.FL_FULLBORDER, "timerform")

    xf.fl_do_forms()

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

