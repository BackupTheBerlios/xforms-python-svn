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



def slider_cb(pobj, data):
    strng = "%f" % xf.fl_get_slider_value(pobj)
    xf.fl_set_object_label(pboxvalue, strng)



def main(lsysargv, sysargv):
    global pboxvalue

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    pform = xf.fl_bgn_form(xfc.FL_UP_BOX, 240, 400)

    pboxvalue = xf.fl_add_box(xfc.FL_DOWN_BOX, 120, 180, 100, 30, "")
    xf.fl_set_object_lalign(pboxvalue, xfc.FL_ALIGN_CENTER)

    pslider = xf.fl_add_slider(xfc.FL_VERT_SLIDER, 40, 40, 60, 320, "")
    xf.fl_set_slider_bounds(pslider, -1, 1)
    xf.fl_set_slider_value(pslider, 0)
    xf.fl_set_object_color(pslider, xfc.FL_SLIDER_COL1, xfc.FL_GREEN)
    xf.fl_set_object_callback(pslider, slider_cb, 0)

    xf.fl_add_button(xfc.FL_RETURN_BUTTON, 120, 290, 100, 30, "Exit")

    xf.fl_end_form()

    xf.fl_show_form(pform, xfc.FL_PLACE_CENTER, xfc.FL_NOBORDER, "Slider")

    xf.fl_do_forms()
    xf.fl_finish()

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

