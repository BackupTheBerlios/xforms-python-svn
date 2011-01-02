#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  minput XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
#

import sys
import xformslib as xfl



def input_cb(pobj, data):
    notused, x, y = xfl.fl_get_input_cursorpos(pobj)
    print("INPUT - x=%d y=%d\n" % x, y)


def input2_cb(pobj, data):
    notused, x, y = xfl.fl_get_input_cursorpos(pobj)
    print("INPUT2 - y=%d x=%d\n" % y, x)


def main(lsysargv, sysargv):

    xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)

    pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 400, 450)

    pobj1 = xfl.fl_add_input(xfl.FL_MULTILINE_INPUT, 30, 270, 340, 150, "")
    xfl.fl_set_object_callback(pobj1, input2_cb, 0)

    pobj2 = xfl.fl_add_input(xfl.FL_MULTILINE_INPUT, 30, 90, 340, 150, "")
    xfl.fl_set_object_lsize(pobj2, xfl.FL_NORMAL_SIZE)
    xfl.fl_set_object_callback(pobj2, input_cb, 0)

    pbut = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 160, 30, 80, 30, "Exit")

    xfl.fl_end_form()

    xfl.fl_show_form(pform, xfl.FL_PLACE_CENTERFREE, xfl.FL_FULLBORDER, \
            "MultiLineInput")

    while True:
        pobj = xfl.fl_do_forms()
        if xfl.fl_is_same_object(pobj, pbut):
            break

    xfl.fl_finish()
    return 0



if __name__ == '__main__':
    print("********* minput.py *********")
    main(len(sys.argv), sys.argv)

