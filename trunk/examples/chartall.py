#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  chartall.c XForms demo, with some adaptations.
#
#  chartall.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Showing all different charts
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flchart import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *



class ChartAll(object):

    def __init__(self, lsysargv, sysargv):

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        self.create_form_form()
        self.fill_in(self.pbarchart)
        self.fill_in(self.phorbarchart)
        self.fill_in(self.plinechart)
        fl_set_object_helper(self.plinechart, "A LineChart")
        self.fill_in(self.pfillchart)
        self.fill_in(self.pspikechart)
        self.fill_in(self.ppiechart)
        self.fill_in(self.pspecialpiechart)

        fl_show_form(self.pform, FL_PLACE_CENTER, FL_TRANSIENT, \
                     "Charts")
        fl_do_forms()


    def fill_in(self, pobj):

        c = FL_BLACK + 1
        fl_add_chart_value(pobj, 15.0, "item 1", c)
        c += 1
        fl_add_chart_value(pobj, 5.0, "item 2", c)
        c += 1
        fl_add_chart_value(pobj, 0.0, "item 3", c)
        c += 1
        fl_add_chart_value(pobj, -10., "item 4", c)
        c += 1
        fl_add_chart_value(pobj, 25.0, "item 5", c)
        c += 1
        fl_add_chart_value(pobj, 12.0, "item 6", c)


    def create_form_form(self):

        self.pform = fl_bgn_form(FL_NO_BOX, 940, 360)

        pobj = fl_add_box(FL_UP_BOX, 0, 0, 940, 360, "")

        self.pbarchart = fl_add_chart(FL_BAR_CHART, 20, 20, 210, 140,
                                "BAR_CHART")
        fl_set_object_boxtype(self.pbarchart, FL_RSHADOW_BOX)

        self.plinechart = fl_add_chart(FL_LINE_CHART, 250, 20, 210, 140,
                                 "LINE_CHART")
        fl_set_object_boxtype(self.plinechart, FL_RSHADOW_BOX)

        self.pfillchart = fl_add_chart(FL_FILL_CHART, 250, 190, 210, 140,
                                   "FILL_CHART")
        fl_set_object_boxtype(self.pfillchart, FL_RSHADOW_BOX)

        self.ppiechart = fl_add_chart(FL_PIE_CHART, 480, 190, 210, 140,
                                "PIE_CHART")
        fl_set_object_boxtype(self.ppiechart, FL_RSHADOW_BOX)

        self.pspecialpiechart = fl_add_chart(FL_SPECIALPIE_CHART,
                                       710, 20, 210, 140, "SPECIALPIE_CHART")
        fl_set_object_boxtype(self.pspecialpiechart, FL_RSHADOW_BOX)

        self.phorbarchart = fl_add_chart(FL_HORBAR_CHART, 20, 190, 210, 140,
                                   "HORBAR_CHART")
        fl_set_object_boxtype(self.phorbarchart, FL_RSHADOW_BOX)

        self.pspikechart = fl_add_chart(FL_SPIKE_CHART, 480, 20, 210, 140,
                                  "SPIKE_CHART")
        fl_set_object_boxtype(self.pspikechart, FL_RSHADOW_BOX)

        self.pexitbut = fl_add_button(FL_NORMAL_BUTTON, 750, 260, 140, 30, \
                                "Exit")

        fl_end_form()



if __name__ == '__main__':
    appl = ChartAll(len(sys.argv), sys.argv)

