#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  yesno.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# A box with two buttons and a string. Simple boxes like this
#  are very usefull for asking questions
#


import sys
import xformslib as xfl
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *



def main(lsysargv, sysargv):

    xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0 )

    pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 320, 120)

    xfl.fl_add_box(xfl.FL_NO_BOX, 0, 10, 320, 40, "Do you want to quit?")
    pyes = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 40, 70, 80, 30," Yes")
    pno = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 200, 70, 80, 30, "No")

    xfl.fl_end_form()

    xfl.fl_show_form(pform, xfl.FL_PLACE_MOUSE, xfl.FL_TRANSIENT, "Question")

    while True:
        pobj = xfl.fl_do_forms()
        if xfl.fl_is_same_object(pobj, pyes):
            xfl.fl_hide_form(pform)
            sys.exit(0)

    xfl.fl_finish()

    return 0



if __name__ == '__main__':
    print ("********* yesno.py *********")
    main(len(sys.argv), sys.argv)

