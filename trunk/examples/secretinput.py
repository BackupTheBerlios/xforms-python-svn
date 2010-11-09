#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  secretinput.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Demo showing secret input fields
#

import sys
#sys.path.append("..")
import xformslib as xfl



class Flsecrinp(object):
    def __init__(self, lsysargv, sysargv):

        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        self.pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 400, 300)

        ppassword1 = xfl.fl_add_input(xfl.FL_SECRET_INPUT, 140, 40, \
                160, 40, "Password 1:")
        ppassword2 = xfl.fl_add_input(xfl.FL_SECRET_INPUT, 140, 100, \
                160, 40, "Password 2:")
        pinfo = xfl.fl_add_box(xfl.FL_SHADOW_BOX, 20, 160, 360, 40, "")
        pbut = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 280, 240, \
                100, 40, "Quit")
        xfl.fl_set_object_callback(pbut, self.exitcb, 0)

        xfl.fl_end_form()

        xfl.fl_show_form(self.pform, xfl.FL_PLACE_MOUSE, xfl.FL_NOBORDER, 0)

        while xfl.fl_do_forms():
            strng = "Password 1 is: %s , Password 2 is: %s" % \
                    (xfl.fl_get_input(ppassword1), \
                    xfl.fl_get_input(ppassword2))
            xfl.fl_set_object_label(pinfo, strng)


    def exitcb(self, pobj, data):
        xfl.fl_hide_form(self.pform)
        xfl.fl_finish()
        sys.exit(0)



if __name__ == '__main__':
    Flsecrinp(len(sys.argv), sys.argv)
