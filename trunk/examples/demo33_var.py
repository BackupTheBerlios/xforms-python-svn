#!/usr/bin/env python3

#  This file is part of xforms-python, and it is a variant of
#  demo33.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Testing bitmaps Class.
#

import sys
import xformslib as xfl


bmpfilename = "srs.xbm"


def main(lsysargv, sysargv):
    xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0 )
    pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 200, 200)
    pobj = xfl.fl_add_bitmap(xfl.FL_NORMAL_BITMAP, 50, 50, 100, 100, \
            "A bitmap")
    xfl.fl_set_object_lcol(pobj, xfl.FL_BLUE)
    xfl.fl_add_button(xfl.FL_HIDDEN_BUTTON, 50, 50, 100, 100, "")
    xfl.fl_end_form()
    xfl.fl_set_bitmap_file(pobj, bmpfilename)
    xfl.fl_show_form(pform, xfl.FL_PLACE_MOUSE, xfl.FL_NOBORDER, \
            "X Bitmap")
    xfl.fl_do_forms()
    xfl.fl_hide_form(pform)
    xfl.fl_finish()
    return 0


if __name__ == '__main__':
    print("********* demo33_var.py *********")
    main(len(sys.argv), sys.argv)
