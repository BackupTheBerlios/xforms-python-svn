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
import xformslib as xfl



class FLCounter(object):
    def __init__(self, lsysargv, sysargv):

        self.pco = [0, 0, 0]
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        self.create_form_form()
        xfl.fl_set_object_color(self.presult, xfl.FL_FREE_COL1, \
                xfl.FL_FREE_COL1)

        for i in range(0, 3):
            xfl.fl_set_counter_bounds(self.pco[i], 0.0, 255.0)
            xfl.fl_set_counter_step(self.pco[i], 1.0, 10.0)
            xfl.fl_set_counter_precision(self.pco[i], 0)
            xfl.fl_set_object_return(self.pco[i], 1)

        xfl.fl_call_object_callback(self.pco[0])

        xfl.fl_show_form(self.pform, xfl.FL_PLACE_CENTER, xfl.FL_TRANSIENT, \
                    "Counter")
        xfl.fl_do_forms()

        xfl.fl_finish()


    def color_change(self, pobj, data):
        c = [0, 0, 0]
        for i in range(0, 3):
            c[i] = xfl.fl_get_counter_value(self.pco[i])
        xfl.fl_mapcolor(xfl.FL_FREE_COL1, c[0], c[1], c[2])
        xfl.fl_redraw_object(self.presult)


    def create_form_form(self):
        self.pform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 480, 200)

        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 480, 200, "")

        self.presult = xfl.fl_add_box(xfl.FL_DOWN_BOX, 310, 20, 150, 160, "")
        xfl.fl_set_object_dblbuffer(self.presult, 1)

        self.pco[0] = xfl.fl_add_counter(xfl.FL_NORMAL_COUNTER, 20, 20, \
                270, 30, "")
        xfl.fl_set_object_color(self.pco[0], xfl.FL_INDIANRED, xfl.FL_RED)
        xfl.fl_set_object_callback(self.pco[0], self.color_change, 0)

        self.pco[1] = xfl.fl_add_counter(xfl.FL_NORMAL_COUNTER, 20, 60, \
                270, 30, "")
        xfl.fl_set_object_color(self.pco[1], xfl.FL_PALEGREEN, xfl.FL_GREEN)
        xfl.fl_set_object_callback(self.pco[1], self.color_change, 0)

        self.pco[2] = xfl.fl_add_counter(xfl.FL_NORMAL_COUNTER, 20, 100, \
                270, 30, "")
        xfl.fl_set_object_color(self.pco[2], xfl.FL_SLATEBLUE, xfl.FL_BLUE)
        xfl.fl_set_object_callback(self.pco[2], self.color_change, 0)

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 100, 150, 110, 30, \
                "Exit")

        xfl.fl_end_form()



if __name__ == '__main__':
    print("********* counter.py *********")
    appl = FLCounter(len(sys.argv), sys.argv)
