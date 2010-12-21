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
import xformslib as xfl



class Demo05(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)

        pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 240, 400)

        self.pboxvalue = xfl.fl_add_box(xfl.FL_DOWN_BOX, 120, 180, 100, 30, "")
        xfl.fl_set_object_lalign(self.pboxvalue, xfl.FL_ALIGN_CENTER)

        pslider = xfl.fl_add_slider(xfl.FL_VERT_SLIDER, 40, 40, 60, 320, "")
        xfl.fl_set_slider_bounds(pslider, -1, 1)
        xfl.fl_set_slider_value(pslider, 0)
        xfl.fl_set_object_color(pslider, xfl.FL_SLIDER_COL1, xfl.FL_GREEN)
        xfl.fl_set_object_callback(pslider, self.slider_cb, 0)

        xfl.fl_add_button(xfl.FL_RETURN_BUTTON, 120, 290, 100, 30, "Exit")

        xfl.fl_end_form()
        xfl.fl_show_form(pform, xfl.FL_PLACE_CENTER, xfl.FL_NOBORDER, "Slider")

        xfl.fl_do_forms()
        xfl.fl_finish()


    def slider_cb(self, pobj, data):
        strng = "%f" % xfl.fl_get_slider_value(pobj)
        xfl.fl_set_object_label(self.pboxvalue, strng)



if __name__ == '__main__':
    print("********* demo05.py *********")
    appl = Demo05(len(sys.argv), sys.argv)
