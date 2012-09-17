#!/usr/bin/env python3

#  This file is part of xforms-python, and it has been ported from
#  pushme.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#

import sys
import xformslib as xfl


def main(lsysargv, sysargv):
    xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
    psimpleform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 230, 160)
    xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 40, 50, 150, 60, "Push Me")
    xfl.fl_end_form()
    xfl.fl_show_form(psimpleform, xfl.FL_PLACE_MOUSE, \
            xfl.FL_NOBORDER, "PushMe")
    xfl.fl_do_forms()
    xfl.fl_hide_form(psimpleform)
    return 0


if __name__ == '__main__':
    print ("********* pushme.py *********")
    main(len(sys.argv), sys.argv)
