#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  fdial.c XForms demo, with some adaptations.
#
#  fdial.c was written by M. Overmars and T.C. Zhao
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This is an example of the use of filled dials, dial range
# and dial direction.
#

import sys
#sys.path.append("..")
import xformslib as xfl


class Flfdial(object):
    def __init__(self, lsysargv, sysargv):
        strng = ""
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.makeform()
        xfl.fl_show_form(self.pform, xfl.FL_PLACE_MOUSE, \
                xfl.FL_TRANSIENT, "A Form")
        r = xfl.fl_get_dial_value(self.pred) + 0.001
        g = xfl.fl_get_dial_value(self.pgreen) + 0.001
        b = xfl.fl_get_dial_value(self.pblue) + 0.001
        xfl.fl_freeze_form(self.pform)
        xfl.fl_mapcolor(xfl.FL_FREE_COL1, r, g, b)
        strng = "%d" % r
        xfl.fl_set_object_label(self.predtext, strng)
        strng = "%d" % g
        xfl.fl_set_object_label(self.pgreentext, strng)
        strng = "%d" % b
        xfl.fl_set_object_label(self.pbluetext, strng)
        xfl.fl_unfreeze_form(self.pform)
        while True:
            if xfl.fl_is_same_object(xfl.fl_do_forms(), self.pbutton):
                break
            r = xfl.fl_get_dial_value(self.pred) + 0.001
            g = xfl.fl_get_dial_value(self.pgreen) + 0.001
            b = xfl.fl_get_dial_value(self.pblue) + 0.001
            xfl.fl_freeze_form(self.pform)
            xfl.fl_mapcolor(xfl.FL_FREE_COL1, r, g, b)
            strng = "%d" % r
            xfl.fl_set_object_label(self.predtext, strng)
            strng = "%d" % g
            xfl.fl_set_object_label(self.pgreentext, strng)
            strng = "%d" % b
            xfl.fl_set_object_label(self.pbluetext, strng)
            xfl.fl_unfreeze_form(self.pform)
        xfl.fl_hide_form(self.pform)
        xfl.fl_finish()
        sys.exit(0)


    def makeform(self):
        self.pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 300, 330)
        self.pbutton = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 45, 15, \
                210, 45, "A Color Editor")
        xfl.fl_set_object_lsize(self.pbutton, xfl.FL_LARGE_SIZE)
        #xfl.fl_set_object_callback(self.pbutton, self.exit_cb, 0)
        self.pred = xfl.fl_add_dial(xfl.FL_FILL_DIAL, 30, 240, 60, 60, "Red")
        xfl.fl_set_dial_bounds(self.pred, 0.0, 255.0)
        xfl.fl_set_dial_value(self.pred, 128.0)
        xfl.fl_set_object_color(self.pred, xfl.FL_DIAL_COL1, xfl.FL_RED)
        xfl.fl_set_object_return(self.pred, xfl.FL_RETURN_CHANGED)
        self.predtext = xfl.fl_add_box(xfl.FL_DOWN_BOX, 105, 255, 50, 25, \
                "")
        self.pgreen = xfl.fl_add_dial(xfl.FL_FILL_DIAL, 30, 155, 60, 60, \
                "Green")
        xfl.fl_set_dial_bounds(self.pgreen, 0.0, 255.0)
        xfl.fl_set_dial_value(self.pgreen, 128.0)
        xfl.fl_set_dial_angles(self.pgreen, 45.0, 360 - 45.0)
        xfl.fl_set_object_color(self.pgreen, xfl.FL_DIAL_COL1, xfl.FL_GREEN)
        xfl.fl_set_object_return(self.pgreen, xfl.FL_RETURN_CHANGED)
        self.pgreentext = xfl.fl_add_box(xfl.FL_DOWN_BOX, 105, 170, 50, \
                25, "")
        self.pblue = xfl.fl_add_dial(xfl.FL_FILL_DIAL, 30, 70, 60, 60, \
                "Blue")
        xfl.fl_set_dial_bounds(self.pblue, 0.0, 255.0)
        xfl.fl_set_dial_value(self.pblue, 128.0)
        xfl.fl_set_object_color(self.pblue, xfl.FL_DIAL_COL1, xfl.FL_BLUE)
        xfl.fl_set_dial_direction(self.pblue, xfl.FL_DIAL_CCW)
        xfl.fl_set_object_return(self.pblue, xfl.FL_RETURN_CHANGED)
        self.pbluetext = xfl.fl_add_box(xfl.FL_DOWN_BOX, 105, 90, 50, 25, "")
        self.presult = xfl.fl_add_box(xfl.FL_DOWN_BOX, 180, 70, 90, 245, "")
        xfl.fl_set_object_color(self.presult, xfl.FL_FREE_COL1, \
                xfl.FL_FREE_COL1)
        xfl.fl_set_object_dblbuffer(self.presult, 1)
        xfl.fl_end_form()


if __name__ == '__main__':
    print("********* fdial.py *********")
    Flfdial(len(sys.argv), sys.argv)
