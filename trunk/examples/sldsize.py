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
import xformslib as xfl



class Flsldsize(object):
    def __init__(self, lsysargv, sysargv):

        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0 )
        self.pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 150, 300)

        self.psl1 = xfl.fl_add_slider(xfl.FL_VERT_SLIDER, 20, 20, \
                40, 180, "X")
        xfl.fl_set_object_callback(self.psl1, self.rightslider_cb, 0)

        self.psl2 = xfl.fl_add_slider(xfl.FL_VERT_SLIDER, 90, 20, \
                40, 180, "Y")
        xfl.fl_set_object_callback(self.psl2, self.leftslider_cb, 0)

        self.pbut = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 40, 250, \
                70, 30, "Exit")
        xfl.fl_set_object_callback(self.pbut, self.exit_cb, 0)

        xfl.fl_set_slider_size(self.psl2, xfl.fl_get_slider_value(self.psl1))
        xfl.fl_set_slider_size(self.psl1, xfl.fl_get_slider_value(self.psl2))

        xfl.fl_end_form()

        xfl.fl_show_form(self.pform, xfl.FL_PLACE_CENTER, \
                xfl.FL_NOBORDER, "Slider Size")

        while xfl.fl_do_forms():
            xfl.fl_set_slider_size(self.psl2, \
                    xfl.fl_get_slider_value(self.psl1))
            xfl.fl_set_slider_size(self.psl1, \
                    xfl.fl_get_slider_value(self.psl2))


    def exit_cb(self, pobj, data):
        xfl.fl_hide_form(self.pform)
        xfl.fl_finish()
        sys.exit(0)


    def leftslider_cb(self, pobj, data):
        xfl.fl_set_slider_size(self.psl1, xfl.fl_get_slider_value(self.psl2))


    def rightslider_cb(self, pobj, data):
        xfl.fl_set_slider_size(self.psl2, xfl.fl_get_slider_value(self.psl1))



if __name__ == '__main__':
    print ("********* sldsize.py *********")
    Flsldsize(len(sys.argv), sys.argv)

