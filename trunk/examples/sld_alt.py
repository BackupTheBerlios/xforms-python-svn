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
import xformslib as xfl



class Flsldalt(object):
    def __init__(self, lsysargv, sysarg):

        xfl.fl_initialize(lsysargv, sysarg, "FormDemo", None, 0)
        self.pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 300, 300)
        self.psl = xfl.fl_add_slider(xfl.FL_VERT_SLIDER, 40, 40, 60, 220, "X")
        xfl.fl_set_slider_value(self.psl, 0.5)
        xfl.fl_set_object_callback(self.psl, self.slider_callback, 0)
        self.pbut1 = xfl.fl_add_lightbutton(xfl.FL_PUSH_BUTTON, 140, 220, \
                120, 40, "0.0")
        xfl.fl_set_object_callback(self.pbut1, self.but1_callback, 0)
        self.pbut2 = xfl.fl_add_lightbutton(xfl.FL_PUSH_BUTTON, 140, 160, \
                120, 40, "0.5")
        xfl.fl_set_button(self.pbut2, 1)
        xfl.fl_set_object_callback(self.pbut2, self.but2_callback, 0)
        self.pbut3 = xfl.fl_add_lightbutton(xfl.FL_PUSH_BUTTON, 140, 100, \
                120, 40, "1.0")
        xfl.fl_set_object_callback(self.pbut3, self.but3_callback, 0)
        self.pbut = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 140, 40, \
                120, 40, "Exit")
        xfl.fl_set_object_callback(self.pbut, self.but_callback, 0)
        xfl.fl_end_form()

        xfl.fl_show_form(self.pform, xfl.FL_PLACE_CENTER, xfl.FL_NOBORDER, \
                "slRadio")

        while xfl.fl_do_forms():
            pass

        xfl.fl_finish()


    def slider_callback(self, a, b):
        val = xfl.fl_get_slider_value(a)
        xfl.fl_set_button(self.pbut1, 0)
        xfl.fl_set_button(self.pbut2, 0)
        xfl.fl_set_button(self.pbut3, 0)
        if (val <= 0.01):
            xfl.fl_set_button(self.pbut1, 1)
        elif (val >= 0.49 and val <= 0.51):
            xfl.fl_set_button(self.pbut2, 1)
        elif (val >= 0.99):
            xfl.fl_set_button(self.pbut3, 1)


    def but_callback(self, a, b):
        xfl.fl_hide_form(self.pform)
        sys.exit(0)


    def but1_callback(self, a, b):
        if xfl.fl_get_button(self.pbut1):
            xfl.fl_set_slider_value(self.psl, 0.0)
            xfl.fl_set_button(self.pbut2, 0)
            xfl.fl_set_button(self.pbut3, 0)
        else:
            xfl.fl_set_button(self.pbut1, 1)


    def but2_callback(self, a, b):
        if xfl.fl_get_button(self.pbut2):
            xfl.fl_set_slider_value(self.psl, 0.5)
            xfl.fl_set_button(self.pbut1, 0)
            xfl.fl_set_button(self.pbut3, 0)
        else:
            xfl.fl_set_button(self.pbut2, 1)


    def but3_callback(self, a, b):
        if xfl.fl_get_button(self.pbut3):
            xfl.fl_set_slider_value(self.psl, 1.0)
            xfl.fl_set_button(self.pbut1, 0)
            xfl.fl_set_button(self.pbut2, 0)
        else:
            xfl.fl_set_button(self.pbut3, 1)



if __name__ == '__main__':
    print ("********* sld_alt.py *********")
    Flsldalt(len(sys.argv), sys.argv)

