#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  preemptive.c XForms demo, with some adaptations.
#
# preemptive.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Demo showing the use of preemptive and post-object handler,
# and one possible way of implementing a "tool tip"
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



class FD_form0(object):
    form0 = None
    vdata = None
    cdata = ""
    ldata = 0
    butt = None
    enter = None
    leave = None
    push = None
    release = None
    peek = None
    override = None
    event = None
    done = None



# which event to take over is better kept in a state variable even though
# query the status via xf.fl_get_button is cheap

def preemptive_handler(ob, event, mx, my, key, xev):

    override = xf.fl_get_button(fd_form0.override)
    if override:
        what = "preempted"
    else:
        what = "detected"

    if event == xfc.FL_ENTER:
        if xf.fl_get_button(fd_form0.enter):
            buf = "%s %s" % ("FL_ENTER", what)
            xf.fl_set_object_label(fd_form0.event, buf)
            if override:
                return xfc.FL_PREEMPT
            else:
                return 0

    elif event == xfc.FL_LEAVE:
        if xf.fl_get_button( fd_form0.leave):
            buf ="%s %s" % ("FL_LEAVE", what)
            xf.fl_set_object_label(fd_form0.event, buf)
            if override:
                return xfc.FL_PREEMPT
            else:
                return 0

    elif event == xfc.FL_PUSH or event == xfc.FL_MOTION: 
        # one of the quirks of the button class
        if xf.fl_get_button(fd_form0.push):
            buf = "%s %s" % ("FL_PUSH", what)
            xf.fl_set_object_label(fd_form0.event, buf)
            if override:
                return xfc.FL_PREEMPT
            else:
                return 0

    elif event == xfc.FL_RELEASE:
        if xf.fl_get_button(fd_form0.release):
            buf = "%s %s" % ("FL_RELEASE", what)
            xf.fl_set_object_label(fd_form0.event, buf)
            if override:
                return xfc.FL_PREEMPT
            else:
                return 0

    return 0



INTERVAL = 800          # wait this long before show tip


def do_tips(id_, p):

    ob = p
    xf.fl_show_oneliner(ob[0].u_vdata, ob[0].form.x + ob[0].x, \
                        ob[0].form.y + ob[0].y + ob[0].h + 1)
    timeoutID = xf.fl_add_timeout(INTERVAL, do_tips, ob)



# use the post handler as a tipper

def post_handler(ob, event, mx, my, key, xev):

    if not ob[0].u_vdata:
        return 0

    if event == xfc.FL_ENTER:
        timeoutID = xf.fl_add_timeout(INTERVAL, do_tips, ob)
    elif event == xfc.FL_LEAVE or event == xfc.FL_PUSH:
        xf.fl_hide_oneliner()
        if timeoutID:
            xf.fl_remove_timeout(timeoutID)
            timeoutID = 0

    return 0



def set_tip(ob, strng):
    ob[0].u_cdata = strng
    xf.fl_set_object_posthandler(ob, post_handler)



def main(lsysargv, sysargv):
    global fd_form0

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    fd_form0 = create_form_form0()

    # Fill-in form initialization code

    xf.fl_set_button(fd_form0.peek, 1)
    xf.fl_set_button(fd_form0.enter, 1)
    xf.fl_set_button(fd_form0.leave, 1)
    xf.fl_set_button(fd_form0.push, 1)
    xf.fl_set_button(fd_form0.release, 1)

    xf.fl_set_object_prehandler(fd_form0.butt, preemptive_handler)

    set_tip(fd_form0.done, "Want to quit ?\nPress me")
    set_tip(fd_form0.peek, "Turn preempting off")
    set_tip(fd_form0.override, "Turn preempting on")

    # Show the first form

    xf.fl_show_form(fd_form0.form0, xfc.FL_PLACE_CENTER, \
                    xfc.FL_TRANSIENT, "Preemptive")

    while xf.fl_do_forms()[0].u_ldata != fd_form0.done[0].u_ldata:
        pass        # empty

    return 0



# Form definition

def create_form_form0():

    fdui = FD_form0()

    fdui.form0 = xf.fl_bgn_form(xfc.FL_NO_BOX, 320, 250)

    xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 320, 250, "")

    xf.fl_add_frame(xfc.FL_ENGRAVED_FRAME, 200, 70, 95, 100, "")

    fdui.butt = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 20, 70, 170, 100,
                                 "A Button")

    fdui.enter = xf.fl_add_checkbutton(xfc.FL_PUSH_BUTTON, 210, 70, 45, 30,
                                       "Enter")

    fdui.leave = xf.fl_add_checkbutton(xfc.FL_PUSH_BUTTON, 210, 95, 40, 30,
                                       "Leave")

    fdui.push = xf.fl_add_checkbutton(xfc.FL_PUSH_BUTTON, 210, 120, 50, 30, 
                                      "Push")

    fdui.release = xf.fl_add_checkbutton(xfc.FL_PUSH_BUTTON, 210, 140, 60, 30,
                                         "Release")

    obj = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 55, 15, 220, 30, "Pre-emptive Handler")
    xf.fl_set_object_lsize(obj, xfc.FL_MEDIUM_SIZE)
    xf.fl_set_object_lalign(obj, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_lstyle(obj, xfc.FL_BOLD_STYLE)

    fdui.peek = obj = xf.fl_add_checkbutton(xfc.FL_RADIO_BUTTON, 190, 40, 35, 30,
                                            "Peek")
    xf.fl_set_object_color(obj, xfc.FL_COL1, xfc.FL_BLUE)

    fdui.override = xf.fl_add_checkbutton(xfc.FL_RADIO_BUTTON, 240, 40, \
                                          35, 30, "Override")
    xf.fl_set_object_color(fdui.override, xfc.FL_COL1, xfc.FL_BLUE)

    fdui.event = xf.fl_add_box(xfc.FL_FLAT_BOX, 40, 180, 245, 25, "")

    fdui.done = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 170, 210, 100, 30, "Done")
    fdui.done[0].u_ldata = xfc.EXITVAL
    xf.fl_end_form()

    return fdui




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

