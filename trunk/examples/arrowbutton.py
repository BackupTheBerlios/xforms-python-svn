#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  related XForms demo, with some adaptation.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of special symbol labels
#

import sys
sys.path.append("..")
import xformslib as xf

form = obj1 = obj2 = obj3 = obj4 = obj5 = obj6 = obj7 = obj8 = objexit = None

def exit_cb(obj, data):
    xf.fl_finish()
    sys.exit(1)

def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    form = xf.fl_bgn_form(xf.FL_UP_BOX, 400, 400)

    obj1 = xf.fl_add_button(xf.FL_NORMAL_BUTTON, 50, 250, 100, 100, "@1")
    xf.fl_set_object_lcol(obj1, xf.FL_BLUE)

    obj2 = xf.fl_add_button(xf.FL_NORMAL_BUTTON, 150, 250, 100, 100, "@2")
    xf.fl_set_object_lcol(obj2, xf.FL_BLUE)

    obj3 = xf.fl_add_button(xf.FL_NORMAL_BUTTON, 250, 250, 100, 100, "@3")
    xf.fl_set_object_lcol(obj3, xf.FL_BLUE)

    obj4 = xf.fl_add_button(xf.FL_NORMAL_BUTTON, 50, 150, 100, 100, "@4")
    xf.fl_set_object_lcol(obj4, xf.FL_BLUE)

    obj5 = xf.fl_add_button(xf.FL_NORMAL_BUTTON, 250, 150, 100, 100, "@6")
    xf.fl_set_object_lcol(obj5, xf.FL_BLUE)

    obj6 = xf.fl_add_button(xf.FL_NORMAL_BUTTON, 50, 50, 100, 100, "@7")
    xf.fl_set_object_lcol(obj6, xf.FL_BLUE)

    obj7 = xf.fl_add_button(xf.FL_NORMAL_BUTTON, 150, 50, 100, 100, "@8")
    xf.fl_set_object_lcol(obj7, xf.FL_BLUE)

    obj8 = xf.fl_add_button(xf.FL_NORMAL_BUTTON, 250, 50, 100, 100, "@9")
    xf.fl_set_object_lcol(obj8, xf.FL_BLUE)

    objexit = xf.fl_add_button(xf.FL_NORMAL_BUTTON, 150, 150, 100, 100, "@square")
    xf.fl_set_object_lcol(objexit, xf.FL_GREEN)
    xf.fl_set_object_color(objexit, xf.FL_MAGENTA, xf.FL_RED)

    xf.fl_set_object_callback(objexit, exit_cb, 0)

    xf.fl_end_form()

    xf.fl_show_form(form, xf.FL_PLACE_ASPECT, xf.FL_TRANSIENT, "Buttons")

    while xf.fl_do_forms():
        pass                        # empty


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
    #main(0, "")
