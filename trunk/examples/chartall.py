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
import xformslib as xfl


class ChartAll(object):

    def __init__(self, lsysargv, sysargv):

        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        self.create_form_form()
        self.fill_in(self.pbarchart)
        self.fill_in(self.phorbarchart)
        self.fill_in(self.plinechart)
        xfl.fl_set_object_helper(self.plinechart, "A LineChart")
        self.fill_in(self.pfillchart)
        self.fill_in(self.pspikechart)
        self.fill_in(self.ppiechart)
        self.fill_in(self.pspecialpiechart)

        xfl.fl_show_form(self.pform, xfl.FL_PLACE_CENTER, xfl.FL_TRANSIENT, \
                "Charts")
        xfl.fl_do_forms()


    def fill_in(self, pobj):

        c = xfl.FL_BLACK + 1
        xfl.fl_add_chart_value(pobj, 15.0, "item 1", c)
        c += 1
        xfl.fl_add_chart_value(pobj, 5.0, "item 2", c)
        c += 1
        xfl.fl_add_chart_value(pobj, 0.0, "item 3", c)
        c += 1
        xfl.fl_add_chart_value(pobj, -10., "item 4", c)
        c += 1
        xfl.fl_add_chart_value(pobj, 25.0, "item 5", c)
        c += 1
        xfl.fl_add_chart_value(pobj, 12.0, "item 6", c)


    def create_form_form(self):

        self.pform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 940, 360)

        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 940, 360, "")

        self.pbarchart = xfl.fl_add_chart(xfl.FL_BAR_CHART, 20, 20, 210, 140,
                "BAR_CHART")
        xfl.fl_set_object_boxtype(self.pbarchart, xfl.FL_RSHADOW_BOX)

        self.plinechart = xfl.fl_add_chart(xfl.FL_LINE_CHART, 250, 20, \
                210, 140, "LINE_CHART")
        xfl.fl_set_object_boxtype(self.plinechart, xfl.FL_RSHADOW_BOX)

        self.pfillchart = xfl.fl_add_chart(xfl.FL_FILL_CHART, 250, 190, \
                210, 140, "FILL_CHART")
        xfl.fl_set_object_boxtype(self.pfillchart, xfl.FL_RSHADOW_BOX)

        self.ppiechart = xfl.fl_add_chart(xfl.FL_PIE_CHART, 480, 190, \
                210, 140, "PIE_CHART")
        xfl.fl_set_object_boxtype(self.ppiechart, xfl.FL_RSHADOW_BOX)

        self.pspecialpiechart = xfl.fl_add_chart(xfl.FL_SPECIALPIE_CHART, \
                710, 20, 210, 140, "SPECIALPIE_CHART")
        xfl.fl_set_object_boxtype(self.pspecialpiechart, xfl.FL_RSHADOW_BOX)

        self.phorbarchart = xfl.fl_add_chart(xfl.FL_HORBAR_CHART, 20, 190, \
                210, 140, "HORBAR_CHART")
        xfl.fl_set_object_boxtype(self.phorbarchart, xfl.FL_RSHADOW_BOX)

        self.pspikechart = xfl.fl_add_chart(xfl.FL_SPIKE_CHART, 480, 20, \
                210, 140, "SPIKE_CHART")
        xfl.fl_set_object_boxtype(self.pspikechart, xfl.FL_RSHADOW_BOX)

        self.pexitbut = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 750, 260, \
                140, 30, "Exit")

        xfl.fl_end_form()



if __name__ == '__main__':
    appl = ChartAll(len(sys.argv), sys.argv)
