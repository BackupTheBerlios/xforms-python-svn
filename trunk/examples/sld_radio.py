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
import xformslib as xfl



def main(lsysarg, sysargv):

    xfl.fl_initialize(lsysarg, sysargv, "FormDemo", 0, 0)

    pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 300, 300)
    psl = xfl.fl_add_slider(xfl.FL_VERT_SLIDER, 40, 40, 60, 220, "X")
    psl.contents.radio = 1
    pbut1 = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 140, 220, \
            120, 40, "0.0")
    pbut2 = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 140, 160, \
            120, 40, "0.5")
    pbut3 = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 140, 100, \
            120, 40, "1.0")
    pbut = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 140, 40, 120, 40, "Exit")
    xfl.fl_end_form()

    xfl.fl_show_form(pform, xfl.FL_PLACE_CENTER, xfl.FL_NOBORDER, "slRadio")

    while True:
        pobj = xfl.fl_do_forms()
        if xfl.fl_is_same_object(pobj, pbut1):
            xfl.fl_set_slider_value(psl, 0.0)
        elif xfl.fl_is_same_object(pobj, pbut2):
            xfl.fl_set_slider_value(psl, 0.5)
        elif xfl.fl_is_same_object(pobj, pbut3):
            xfl.fl_set_slider_value(psl, 1.0)
        elif xfl.fl_is_same_object(pobj, pbut):
            break

    xfl.fl_finish()
    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
