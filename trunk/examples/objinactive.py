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
import xformslib as xfl


class Flobjinactive(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.create_form()
        xfl.fl_set_button(self.pfirstbut, 1)
        xfl.fl_show_form(self.pform, xfl.FL_PLACE_CENTER, xfl.FL_NOBORDER, \
                "")
        while xfl.fl_do_forms():
            pass            # empty
        sys.exit(0)


    def exit_cb(self, pobj, data):
        xfl.fl_finish()
        sys.exit(0)


    def setit(self, pobj, val):
        if val:
            xfl.fl_set_object_lcol(pobj, xfl.FL_BLACK)
            xfl.fl_activate_object(pobj)
        else:
            xfl.fl_set_object_lcol(pobj, xfl.FL_INACTIVE)
            xfl.fl_deactivate_object(pobj)


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
        self.pform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 420, 230)
        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 420, 230, "")
        xfl.fl_set_object_color(pobj, xfl.FL_SLATEBLUE, xfl.FL_COL1)
        self.pbutton1 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 20, 170, \
                150, 40, "Button 1")
        xfl.fl_set_object_lsize(self.pbutton1 ,xfl.FL_LARGE_SIZE)
        xfl.fl_set_button_shortcut(self.pbutton1, "1", 1)
        self.pbutton2 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 20, 120, \
                150, 40, "Button 2")
        xfl.fl_set_object_lsize(self.pbutton2, xfl.FL_LARGE_SIZE)
        xfl.fl_set_button_shortcut(self.pbutton2, "2", 1)
        self.pbutton3 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 20, 70, \
                150, 40, "Button 3")
        xfl.fl_set_object_lsize(self.pbutton3, xfl.FL_LARGE_SIZE)
        xfl.fl_set_button_shortcut(self.pbutton3, "3", 1)
        self.pbutton4 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 20, 20, \
                150, 40, "Button 4")
        xfl.fl_set_button_shortcut(self.pbutton4, "4", 1)
        xfl.fl_set_object_lsize(self.pbutton4,xfl.FL_LARGE_SIZE)
        pgroup = xfl.fl_bgn_group()
        self.pfirstbut = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, \
                260, 180, 140, 30, "All active")
        xfl.fl_set_object_callback(self.pfirstbut, self.set_active, 0)
        pobj = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 260, 150, \
                140, 30, "Non active")
        xfl.fl_set_object_callback(pobj, self.set_active, 1)
        pobj = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 260, 120, \
                140 ,30, "Even active")
        xfl.fl_set_object_callback(pobj, self.set_active, 2)
        pobj = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 260, 90, \
                140, 30, "Odd active")
        xfl.fl_set_object_callback(pobj, self.set_active, 3)
        xfl.fl_end_group()
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 270, 20, \
                130, 30, "Quit")
        xfl.fl_set_object_callback(pobj, self.exit_cb, 0)
        xfl.fl_end_form()


if __name__ == '__main__':
    print ("********* objinactive.py *********")
    Flobjinactive(len(sys.argv), sys.argv)
