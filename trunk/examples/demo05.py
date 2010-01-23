#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  demo05.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a slider. Every time the slider changes
#   position it is returned by do_forms() and the text field showing its
#   value is adapted.
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flslider import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *




class Demo05(object):
    def __init__(self, lsysargv, sysargv):
        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        pform = fl_bgn_form(FL_UP_BOX, 240, 400)

        self.pboxvalue = fl_add_box(FL_DOWN_BOX, 120, 180, 100, 30, "")
        fl_set_object_lalign(self.pboxvalue, FL_ALIGN_CENTER)

        pslider = fl_add_slider(FL_VERT_SLIDER, 40, 40, 60, 320, "")
        fl_set_slider_bounds(pslider, -1, 1)
        fl_set_slider_value(pslider, 0)
        fl_set_object_color(pslider, FL_SLIDER_COL1, FL_GREEN)
        fl_set_object_callback(pslider, self.slider_cb, 0)

        fl_add_button(FL_RETURN_BUTTON, 120, 290, 100, 30, "Exit")

        fl_end_form()
        fl_show_form(pform, FL_PLACE_CENTER, FL_NOBORDER, "Slider")

        fl_do_forms()
        fl_finish()


    def slider_cb(self, pobj, data):
        strng = "%f" % fl_get_slider_value(pobj)
        fl_set_object_label(self.pboxvalue, strng)




if __name__ == '__main__':
    Demo05(len(sys.argv), sys.argv)

