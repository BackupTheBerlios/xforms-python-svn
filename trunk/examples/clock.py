#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  flclock.c XForms demo, with some adaptations.
#
#  flclock.c was written by M. Overmars and T.C. Zhao.
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Built-in xforms clock
#

import sys
#sys.path.append("..")
import xformslib as xfl



class Flclock(object):

    def __init__(self, lsysargv, sysargv):
        self.pfclock = None

        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0,  0)

        self.create_form_clock()
        xfl.fl_show_form(self.pfclock, xfl.FL_PLACE_CENTER, \
                xfl.FL_TRANSIENT, "clocks")

        xfl.fl_do_forms()
        xfl.fl_finish()


    def exit_cb(self, pobj, q):
        xfl.fl_finish()
        sys.exit(0)


    def create_form_clock(self):
        if self.pfclock:
            return

        self.pfclock = xfl.fl_bgn_form(xfl.FL_NO_BOX, 500, 350)
        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 500, 350, "")

        pobj = xfl.fl_add_clock(xfl.FL_DIGITAL_CLOCK, 185, 20, 150, 35, "")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_ROUNDED_BOX)
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_BLACK)
        xfl.fl_set_object_lsize(pobj, xfl.FL_MEDIUM_SIZE)
        xfl.fl_set_object_lstyle(pobj, xfl.FL_BOLD_STYLE)

        pobj = xfl.fl_add_clock(xfl.FL_ANALOG_CLOCK, 30, 70, 220, 200, "")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_UP_BOX)

        pobj = xfl.fl_add_clock(xfl.FL_ANALOG_CLOCK, 260, 70, 220, 200, "")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_OVAL3D_UPBOX)

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 375, 300, 110, 35, \
                "Exit")
        xfl.fl_set_object_callback(pobj, self.exit_cb, 0)

        xfl.fl_end_form()

        xfl.fl_scale_form(self.pfclock, 0.7, 0.7)



if __name__ == '__main__':
    Flclock(len(sys.argv), sys.argv)
