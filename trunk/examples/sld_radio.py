#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  sld_radio.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a slider as radio object
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flslider import *
from xformslib.xfdata import *




def main(lsysarg, sysargv):

    fl_initialize(lsysarg, sysargv, "FormDemo", 0, 0)

    pform = fl_bgn_form(FL_UP_BOX, 300, 300)
    psl = fl_add_slider(FL_VERT_SLIDER, 40, 40, 60, 220, "X")
    psl.contents.radio = 1
    pbut1 = fl_add_lightbutton(FL_RADIO_BUTTON, 140, 220, 120, 40, "0.0")
    pbut2 = fl_add_lightbutton(FL_RADIO_BUTTON, 140, 160, 120, 40, "0.5")
    pbut3 = fl_add_lightbutton(FL_RADIO_BUTTON, 140, 100, 120, 40, "1.0")
    pbut = fl_add_button(FL_NORMAL_BUTTON, 140, 40, 120, 40, "Exit")
    fl_end_form()

    fl_show_form(pform, FL_PLACE_CENTER, FL_NOBORDER, "slRadio")

    while True:
        pobj = fl_do_forms()
        if fl_is_same_object(pobj, pbut1):
            fl_set_slider_value(psl, 0.0)
        elif fl_is_same_object(pobj, pbut2):
            fl_set_slider_value(psl, 0.5)
        elif fl_is_same_object(pobj, pbut3):
            fl_set_slider_value(psl, 1.0)
        elif fl_is_same_object(pobj, pbut):
            break

    fl_finish()
    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)


