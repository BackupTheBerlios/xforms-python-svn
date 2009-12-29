#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  invslider.c XForms demo, with some adaptations.
#
#  invslider.c was written by M. Overmars and T.C. Zhao
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Inverted slider
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



class FD_inv(object):
    inv = None
    vdata = None
    cdata = ""
    ldata = 0
    sl = [0, 0, 0]
    done = None


def invert_it(pobj, data):

    if xf.fl_get_button(pobj):
        xf.fl_set_slider_bounds(ui.sl[0], 1.0, 0.0)
        xf.fl_set_slider_bounds(ui.sl[1], 1.0, 0.0)
        xf.fl_set_slider_bounds(ui.sl[2], 1.0, 0.0)
    else:
        xf.fl_set_slider_bounds(ui.sl[0], 0.0, 1.0)
        xf.fl_set_slider_bounds(ui.sl[1], 0.0, 1.0)
        xf.fl_set_slider_bounds(ui.sl[2], 0.0, 1.0)


def exitcb(pobj, data):
    xf.fl_finish()
    sys.exit(0)


def main(lsysargv, sysargv):
    global ui

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    ui = create_form_inv()

    # fill-in form initialization code

    xf.fl_show_form(ui.inv, xfc.FL_PLACE_CENTER | xfc.FL_FREE_SIZE, \
                    xfc.FL_TRANSIENT, "inv")

    while xf.fl_do_forms():
        pass            # empty


    return 0


# Form definition

def create_form_inv():

    fdui = FD_inv()

    fdui.inv = xf.fl_bgn_form(xfc.FL_NO_BOX, 245, 280)

    xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 245, 280, "")

    fdui.sl[0] = xf.fl_add_valslider(xfc.FL_VERT_SLIDER, 20, 30, 35, 230, "")

    fdui.sl[1] = xf.fl_add_valslider(xfc.FL_VERT_FILL_SLIDER, 65, 30, 35, 230, "")

    fdui.sl[2] = xf.fl_add_valslider(xfc.FL_VERT_NICE_SLIDER, 115, 30, 35, 230, "")
    xf.fl_set_object_boxtype(fdui.sl[2], xfc.FL_FLAT_BOX)
    xf.fl_set_object_color(fdui.sl[2], xfc.FL_COL1, xfc.FL_BLUE)

    fdui.done = xf.fl_add_button(xfc.FL_RETURN_BUTTON, 160, 235, 75, 30, "Exit")
    xf.fl_set_object_callback(fdui.done, exitcb, 0)

    pobj = xf.fl_add_checkbutton(xfc.FL_PUSH_BUTTON, 165, 30, 75, 35, "Invert")
    xf.fl_set_object_callback(pobj, invert_it, 0)

    xf.fl_end_form()

    return fdui




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

