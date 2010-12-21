#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  chartstrip.c XForms demo, with some adaptations.
#
#  chartstrip.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# A demo of a moving chart
#

import sys, math
#sys.path.append("..")
import xformslib as xfl



class ChartStrip(object):
    def __init__(self, lsysargv, sysargv):

        self.func = 1
        self.x = 0.0
        self.step = 0.15

        xfl.fl_flip_yorigin()
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.create_form_form()
        xfl.fl_set_chart_bounds(self.pchartobj, -1.5, 1.5)
        xfl.fl_set_chart_maxnumb(self.pchartobj, 80)
        xfl.fl_set_chart_autosize(self.pchartobj, 0)
        xfl.fl_set_button(self.psinobj, 1)
        xfl.fl_set_slider_value(self.pstepobj, 0.5)
        xfl.fl_set_slider_bounds(self.pstepobj, 0.0, 1.0)

        xfl.fl_show_form(self.pform, xfl.FL_PLACE_CENTER | xfl.FL_FREE_SIZE, \
                     xfl.FL_TRANSIENT, "StripChart")

        while True:
            xfl.fl_insert_chart_value(self.pchartobj, 1, self.next_step(), \
                    "", 1)
            pobj = xfl.fl_check_forms()
            if xfl.fl_is_same_object(pobj, self.pexitbut):
                break
        xfl.fl_finish()


    def set_function(self, obj, arg):
        self.func = arg
        xfl.fl_clear_chart(self.pchartobj)
        self.x = 0.0


    def set_step(self, obj, arg):
        self.step = xfl.fl_get_slider_value(self.pstepobj)


    def next_step(self):
        res = 0.0
        if self.func == 1:
            res = math.sin(self.x)
        elif self.func == 2:
            res = math.sin(2 * self.x) * math.cos(self.x)
        elif self.func == 3:
            res = math.sin(2 * self.x) + math.cos(self.x)
        elif self.func == 4:
            res = math.sin(3 * self.x) + math.cos(self.x)
        elif self.func == 5:
            res = math.sin(self.x) * math.sin(self.x) + math.cos(self.x)
        elif self.func == 6:
            res = math.sin(self.x) * math.sin(self.x) * math.sin(self.x)
        self.x += 0.2 * self.step
        return res


    def idle_cb(self, xev, d):
        xfl.fl_insert_chart_value(self.pchartobj, 1, self.next_step(), "", 1)
        return 0


    def add_value(self, xev, a):
        xfl.fl_insert_chart_value(self.pchartobj, 1, self.next_step(), "", 1)


    def create_form_form(self):
        self.pform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 490, 320)

        xfl.fl_add_box(xfl.FL_BORDER_BOX, 0, 0, 490, 320, "")

        self.pchartobj = xfl.fl_add_chart(xfl.FL_LINE_CHART, 20, 160, \
                390, 140, "")
        xfl.fl_set_object_dblbuffer(self.pchartobj, 1)

        xfl.fl_bgn_group()

        self.psinobj = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 30, 120, \
                170, 30, "sin(x)")
        xfl.fl_set_object_boxtype(self.psinobj, xfl.FL_BORDER_BOX)
        xfl.fl_set_object_callback(self.psinobj, self.set_function, 1)

        pobj = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 30, 90, 170, 30,
                "sin(2x)*cos(x)")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_BORDER_BOX)
        xfl.fl_set_object_callback(pobj, self.set_function, 2)

        pobj = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 30, 60, 170, 30,
                "sin(2x)+cos(x)")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_BORDER_BOX)
        xfl.fl_set_object_callback(pobj, self.set_function, 3)

        pobj = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 240, 120, 160, 30,
                "sin(3x)+cos(x)")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_BORDER_BOX)
        xfl.fl_set_object_callback(pobj, self.set_function, 4)

        pobj = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 240, 90, 160, 30,
                "sin(x)^2 + cos(x)")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_BORDER_BOX)
        xfl.fl_set_object_callback(pobj, self.set_function, 5)

        pobj = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 240, 60, 160, 30,
                "sin(x)^3")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_BORDER_BOX)
        xfl.fl_set_object_callback(pobj, self.set_function, 6)

        xfl.fl_end_group()

        self.pexitbut = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 150, 20, \
                140, 30, "Exit")
        xfl.fl_set_object_boxtype(self.pexitbut, xfl.FL_BORDER_BOX)

        self.pstepobj = xfl.fl_add_valslider(xfl.FL_VERT_SLIDER, 430, 20, \
                40, 280, "")
        xfl.fl_set_object_boxtype(self.pstepobj, xfl.FL_BORDER_BOX)
        xfl.fl_set_object_callback(self.pstepobj, self.set_step, 0)

        xfl.fl_end_form()



if __name__ == '__main__':
    print("********* chartstrip.py *********")
    appl = ChartStrip(len(sys.argv), sys.argv)

