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



def exit_cb(ob, data):
    xf.fl_hide_form(form)
    sys.exit(0)


def makeform():
    global form, button, red, redtext, green, greentext, blue, bluetext, result

    form = xf.fl_bgn_form(xfc.FL_UP_BOX, 300, 330)

    button = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 45, 15, 210, 45,
                              "A Color Editor")
    xf.fl_set_object_lsize(button, xfc.FL_LARGE_SIZE)
    xf.fl_set_object_callback(button, exit_cb, 0)

    red = xf.fl_add_dial(xfc.FL_FILL_DIAL, 30, 240, 60, 60, "Red")
    xf.fl_set_dial_bounds(red, 0.0, 255.0)
    xf.fl_set_dial_value(red, 128.0)
    xf.fl_set_object_color(red, xfc.FL_DIAL_COL1, xfc.FL_RED)
    xf.fl_set_object_return(red, xfc.FL_RETURN_CHANGED)

    redtext = xf.fl_add_box(xfc.FL_DOWN_BOX, 105, 255, 50, 25, "")

    green = xf.fl_add_dial(xfc.FL_FILL_DIAL, 30, 155, 60, 60, "Green")
    xf.fl_set_dial_bounds(green, 0.0, 255.0)
    xf.fl_set_dial_value(green, 128.0)
    xf.fl_set_dial_angles(green, 45.0, 360 - 45.0)
    xf.fl_set_object_color(green, xfc.FL_DIAL_COL1, xfc.FL_GREEN)
    xf.fl_set_object_return(green, xfc.FL_RETURN_CHANGED)

    greentext = xf.fl_add_box(xfc.FL_DOWN_BOX, 105, 170, 50, 25,"")

    blue = xf.fl_add_dial(xfc.FL_FILL_DIAL, 30, 70, 60, 60, "Blue")
    xf.fl_set_dial_bounds(blue, 0.0, 255.0)
    xf.fl_set_dial_value(blue, 128.0)
    xf.fl_set_object_color(blue, xfc.FL_DIAL_COL1, xfc.FL_BLUE)
    xf.fl_set_dial_direction(blue, xfc.FL_DIAL_CCW)
    xf.fl_set_object_return(blue, xfc.FL_RETURN_CHANGED)

    bluetext = xf.fl_add_box(xfc.FL_DOWN_BOX, 105, 90, 50, 25, "")

    result = xf.fl_add_box(xfc.FL_DOWN_BOX, 180, 70, 90, 245, "")
    xf.fl_set_object_color(result, xfc.FL_FREE_COL1, xfc.FL_FREE_COL1)
    xf.fl_set_object_dblbuffer(result, 1)

    xf.fl_end_form()



def main(lsysargv, sysargv):
    strng = ""

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    makeform()

    xf.fl_show_form(form, xfc.FL_PLACE_MOUSE, xfc.FL_TRANSIENT, "A Form")

    r = xf.fl_get_dial_value(red)       # + 0.001
    g = xf.fl_get_dial_value(green)     # + 0.001
    b = xf.fl_get_dial_value(blue)      # + 0.001

    print r, g, b
    xf.fl_mapcolor(xfc.FL_FREE_COL1, r, g, b)
    xf.fl_redraw_object(result)

    strng = "%d" % r
    xf.fl_set_object_label(redtext, strng)
    strng = "%d" % g
    xf.fl_set_object_label(greentext, strng)
    strng = "%d" % b
    xf.fl_set_object_label(bluetext, strng)

    while xf.fl_do_forms():
        r = xf.fl_get_dial_value(red) + 0.001
	g = xf.fl_get_dial_value(green) + 0.001
	b = xf.fl_get_dial_value(blue) + 0.001

	xf.fl_mapcolor(xfc.FL_FREE_COL1, r, g, b)
	xf.fl_redraw_object(result)

        strng = "%d" % r
	xf.fl_set_object_label(redtext, strng)
        strng = "%d" % g
	xf.fl_set_object_label(greentext, strng)
        strng = "%d" % b
	xf.fl_set_object_label(bluetext, strng)


    xf.fl_finish()

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

