#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  sldinactive.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a slider that is not active
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flslider import *
from xformslib.xfdata import *




def exitcb(pobj, data):
    fl_finish()
    sys.exit(0)


def main(lsysargv, sysargv):
    fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    pform = fl_bgn_form(FL_UP_BOX, 150 ,300)
    psl1 = fl_add_slider(FL_VERT_SLIDER, 20, 20, \
                            40, 180, "X")
    psl2 = fl_add_slider(FL_VERT_SLIDER, 90, 20, \
                            40, 180, "1-X")
    fl_deactivate_object(psl2)
    pbut = fl_add_button(FL_NORMAL_BUTTON, 40, 250, \
                            70, 30, "Exit")
    fl_set_object_callback(pbut, exitcb, 0)

    fl_end_form()

    fl_show_form(pform, FL_PLACE_CENTER, FL_NOBORDER, \
                    "Inactive Slider")

    while True:
        pobj = fl_do_forms()
        fl_set_slider_value(psl2, 1.0 - fl_get_slider_value(psl1))

    fl_hide_form(pform)
    fl_finish()

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

