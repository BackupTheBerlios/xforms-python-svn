#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  related XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#


import sys
import xformslib as xf


def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    simpleform = xf.fl_bgn_form(xf.FL_UP_BOX, 230, 160)
    xf.fl_add_button(xf.FL_NORMAL_BUTTON, 40, 50, 150, 60, "Push Me")
    xf.fl_end_form()

    xf.fl_show_form(simpleform, xf.FL_PLACE_MOUSE, xf.FL_NOBORDER, "PushMe")

    xf.fl_do_forms()
    xf.fl_hide_form(simpleform)
    return 0


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

