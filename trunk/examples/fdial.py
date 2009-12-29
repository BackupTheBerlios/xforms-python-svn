#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  fdial.c XForms demo, with some adaptations.
#
#  fdial.c was written by M. Overmars and T.C. Zhao
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This is an example of the use of filled dials, dial range
# and dial direction.
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



def exit_cb(pobj, data):
    xf.fl_hide_form(pform)
    sys.exit(0)


def makeform():
    global pform, pbutton, pred, predtext, pgreen, pgreentext
    global pblue, pbluetext, presult

    pform = xf.fl_bgn_form(xfc.FL_UP_BOX, 300, 330)

    pbutton = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 45, 15, 210, 45,
                              "A Color Editor")
    xf.fl_set_object_lsize(pbutton, xfc.FL_LARGE_SIZE)
    xf.fl_set_object_callback(pbutton, exit_cb, 0)

    pred = xf.fl_add_dial(xfc.FL_FILL_DIAL, 30, 240, 60, 60, "Red")
    xf.fl_set_dial_bounds(pred, 0.0, 255.0)
    xf.fl_set_dial_value(pred, 128.0)
    xf.fl_set_object_color(pred, xfc.FL_DIAL_COL1, xfc.FL_RED)
    xf.fl_set_object_return(pred, xfc.FL_RETURN_CHANGED)

    predtext = xf.fl_add_box(xfc.FL_DOWN_BOX, 105, 255, 50, 25, "")

    pgreen = xf.fl_add_dial(xfc.FL_FILL_DIAL, 30, 155, 60, 60, "Green")
    xf.fl_set_dial_bounds(pgreen, 0.0, 255.0)
    xf.fl_set_dial_value(pgreen, 128.0)
    xf.fl_set_dial_angles(pgreen, 45.0, 360 - 45.0)
    xf.fl_set_object_color(pgreen, xfc.FL_DIAL_COL1, xfc.FL_GREEN)
    xf.fl_set_object_return(pgreen, xfc.FL_RETURN_CHANGED)

    pgreentext = xf.fl_add_box(xfc.FL_DOWN_BOX, 105, 170, 50, 25,"")

    pblue = xf.fl_add_dial(xfc.FL_FILL_DIAL, 30, 70, 60, 60, "Blue")
    xf.fl_set_dial_bounds(pblue, 0.0, 255.0)
    xf.fl_set_dial_value(pblue, 128.0)
    xf.fl_set_object_color(pblue, xfc.FL_DIAL_COL1, xfc.FL_BLUE)
    xf.fl_set_dial_direction(pblue, xfc.FL_DIAL_CCW)
    xf.fl_set_object_return(pblue, xfc.FL_RETURN_CHANGED)

    pbluetext = xf.fl_add_box(xfc.FL_DOWN_BOX, 105, 90, 50, 25, "")

    presult = xf.fl_add_box(xfc.FL_DOWN_BOX, 180, 70, 90, 245, "")
    xf.fl_set_object_color(presult, xfc.FL_FREE_COL1, xfc.FL_FREE_COL1)
    xf.fl_set_object_dblbuffer(presult, 1)

    xf.fl_end_form()



def main(lsysargv, sysargv):
    strng = ""

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    makeform()

    xf.fl_show_form(pform, xfc.FL_PLACE_MOUSE, xfc.FL_TRANSIENT, "A Form")

    r = xf.fl_get_dial_value(pred)       # + 0.001
    g = xf.fl_get_dial_value(pgreen)     # + 0.001
    b = xf.fl_get_dial_value(pblue)      # + 0.001

    xf.fl_mapcolor(xfc.FL_FREE_COL1, r, g, b)
    xf.fl_redraw_object(presult)

    strng = "%d" % r
    xf.fl_set_object_label(predtext, strng)
    strng = "%d" % g
    xf.fl_set_object_label(pgreentext, strng)
    strng = "%d" % b
    xf.fl_set_object_label(pbluetext, strng)

    while xf.fl_do_forms():
        r = xf.fl_get_dial_value(pred) + 0.001
        g = xf.fl_get_dial_value(pgreen) + 0.001
        b = xf.fl_get_dial_value(pblue) + 0.001

        xf.fl_mapcolor(xfc.FL_FREE_COL1, r, g, b)
        xf.fl_redraw_object(presult)

        strng = "%d" % r
        xf.fl_set_object_label(predtext, strng)
        strng = "%d" % g
        xf.fl_set_object_label(pgreentext, strng)
        strng = "%d" % b
        xf.fl_set_object_label(pbluetext, strng)


    xf.fl_finish()

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

