#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  pushme.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#

import sys
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.xfdata import *



def main(lsysargv, sysargv):

    fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    psimpleform = fl_bgn_form(FL_UP_BOX, 230, 160)
    fl_add_button(FL_NORMAL_BUTTON, 40, 50, 150, 60, "Push Me")
    fl_end_form()

    fl_show_form(psimpleform, FL_PLACE_MOUSE, FL_NOBORDER, "PushMe")

    fl_do_forms()
    fl_hide_form(psimpleform)
    return 0


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

