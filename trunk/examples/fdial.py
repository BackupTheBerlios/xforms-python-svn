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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.fldial import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *





class Flfdial(object):

    def __init__(self, lsysargv, sysargv):
        strng = ""

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.makeform()

        fl_show_form(self.pform, FL_PLACE_MOUSE, FL_TRANSIENT, "A Form")

        r = fl_get_dial_value(self.pred)       # + 0.001
        g = fl_get_dial_value(self.pgreen)     # + 0.001
        b = fl_get_dial_value(self.pblue)      # + 0.001

        fl_mapcolor(FL_FREE_COL1, r, g, b)
        fl_redraw_object(self.presult)

        strng = "%d" % r
        fl_set_object_label(self.predtext, strng)
        strng = "%d" % g
        fl_set_object_label(self.pgreentext, strng)
        strng = "%d" % b
        fl_set_object_label(self.pbluetext, strng)

        while fl_do_forms():
            r = fl_get_dial_value(self.pred) + 0.001
            g = fl_get_dial_value(self.pgreen) + 0.001
            b = fl_get_dial_value(self.pblue) + 0.001

            fl_mapcolor(FL_FREE_COL1, r, g, b)
            fl_redraw_object(self.presult)

            strng = "%d" % r
            fl_set_object_label(self.predtext, strng)
            strng = "%d" % g
            fl_set_object_label(self.pgreentext, strng)
            strng = "%d" % b
            fl_set_object_label(self.pbluetext, strng)

        fl_finish()


    def exit_cb(self, pobj, data):
        fl_hide_form(self.pform)
        sys.exit(0)


    def makeform(self):

        self.pform = fl_bgn_form(FL_UP_BOX, 300, 330)

        self.pbutton = fl_add_button(FL_NORMAL_BUTTON, 45, 15, 210, 45,
                              "A Color Editor")
        fl_set_object_lsize(self.pbutton, FL_LARGE_SIZE)
        fl_set_object_callback(self.pbutton, self.exit_cb, 0)

        self.pred = fl_add_dial(FL_FILL_DIAL, 30, 240, 60, 60, "Red")
        fl_set_dial_bounds(self.pred, 0.0, 255.0)
        fl_set_dial_value(self.pred, 128.0)
        fl_set_object_color(self.pred, FL_DIAL_COL1, FL_RED)
        fl_set_object_return(self.pred, FL_RETURN_CHANGED)

        self.predtext = fl_add_box(FL_DOWN_BOX, 105, 255, 50, 25, "")

        self.pgreen = fl_add_dial(FL_FILL_DIAL, 30, 155, 60, 60, "Green")
        fl_set_dial_bounds(self.pgreen, 0.0, 255.0)
        fl_set_dial_value(self.pgreen, 128.0)
        fl_set_dial_angles(self.pgreen, 45.0, 360 - 45.0)
        fl_set_object_color(self.pgreen, FL_DIAL_COL1, FL_GREEN)
        fl_set_object_return(self.pgreen, FL_RETURN_CHANGED)

        self.pgreentext = fl_add_box(FL_DOWN_BOX, 105, 170, 50, 25,"")

        self.pblue = fl_add_dial(FL_FILL_DIAL, 30, 70, 60, 60, "Blue")
        fl_set_dial_bounds(self.pblue, 0.0, 255.0)
        fl_set_dial_value(self.pblue, 128.0)
        fl_set_object_color(self.pblue, FL_DIAL_COL1, FL_BLUE)
        fl_set_dial_direction(self.pblue, FL_DIAL_CCW)
        fl_set_object_return(self.pblue, FL_RETURN_CHANGED)

        self.pbluetext = fl_add_box(FL_DOWN_BOX, 105, 90, 50, 25, "")

        self.presult = fl_add_box(FL_DOWN_BOX, 180, 70, 90, 245, "")
        fl_set_object_color(self.presult, FL_FREE_COL1, FL_FREE_COL1)
        fl_set_object_dblbuffer(self.presult, 1)

        fl_end_form()




if __name__ == '__main__':
    Flfdial(len(sys.argv), sys.argv)

