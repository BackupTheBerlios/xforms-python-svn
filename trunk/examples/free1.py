#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  free1.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo is meant to demonstrate the use of a free
#  object in a form.
#

import sys
from xformslib import library as xf
from xformslib import xfdata as xfc



# The call back routine

def handle_free1(pobj, event, mx, my, key, ev):

    global dcol, on

    if event == xfc.FL_DRAW:
        xf.fl_rectf(pobj.contents.x, pobj.contents.y, pobj.contents.w, \
                    pobj.contents.h, pobj.contents.u_ldata)
    elif event == xfc.FL_RELEASE:
        on = not on
    elif event == xfc.FL_STEP:
        if on:
            if pobj.contents.u_ldata >= cole:
                dcol = -1
            elif pobj.contents.u_ldata <= xfc.FL_FREE_COL1:
                dcol = 1
            pobj.contents.u_ldata += dcol
            xf.fl_redraw_object(pobj)

    return 0


def done(pobj, data):
    xf.fl_finish()
    sys.exit(0)




def main(lsysargv, sysargv):
    global cole
    global on, dcol
    dcol = on = 1

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    pform = xf.fl_bgn_form(xfc.FL_UP_BOX, 400, 400)
    pobj1 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 320, 20, 40, 30, \
                            "Exit")
    xf.fl_set_object_callback(pobj1, done, 0)

    pobj2 = xf.fl_add_free(xfc.FL_CONTINUOUS_FREE, 40, 80, 320, 280, \
                          "", handle_free1)
    xf.fl_end_form()

    depth  = xf.fl_get_visual_depth()

    # Can't do it if less than 4 bit deep...
    if depth < 4:
        print "This Demo requires a depth of at least 4 bits\n"
        xf.fl_finish()
        sys.exit(1)
    # ...but too large a depth also won't do
    elif depth > 7:
        depth = 7

    cole = (1 << depth) - 1
    if cole > 64:
        cole = 64

    pobj2.contents.u_ldata = col = xfc.FL_FREE_COL1
    cole += col

    for i in range(col, cole + 1):
        j =  255 * (i - col) / (cole - col)
        xf.fl_mapcolor(i, j, j, j)

    xf.fl_show_form(pform, xfc.FL_PLACE_CENTER, xfc.FL_NOBORDER, \
                    "Free Object")
    xf.fl_do_forms()

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

