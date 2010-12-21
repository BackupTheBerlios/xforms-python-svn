#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  yesno_cb.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# same functionality as yesno, but with callbacks.
#

import sys
import xformslib as xfl



def yes_push(pobj, data):
    print "Yes is pushed"
    sys.exit(0)


def no_push(pobj, data):
    print "No is pushed"


def main(lsysargv, sysargv):
    xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)

    pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 320, 120)

    xfl.fl_add_box(xfl.FL_NO_BOX, 80, 20, 160, 40, "Do you want to Quit?")
    pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 40, 70, 80, 30, "Yes")
    xfl.fl_set_object_callback(pobj, yes_push, 0)
    pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 200, 70, 80, 30, "No")
    xfl.fl_set_object_callback(pobj, no_push, 0)

    xfl.fl_end_form()

    xfl.fl_show_form(pform, xfl.FL_PLACE_MOUSE, xfl.FL_TRANSIENT, "Question")

    xfl.fl_do_forms()

    xfl.fl_hide_form(pform)
    xfl.fl_finish()
    return 0



if __name__ == '__main__':
    print ("********* yesno_cb.py *********")
    main(len(sys.argv), sys.argv)

