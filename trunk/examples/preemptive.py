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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flmisc import *
from xformslib.flbutton import *
from xformslib.flgoodies import *
from xformslib.xfdata import *




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

        self.INTERVAL = 800          # wait this long before show tip
        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        self.fd_form0 = self.create_form_form0()

        # Fill-in form initialization code
        fl_set_button(self.fd_form0.peek, 1)
        fl_set_button(self.fd_form0.enter, 1)
        fl_set_button(self.fd_form0.leave, 1)
        fl_set_button(self.fd_form0.push, 1)
        fl_set_button(self.fd_form0.release, 1)

        fl_set_object_prehandler(self.fd_form0.butt, self.preemptive_handler)

        print self.fd_form0.done
        print self.fd_form0.peek
        print self.fd_form0.override

        self.set_tip(self.fd_form0.done, "Want to quit ?\nPress me")
        self.set_tip(self.fd_form0.peek, "Turn preempting off")
        self.set_tip(self.fd_form0.override, "Turn preempting on")

        #fl_set_object_helper(self.fd_form0.done, "Want to quit ?\nPress me")
        #fl_set_object_helper(self.fd_form0.peek, "Turn preempting off")
        #fl_set_object_helper(self.fd_form0.override, "Turn preempting on")

        # Show the first form
        fl_show_form(self.fd_form0.form0, FL_PLACE_CENTER, \
                     FL_TRANSIENT, "Preemptive")

        while not fl_is_same_object(fl_do_forms(), self.fd_form0.done):
            pass        # empty

        fl_finish()


    # use the post handler as a tipper
    def post_handler(self, pobj, event, mx, my, key, xev):
        if not pobj.contents.u_cdata:
            return 0
        if event == FL_ENTER:
            self.timeoutID = fl_add_timeout(self.INTERVAL, self.do_tips, pobj)
        elif event == FL_LEAVE or event == FL_PUSH:
            fl_hide_oneliner()
            if self.timeoutID:
                fl_remove_timeout(self.timeoutID)
                self.timeoutID = 0
        return 0


    # which event to take over is better kept in a state variable even though
    # query the status via fl_get_button is cheap
    def preemptive_handler(self, pobj, event, mx, my, key, xev):

        override = fl_get_button(self.fd_form0.override)
        if override:
            what = "preempted"
        else:
            what = "detected"

        if event == FL_ENTER:
            if fl_get_button(self.fd_form0.enter):
                buf = "%s %s" % ("FL_ENTER", what)
                fl_set_object_label(self.fd_form0.event, buf)
                if override:
                    return FL_PREEMPT
                else:
                    return 0
        elif event == FL_LEAVE:
            if fl_get_button(self.fd_form0.leave):
                buf ="%s %s" % ("FL_LEAVE", what)
                fl_set_object_label(self.fd_form0.event, buf)
                if override:
                     return FL_PREEMPT
                else:
                    return 0
        elif event == FL_PUSH or event == FL_MOTION: 
            # one of the quirks of the button class
            if fl_get_button(self.fd_form0.push):
                buf = "%s %s" % ("FL_PUSH", what)
                fl_set_object_label(self.fd_form0.event, buf)
                if override:
                    return FL_PREEMPT
                else:
                    return 0
        elif event == FL_RELEASE:
            if fl_get_button(self.fd_form0.release):
                buf = "%s %s" % ("FL_RELEASE", what)
                fl_set_object_label(self.fd_form0.event, buf)
                if override:
                    return FL_PREEMPT
                else:
                    return 0
        return 0


    def do_tips(self, id_, pobj):
        onetext = ""
        #if fl_is_same_object(pobj, self.fd_form0.done):
        #    onetext = "Want to quit ?\nPress me"
        #elif fl_is_same_object(pobj, self.fd_form0.peek):
        #    onetext = "Turn preempting off"
        #elif fl_is_same_object(pobj, self.fd_form0.override):
        #    onetext = "Turn preempting on"
        fl_show_oneliner(onetext, pobj.contents.form.x + \
                         pobj.contents.x, pobj.contents.form.y + \
                         pobj.contents.y + pobj.contents.h + 1)
        self.timeoutID = fl_add_timeout(self.INTERVAL, self.do_tips, pobj)


    def set_tip(self, pobj, strng):
        pobj.contents.u_cdata = strng
        fl_set_object_posthandler(pobj, self.post_handler)


    # Form definition
    def create_form_form0(self):

        fdui = FD_form0()
        fdui.form0 = fl_bgn_form(FL_NO_BOX, 320, 250)
        fl_add_box(FL_UP_BOX, 0, 0, 320, 250, "")
        fl_add_frame(FL_ENGRAVED_FRAME, 200, 70, 95, 100, "")

        fdui.butt = fl_add_button(FL_NORMAL_BUTTON, 20, 70, 170, 100,
                                 "A Button")
        fdui.enter = fl_add_checkbutton(FL_PUSH_BUTTON, 210, 70, 45, 30,
                                       "Enter")
        fdui.leave = fl_add_checkbutton(FL_PUSH_BUTTON, 210, 95, 40, 30,
                                       "Leave")
        fdui.push = fl_add_checkbutton(FL_PUSH_BUTTON, 210, 120, 50, 30, 
                                      "Push")
        fdui.release = fl_add_checkbutton(FL_PUSH_BUTTON, 210, 140, 60, 30,
                                         "Release")
        pobj = fl_add_text(FL_NORMAL_TEXT, 55, 15, 220, 30, "Pre-emptive Handler")
        fl_set_object_lsize(pobj, FL_MEDIUM_SIZE)
        fl_set_object_lalign(pobj, FL_ALIGN_CENTER)
        fl_set_object_lstyle(pobj, FL_BOLD_STYLE)
        fdui.peek = fl_add_checkbutton(FL_RADIO_BUTTON, 165, 40, 35, 30,
                                      "Peek")
        fl_set_object_color(fdui.peek, FL_COL1, FL_BLUE)
        fdui.override = fl_add_checkbutton(FL_RADIO_BUTTON, 230, 40, \
                                          35, 30, "Override")
        fl_set_object_color(fdui.override, FL_COL1, FL_BLUE)
        fdui.event = fl_add_box(FL_FLAT_BOX, 40, 180, 245, 25, "")
        fdui.done = fl_add_button(FL_NORMAL_BUTTON, 170, 210, 100, 30, "Done")
        fl_end_form()
        return fdui




if __name__ == '__main__':
    Flpreempt(len(sys.argv), sys.argv)

