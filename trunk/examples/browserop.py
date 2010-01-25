#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  browserop.c XForms demo, with some adaptations.
#
#  browserop.c was written by M. Overmars and T.C. Zhao (1997)
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the basic browsers browsers
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbrowser import *
from xformslib.flbutton import *
from xformslib.flinput import *
from xformslib.xfdata import *




class BrowserOp(object):
    def __init__(self, lsysargv, sysargv):
        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.create_form()
        fl_show_form(self.pform, FL_PLACE_CENTER, FL_TRANSIENT, "Browser Op")

        while fl_do_forms():
            pass

        fl_hide_form(self.pform)


    def addit(self, pobj, data):
        # append and show the last line. Don't use this if you just want
        # to add some lines. use fl_add_browser_line
        fl_addto_browser(self.pbrowserobj, fl_get_input(self.pinputobj))


    def insertit(self, pobj, arg):
        fl_insert_browser_line(self.pbrowserobj, fl_get_browser(self.pbrowserobj), \
                                         fl_get_input(self.pinputobj))


    def replaceit(self, pobj, arg):
        n = fl_get_browser(self.pbrowserobj)
        if n:
            fl_replace_browser_line(self.pbrowserobj, n, fl_get_input(self.pinputobj))


    def deleteit(self, pobj, arg):
        n = fl_get_browser(self.pbrowserobj)
        if n:
            fl_delete_browser_line(self.pbrowserobj, n)


    def clearit(self, pobj, arg):
        fl_clear_browser(self.pbrowserobj)


    def exitcb(self, pobj, arg):
        fl_finish()
        sys.exit(0)


    def create_form(self):
        #global pform, pbrowserobj, pinputobj, pexitobj

        self.pform = fl_bgn_form(FL_UP_BOX, 390, 420)

        self.pbrowserobj = fl_add_browser(FL_HOLD_BROWSER, 20, 20, 210, 330, "")
        fl_set_object_dblbuffer(self.pbrowserobj, 1)

        self.pinputobj = fl_add_input(FL_NORMAL_INPUT, 20, 370, 210, 30, "")

        self.pobj = fl_add_button(FL_NORMAL_BUTTON, 250, 20, 120, 30, "Add")
        fl_set_object_callback(self.pobj, self.addit, 0)

        self.pobj = fl_add_button(FL_NORMAL_BUTTON, 250, 60, 120, 30, "Insert")
        fl_set_object_callback(self.pobj, self.insertit, 0)

        self.pobj = fl_add_button(FL_NORMAL_BUTTON, 250, 100, 120, 30, "Replace")
        fl_set_object_callback(self.pobj, self.replaceit, 0)

        self.pobj = fl_add_button(FL_NORMAL_BUTTON, 250, 160, 120, 30, "Delete")
        fl_set_object_callback(self.pobj, self.deleteit, 0)

        self.pobj = fl_add_button(FL_NORMAL_BUTTON, 250, 200, 120, 30, "Clear")
        fl_set_object_callback(self.pobj, self.clearit, 0)

        self.pexitobj = fl_add_button(FL_NORMAL_BUTTON, 250, 370, 120, 30, "Exit")
        fl_set_object_callback(self.pexitobj, self.exitcb, 0)

        fl_end_form()



if __name__ == '__main__':
    BrowserOp(len(sys.argv), sys.argv)

