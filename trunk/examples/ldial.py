#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  ldial.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This is an example of the use of dials.
#

import sys
#sys.path.append("..")
import xformslib as xfl


RED = 0
GREEN = 1
BLUE = 2

class Flldial(object):

    def __init__(self, lsysargv, sysargv):

        self.pdial =  [None] * 3
        self.ptext =  [None] * 3

        xfl.fl_initialize(lsysargv, sysargv, "ColorEditor", 0, 0)
        self.makeform()
        xfl.fl_show_form(self.pform, xfl.FL_PLACE_MOUSE, xfl.FL_TRANSIENT, \
                "Color Editor")
        xfl.fl_do_forms()
        xfl.fl_finish()


    def dial_callback(self, pobj, arg):
        clr = [0, 1, 2]

        for i in range(RED, BLUE+1):
            clr[i] = xfl.fl_get_dial_value(self.pdial[i])

        strng = "%d" % clr[arg]
        xfl.fl_set_object_label(self.ptext[arg], strng)

        xfl.fl_mapcolor(xfl.FL_FREE_COL1, clr[0], clr[1], clr[2])
        xfl.fl_redraw_object(self.presult)


    def makeform(self):

        txt = ["Red", "Green", "Blue"]
        clr = [xfl.FL_RED, xfl.FL_GREEN, xfl.FL_BLUE]

        self.pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 300, 330)

        pquit = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 45, 15, \
                210, 45, "A Color Editor")
        xfl.fl_set_object_lsize(pquit, xfl.FL_LARGE_SIZE)

        for i in range(RED, BLUE+1):
            self.pdial[i] = xfl.fl_add_dial(xfl.FL_LINE_DIAL, 30, \
                    240 - i * 85, 60, 60, txt[i])
            xfl.fl_set_dial_bounds(self.pdial[i], 0.0, 255.0)
            xfl.fl_set_dial_angles(self.pdial[i], 15.0, 345.0)
            xfl.fl_set_dial_value(self.pdial[i], 128.0)
            xfl.fl_set_object_color(self.pdial[i], clr[i], xfl.FL_DIAL_COL2)
            xfl.fl_set_object_return(self.pdial[i], xfl.FL_RETURN_CHANGED)
            xfl.fl_set_object_callback(self.pdial[i], self.dial_callback, i)
            self.ptext[i] = xfl.fl_add_box(xfl.FL_DOWN_BOX, 105, \
                    255 - i * 85, 50, 25, "128")

        self.presult = xfl.fl_add_box(xfl.FL_DOWN_BOX, 180, 70, 90, 245, "")
        xfl.fl_mapcolor(xfl.FL_FREE_COL1, 128, 128, 128)
        xfl.fl_set_object_color(self.presult, xfl.FL_FREE_COL1, \
                xfl.FL_FREE_COL1)
        xfl.fl_set_object_dblbuffer(self.presult, 1)

        xfl.fl_end_form()



if __name__ == '__main__':
    print("********* ldial.py *********")
    appl = Flldial(len(sys.argv), sys.argv)

