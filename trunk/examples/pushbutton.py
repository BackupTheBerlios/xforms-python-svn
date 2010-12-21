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
import xformslib as xfl



class Flpushbtn(object):
    def __init__(self, lsysarg, sysarg):
        self.pabox = [0] * 8

        xfl.fl_initialize(lsysarg, sysarg, "FormDemo", None, 0)
        self.makeform()

        xfl.fl_show_form(self.pform, xfl.FL_PLACE_CENTER, xfl.FL_NOBORDER, \
                "Push Buttons")
        # xfl.fl_do_forms will return only when Exit is pressed
        xfl.fl_do_forms()
        xfl.fl_finish()


    def push_cb(self, pobj, n):
        if xfl.fl_get_button(pobj):
            xfl.fl_show_object(self.pabox[n])
        else:
            xfl.fl_hide_object(self.pabox[n])


    def makeform(self):
        self.pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 400, 400)

        for i in range(0, 8):
            pobj = xfl.fl_add_button(xfl.FL_PUSH_BUTTON, 40, 310 - 40 * i, \
                    80, 30, "")
            xfl.fl_set_object_color(pobj, xfl.FL_BLACK + i + 1, \
                    xfl.FL_BLACK + i + 1)
            xfl.fl_set_object_callback(pobj, self.push_cb, i)

            self.pabox[i] = xfl.fl_add_box(xfl.FL_DOWN_BOX, 150 + 30 * i, \
                    40, 25, 320, "")
            xfl.fl_set_object_color(self.pabox[i], xfl.FL_BLACK + i + 1, \
                    xfl.FL_BLACK + i + 1)
            xfl.fl_hide_object(self.pabox[i])

        xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 40, 350, 80, 30, "Exit")
        xfl.fl_end_form()



if __name__ == '__main__':
    print ("********* pushbutton.py *********")
    Flpushbtn(len(sys.argv), sys.argv)
