#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  objinactive.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Demo showing activating and deactivating objects
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *




class Flobjinactive(object):

    def __init__(self, lsysargv, sysargv):

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.create_form()

        fl_set_button(self.pfirstbut, 1)

        fl_show_form(self.pform, FL_PLACE_CENTER, FL_NOBORDER, None)

        while fl_do_forms():
            pass            # empty


    def exit_cb(self, pobj, data):
        fl_finish()
        sys.exit(0)


    def setit(self, pobj, val):
        if val:
            fl_set_object_lcol(pobj, FL_BLACK)
            fl_activate_object(pobj)
        else:
            fl_set_object_lcol(pobj, FL_INACTIVE)
            fl_deactivate_object(pobj)


    def doit(self, b1, b2, b3, b4):

        self.setit(self.pbutton1, b1)
        self.setit(self.pbutton2, b2)
        self.setit(self.pbutton3, b3)
        self.setit(self.pbutton4, b4)


    def set_active(self, pobj, arg):
        if arg == 0:
            self.doit(1, 1, 1, 1)
        elif arg == 1:
            self.doit(0, 0, 0, 0)
        elif arg == 2:
            self.doit(0, 1, 0, 1)
        elif arg == 3:
            self.doit(1, 0, 1, 0)


    def create_form(self):

        self.pform = fl_bgn_form(FL_NO_BOX, 420, 230)

        pobj = fl_add_box(FL_UP_BOX, 0, 0, 420, 230, "")
        fl_set_object_color(pobj, FL_SLATEBLUE, FL_COL1)

        self.pbutton1 = fl_add_button(FL_NORMAL_BUTTON, 20, 170, 150, 40,
                                     "Button 1")
        fl_set_object_lsize(self.pbutton1 ,FL_LARGE_SIZE)
        fl_set_button_shortcut(self.pbutton1, "1", 1)

        self.pbutton2 = fl_add_button(FL_NORMAL_BUTTON, 20, 120, 150, 40,
                                      "Button 2")
        fl_set_object_lsize(self.pbutton2, FL_LARGE_SIZE)
        fl_set_button_shortcut(self.pbutton2, "2", 1)

        self.pbutton3 = fl_add_button(FL_NORMAL_BUTTON, 20, 70, 150, 40,
                                      "Button 3")
        fl_set_object_lsize(self.pbutton3, FL_LARGE_SIZE)
        fl_set_button_shortcut(self.pbutton3, "3", 1)

        self.pbutton4 = fl_add_button(FL_NORMAL_BUTTON, 20, 20, 150, 40,
                                      "Button 4")
        fl_set_button_shortcut(self.pbutton4, "4", 1)
        fl_set_object_lsize(self.pbutton4,FL_LARGE_SIZE)

        pgroup = fl_bgn_group()

        self.pfirstbut = fl_add_lightbutton(FL_RADIO_BUTTON, 260, 180, 140, 30,
                                            "All active")
        fl_set_object_callback(self.pfirstbut, self.set_active, 0)

        pobj = fl_add_lightbutton(FL_RADIO_BUTTON, 260, 150, 140, 30,
                                  "Non active")
        fl_set_object_callback(pobj, self.set_active, 1)

        pobj = fl_add_lightbutton(FL_RADIO_BUTTON, 260, 120, 140 ,30,
                                  "Even active")
        fl_set_object_callback(pobj, self.set_active, 2)

        pobj = fl_add_lightbutton(FL_RADIO_BUTTON, 260, 90, 140, 30, \
                                  "Odd active")
        fl_set_object_callback(pobj, self.set_active, 3)

        fl_end_group()

        pobj = fl_add_button(FL_NORMAL_BUTTON, 270, 20, 130, 30, "Quit")
        fl_set_object_callback(pobj, self.exit_cb, 0)

        fl_end_form()





if __name__ == '__main__':
    Flobjinactive(len(sys.argv), sys.argv)

