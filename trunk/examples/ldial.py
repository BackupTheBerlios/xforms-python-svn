#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  ldial.c XForms demo, with some adaptation.
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


global dial, text
dial = [0, 1, 2]
text = [0, 1, 2]

RED = 0
GREEN = 1
BLUE = 2


def dial_callback(obj, arg):
    clr = [0, 1, 2]

    for i in range(RED, BLUE+1):
        clr[i] = xf.fl_get_dial_value(dial[i])

    strng = "%d" % clr[arg]
    xf.fl_set_object_label(text[arg], strng)

    xf.fl_mapcolor(xfc.FL_FREE_COL1, clr[0], clr[1], clr[2])
    xf.fl_redraw_object(result)



def makeform():
    global form, result

    txt = ["Red", "Green", "Blue"]
    clr = [xfc.FL_RED, xfc.FL_GREEN, xfc.FL_BLUE]

    form = xf.fl_bgn_form(xfc.FL_UP_BOX, 300, 330)

    quit = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 45, 15, \
                            210, 45, "A Color Editor")
    xf.fl_set_object_lsize(quit, xfc.FL_LARGE_SIZE)

    for i in range(RED, BLUE+1):
        dial[i] = xf.fl_add_dial(xfc.FL_LINE_DIAL, 30, \
                    240 - i * 85, 60, 60, txt[i])
        xf.fl_set_dial_bounds(dial[i], 0.0, 255.0)
        xf.fl_set_dial_angles(dial[i], 15.0, 345.0)
        xf.fl_set_dial_value(dial[i], 128.0)
        xf.fl_set_object_color(dial[i], clr[i], xfc.FL_DIAL_COL2)
        xf.fl_set_object_return(dial[i], xfc.FL_RETURN_CHANGED)
        xf.fl_set_object_callback(dial[i], dial_callback, i)
        text[i] = xf.fl_add_box(xfc.FL_DOWN_BOX, 105, \
                        255 - i * 85, 50, 25, "128")

    result = xf.fl_add_box(xfc.FL_DOWN_BOX, 180, 70, 90, 245, "")
    xf.fl_mapcolor(xfc.FL_FREE_COL1, 128, 128, 128)
    xf.fl_set_object_color(result, xfc.FL_FREE_COL1, xfc.FL_FREE_COL1)
    xf.fl_set_object_dblbuffer(result, 1)

    xf.fl_end_form()



def main(lsysargv, sysargv):
    xf.fl_initialize(lsysargv, sysargv, "ColorEditor", 0, 0)
    makeform()
    xf.fl_show_form(form, xf.FL_PLACE_MOUSE, xf.FL_TRANSIENT, \
                    "Color Editor")
    xf.fl_do_forms()
    xf.fl_finish()
    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

