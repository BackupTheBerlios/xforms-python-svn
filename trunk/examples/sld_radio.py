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

    form = xf.fl_bgn_form(xfc.FL_UP_BOX, 300, 300)
    sl = xf.fl_add_slider(xfc.FL_VERT_SLIDER, 40, 40, 60, 220, "X")
    sl[0].radio = 1
    but1 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 140, 220, 120, 40, "0.0")
    but1[0].u_ldata = 252
    but2 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 140, 160, 120, 40, "0.5")
    but2[0].u_ldata = 253
    but3 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 140, 100, 120, 40, "1.0")
    but3[0].u_ldata = 254
    but = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 140, 40, 120, 40, "Exit")
    but[0].u_ldata = xfc.EXITVAL
    xf.fl_end_form()

    xf.fl_show_form(form, xfc.FL_PLACE_CENTER, xfc.FL_NOBORDER, "slRadio")

    while True:
        obj = xf.fl_do_forms()
        if obj[0].u_ldata == but1[0].u_ldata:
            xf.fl_set_slider_value(sl, 0.0)
        elif obj[0].u_ldata == but2[0].u_ldata:
            xf.fl_set_slider_value(sl, 0.5)
        elif obj[0].u_ldata == but3[0].u_ldata:
            xf.fl_set_slider_value(sl, 1.0)
        elif obj[0].u_ldata == but[0].u_ldata:
            break

    xf.fl_finish()
    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)


