#!/usr/bin/env python3

#  This file is part of xforms-python, and it has been ported from
#  touchbutton.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a touch buttons.
#

import sys
#sys.path.append("..")
import xformslib as xfl



class Fltouchbtn(object):
    def __init__(self, lsysargv, sysarg):

        self.val = 0
        xfl.fl_initialize(lsysargv, sysarg, "FormDemo", None, 0)

        pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 360, 140)

        pobj = xfl.fl_add_button(xfl.FL_TOUCH_BUTTON, 50, 30, 40, 30, "@<<")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_FRAME_BOX)
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_INDIANRED)
        xfl.fl_set_object_callback(pobj, self.show_val, -5)
        xfl.fl_set_button_shortcut(pobj, "1", 0)

        pobj = xfl.fl_add_button(xfl.FL_TOUCH_BUTTON, 90, 30, 40, 30, "@<")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_FRAME_BOX)
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_INDIANRED)
        xfl.fl_set_object_callback(pobj, self.show_val, -1)
        xfl.fl_set_button_shortcut(pobj, "2",  0)

        self.pvalobj = xfl.fl_add_box(xfl.FL_BORDER_BOX, 130, 30, 100, 30, "")
        xfl.fl_set_object_color(self.pvalobj, xfl.FL_LEFT_BCOL, \
                xfl.FL_LEFT_BCOL)

        pobj = xfl.fl_add_button(xfl.FL_TOUCH_BUTTON, 230, 30, 40, 30, "@>")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_FRAME_BOX)
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_INDIANRED)
        xfl.fl_set_object_callback(pobj, self.show_val, 1)
        xfl.fl_set_button_shortcut(pobj, "3", 0)

        pobj = xfl.fl_add_button(xfl.FL_TOUCH_BUTTON, 270, 30, 40, 30, "@>>")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_FRAME_BOX)
        xfl.fl_set_object_callback(pobj, self.show_val, 5)
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_INDIANRED)
        xfl.fl_set_button_shortcut(pobj, "4", 0)

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 220, 90, \
                100, 30, "Exit")

        xfl.fl_end_form()
        xfl.fl_show_form(pform, xfl.FL_PLACE_CENTER, xfl.FL_NOBORDER, \
                "Touch Buttons")

        xfl.fl_do_forms()
        xfl.fl_finish()


    def show_val(self, pob, delta):
        self.val += delta
        strng = "%d" % self.val
        xfl.fl_set_object_label(self.pvalobj, strng)



if __name__ == '__main__':
    print ("********* touchbutton.py *********")
    Fltouchbtn(len(sys.argv), sys.argv)

