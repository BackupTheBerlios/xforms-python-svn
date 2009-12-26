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



def fill_in(ob):

    c = xfc.FL_BLACK + 1
    xf.fl_add_chart_value(ob, 15.0, "item 1", c)
    c += 1
    xf.fl_add_chart_value(ob,  5.0, "item 2", c)
    c += 1
    xf.fl_add_chart_value(ob,  0.0, "item 3", c)
    c += 1
    xf.fl_add_chart_value(ob, -10., "item 4", c)
    c += 1
    xf.fl_add_chart_value(ob, 25.0, "item 5", c)
    c += 1
    xf.fl_add_chart_value(ob, 12.0, "item 6", c)



def main(lsysargv, sysargv):

   xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

   create_form_form()
   fill_in(barchart)
   fill_in(horbarchart)
   fill_in(linechart)
   xf.fl_set_object_helper(linechart, "A LineChart")
   fill_in(filledchart)
   fill_in(spikechart)
   fill_in(piechart)
   fill_in(specialpiechart)

   xf.fl_show_form(form, xfc.FL_PLACE_CENTER, xfc.FL_TRANSIENT, \
                   "Charts")

   xf.fl_do_forms()

   return 0



def create_form_form():
    global form, barchart, horbarchart, linechart, filledchart
    global spikechart, piechart, specialpiechart

    form = xf.fl_bgn_form(xfc.FL_NO_BOX, 940, 360)

    obj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 940, 360, "")

    barchart = xf.fl_add_chart(xfc.FL_BAR_CHART, 20, 20, 210, 140,
                               "BAR_CHART")
    xf.fl_set_object_boxtype(barchart, xfc.FL_RSHADOW_BOX)

    linechart = xf.fl_add_chart(xfc.FL_LINE_CHART, 250, 20, 210, 140,
                               "LINE_CHART")
    xf.fl_set_object_boxtype(linechart, xfc.FL_RSHADOW_BOX)

    filledchart = xf.fl_add_chart(xfc.FL_FILLED_CHART, 250, 190, 210, 140,
                                  "FILLED_CHART")
    xf.fl_set_object_boxtype(filledchart ,xfc.FL_RSHADOW_BOX)

    piechart = xf.fl_add_chart(xfc.FL_PIE_CHART, 480, 190, 210, 140,
                               "PIE_CHART")
    xf.fl_set_object_boxtype(piechart, xfc.FL_RSHADOW_BOX)

    specialpiechart = xf.fl_add_chart(xfc.FL_SPECIALPIE_CHART,
                                      710, 20, 210, 140, "SPECIALPIE_CHART")
    xf.fl_set_object_boxtype(specialpiechart, xfc.FL_RSHADOW_BOX)

    horbarchart = obj = xf.fl_add_chart(xfc.FL_HORBAR_CHART, 20, 190, 210, 140,
                                        "HORBAR_CHART")
    xf.fl_set_object_boxtype(horbarchart, xfc.FL_RSHADOW_BOX)

    spikechart = xf.fl_add_chart(xfc.FL_SPIKE_CHART, 480, 20, 210, 140,
                                 "SPIKE_CHART")
    xf.fl_set_object_boxtype(spikechart, xfc.FL_RSHADOW_BOX)

    exitbut = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 750, 260, 140, 30, "Exit")

    xf.fl_end_form()




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

