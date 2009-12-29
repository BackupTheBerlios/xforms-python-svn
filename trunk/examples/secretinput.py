#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  secretinput.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Demo showing secret input fields
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc


def exitcb(pobj, data):
    xf.fl_hide_form(pform)
    xf.fl_finish()
    sys.exit(0)


def main(lsysargv, sysargv):
    global pform

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    pform = xf.fl_bgn_form(xfc.FL_UP_BOX, 400, 300)
    ppassword1 = xf.fl_add_input(xfc.FL_SECRET_INPUT, 140, 40, \
                                 160, 40, "Password 1:")
    ppassword2 = xf.fl_add_input(xfc.FL_SECRET_INPUT, 140, 100, \
                                 160, 40, "Password 2:")
    pinfo = xf.fl_add_box(xfc.FL_SHADOW_BOX, 20, 160, 360, 40, "")
    pbut = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 280, 240, \
                            100, 40, "Quit")
    xf.fl_set_object_callback(pbut, exitcb, 0)

    xf.fl_end_form()

    xf.fl_show_form(pform, xfc.FL_PLACE_MOUSE, xfc.FL_NOBORDER, 0)

    while xf.fl_do_forms():
        strng = "Password 1 is: %s , Password 2 is: %s" % \
                (xf.fl_get_input(ppassword1), xf.fl_get_input(ppassword2))
        xf.fl_set_object_label(pinfo, strng)


    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

