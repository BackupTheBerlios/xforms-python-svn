#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  sldsize.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a setting slider sizes
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flslider import *
from xformslib.xfdata import *




class Flsldsize(object):
    def __init__(self, lsysargv, sysargv):

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0 )
        self.pform = fl_bgn_form(FL_UP_BOX, 150, 300)

        self.psl1 = fl_add_slider(FL_VERT_SLIDER, 20, 20, 40, 180, "X")
        fl_set_object_callback(self.psl1, self.rightslider_cb, 0)

        self.psl2 = fl_add_slider(FL_VERT_SLIDER, 90, 20, 40, 180, "Y")
        fl_set_object_callback(self.psl2, self.leftslider_cb, 0)

        self.pbut = fl_add_button(FL_NORMAL_BUTTON, 40, 250, 70, 30, "Exit")
        fl_set_object_callback(self.pbut, self.exit_cb, 0)

        fl_set_slider_size(self.psl2, fl_get_slider_value(self.psl1))
        fl_set_slider_size(self.psl1, fl_get_slider_value(self.psl2))

        fl_end_form()

        fl_show_form(self.pform, FL_PLACE_CENTER, FL_NOBORDER, "Slider Size")

        while fl_do_forms():
            fl_set_slider_size(self.psl2, fl_get_slider_value(self.psl1))
            fl_set_slider_size(self.psl1, fl_get_slider_value(self.psl2))


    def exit_cb(self, pobj, data):
        fl_hide_form(self.pform)
        fl_finish()
        sys.exit(0)


    def leftslider_cb(self, pobj, data):
        fl_set_slider_size(self.psl1, fl_get_slider_value(self.psl2))


    def rightslider_cb(self, pobj, data):
        fl_set_slider_size(self.psl2, fl_get_slider_value(self.psl1))




if __name__ == '__main__':
    Flsldsize(len(sys.argv), sys.argv)

