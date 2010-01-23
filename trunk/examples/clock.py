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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.flclock import *
from xformslib.xfdata import *



class Flflclock(object):

    def __init__(self, lsysargv, sysargv):
        self.pfclock = None

        fl_initialize(lsysargv, sysargv, "FormDemo", 0,  0)

        self.create_form_clock()
        fl_show_form(self.pfclock, FL_PLACE_CENTER, FL_TRANSIENT, "clocks")

        fl_do_forms()
        fl_finish()


    def exit_cb(self, pobj, q):
        fl_finish()
        sys.exit(0)


    def create_form_clock(self):
        if self.pfclock:
            return

        self.pfclock = fl_bgn_form(FL_NO_BOX, 500, 350)
        pobj = fl_add_box(FL_UP_BOX, 0, 0, 500, 350, "")

        pobj = fl_add_clock(FL_DIGITAL_CLOCK, 185, 20, 150, 35, "")
        fl_set_object_boxtype(pobj, FL_ROUNDED_BOX)
        fl_set_object_color(pobj, FL_COL1, FL_BLACK)
        fl_set_object_lsize(pobj, FL_MEDIUM_SIZE)
        fl_set_object_lstyle(pobj, FL_BOLD_STYLE)

        pobj = fl_add_clock(FL_ANALOG_CLOCK, 30, 70, 220, 200, "")
        fl_set_object_boxtype(pobj, FL_UP_BOX)

        pobj = fl_add_clock(FL_ANALOG_CLOCK, 260, 70, 220, 200, "")
        fl_set_object_boxtype(pobj, FL_OVAL3D_UPBOX)

        pobj = fl_add_button(FL_NORMAL_BUTTON, 375, 300, 110, 35, "Exit")
        fl_set_object_callback(pobj, self.exit_cb, 0)

        fl_end_form()

        fl_scale_form(self.pfclock, 0.7, 0.7)




if __name__ == '__main__':
    Flflclock(len(sys.argv), sys.argv)

