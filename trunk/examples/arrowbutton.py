#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  arrowbutton.c XForms demo, with some adaptations.
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
from xformslib import xfdata as xfc


def exit_cb(pobj, data):
    xf.fl_finish()
    sys.exit(1)

def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    pform = xf.fl_bgn_form(xfc.FL_UP_BOX, 400, 400)

    pobj1 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 50, 250, 100, 100, "@1")
    xf.fl_set_object_lcol(pobj1, xfc.FL_BLUE)

    pobj2 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 150, 250, 100, 100, "@2")
    xf.fl_set_object_lcol(pobj2, xfc.FL_BLUE)

    pobj3 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 250, 100, 100, "@3")
    xf.fl_set_object_lcol(pobj3, xfc.FL_BLUE)

    pobj4 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 50, 150, 100, 100, "@4")
    xf.fl_set_object_lcol(pobj4, xfc.FL_BLUE)

    pobj5 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 150, 100, 100, "@6")
    xf.fl_set_object_lcol(pobj5, xfc.FL_BLUE)

    pobj6 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 50, 50, 100, 100, "@7")
    xf.fl_set_object_lcol(pobj6, xfc.FL_BLUE)

    pobj7 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 150, 50, 100, 100, "@8")
    xf.fl_set_object_lcol(pobj7, xfc.FL_BLUE)

    pobj8 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 50, 100, 100, "@9")
    xf.fl_set_object_lcol(pobj8, xfc.FL_BLUE)

    pobjexit = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 150, 150, 100, 100, "@square")
    xf.fl_set_object_lcol(pobjexit, xfc.FL_GREEN)
    xf.fl_set_object_color(pobjexit, xfc.FL_MAGENTA, xfc.FL_RED)

    xf.fl_set_object_callback(pobjexit, exit_cb, 0)

    xf.fl_end_form()

    xf.fl_show_form(pform, xfc.FL_PLACE_ASPECT, xfc.FL_TRANSIENT, "Buttons")

    while xf.fl_do_forms():
        pass                    # empty


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

