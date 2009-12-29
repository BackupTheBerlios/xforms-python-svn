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
from xformslib import library as xf
from xformslib import xfdata as xfc



def fill_in(pobj):

    c = xfc.FL_BLACK + 1
    xf.fl_add_chart_value(pobj, 15.0, "item 1", c)
    c += 1
    xf.fl_add_chart_value(pobj, 5.0, "item 2", c)
    c += 1
    xf.fl_add_chart_value(pobj, 0.0, "item 3", c)
    c += 1
    xf.fl_add_chart_value(pobj, -10., "item 4", c)
    c += 1
    xf.fl_add_chart_value(pobj, 25.0, "item 5", c)
    c += 1
    xf.fl_add_chart_value(pobj, 12.0, "item 6", c)



def main(lsysargv, sysargv):

   xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

   create_form_form()
   fill_in(pbarchart)
   fill_in(phorbarchart)
   fill_in(plinechart)
   xf.fl_set_object_helper(plinechart, "A LineChart")
   fill_in(pfilledchart)
   fill_in(pspikechart)
   fill_in(ppiechart)
   fill_in(pspecialpiechart)

   xf.fl_show_form(pform, xfc.FL_PLACE_CENTER, xfc.FL_TRANSIENT, \
                   "Charts")

   xf.fl_do_forms()

   return 0



def create_form_form():
    global pform, pbarchart, phorbarchart, plinechart, pfilledchart
    global pspikechart, ppiechart, pspecialpiechart

    pform = xf.fl_bgn_form(xfc.FL_NO_BOX, 940, 360)

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 940, 360, "")

    pbarchart = xf.fl_add_chart(xfc.FL_BAR_CHART, 20, 20, 210, 140,
                                "BAR_CHART")
    xf.fl_set_object_boxtype(pbarchart, xfc.FL_RSHADOW_BOX)

    plinechart = xf.fl_add_chart(xfc.FL_LINE_CHART, 250, 20, 210, 140,
                                 "LINE_CHART")
    xf.fl_set_object_boxtype(plinechart, xfc.FL_RSHADOW_BOX)

    pfilledchart = xf.fl_add_chart(xfc.FL_FILLED_CHART, 250, 190, 210, 140,
                                   "FILLED_CHART")
    xf.fl_set_object_boxtype(pfilledchart, xfc.FL_RSHADOW_BOX)

    ppiechart = xf.fl_add_chart(xfc.FL_PIE_CHART, 480, 190, 210, 140,
                                "PIE_CHART")
    xf.fl_set_object_boxtype(ppiechart, xfc.FL_RSHADOW_BOX)

    pspecialpiechart = xf.fl_add_chart(xfc.FL_SPECIALPIE_CHART,
                                       710, 20, 210, 140, "SPECIALPIE_CHART")
    xf.fl_set_object_boxtype(pspecialpiechart, xfc.FL_RSHADOW_BOX)

    phorbarchart = xf.fl_add_chart(xfc.FL_HORBAR_CHART, 20, 190, 210, 140,
                                   "HORBAR_CHART")
    xf.fl_set_object_boxtype(phorbarchart, xfc.FL_RSHADOW_BOX)

    pspikechart = xf.fl_add_chart(xfc.FL_SPIKE_CHART, 480, 20, 210, 140,
                                  "SPIKE_CHART")
    xf.fl_set_object_boxtype(pspikechart, xfc.FL_RSHADOW_BOX)

    pexitbut = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 750, 260, 140, 30, \
				"Exit")

    xf.fl_end_form()




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

