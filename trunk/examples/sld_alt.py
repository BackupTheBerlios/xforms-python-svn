#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  sld_alt.c XForms demo, with some adaptations and modifications.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flslider import *
from xformslib.flbutton import *
from xformslib.xfdata import *




class Flsldalt(object):
    def __init__(self, lsysargv, sysarg):

        fl_initialize(lsysargv, sysarg, "FormDemo", 0, 0)
        self.pform = fl_bgn_form(FL_UP_BOX, 300, 300)
        self.psl = fl_add_slider(FL_VERT_SLIDER, 40, 40, 60, 220, "X")
        fl_set_slider_value(self.psl, 0.5)
        fl_set_object_callback(self.psl, self.slider_callback, 0)
        self.pbut1 = fl_add_lightbutton(FL_PUSH_BUTTON, 140, 220, \
                                           120, 40, "0.0")
        fl_set_object_callback(self.pbut1, self.but1_callback, 0)
        self.pbut2 = fl_add_lightbutton(FL_PUSH_BUTTON, 140, 160, \
                                             120, 40, "0.5")
        fl_set_button(self.pbut2, 1)
        fl_set_object_callback(self.pbut2, self.but2_callback, 0)
        self.pbut3 = fl_add_lightbutton(FL_PUSH_BUTTON, 140, 100, \
                                     120, 40, "1.0")
        fl_set_object_callback(self.pbut3, self.but3_callback, 0)
        self.pbut = fl_add_button(FL_NORMAL_BUTTON, 140, 40, \
                               120, 40, "Exit")
        fl_set_object_callback(self.pbut, self.but_callback, 0)
        fl_end_form()

        fl_show_form(self.pform, FL_PLACE_CENTER, FL_NOBORDER, \
                        "slRadio")

        while fl_do_forms():
            pass

        fl_finish()


    def slider_callback(self, a, b):

        val = fl_get_slider_value(a)

        fl_set_button(self.pbut1, 0)
        fl_set_button(self.pbut2, 0)
        fl_set_button(self.pbut3, 0)

        if (val <= 0.01):
            fl_set_button(self.pbut1, 1)
        elif (val >= 0.49 and val <= 0.51):
            fl_set_button(self.pbut2, 1)
        elif (val >= 0.99):
            fl_set_button(self.pbut3, 1)


    def but_callback(self, a, b):
        fl_hide_form(self.pform)
        sys.exit(0)


    def but1_callback(self, a, b):
        if fl_get_button(self.pbut1):
            fl_set_slider_value(self.psl, 0.0)
            fl_set_button(self.pbut2, 0)
            fl_set_button(self.pbut3, 0)
        else:
            fl_set_button(self.pbut1, 1)


    def but2_callback(self, a, b):
        if fl_get_button(self.pbut2):
            fl_set_slider_value(self.psl, 0.5)
            fl_set_button(self.pbut1, 0)
            fl_set_button(self.pbut3, 0)
        else:
            fl_set_button(self.pbut2, 1)


    def but3_callback(self, a, b):
        if fl_get_button(self.pbut3):
            fl_set_slider_value(self.psl, 1.0)
            fl_set_button(self.pbut1, 0)
            fl_set_button(self.pbut2, 0)
        else:
            fl_set_button(self.pbut3, 1)




if __name__ == '__main__':
    Flsldalt(len(sys.argv), sys.argv)

