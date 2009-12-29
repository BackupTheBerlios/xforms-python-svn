#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  sld_radio.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a slider as radio object
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



def main(lsysarg, sysargv):

    xf.fl_initialize(lsysarg, sysargv, "FormDemo", 0, 0)

    pform = xf.fl_bgn_form(xfc.FL_UP_BOX, 300, 300)
    psl = xf.fl_add_slider(xfc.FL_VERT_SLIDER, 40, 40, 60, 220, "X")
    psl.contents.radio = 1
    pbut1 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 140, 220, 120, 40, "0.0")
    pbut2 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 140, 160, 120, 40, "0.5")
    pbut3 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 140, 100, 120, 40, "1.0")
    pbut = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 140, 40, 120, 40, "Exit")
    xf.fl_end_form()

    xf.fl_show_form(pform, xfc.FL_PLACE_CENTER, xfc.FL_NOBORDER, "slRadio")

    while True:
        pobj = xf.fl_do_forms()
        if xf.fl_is_same_object(pobj, pbut1):
            xf.fl_set_slider_value(psl, 0.0)
        elif xf.fl_is_same_object(pobj, pbut2):
            xf.fl_set_slider_value(psl, 0.5)
        elif xf.fl_is_same_object(pobj, pbut3):
            xf.fl_set_slider_value(psl, 1.0)
        elif xf.fl_is_same_object(pobj, pbut):
            break

    xf.fl_finish()
    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)


