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
from xformslib import library as xf
from xformslib import xfdata as xfc



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0 )

    form = xf.fl_bgn_form(xfc.FL_UP_BOX, 320, 120)

    xf.fl_add_box(xfc.FL_NO_BOX, 0, 10, 320, 40, "Do you want to quit?")
    yes = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 40, 70, 80, 30," Yes")
    yes[0].u_ldata = 254
    no = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 200, 70, 80, 30, "No")

    xf.fl_end_form()

    xf.fl_show_form(form, xfc.FL_PLACE_MOUSE, xfc.FL_TRANSIENT, "Question")

    while True:
        obj = xf.fl_do_forms()
        if obj[0].u_ldata == yes[0].u_ldata:
            xf.fl_hide_form(form)
            sys.exit(0)

    xf.fl_finish()

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
