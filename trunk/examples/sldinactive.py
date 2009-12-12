#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  sldinactive.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a slider that is not active
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc


def exitcb(ob, data):
    xf.fl_finish()
    sys.exit(0)


def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    form = xf.fl_bgn_form(xfc.FL_UP_BOX, 150 ,300)
    sl1 = xf.fl_add_slider(xfc.FL_VERT_SLIDER, 20, 20, \
                           40, 180, "X")
    sl2 = xf.fl_add_slider(xfc.FL_VERT_SLIDER, 90, 20, \
                           40, 180, "1-X")
    xf.fl_deactivate_object(sl2)
    but = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 40, 250, \
                           70, 30, "Exit")
    xf.fl_set_object_callback(but, exitcb, 0)

    xf.fl_end_form()

    xf.fl_show_form(form, xfc.FL_PLACE_CENTER, xfc.FL_NOBORDER, \
                    "Inactive Slider")

    while True:
        obj = xf.fl_do_forms()
        xf.fl_set_slider_value(sl2, 1.0 - xf.fl_get_slider_value(sl1))


    xf.fl_hide_form(form)
    xf.fl_finish()

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
