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
#from xformslib import flbasic as flba
#from xformslib import flxbasic as flxb
#from xformslib import flbutton as flbt
#from xformslib import xfdata as xfc
import xformslib as xfl


def exit_cb(pobj, data):
    xfl.fl_finish()
    sys.exit(1)

def main(lsysargv, sysargv):

    xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 400, 400)

    pobj1 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 50, 250, 100, 100, "@1")
    xfl.fl_set_object_lcol(pobj1, xfl.FL_BLUE)

    pobj2 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 150, 250, 100, 100, "@2")
    xfl.fl_set_object_lcol(pobj2, xfl.FL_BLUE)

    pobj3 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 250, 250, 100, 100, "@3")
    xfl.fl_set_object_lcol(pobj3, xfl.FL_BLUE)

    pobj4 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 50, 150, 100, 100, "@4")
    xfl.fl_set_object_lcol(pobj4, xfl.FL_BLUE)

    pobj5 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 250, 150, 100, 100, "@6")
    xfl.fl_set_object_lcol(pobj5, xfl.FL_BLUE)

    pobj6 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 50, 50, 100, 100, "@7")
    xfl.fl_set_object_lcol(pobj6, xfl.FL_BLUE)

    pobj7 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 150, 50, 100, 100, "@8")
    xfl.fl_set_object_lcol(pobj7, xfl.FL_BLUE)

    pobj8 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 250, 50, 100, 100, "@9")
    xfl.fl_set_object_lcol(pobj8, xfl.FL_BLUE)

    pobjexit = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 150, 150, 100, 100, \
                                "@square")
    xfl.fl_set_object_lcol(pobjexit, xfl.FL_GREEN)
    xfl.fl_set_object_color(pobjexit, xfl.FL_MAGENTA, xfl.FL_RED)

    xfl.fl_set_object_callback(pobjexit, exit_cb, 0)

    xfl.fl_end_form()

    xfl.fl_show_form(pform, xfl.FL_PLACE_ASPECT, xfl.FL_TRANSIENT, "Buttons")

    while xfl.fl_do_forms():
        pass                    # empty


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
