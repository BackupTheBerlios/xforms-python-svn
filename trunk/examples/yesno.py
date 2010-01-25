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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *



def main(lsysargv, sysargv):

    fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0 )

    pform = fl_bgn_form(FL_UP_BOX, 320, 120)

    fl_add_box(FL_NO_BOX, 0, 10, 320, 40, "Do you want to quit?")
    pyes = fl_add_button(FL_NORMAL_BUTTON, 40, 70, 80, 30," Yes")
    pno = fl_add_button(FL_NORMAL_BUTTON, 200, 70, 80, 30, "No")

    fl_end_form()

    fl_show_form(pform, FL_PLACE_MOUSE, FL_TRANSIENT, "Question")

    while True:
        pobj = fl_do_forms()
        if fl_is_same_object(pobj, pyes):
            fl_hide_form(pform)
            sys.exit(0)

    fl_finish()

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

