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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flmisc import *
from xformslib.flbutton import *
from xformslib.flinput import *
from xformslib.xfdata import *



class FD_form(object):
    pform = None
    psmallerobj = None
    plargerobj = None
    pscaleobj = None
    pcell00 = None
    pexitobj = None



def create_form_form():

    fdui = FD_form()

    fdui.pform = fl_bgn_form(FL_NO_BOX, 470, 370)
    pobj = fl_add_box(FL_UP_BOX, 0, 0, 470, 370, "")
    pobj = fl_add_box(FL_SHADOW_BOX, 30, 30, 410, 70, "Scaling Forms")
    fl_set_object_color(pobj, 9, 47)
    fl_set_object_lsize(pobj, 16)

    fdui.psmallerobj = fl_add_button(FL_NORMAL_BUTTON, 30, 220, 130, 40,
                                       "Smaller")
    fdui.plargerobj = fl_add_button(FL_NORMAL_BUTTON, 310, 220, 130, 40,
                                      "Larger")
    fdui.pscaleobj = fl_add_input(FL_FLOAT_INPUT, 170, 140, 270, 40,
                                    "Scale:")
    fdui.pexitobj = fl_add_button(FL_NORMAL_BUTTON, 310, 300, 130, 40,
                                    "Exit")
    fl_end_form()
    return fdui


def main(lsysargv, sysargv):
    sc = 1.0

    fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    ui = create_form_form()
    strng = "%.2f" % sc
    fl_set_input(ui.pscaleobj, strng)

    fl_show_form(ui.pform, FL_PLACE_CENTER | FL_FREE_SIZE,
                    FL_FULLBORDER, "Scaling")

    while True:
        oldsc = sc
        pobj = fl_do_forms()

        if fl_is_same_object(pobj, ui.pexitobj):
            sys.exit(0)
        elif fl_is_same_object(pobj, ui.psmallerobj):
            sc = sc * 0.8
        elif fl_is_same_object(pobj, ui.plargerobj):
            sc = sc / 0.8
        elif fl_is_same_object(pobj, ui.pscaleobj):
            sc = float(fl_get_input(ui.pscaleobj))

        if sc < 0.50:
            sc = 0.50
        elif sc > 3:
            sc = 3

        if sc != oldsc:
            fl_scale_form(ui.pform, sc/oldsc, sc/oldsc)
            fl_redraw_form(ui.pform)      # to avoid garbage on screen
            strng = "%.2f" % sc
            fl_set_input(ui.pscaleobj, strng)






if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

