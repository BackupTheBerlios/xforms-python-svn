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
from xformslib import library as xf
from xformslib import xfdata as xfc


def yes_push(obj, data):
    print "Yes is pushed\n"
    sys.exit(1)


def no_push(obj, data):
    print "No is pushed\n"




def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    form = xf.fl_bgn_form(xfc.FL_UP_BOX, 320, 120)

    xf.fl_add_box(xfc.FL_NO_BOX, 160, 40, 0, 0, "Do you want to Quit?")

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 40, 70, 80, 30, "Yes")
    xf.fl_set_object_callback(obj, yes_push, 0)

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 200, 70, 80, 30, "No")
    xf.fl_set_object_callback(obj, no_push, 0)

    xf.fl_end_form()

    xf.fl_show_form(form, xfc.FL_PLACE_MOUSE, xfc.FL_TRANSIENT, "Question")

    xf.fl_do_forms()

    xf.fl_hide_form(form)
    xf.fl_finish()

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

