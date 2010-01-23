#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  invslider.c XForms demo, with some adaptations.
#
#  invslider.c was written by M. Overmars and T.C. Zhao
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Inverted slider
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flmisc import *
from xformslib.flbutton import *
from xformslib.flslider import *
from xformslib.xfdata import *



class FD_inv(object):
    inv = None
    vdata = None
    cdata = ""
    ldata = 0
    sl = [0, 0, 0]
    done = None



class Flinvslider(object):

    def __init__(self, lsysargv, sysargv):
        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.ui = self.create_form_inv()
        fl_show_form(self.ui.inv, FL_PLACE_CENTER | FL_FREE_SIZE, \
                     FL_TRANSIENT, "inv")
        while fl_do_forms():
            pass            # empty


    def invert_it(self, pobj, data):

        if fl_get_button(pobj):
            fl_set_slider_bounds(self.ui.sl[0], 1.0, 0.0)
            fl_set_slider_bounds(self.ui.sl[1], 1.0, 0.0)
            fl_set_slider_bounds(self.ui.sl[2], 1.0, 0.0)
        else:
            fl_set_slider_bounds(self.ui.sl[0], 0.0, 1.0)
            fl_set_slider_bounds(self.ui.sl[1], 0.0, 1.0)
            fl_set_slider_bounds(self.ui.sl[2], 0.0, 1.0)


    def exitcb(self, pobj, data):
        fl_finish()
        sys.exit(0)


    # Form definition
    def create_form_inv(self):

        fdui = FD_inv()

        fdui.inv = fl_bgn_form(FL_NO_BOX, 245, 280)

        fl_add_box(FL_UP_BOX, 0, 0, 245, 280, "")

        fdui.sl[0] = fl_add_valslider(FL_VERT_SLIDER, 20, 30, 35, 230, "")

        fdui.sl[1] = fl_add_valslider(FL_VERT_FILL_SLIDER, 65, 30, 35, 230, "")

        fdui.sl[2] = fl_add_valslider(FL_VERT_NICE_SLIDER, 115, 30, 35, 230, "")
        fl_set_object_boxtype(fdui.sl[2], FL_FLAT_BOX)
        fl_set_object_color(fdui.sl[2], FL_COL1, FL_BLUE)

        fdui.done = fl_add_button(FL_RETURN_BUTTON, 160, 235, 75, 30, "Exit")
        fl_set_object_callback(fdui.done, self.exitcb, 0)

        pobj = fl_add_checkbutton(FL_PUSH_BUTTON, 165, 30, 75, 35, "Invert")
        fl_set_object_callback(pobj, self.invert_it, 0)

        fl_end_form()

        return fdui




if __name__ == '__main__':
    Flinvslider(len(sys.argv), sys.argv)

