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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flchart import *
from xformslib.flbutton import *
from xformslib.flslider import *
from xformslib.flmisc import *
from xformslib.xfdata import *




class ChartStrip(object):
    def __init__(self, lsysargv, sysargv):

        self.func = 1
        self.x = 0.0
        self.step = 0.15

        fl_flip_yorigin()
        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.create_form_form()
        fl_set_chart_bounds(self.pchartobj, -1.5, 1.5)
        fl_set_chart_maxnumb(self.pchartobj, 80)
        fl_set_chart_autosize(self.pchartobj, 0)
        fl_set_button(self.psinobj, 1)
        fl_set_slider_value(self.pstepobj, 0.5)
        fl_set_slider_bounds(self.pstepobj, 0.0, 1.0)

        fl_show_form(self.pform, FL_PLACE_CENTER | FL_FREE_SIZE, \
                     FL_TRANSIENT, "StripChart")

        while True:
            fl_insert_chart_value(self.pchartobj, 1, self.next_step(), "", 1)
            pobj = fl_check_forms()
            if fl_is_same_object(pobj, self.pexitbut):
                break
        fl_finish()


    def set_function(self, obj, arg):
        self.func = arg
        fl_clear_chart(self.pchartobj)
        self.x = 0.0


    def set_step(self, obj, arg):
        self.step = fl_get_slider_value(self.pstepobj)


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
        fl_insert_chart_value(self.pchartobj, 1, self.next_step(), "", 1)
        return 0


    def add_value(self, xev, a):
        fl_insert_chart_value(self.pchartobj, 1, self.next_step(), "", 1)


    def create_form_form(self):
        self.pform = fl_bgn_form(FL_NO_BOX, 490, 320)

        fl_add_box(FL_BORDER_BOX, 0, 0, 490, 320, "")

        self.pchartobj = fl_add_chart(FL_LINE_CHART, 20, 160, 390, 140, "")
        fl_set_object_dblbuffer(self.pchartobj, 1)

        fl_bgn_group()

        self.psinobj = fl_add_lightbutton(FL_RADIO_BUTTON, 30, 120, 170, 30,
                                          "sin(x)")
        fl_set_object_boxtype(self.psinobj, FL_BORDER_BOX)
        fl_set_object_callback(self.psinobj, self.set_function, 1)

        pobj = fl_add_lightbutton(FL_RADIO_BUTTON, 30, 90, 170, 30,
                                 "sin(2x)*cos(x)")
        fl_set_object_boxtype(pobj, FL_BORDER_BOX)
        fl_set_object_callback(pobj, self.set_function, 2)

        pobj = fl_add_lightbutton(FL_RADIO_BUTTON, 30, 60, 170, 30,
                                 "sin(2x)+cos(x)")
        fl_set_object_boxtype(pobj, FL_BORDER_BOX)
        fl_set_object_callback(pobj, self.set_function, 3)

        pobj = fl_add_lightbutton(FL_RADIO_BUTTON, 240, 120, 160, 30,
                                 "sin(3x)+cos(x)")
        fl_set_object_boxtype(pobj, FL_BORDER_BOX)
        fl_set_object_callback(pobj, self.set_function, 4)

        pobj = fl_add_lightbutton(FL_RADIO_BUTTON, 240, 90, 160, 30,
                                 "sin(x)^2 + cos(x)")
        fl_set_object_boxtype(pobj, FL_BORDER_BOX)
        fl_set_object_callback(pobj, self.set_function, 5)

        pobj = fl_add_lightbutton(FL_RADIO_BUTTON, 240, 60, 160, 30,
                                 "sin(x)^3")
        fl_set_object_boxtype(pobj, FL_BORDER_BOX)
        fl_set_object_callback(pobj, self.set_function, 6)

        fl_end_group()

        self.pexitbut = fl_add_button(FL_NORMAL_BUTTON, 150, 20, 140, 30, \
                                "Exit")
        fl_set_object_boxtype(self.pexitbut, FL_BORDER_BOX)

        self.pstepobj = fl_add_valslider(FL_VERT_SLIDER, 430, 20, 40, 280, "")
        fl_set_object_boxtype(self.pstepobj, FL_BORDER_BOX)
        fl_set_object_callback(self.pstepobj, self.set_step, 0)

        fl_end_form()



if __name__ == '__main__':
    appl = ChartStrip(len(sys.argv), sys.argv)

