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
import xformslib as xfl



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


class Flpreempt(object):
    def __init__(self, lsysargv, sysargv):

        self.INTERVAL = 800      # wait this long before show tip
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)

        self.fd_form0 = self.create_form_form0()

        # Fill-in form initialization code
        xfl.fl_set_button(self.fd_form0.peek, 1)
        xfl.fl_set_button(self.fd_form0.enter, 1)
        xfl.fl_set_button(self.fd_form0.leave, 1)
        xfl.fl_set_button(self.fd_form0.push, 1)
        xfl.fl_set_button(self.fd_form0.release, 1)

        xfl.fl_set_object_prehandler(self.fd_form0.butt, \
                self.preemptive_handler)

        print(self.fd_form0.done, self.fd_form0.peek, self.fd_form0.override)

        self.set_tip(self.fd_form0.done, "Want to quit ?\nPress me")
        self.set_tip(self.fd_form0.peek, "Turn preempting off")
        self.set_tip(self.fd_form0.override, "Turn preempting on")
        #xfl.fl_set_object_helper(self.fd_form0.done, "Want to quit ?\nPress me")
        #xfl.fl_set_object_helper(self.fd_form0.peek, "Turn preempting off")
        #xfl.fl_set_object_helper(self.fd_form0.override, "Turn preempting on")

        # Show the first form
        xfl.fl_show_form(self.fd_form0.form0, xfl.FL_PLACE_CENTER, \
                     xfl.FL_TRANSIENT, "Preemptive")

        while not xfl.fl_is_same_object(xfl.fl_do_forms(), self.fd_form0.done):
            pass        # empty

        xfl.fl_finish()


    # use the post handler as a tipper
    def post_handler(self, pobj, event, mx, my, key, xev):
        if not pobj.contents.u_cdata:
            return 0
        if event == xfl.FL_ENTER:
            self.timeoutID = xfl.fl_add_timeout(self.INTERVAL, \
                    self.do_tips, pobj)
        elif event == xfl.FL_LEAVE or event == xfl.FL_PUSH:
            xfl.fl_hide_oneliner()
            if self.timeoutID:
                xfl.fl_remove_timeout(self.timeoutID)
                self.timeoutID = 0
        return 0


    # which event to take over is better kept in a state variable even though
    # query the status via xfl.fl_get_button is cheap
    def preemptive_handler(self, pobj, event, mx, my, key, xev):

        override = xfl.fl_get_button(self.fd_form0.override)
        if override:
            what = "preempted"
        else:
            what = "detected"

        if event == xfl.FL_ENTER:
            if xfl.fl_get_button(self.fd_form0.enter):
                buf = "%s %s" % ("FL_ENTER", what)
                xfl.fl_set_object_label(self.fd_form0.event, buf)
                if override:
                    return xfl.FL_PREEMPT
                else:
                    return 0
        elif event == xfl.FL_LEAVE:
            if xfl.fl_get_button(self.fd_form0.leave):
                buf ="%s %s" % ("FL_LEAVE", what)
                xfl.fl_set_object_label(self.fd_form0.event, buf)
                if override:
                     return xfl.FL_PREEMPT
                else:
                    return 0
        elif event == xfl.FL_PUSH or event == xfl.FL_MOTION: 
            # one of the quirks of the button class
            if xfl.fl_get_button(self.fd_form0.push):
                buf = "%s %s" % ("FL_PUSH", what)
                xfl.fl_set_object_label(self.fd_form0.event, buf)
                if override:
                    return xfl.FL_PREEMPT
                else:
                    return 0
        elif event == xfl.FL_RELEASE:
            if xfl.fl_get_button(self.fd_form0.release):
                buf = "%s %s" % ("FL_RELEASE", what)
                xfl.fl_set_object_label(self.fd_form0.event, buf)
                if override:
                    return xfl.FL_PREEMPT
                else:
                    return 0
        return 0


    def do_tips(self, id_, pobj):
        onetext = ""
        #if xfl.fl_is_same_object(pobj, self.fd_form0.done):
        #    onetext = "Want to quit ?\nPress me"
        #elif xfl.fl_is_same_object(pobj, self.fd_form0.peek):
        #    onetext = "Turn preempting off"
        #elif xfl.fl_is_same_object(pobj, self.fd_form0.override):
        #    onetext = "Turn preempting on"
        xfl.fl_show_oneliner(onetext, pobj.contents.form.x + \
                pobj.contents.x, pobj.contents.form.y + \
                pobj.contents.y + pobj.contents.h + 1)
        self.timeoutID = xfl.fl_add_timeout(self.INTERVAL, self.do_tips, pobj)


    def set_tip(self, pobj, strng):
        pobj.contents.u_cdata = strng
        xfl.fl_set_object_posthandler(pobj, self.post_handler)


    # Form definition
    def create_form_form0(self):

        fdui = FD_form0()
        fdui.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 320, 250)
        xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 320, 250, "")
        xfl.fl_add_frame(xfl.FL_ENGRAVED_FRAME, 200, 70, 95, 100, "")

        fdui.butt = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 20, 70, \
                170, 100, "A Button")
        fdui.enter = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 210, 70, \
                45, 30, "Enter")
        fdui.leave = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 210, 95, \
                40, 30, "Leave")
        fdui.push = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 210, 120, \
                50, 30, "Push")
        fdui.release = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 210, 140, \
                60, 30, "Release")
        pobj = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 55, 15, 220, 30, \
                "Pre-emptive Handler")
        xfl.fl_set_object_lsize(pobj, xfl.FL_MEDIUM_SIZE)
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(pobj, xfl.FL_BOLD_STYLE)
        fdui.peek = xfl.fl_add_checkbutton(xfl.FL_RADIO_BUTTON, 150, 40, \
                35, 30, "Peek")
        xfl.fl_set_object_color(fdui.peek, xfl.FL_COL1, xfl.FL_BLUE)
        fdui.override = xfl.fl_add_checkbutton(xfl.FL_RADIO_BUTTON, \
                210, 40, 35, 30, "Override")
        xfl.fl_set_object_color(fdui.override, xfl.FL_COL1, xfl.FL_BLUE)
        fdui.event = xfl.fl_add_box(xfl.FL_FLAT_BOX, 40, 180, 245, 25, "")
        fdui.done = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 170, 210, \
                100, 30, "Done")
        xfl.fl_end_form()
        return fdui



if __name__ == '__main__':
    print ("********* preemptive.py *********")
    Flpreempt(len(sys.argv), sys.argv)
