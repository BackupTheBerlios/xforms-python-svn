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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *




def yes_push(pobj, data):
    print "Yes is pushed\n"
    sys.exit(0)


def no_push(pobj, data):
    print "No is pushed\n"


def main(lsysargv, sysargv):

    fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    pform = fl_bgn_form(FL_UP_BOX, 320, 120)

    fl_add_box(FL_NO_BOX, 80, 20, 160, 40, "Do you want to Quit?")

    pobj = fl_add_button(FL_NORMAL_BUTTON, 40, 70, 80, 30, "Yes")
    fl_set_object_callback(pobj, yes_push, 0)

    pobj = fl_add_button(FL_NORMAL_BUTTON, 200, 70, 80, 30, "No")
    fl_set_object_callback(pobj, no_push, 0)

    fl_end_form()

    fl_show_form(pform, FL_PLACE_MOUSE, FL_TRANSIENT, "Question")

    fl_do_forms()

    fl_hide_form(pform)
    fl_finish()
    return 0


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

