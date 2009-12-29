#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  rescale.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Demo for scaling forms.
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



class FD_form(object):
    pform = None
    psmallerobj = None
    plargerobj = None
    pscaleobj = None
    pcell00 = None
    pexitobj = None



def create_form_form():

    fdui = FD_form()

    fdui.pform = xf.fl_bgn_form(xfc.FL_NO_BOX, 470, 370)

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 470, 370, "")

    pobj = xf.fl_add_box(xfc.FL_SHADOW_BOX, 30, 30, 410, 70, "Scaling Forms")
    xf.fl_set_object_color(pobj, 9, 47)
    xf.fl_set_object_lsize(pobj, 16)

    fdui.psmallerobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 30, 220, 130, 40,
                                       "Smaller")

    fdui.plargerobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 310, 220, 130, 40,
                                      "Larger")

    fdui.pscaleobj = xf.fl_add_input(xfc.FL_FLOAT_INPUT, 170, 140, 270, 40,
                                    "Scale:")

    fdui.pexitobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 310, 300, 130, 40,
                                    "Exit")

    xf.fl_end_form()

    return fdui



def main(lsysargv, sysargv):
    global sc, ui
    sc = 1.0

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    ui = create_form_form()
    strng = "%.2f" % sc
    xf.fl_set_input(ui.pscaleobj, strng)

    xf.fl_show_form(ui.pform, xfc.FL_PLACE_CENTER | xfc.FL_FREE_SIZE,
                    xfc.FL_FULLBORDER, "Scaling")

    while True:
        oldsc = sc
        pobj = xf.fl_do_forms()

        if xf.fl_is_same_object(pobj, ui.pexitobj):
            sys.exit(0)
        elif xf.fl_is_same_object(pobj, ui.psmallerobj):
            sc = sc * 0.8
        elif xf.fl_is_same_object(pobj, ui.plargerobj):
            sc = sc / 0.8
        elif xf.fl_is_same_object(pobj, ui.pscaleobj):
            sc = float(xf.fl_get_input(ui.pscaleobj))

        if sc < 0.50:
            sc = 0.50
        elif sc > 3:
            sc = 3

        if sc != oldsc:
            xf.fl_scale_form(ui.pform, sc/oldsc, sc/oldsc)
            xf.fl_redraw_form(ui.pform)          # to avoid garbage on screen
            strng = "%.2f" % sc
            xf.fl_set_input(ui.pscaleobj, strng)




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

