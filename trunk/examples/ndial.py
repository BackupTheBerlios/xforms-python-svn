#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  ndial.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This is an example of the use of dials.
#

import sys
#sys.path.append("..")
import xformslib as xfl


class Flndial(object):
    def __init__(self, lsysargv, sysargv):
        self.pdials = [0] * 3
        self.ptexts = [0] * 3
        self.cols = [128] * 3
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.makeform()
        xfl.fl_show_form(self.pform, xfl.FL_PLACE_MOUSE, xfl.FL_TRANSIENT, \
                "A Form")
        xfl.fl_do_forms()
        xfl.fl_finish()
        sys.exit(0)


    def cb(self, pobj, data):
        self.cols[data] = xfl.fl_get_dial_value(pobj)
        xfl.fl_mapcolor(xfl.FL_FREE_COL1, self.cols[0], self.cols[1], \
                self.cols[2])
        xfl.fl_redraw_object(self.presult)
        strng = "%d" % self.cols[data]
        xfl.fl_set_object_label(self.ptexts[data], strng)


    def makeform(self):
        label = ["Red", "Green", "Blue"]
        col = [xfl.FL_RED, xfl.FL_GREEN, xfl.FL_BLUE]
        y = 70
        self.pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 300, 330)
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 45, 15, \
                210, 45, "Color Editor")
        xfl.fl_set_object_lsize(pobj, xfl.FL_LARGE_SIZE)
        for i in range (0, 3):
            self.pdials[i] = xfl.fl_add_dial(xfl.FL_NORMAL_DIAL, 30, y, \
                    60, 60, label[i])
            xfl.fl_set_object_boxtype(self.pdials[i], xfl.FL_UP_BOX)
            xfl.fl_set_dial_bounds(self.pdials[i], 0.0, 255.0)
            xfl.fl_set_dial_value(self.pdials[i], 128.0)
            xfl.fl_set_object_color(self.pdials[i], col[i], xfl.FL_DIAL_COL2)
            xfl.fl_set_object_callback(self.pdials[i], self.cb, i)
            xfl.fl_set_object_return(self.pdials[i], xfl.FL_RETURN_CHANGED)
            self.ptexts[i] = xfl.fl_add_box(xfl.FL_DOWN_BOX, 105, y + 17, \
                    50, 25, "128")
            y += 85
        self.presult = xfl.fl_add_box(xfl.FL_DOWN_BOX, 180, 70, 90, 245, "")
        xfl.fl_set_object_color(self.presult, xfl.FL_FREE_COL1, \
                xfl.FL_FREE_COL1)
        xfl.fl_mapcolor(xfl.FL_FREE_COL1, 128, 128, 128)
        xfl.fl_set_object_dblbuffer(self.presult, 1)    # to avoid flicker
        xfl.fl_end_form()


if __name__ == '__main__':
    print("********* ndial.py *********")
    Flndial(len(sys.argv), sys.argv)
