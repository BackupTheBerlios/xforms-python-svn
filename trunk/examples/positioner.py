#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  positioner.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a positioner.
#

import sys
#sys.path.append("..")
import xformslib as xfl



class Flpositioner(object):
    def __init__(self, lsysargv, sysargv):

        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 400, 280)

        ppos = xfl.fl_add_positioner(xfl.FL_NORMAL_POSITIONER, 40, 40, \
                200, 200, "")
        xfl.fl_set_positioner_xbounds(ppos, 0, 1)
        xfl.fl_set_positioner_ybounds(ppos, 0, 1)
        xfl.fl_set_object_callback(ppos, self.positioner_cb, 0)

        self.pxval = xfl.fl_add_box(xfl.FL_DOWN_BOX, 270, 40, 100, 30, "")
        xfl.fl_set_object_color(self.pxval, xfl.FL_COL1, xfl.FL_COL1)

        self.pyval = xfl.fl_add_box(xfl.FL_DOWN_BOX, 270, 90, 100, 30, "")
        xfl.fl_set_object_color(self.pyval, xfl.FL_COL1, xfl.FL_COL1)

        xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 270, 210, 100, 30, \
                "Exit")
        xfl.fl_end_form()
        xfl.fl_show_form(pform, xfl.FL_PLACE_CENTER, xfl.FL_NOBORDER, \
                "positioner")

        self.positioner_cb(ppos, 0)

        xfl.fl_do_forms()
        xfl.fl_hide_form(pform)
        xfl.fl_finish()


    # callback routine
    def positioner_cb(self, pobj, q):

        strng = "%f" % xfl.fl_get_positioner_xvalue(pobj)
        xfl.fl_set_object_label(self.pxval, strng)
        strng = "%f" % xfl.fl_get_positioner_yvalue(pobj)
        xfl.fl_set_object_label(self.pyval, strng)



if __name__ == '__main__':
    print ("********* positioner.py *********")
    Flpositioner(len(sys.argv), sys.argv)

