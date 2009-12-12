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
    form = None
    smallerobj = None
    largerobj = None
    scaleobj = None
    cell00 = None
    exitobj = None



def create_form_form():

    fdui = FD_form()

    fdui.form = xf.fl_bgn_form(xfc.FL_NO_BOX, 470, 370)

    obj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 470, 370, "")

    obj = xf.fl_add_box(xfc.FL_SHADOW_BOX, 30, 30, 410, 70, "Scaling Forms")
    xf.fl_set_object_color(obj, 9, 47)
    xf.fl_set_object_lsize(obj, 16)

    fdui.smallerobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 30, 220, 130, 40,
                                       "Smaller")
    fdui.smallerobj[0].u_ldata = 254

    fdui.largerobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 310, 220, 130, 40,
                                      "Larger")
    fdui.largerobj[0].u_ldata = 253

    fdui.scaleobj = xf.fl_add_input(xfc.FL_FLOAT_INPUT, 170, 140, 270, 40,
                                    "Scale:")
    fdui.scaleobj[0].u_ldata = 252

    fdui.exitobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 310, 300, 130, 40,
                                    "Exit")
    fdui.exitobj[0].u_ldata = 251

    xf.fl_end_form()

    return fdui



def main(lsysargv, sysargv):
    global sc, ui
    sc = 1.0

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    ui = create_form_form()
    strng = "%.2f" % sc
    xf.fl_set_input(ui.scaleobj, strng)

    xf.fl_show_form(ui.form, xfc.FL_PLACE_CENTER | xfc.FL_FREE_SIZE,
                    xfc.FL_FULLBORDER, "Scaling")

    while True:
        oldsc = sc
        obj = xf.fl_do_forms()

        if obj[0].u_ldata == ui.exitobj[0].u_ldata:
            sys.exit(0)
        elif obj[0].u_ldata == ui.smallerobj[0].u_ldata:
            sc = sc * 0.8
        elif obj[0].u_ldata == ui.largerobj[0].u_ldata:
            sc = sc / 0.8
        elif obj[0].u_ldata == ui.scaleobj[0].u_ldata:
            sc = float(xf.fl_get_input( ui.scaleobj))

        if sc < 0.50:
            sc = 0.50
        elif sc > 3:
            sc = 3

        if sc != oldsc:
            xf.fl_scale_form(ui.form, sc/oldsc, sc/oldsc)
            xf.fl_redraw_form(ui.form)          # to avoid garbage on screen
            strng = "%.2f" % sc
            xf.fl_set_input(ui.scaleobj, strng)




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

