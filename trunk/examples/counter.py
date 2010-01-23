#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  counter.c XForms demo, with some adaptations.
#
#  counter.c was written by M. Overmars and T.C. Zhao.
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This is an example of the use of counters.
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flcounter import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *




class FLCounter(object):
    def __init__(self, lsysargv, sysargv):

        self.pco = [0, 0, 0]
        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        self.create_form_form()
        fl_set_object_color(self.presult, FL_FREE_COL1, FL_FREE_COL1)

        for i in range(0, 3):
            fl_set_counter_bounds(self.pco[i], 0.0, 255.0)
            fl_set_counter_step(self.pco[i], 1.0, 10.0)
            fl_set_counter_precision(self.pco[i], 0)
            fl_set_object_return(self.pco[i], 1)

        fl_call_object_callback(self.pco[0])

        fl_show_form(self.pform, FL_PLACE_CENTER, FL_TRANSIENT, \
                    "Counter")
        fl_do_forms()

        fl_finish()


    def color_change(self, pobj, data):
        c = [0, 0, 0]
        for i in range(0, 3):
            c[i] = fl_get_counter_value(self.pco[i])
        fl_mapcolor(FL_FREE_COL1, c[0], c[1], c[2])
        fl_redraw_object(self.presult)


    def create_form_form(self):
        self.pform = fl_bgn_form(FL_NO_BOX, 480, 200)

        pobj = fl_add_box(FL_UP_BOX, 0, 0, 480, 200, "")

        self.presult = fl_add_box(FL_DOWN_BOX, 310, 20, 150, 160, "")
        fl_set_object_dblbuffer(self.presult, 1)

        self.pco[0] = fl_add_counter(FL_NORMAL_COUNTER, 20, 20, 270, 30, \
                               "")
        fl_set_object_color(self.pco[0], FL_INDIANRED, FL_RED)
        fl_set_object_callback(self.pco[0], self.color_change, 0)

        self.pco[1] = fl_add_counter(FL_NORMAL_COUNTER, 20, 60, 270, 30, \
                               "")
        fl_set_object_color(self.pco[1], FL_PALEGREEN, FL_GREEN)
        fl_set_object_callback(self.pco[1], self.color_change, 0)

        self.pco[2] = fl_add_counter(FL_NORMAL_COUNTER, 20, 100, 270, 30, \
                               "")
        fl_set_object_color(self.pco[2], FL_SLATEBLUE, FL_BLUE)
        fl_set_object_callback(self.pco[2], self.color_change, 0)

        pobj = fl_add_button(FL_NORMAL_BUTTON, 100, 150, 110, 30, "Exit")

        fl_end_form()



if __name__ == '__main__':
    appl = FLCounter(len(sys.argv), sys.argv)

