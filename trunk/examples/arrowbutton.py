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
from xformslib import flbasic, flxbasic, flbutton, xfdata



def exit_cb(pobj, data):
    flxbasic.fl_finish()
    sys.exit(1)

def main(lsysargv, sysargv):

    flxbasic.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    pform = flbasic.fl_bgn_form(xfdata.FL_UP_BOX, 400, 400)

    pobj1 = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 50, 250, 100, 100, "@1")
    flbasic.fl_set_object_lcol(pobj1, xfdata.FL_BLUE)

    pobj2 = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 150, 250, 100, 100, "@2")
    flbasic.fl_set_object_lcol(pobj2, xfdata.FL_BLUE)

    pobj3 = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 250, 250, 100, 100, "@3")
    flbasic.fl_set_object_lcol(pobj3, xfdata.FL_BLUE)

    pobj4 = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 50, 150, 100, 100, "@4")
    flbasic.fl_set_object_lcol(pobj4, xfdata.FL_BLUE)

    pobj5 = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 250, 150, 100, 100, "@6")
    flbasic.fl_set_object_lcol(pobj5, xfdata.FL_BLUE)

    pobj6 = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 50, 50, 100, 100, "@7")
    flbasic.fl_set_object_lcol(pobj6, xfdata.FL_BLUE)

    pobj7 = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 150, 50, 100, 100, "@8")
    flbasic.fl_set_object_lcol(pobj7, xfdata.FL_BLUE)

    pobj8 = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 250, 50, 100, 100, "@9")
    flbasic.fl_set_object_lcol(pobj8, xfdata.FL_BLUE)

    pobjexit = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 150, 150, 100, 100, "@square")
    flbasic.fl_set_object_lcol(pobjexit, xfdata.FL_GREEN)
    flbasic.fl_set_object_color(pobjexit, xfdata.FL_MAGENTA, xfdata.FL_RED)

    flbasic.fl_set_object_callback(pobjexit, exit_cb, 0)

    flbasic.fl_end_form()

    flbasic.fl_show_form(pform, xfdata.FL_PLACE_ASPECT, xfdata.FL_TRANSIENT, "Buttons")

    while flbasic.fl_do_forms():
        pass                    # empty


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

