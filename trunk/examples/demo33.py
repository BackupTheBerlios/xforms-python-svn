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
from xformslib import xfconst as xfc


bmpfilename = "srs.xbm"


def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0 )
    form = xf.fl_bgn_form(xfc.FL_UP_BOX, 200, 200)

    obj = xf.fl_add_bitmap(xfc.FL_NORMAL_BITMAP, 50, 50, 100, 100, "A bitmap")
    xf.fl_set_object_lcol(obj, xfc.FL_BLUE)
    xf.fl_add_button(xfc.FL_HIDDEN_BUTTON, 50, 50, 100, 100, "")

    xf.fl_end_form()

    # xf.fl_set_bitmap_data replaced
    xf.fl_set_bitmap_file(obj, bmpfilename)

    xf.fl_show_form(form, xfc.FL_PLACE_MOUSE, xfc.FL_NOBORDER, "X Bitmap")

    xf.fl_do_forms()
    xf.fl_hide_form(form)
    xf.fl_finish()

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

