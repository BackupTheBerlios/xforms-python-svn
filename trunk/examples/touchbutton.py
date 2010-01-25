#!/usr/bin/env python

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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *



class Fltouchbtn(object):
    def __init__(self, lsysargv, sysarg):

        self.val = 0
        fl_initialize(lsysargv, sysarg, "FormDemo", 0, 0)

        pform = fl_bgn_form(FL_UP_BOX, 360, 140)

        pobj = fl_add_button(FL_TOUCH_BUTTON, 50, 30, 40, 30, "@<<")
        fl_set_object_boxtype(pobj, FL_FRAME_BOX)
        fl_set_object_color(pobj, FL_COL1, FL_INDIANRED)
        fl_set_object_callback(pobj, self.show_val, -5)
        fl_set_button_shortcut(pobj, "1", 0)

        pobj = fl_add_button(FL_TOUCH_BUTTON, 90, 30, 40, 30, "@<")
        fl_set_object_boxtype(pobj, FL_FRAME_BOX)
        fl_set_object_color(pobj, FL_COL1, FL_INDIANRED)
        fl_set_object_callback(pobj, self.show_val, -1)
        fl_set_button_shortcut(pobj, "2",  0)

        self.pvalobj = fl_add_box(FL_BORDER_BOX, 130, 30, 100, 30, "")
        fl_set_object_color(self.pvalobj, FL_LEFT_BCOL, FL_LEFT_BCOL)

        pobj = fl_add_button(FL_TOUCH_BUTTON, 230, 30, 40, 30, "@>")
        fl_set_object_boxtype(pobj, FL_FRAME_BOX)
        fl_set_object_color(pobj, FL_COL1, FL_INDIANRED)
        fl_set_object_callback(pobj, self.show_val, 1)
        fl_set_button_shortcut(pobj, "3", 0)

        pobj = fl_add_button(FL_TOUCH_BUTTON, 270, 30, 40, 30, "@>>")
        fl_set_object_boxtype(pobj, FL_FRAME_BOX)
        fl_set_object_callback(pobj, self.show_val, 5)
        fl_set_object_color(pobj, FL_COL1, FL_INDIANRED)
        fl_set_button_shortcut(pobj, "4", 0)

        pobj = fl_add_button(FL_NORMAL_BUTTON, 220, 90, 100, 30, "Exit")

        fl_end_form()
        fl_show_form(pform, FL_PLACE_CENTER, FL_NOBORDER, \
                        "Touch Buttons")

        fl_do_forms()
        fl_finish()


    def show_val(self, pob, delta):
        self.val += delta
        strng = "%d" % self.val
        fl_set_object_label(self.pvalobj, strng)



if __name__ == '__main__':
    Fltouchbtn(len(sys.argv), sys.argv)

