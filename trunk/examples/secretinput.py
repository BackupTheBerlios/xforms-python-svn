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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flinput import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *



class Flsecrinp(object):
    def __init__(self, lsysargv, sysargv):

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        self.pform = fl_bgn_form(FL_UP_BOX, 400, 300)
        ppassword1 = fl_add_input(FL_SECRET_INPUT, 140, 40, \
                                     160, 40, "Password 1:")
        ppassword2 = fl_add_input(FL_SECRET_INPUT, 140, 100, \
                                     160, 40, "Password 2:")
        pinfo = fl_add_box(FL_SHADOW_BOX, 20, 160, 360, 40, "")
        pbut = fl_add_button(FL_NORMAL_BUTTON, 280, 240, \
                                100, 40, "Quit")
        fl_set_object_callback(pbut, self.exitcb, 0)

        fl_end_form()

        fl_show_form(self.pform, FL_PLACE_MOUSE, FL_NOBORDER, 0)

        while fl_do_forms():
            strng = "Password 1 is: %s , Password 2 is: %s" % \
                    (fl_get_input(ppassword1), fl_get_input(ppassword2))
            fl_set_object_label(pinfo, strng)


    def exitcb(self, pobj, data):
        fl_hide_form(self.pform)
        fl_finish()
        sys.exit(0)




if __name__ == '__main__':
    Flsecrinp(len(sys.argv), sys.argv)

