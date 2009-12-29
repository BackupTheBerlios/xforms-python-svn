#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  minput XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
#


import sys
from xformslib import library as xf
from xformslib import xfdata as xfc



def input_cb(pobj, data):
    notused, x, y = xf.fl_get_input_cursorpos(pobj)
    print "x=%d y=%d\n" % x, y


def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    pform = xf.fl_bgn_form(xfc.FL_UP_BOX, 400, 450)

    xf.fl_add_input(xfc.FL_MULTILINE_INPUT, 30, 270, 340, 150, "")

    pobj2 = xf.fl_add_input(xfc.FL_MULTILINE_INPUT, 30, 90, 340, 150, "")
    xf.fl_set_object_lsize(pobj2, xfc.FL_NORMAL_SIZE)

    pbut = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 160, 30, 80, 30, "Exit")

    xf.fl_end_form()

    xf.fl_show_form(pform, xfc.FL_PLACE_CENTERFREE, xfc.FL_FULLBORDER, \
                    "MultiLineInput")

    while True:
        pobj = xf.fl_do_forms()
        if xf.fl_is_same_object(pobj, pbut):
            break

    xf.fl_finish()

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

