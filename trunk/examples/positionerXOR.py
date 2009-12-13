#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  positionerXOR.c XForms demo, with some adaptation.
#
#  positionerXOR.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a positioner with XOR drawmode, most
# useful for overlaying positioner on top of other object
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



# callback routine

def positioner_cb(ob, q):

    strng = "%f" % xf.fl_get_positioner_xvalue(ob)
    xf.fl_set_object_label(xval, strng)

    strng = "%f" % xf.fl_get_positioner_yvalue(ob)
    xf.fl_set_object_label(yval, strng)



def main(lsysargv, sysargv):
    global xval, yval

    xf.fl_set_border_width(-2)
    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    form = xf.fl_bgn_form(xfc.FL_UP_BOX, 350, 250)

    ob = xf.fl_add_pixmap(xfc.FL_NORMAL_PIXMAP, 60, 70, 100, 100, "")
    xf.fl_set_object_boxtype(ob, xfc.FL_DOWN_BOX)
    xf.fl_set_pixmap_file(ob, "porsche.xpm")

    pos = xf.fl_add_positioner(xfc.FL_OVERLAY_POSITIONER, 60, 70, \
                               100, 100, "")
    xf.fl_set_positioner_xbounds(pos, 0, 1)
    xf.fl_set_positioner_ybounds(pos, 0, 1)
    xf.fl_set_object_callback(pos, positioner_cb, 0)

    xval = xf.fl_add_box(xfc.FL_DOWN_BOX, 230, 40, 100, 30, "")
    xf.fl_set_object_color(xval, xfc.FL_COL1, xfc.FL_COL1)

    yval = xf.fl_add_box(xfc.FL_DOWN_BOX, 230, 90, 100, 30, "")
    xf.fl_set_object_color(yval, xfc.FL_COL1, xfc.FL_COL1)

    xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 230, 200, 100, 30, \
                     "Exit")

    xf.fl_end_form()

    xf.fl_show_form(form, xfc.FL_PLACE_CENTER, xfc.FL_TRANSIENT, \
                    "XOR Positioner")

    positioner_cb(pos, 0)
    xf.fl_do_forms()
    xf.fl_hide_form(form)
    xf.fl_finish()

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

