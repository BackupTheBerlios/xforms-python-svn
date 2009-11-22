#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  arrowbutton.c XForms demo, with some adaptation.
#
#  arrowbutton.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of special symbol labels
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfconst as xfc


def exit_cb(obj, data):
    xf.fl_finish()
    sys.exit(1)

def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    form = xf.fl_bgn_form(xfc.FL_UP_BOX, 400, 400)

    obj1 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 50, 250, 100, 100, "@1")
    xf.fl_set_object_lcol(obj1, xfc.FL_BLUE)

    obj2 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 150, 250, 100, 100, "@2")
    xf.fl_set_object_lcol(obj2, xfc.FL_BLUE)

    obj3 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 250, 100, 100, "@3")
    xf.fl_set_object_lcol(obj3, xfc.FL_BLUE)

    obj4 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 50, 150, 100, 100, "@4")
    xf.fl_set_object_lcol(obj4, xfc.FL_BLUE)

    obj5 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 150, 100, 100, "@6")
    xf.fl_set_object_lcol(obj5, xfc.FL_BLUE)

    obj6 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 50, 50, 100, 100, "@7")
    xf.fl_set_object_lcol(obj6, xfc.FL_BLUE)

    obj7 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 150, 50, 100, 100, "@8")
    xf.fl_set_object_lcol(obj7, xfc.FL_BLUE)

    obj8 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 50, 100, 100, "@9")
    xf.fl_set_object_lcol(obj8, xfc.FL_BLUE)

    objexit = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 150, 150, 100, 100, "@square")
    xf.fl_set_object_lcol(objexit, xfc.FL_GREEN)
    xf.fl_set_object_color(objexit, xfc.FL_MAGENTA, xfc.FL_RED)

    xf.fl_set_object_callback(objexit, exit_cb, 0)

    xf.fl_end_form()

    xf.fl_show_form(form, xfc.FL_PLACE_ASPECT, xfc.FL_TRANSIENT, "Buttons")

    while xf.fl_do_forms():
        pass                    # empty


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
    #main(0, "")
