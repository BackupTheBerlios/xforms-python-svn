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
import xformslib as xfl



class FD_form(object):
    pform = None
    psmallerobj = None
    plargerobj = None
    pscaleobj = None
    pcell00 = None
    pexitobj = None


def create_form_form():

    fdui = FD_form()

    fdui.pform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 470, 370)
    pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 470, 370, "")
    pobj = xfl.fl_add_box(xfl.FL_SHADOW_BOX, 30, 30, 410, 70, "Scaling Forms")
    xfl.fl_set_object_color(pobj, xfl.FL_INDIANRED, xfl.FL_CORNSILK)
    xfl.fl_set_object_lsize(pobj, 16)

    fdui.psmallerobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 30, 220, \
            130, 40, "Smaller")
    fdui.plargerobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 310, 220, \
            130, 40, "Larger")
    fdui.pscaleobj = xfl.fl_add_input(xfl.FL_FLOAT_INPUT, 170, 140, \
            270, 40, "Scale:")
    fdui.pexitobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 310, 300, \
            130, 40, "Exit")
    xfl.fl_end_form()
    return fdui


def main(lsysargv, sysargv):
    sc = 1.0

    xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
    ui = create_form_form()
    strng = "%.2f" % sc
    xfl.fl_set_input(ui.pscaleobj, strng)

    xfl.fl_show_form(ui.pform, xfl.FL_PLACE_CENTER | xfl.FL_FREE_SIZE,
            xfl.FL_FULLBORDER, "Scaling")

    while True:
        oldsc = sc
        pobj = xfl.fl_do_forms()

        if xfl.fl_is_same_object(pobj, ui.pexitobj):
            sys.exit(0)
        elif xfl.fl_is_same_object(pobj, ui.psmallerobj):
            sc = sc * 0.8
        elif xfl.fl_is_same_object(pobj, ui.plargerobj):
            sc = sc / 0.8
        elif xfl.fl_is_same_object(pobj, ui.pscaleobj):
            sc = float(xfl.fl_get_input(ui.pscaleobj))

        if sc < 0.50:
            sc = 0.50
        elif sc > 3:
            sc = 3

        if sc != oldsc:
            xfl.fl_scale_form(ui.pform, sc/oldsc, sc/oldsc)
            xfl.fl_redraw_form(ui.pform)    # to avoid garbage on screen
            strng = "%.2f" % sc
            xfl.fl_set_input(ui.pscaleobj, strng)



if __name__ == '__main__':
    print ("********* rescale.py *********")
    main(len(sys.argv), sys.argv)

