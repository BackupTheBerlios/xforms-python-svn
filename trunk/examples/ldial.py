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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.fldial import *
from xformslib.flmisc import *
from xformslib.xfdata import *



RED = 0
GREEN = 1
BLUE = 2


class Flldial(object):

    def __init__(self, lsysargv, sysargv):

        self.pdial = [None, None, None]
        self.ptext = [None, None, None]

        fl_initialize(lsysargv, sysargv, "ColorEditor", 0, 0)
        self.makeform()
        fl_show_form(self.pform, FL_PLACE_MOUSE, FL_TRANSIENT, \
                        "Color Editor")
        fl_do_forms()
        fl_finish()


    def dial_callback(self, pobj, arg):
        clr = [0, 1, 2]

        for i in range(RED, BLUE+1):
            clr[i] = fl_get_dial_value(self.pdial[i])

        strng = "%d" % clr[arg]
        fl_set_object_label(self.ptext[arg], strng)

        fl_mapcolor(FL_FREE_COL1, clr[0], clr[1], clr[2])
        fl_redraw_object(self.presult)


    def makeform(self):

        txt = ["Red", "Green", "Blue"]
        clr = [FL_RED, FL_GREEN, FL_BLUE]

        self.pform = fl_bgn_form(FL_UP_BOX, 300, 330)

        pquit = fl_add_button(FL_NORMAL_BUTTON, 45, 15, \
                              210, 45, "A Color Editor")
        fl_set_object_lsize(pquit, FL_LARGE_SIZE)

        for i in range(RED, BLUE+1):
            self.pdial[i] = fl_add_dial(FL_LINE_DIAL, 30, \
                                        240 - i * 85, 60, 60, txt[i])
            fl_set_dial_bounds(self.pdial[i], 0.0, 255.0)
            fl_set_dial_angles(self.pdial[i], 15.0, 345.0)
            fl_set_dial_value(self.pdial[i], 128.0)
            fl_set_object_color(self.pdial[i], clr[i], FL_DIAL_COL2)
            fl_set_object_return(self.pdial[i], FL_RETURN_CHANGED)
            fl_set_object_callback(self.pdial[i], self.dial_callback, i)
            self.ptext[i] = fl_add_box(FL_DOWN_BOX, 105, \
                                     255 - i * 85, 50, 25, "128")

        self.presult = fl_add_box(FL_DOWN_BOX, 180, 70, 90, 245, "")
        fl_mapcolor(FL_FREE_COL1, 128, 128, 128)
        fl_set_object_color(self.presult, FL_FREE_COL1, FL_FREE_COL1)
        fl_set_object_dblbuffer(self.presult, 1)

        fl_end_form()





if __name__ == '__main__':
    Flldial(len(sys.argv), sys.argv)

