#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  pushbutton.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# A demo that shows the use of push buttons.
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *




class Flpushbtn(object):
    def __init__(self, lsysarg, sysarg):
        self.pabox = [0, 0, 0, 0, 0, 0, 0, 0]

        fl_initialize(lsysarg, sysarg, "FormDemo", 0, 0)
        self.makeform()

        fl_show_form(self.pform, FL_PLACE_CENTER, FL_NOBORDER, \
                        "Push Buttons")
        # fl_do_forms will return only when Exit is pressed
        fl_do_forms()
        fl_finish()


    def push_cb(self, pobj, n):
        if fl_get_button(pobj):
            fl_show_object(self.pabox[n])
        else:
            fl_hide_object(self.pabox[n])


    def makeform(self):
        self.pform = fl_bgn_form(FL_UP_BOX, 400, 400)

        for i in range(0, 8):
            pobj = fl_add_button(FL_PUSH_BUTTON, 40, 310 - 40 * i, \
                                 80, 30, "")
            fl_set_object_color(pobj, FL_BLACK + i + 1, \
                                FL_BLACK + i + 1)
            fl_set_object_callback(pobj, self.push_cb, i)

            self.pabox[i] = fl_add_box(FL_DOWN_BOX, 150 + 30 * i, 40, \
                                       25, 320, "")
            fl_set_object_color(self.pabox[i], FL_BLACK + i + 1, \
                                FL_BLACK + i + 1)
            fl_hide_object(self.pabox[i])

        fl_add_button(FL_NORMAL_BUTTON, 40, 350, 80, 30, "Exit")
        fl_end_form()





if __name__ == '__main__':
    Flpushbtn(len(sys.argv), sys.argv)

