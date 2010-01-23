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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbitmap import *
from xformslib.flbutton import *
from xformslib.xfdata import *


bmpfilename = "srs.xbm"


def main(lsysargv, sysargv):

    fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0 )
    pform = fl_bgn_form(FL_UP_BOX, 200, 200)

    pobj = fl_add_bitmap(FL_NORMAL_BITMAP, 50, 50, 100, 100, "A bitmap")
    fl_set_object_lcol(pobj, FL_BLUE)
    fl_add_button(FL_HIDDEN_BUTTON, 50, 50, 100, 100, "")

    fl_end_form()

    # fl_set_bitmap_data not used
    fl_set_bitmap_file(pobj, bmpfilename)

    fl_show_form(pform, FL_PLACE_MOUSE, FL_NOBORDER, "X Bitmap")

    fl_do_forms()
    fl_hide_form(pform)
    fl_finish()

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

