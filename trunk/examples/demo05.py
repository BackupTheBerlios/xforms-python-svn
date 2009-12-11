#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  demo05.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a slider. Every time the slider changes
#   position it is returned by do_forms() and the text field showing its
#   value is adapted.
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



def slider_cb(ob, data):
    strng = "%f" % xf.fl_get_slider_value(ob)
    xf.fl_set_object_label(boxvalue, strng)



def main(lsysargv, sysargv):
    global boxvalue

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    form = xf.fl_bgn_form(xfc.FL_UP_BOX, 240, 400)

    boxvalue = xf.fl_add_box(xfc.FL_DOWN_BOX, 120, 180, 100, 30, "")
    xf.fl_set_object_lalign(boxvalue, xfc.FL_ALIGN_CENTER)

    slider = xf.fl_add_slider(xfc.FL_VERT_SLIDER, 40, 40, 60, 320, "")
    xf.fl_set_slider_bounds(slider, -1, 1)
    xf.fl_set_slider_value(slider, 0)
    xf.fl_set_object_color(slider, xfc.FL_SLIDER_COL1, xfc.FL_GREEN)
    xf.fl_set_object_callback(slider, slider_cb, 0)

    xf.fl_add_button(xfc.FL_RETURN_BUTTON, 120, 290, 100, 30, "Exit")

    xf.fl_end_form()

    xf.fl_show_form(form, xfc.FL_PLACE_CENTER, xfc.FL_NOBORDER, "Slider")

    xf.fl_do_forms()
    xf.fl_finish()

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

