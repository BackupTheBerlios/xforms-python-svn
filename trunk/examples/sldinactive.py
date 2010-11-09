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
import xformslib as xfl



def exitcb(pobj, data):
    xfl.fl_finish()
    sys.exit(0)


def main(lsysargv, sysargv):
    xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 150 ,300)

    psl1 = xfl.fl_add_slider(xfl.FL_VERT_SLIDER, 20, 20, 40, 180, "X")
    psl2 = xfl.fl_add_slider(xfl.FL_VERT_SLIDER, 90, 20, 40, 180, "1-X")
    xfl.fl_deactivate_object(psl2)
    pbut = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 40, 250, 70, 30, "Exit")
    xfl.fl_set_object_callback(pbut, exitcb, 0)

    xfl.fl_end_form()

    xfl.fl_show_form(pform, xfl.FL_PLACE_CENTER, xfl.FL_NOBORDER, \
            "Inactive Slider")

    while True:
        pobj = xfl.fl_do_forms()
        xfl.fl_set_slider_value(psl2, 1.0 - xfl.fl_get_slider_value(psl1))

    xfl.fl_hide_form(pform)
    xfl.fl_finish()

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
