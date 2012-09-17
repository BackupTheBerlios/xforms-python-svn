#!/usr/bin/env python3

#  This file is part of xforms-python, and it has been ported from
#  positionerXOR.c XForms demo, with some adaptation.
#
#  positionerXOR.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a positioner with XOR drawmode, most
# useful for overlaying positioner on top of other object
#

import sys
#sys.path.append("..")
import xformslib as xfl


class Flpositxor(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_set_border_width(-2)
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 350, 250)
        pobj = xfl.fl_add_pixmap(xfl.FL_NORMAL_PIXMAP, 60, 70, 100, 100, "")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_DOWN_BOX)
        xfl.fl_set_pixmap_file(pobj, "porsche.xpm")
        ppos = xfl.fl_add_positioner(xfl.FL_OVERLAY_POSITIONER, 60, 70, \
                100, 100, "")
        xfl.fl_set_positioner_xbounds(ppos, 0, 1)
        xfl.fl_set_positioner_ybounds(ppos, 0, 1)
        xfl.fl_set_object_callback(ppos, self.positioner_cb, 0)
        self.pxval = xfl.fl_add_box(xfl.FL_DOWN_BOX, 230, 40, 100, 30, "")
        xfl.fl_set_object_color(self.pxval, xfl.FL_COL1, xfl.FL_COL1)
        self.pyval = xfl.fl_add_box(xfl.FL_DOWN_BOX, 230, 90, 100, 30, "")
        xfl.fl_set_object_color(self.pyval, xfl.FL_COL1, xfl.FL_COL1)
        xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 230, 200, 100, 30, \
                "Exit")
        xfl.fl_end_form()
        xfl.fl_show_form(pform, xfl.FL_PLACE_CENTER, xfl.FL_TRANSIENT, \
                "XOR Positioner")
        self.positioner_cb(ppos, 0)
        xfl.fl_do_forms()
        xfl.fl_hide_form(pform)
        xfl.fl_finish()
        sys.exit(0)


    # callback routine
    def positioner_cb(self, pobj, data):
        strng = "%f" % xfl.fl_get_positioner_xvalue(pobj)
        xfl.fl_set_object_label(self.pxval, strng)
        strng = "%f" % xfl.fl_get_positioner_yvalue(pobj)
        xfl.fl_set_object_label(self.pyval, strng)


if __name__ == '__main__':
    print ("********* positionerXOR.py *********")
    Flpositxor(len(sys.argv), sys.argv)
