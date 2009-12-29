#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  demo33.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Testing bitmaps Class.
#


import sys
from xformslib import library as xf
from xformslib import xfdata as xfc


bmpfilename = "srs.xbm"


def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0 )
    pform = xf.fl_bgn_form(xfc.FL_UP_BOX, 200, 200)

    pobj = xf.fl_add_bitmap(xfc.FL_NORMAL_BITMAP, 50, 50, 100, 100, "A bitmap")
    xf.fl_set_object_lcol(pobj, xfc.FL_BLUE)
    xf.fl_add_button(xfc.FL_HIDDEN_BUTTON, 50, 50, 100, 100, "")

    xf.fl_end_form()

    # xf.fl_set_bitmap_data not used
    xf.fl_set_bitmap_file(pobj, bmpfilename)

    xf.fl_show_form(pform, xfc.FL_PLACE_MOUSE, xfc.FL_NOBORDER, "X Bitmap")

    xf.fl_do_forms()
    xf.fl_hide_form(pform)
    xf.fl_finish()

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

