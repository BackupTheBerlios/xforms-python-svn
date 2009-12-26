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



def input_cb(ob, data):

    global x, y
    notused, x, y = xf.fl_get_input_cursorpos(ob)
    print "x=%d y=%d\n" % x, y
    print "vediamo un po"



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    form = xf.fl_bgn_form(xfc.FL_UP_BOX, 400, 450)

    obj1 = xf.fl_add_input(xfc.FL_MULTILINE_INPUT, 30, 270, 340, 150, "")
    xf.fl_set_object_callback(obj1, input_cb, 0)

    obj2 = xf.fl_add_input(xfc.FL_MULTILINE_INPUT, 30, 90, 340, 150, "")
    xf.fl_set_object_lsize(obj2, xfc.FL_NORMAL_SIZE)
    xf.fl_set_object_callback(obj2, input_cb, 0)

    but = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 160, 30, 80, 30, "Exit")
    but[0].u_ldata = xfc.EXITVAL

    xf.fl_end_form()

    xf.fl_show_form(form, xfc.FL_PLACE_CENTERFREE, xfc.FL_FULLBORDER, \
                    "MultiLineInput")

    while True:
        obj = xf.fl_do_forms()
        if obj[0].u_ldata == but[0].u_ldata:
            break

    xf.fl_finish()

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

