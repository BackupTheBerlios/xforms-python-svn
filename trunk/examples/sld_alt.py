#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  sld_alt.c XForms demo, with some adaptations and modifications.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



def slider_callback(a, b):

    val = xf.fl_get_slider_value(a)

    xf.fl_set_button(pbut1, 0)
    xf.fl_set_button(pbut2, 0)
    xf.fl_set_button(pbut3, 0)

    if (val <= 0.01):
        xf.fl_set_button(pbut1, 1)
    elif (val >= 0.49 and val <= 0.51):
        xf.fl_set_button(pbut2, 1)
    elif (val >= 0.99):
        xf.fl_set_button(pbut3, 1)


def but_callback(a, b):
    xf.fl_hide_form(pform)
    sys.exit(0)

def but1_callback(a, b):
    if xf.fl_get_button(pbut1):
        xf.fl_set_slider_value(psl, 0.0)
        xf.fl_set_button(pbut2, 0)
        xf.fl_set_button(pbut3, 0)
    else:
        xf.fl_set_button(pbut1, 1)

def but2_callback(a, b):
    if xf.fl_get_button(pbut2):
        xf.fl_set_slider_value(psl, 0.5)
        xf.fl_set_button(pbut1, 0)
        xf.fl_set_button(pbut3, 0)
    else:
        xf.fl_set_button(pbut2, 1)

def but3_callback(a, b):
    if xf.fl_get_button(pbut3):
        xf.fl_set_slider_value(psl, 1.0)
        xf.fl_set_button(pbut1, 0)
        xf.fl_set_button(pbut2, 0)
    else:
        xf.fl_set_button(pbut3, 1)



def main(lsysargv, sysarg):
    global pbut1, pbut2, pbut3, pform, psl, pbut

    xf.fl_initialize(lsysargv, sysarg, "FormDemo", 0, 0)
    pform = xf.fl_bgn_form(xfc.FL_UP_BOX, 300, 300)
    psl = xf.fl_add_slider(xfc.FL_VERT_SLIDER, 40, 40, 60, 220, "X")
    xf.fl_set_slider_value(psl, 0.5)
    xf.fl_set_object_callback(psl, slider_callback, 0)
    pbut1 = xf.fl_add_lightbutton(xfc.FL_PUSH_BUTTON, 140, 220, \
                                  120, 40, "0.0")
    xf.fl_set_object_callback(pbut1, but1_callback, 0)
    pbut2 = xf.fl_add_lightbutton(xfc.FL_PUSH_BUTTON, 140, 160, \
                                 120, 40, "0.5")
    xf.fl_set_button(pbut2, 1)
    xf.fl_set_object_callback(pbut2, but2_callback, 0)
    pbut3 = xf.fl_add_lightbutton(xfc.FL_PUSH_BUTTON, 140, 100, \
                                 120, 40, "1.0")
    xf.fl_set_object_callback(pbut3, but3_callback, 0)
    pbut = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 140, 40, \
                           120, 40, "Exit")
    xf.fl_set_object_callback(pbut, but_callback, 0)
    xf.fl_end_form()

    xf.fl_show_form(pform, xfc.FL_PLACE_CENTER, xfc.FL_NOBORDER, \
                    "slRadio")

    while xf.fl_do_forms():
        pass


    xf.fl_finish()

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

