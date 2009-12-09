#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  ndial.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This is an example of the use of dials.
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc


global dials, texts

dials = [0, 0, 0]
texts = [0, 0, 0]


def cb(obj, data):

    cols = [128, 128, 128]

    cols[data] = xf.fl_get_dial_value(obj)
    xf.fl_mapcolor(xfc.FL_FREE_COL1, cols[0], cols[1], cols[2])
    xf.fl_redraw_object(result)
    strng = "%d" % cols[data]
    xf.fl_set_object_label(texts[data], strng)


def makeform():
    global form, result

    label = ["Red", "Green", "Blue"]
    col = [xfc.FL_RED, xfc.FL_GREEN, xfc.FL_BLUE]
    y = 70

    form = xf.fl_bgn_form(xfc.FL_UP_BOX, 300, 330)

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 45, 15, \
                           210, 45, "Color Editor")
    xf.fl_set_object_lsize(obj, xfc.FL_LARGE_SIZE)

    for i in range (0, 3):
        dials[i] = xf.fl_add_dial(xfc.FL_NORMAL_DIAL, 30, y, \
                                  60, 60, label[i])
        xf.fl_set_object_boxtype(dials[i], xfc.FL_UP_BOX)
        xf.fl_set_dial_bounds(dials[i], 0.0, 255.0)
        xf.fl_set_dial_value(dials[i], 128.0)
        xf.fl_set_object_color(dials[i], col[i], xfc.FL_DIAL_COL2)
        xf.fl_set_object_callback(dials[i], cb, i)
        xf.fl_set_object_return(dials[i], xfc.FL_RETURN_CHANGED)

        texts[i] = xf.fl_add_box(xfc.FL_DOWN_BOX, 105, y + 17, \
                                 50, 25, "128")
        y += 85

    result = xf.fl_add_box(xfc.FL_DOWN_BOX, 180, 70, 90, 245, "")
    xf.fl_set_object_color(result, xfc.FL_FREE_COL1, xfc.FL_FREE_COL1)
    xf.fl_mapcolor(xfc.FL_FREE_COL1, 128, 128, 128)
    xf.fl_set_object_dblbuffer(result, 1)       # to avoid flicker
    xf.fl_end_form()




def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    makeform()

    xf.fl_show_form(form, xfc.FL_PLACE_MOUSE, xfc.FL_TRANSIENT, \
                    "A Form")

    xf.fl_do_forms()

    xf.fl_finish()
    return 0


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
