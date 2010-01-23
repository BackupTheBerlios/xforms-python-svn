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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.fldial import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *





class Flndial(object):

    def __init__(self, lsysargv, sysargv):

        self.pdials = [0, 0, 0]
        self.ptexts = [0, 0, 0]

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.makeform()

        fl_show_form(self.pform, FL_PLACE_MOUSE, FL_TRANSIENT, \
                        "A Form")

        fl_do_forms()
        fl_finish()


    def cb(self, pobj, data):

        cols = [128, 128, 128]

        cols[data] = fl_get_dial_value(pobj)
        fl_mapcolor(FL_FREE_COL1, cols[0], cols[1], cols[2])
        fl_redraw_object(self.presult)
        strng = "%d" % cols[data]
        fl_set_object_label(self.ptexts[data], strng)


    def makeform(self):

        label = ["Red", "Green", "Blue"]
        col = [FL_RED, FL_GREEN, FL_BLUE]
        y = 70

        self.pform = fl_bgn_form(FL_UP_BOX, 300, 330)

        pobj = fl_add_button(FL_NORMAL_BUTTON, 45, 15, \
                             210, 45, "Color Editor")
        fl_set_object_lsize(pobj, FL_LARGE_SIZE)

        for i in range (0, 3):
            self.pdials[i] = fl_add_dial(FL_NORMAL_DIAL, 30, y, \
                                         60, 60, label[i])
            fl_set_object_boxtype(self.pdials[i], FL_UP_BOX)
            fl_set_dial_bounds(self.pdials[i], 0.0, 255.0)
            fl_set_dial_value(self.pdials[i], 128.0)
            fl_set_object_color(self.pdials[i], col[i], FL_DIAL_COL2)
            fl_set_object_callback(self.pdials[i], self.cb, i)
            fl_set_object_return(self.pdials[i], FL_RETURN_CHANGED)

            self.ptexts[i] = fl_add_box(FL_DOWN_BOX, 105, y + 17, \
                                        50, 25, "128")
            y += 85

        self.presult = fl_add_box(FL_DOWN_BOX, 180, 70, 90, 245, "")
        fl_set_object_color(self.presult, FL_FREE_COL1, FL_FREE_COL1)
        fl_mapcolor(FL_FREE_COL1, 128, 128, 128)
        fl_set_object_dblbuffer(self.presult, 1)       # to avoid flicker
        fl_end_form()





if __name__ == '__main__':
    Flndial(len(sys.argv), sys.argv)

