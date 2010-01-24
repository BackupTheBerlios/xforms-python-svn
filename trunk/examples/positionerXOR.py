#!/usr/bin/env python

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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flpositioner import *
from xformslib.flbutton import *
from xformslib.flbitmap import *
from xformslib.flmisc import *
from xformslib.xfdata import *





class Flpositxor(object):
    def __init__(self, lsysargv, sysargv):

        fl_set_border_width(-2)
        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        pform = fl_bgn_form(FL_UP_BOX, 350, 250)

        pobj = fl_add_pixmap(FL_NORMAL_PIXMAP, 60, 70, 100, 100, "")
        fl_set_object_boxtype(pobj, FL_DOWN_BOX)
        fl_set_pixmap_file(pobj, "porsche.xpm")

        ppos = fl_add_positioner(FL_OVERLAY_POSITIONER, 60, 70, \
                                    100, 100, "")
        fl_set_positioner_xbounds(ppos, 0, 1)
        fl_set_positioner_ybounds(ppos, 0, 1)
        fl_set_object_callback(ppos, self.positioner_cb, 0)

        self.pxval = fl_add_box(FL_DOWN_BOX, 230, 40, 100, 30, "")
        fl_set_object_color(self.pxval, FL_COL1, FL_COL1)

        self.pyval = fl_add_box(FL_DOWN_BOX, 230, 90, 100, 30, "")
        fl_set_object_color(self.pyval, FL_COL1, FL_COL1)

        fl_add_button(FL_NORMAL_BUTTON, 230, 200, 100, 30, \
                         "Exit")

        fl_end_form()
        fl_show_form(pform, FL_PLACE_CENTER, FL_TRANSIENT, \
                        "XOR Positioner")

        self.positioner_cb(ppos, 0)
        fl_do_forms()
        fl_hide_form(pform)
        fl_finish()


    # callback routine

    def positioner_cb(self, pobj, q):

        strng = "%f" % fl_get_positioner_xvalue(pobj)
        fl_set_object_label(self.pxval, strng)

        strng = "%f" % fl_get_positioner_yvalue(pobj)
        fl_set_object_label(self.pyval, strng)





if __name__ == '__main__':
    Flpositxor(len(sys.argv), sys.argv)

