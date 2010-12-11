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
import xformslib as xfl



class FD_inv(object):
    inv = None
    vdata = None
    cdata = ""
    ldata = 0
    sl = [0, 0, 0]
    done = None


class Flinvslider(object):

    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.ui = self.create_form_inv()
        xfl.fl_show_form(self.ui.inv, \
                xfl.FL_PLACE_CENTER | xfl.FL_FREE_SIZE, xfl.FL_TRANSIENT, \
                "inv")
        while xfl.fl_do_forms():
            pass            # empty


    def invert_it(self, pobj, data):

        if xfl.fl_get_button(pobj):
            xfl.fl_set_slider_bounds(self.ui.sl[0], 1.0, 0.0)
            xfl.fl_set_slider_bounds(self.ui.sl[1], 1.0, 0.0)
            xfl.fl_set_slider_bounds(self.ui.sl[2], 1.0, 0.0)
        else:
            xfl.fl_set_slider_bounds(self.ui.sl[0], 0.0, 1.0)
            xfl.fl_set_slider_bounds(self.ui.sl[1], 0.0, 1.0)
            xfl.fl_set_slider_bounds(self.ui.sl[2], 0.0, 1.0)


    def exitcb(self, pobj, data):
        xfl.fl_finish()
        sys.exit(0)


    # Form definition
    def create_form_inv(self):

        fdui = FD_inv()

        fdui.inv = xfl.fl_bgn_form(xfl.FL_NO_BOX, 245, 280)

        xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 245, 280, "")
        fdui.sl[0] = xfl.fl_add_valslider(xfl.FL_VERT_SLIDER, 20, 30, \
                35, 230, "")
        fdui.sl[1] = xfl.fl_add_valslider(xfl.FL_VERT_FILL_SLIDER, 65, 30, \
                35, 230, "")
        fdui.sl[2] = xfl.fl_add_valslider(xfl.FL_VERT_NICE_SLIDER, 115, 30, \
                35, 230, "")
        xfl.fl_set_object_boxtype(fdui.sl[2], xfl.FL_FLAT_BOX)
        xfl.fl_set_object_color(fdui.sl[2], xfl.FL_COL1, xfl.FL_BLUE)
        fdui.done = xfl.fl_add_button(xfl.FL_RETURN_BUTTON, 160, 235, \
                75, 30, "Exit")
        xfl.fl_set_object_callback(fdui.done, self.exitcb, 0)
        pobj = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 165, 30, \
                75, 35, "Invert")
        xfl.fl_set_object_callback(pobj, self.invert_it, 0)

        xfl.fl_end_form()

        return fdui



if __name__ == '__main__':
    print ("********* invslider.py *********")
    Flinvslider(len(sys.argv), sys.argv)

