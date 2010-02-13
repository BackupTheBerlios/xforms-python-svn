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
from xformslib import flbasic as flba
from xformslib import flxbasic as flxb
from xformslib import flbrowser as flbr
from xformslib import flbutton as flbt
from xformslib import flinput as flin
from xformslib import xfdata as xfc




class BrowserOp(object):
    def __init__(self, lsysargv, sysargv):
        flxb.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.create_form()
        flba.fl_show_form(self.pform, xfc.FL_PLACE_CENTER, xfc.FL_TRANSIENT, "Browser Op")

        while flba.fl_do_forms():
            pass

        flba.fl_hide_form(self.pform)


    def addit(self, pobj, data):
        # append and show the last line. Don't use this if you just want
        # to add some lines. use fl_add_browser_line
        flbr.fl_addto_browser(self.pbrowserobj, flin.fl_get_input(self.pinputobj))


    def insertit(self, pobj, arg):
        flbr.fl_insert_browser_line(self.pbrowserobj, flbr.fl_get_browser(self.pbrowserobj), \
                                    flin.fl_get_input(self.pinputobj))


    def replaceit(self, pobj, arg):
        n = flbr.fl_get_browser(self.pbrowserobj)
        if n:
            flbr.fl_replace_browser_line(self.pbrowserobj, n, flin.fl_get_input(self.pinputobj))


    def deleteit(self, pobj, arg):
        n = flbr.fl_get_browser(self.pbrowserobj)
        if n:
            flbr.fl_delete_browser_line(self.pbrowserobj, n)


    def clearit(self, pobj, arg):
        flbr.fl_clear_browser(self.pbrowserobj)


    def exitcb(self, pobj, arg):
        flxb.fl_finish()
        sys.exit(0)


    def create_form(self):
        #global pform, pbrowserobj, pinputobj, pexitobj

        self.pform = flba.fl_bgn_form(xfc.FL_UP_BOX, 390, 420)

        self.pbrowserobj = flbr.fl_add_browser(xfc.FL_HOLD_BROWSER, 20, 20, 210, 330, "")
        flba.fl_set_object_dblbuffer(self.pbrowserobj, 1)

        self.pinputobj = flin.fl_add_input(xfc.FL_NORMAL_INPUT, 20, 370, 210, 30, "")

        self.pobj = flbt.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 20, 120, 30, "Add")
        flba.fl_set_object_callback(self.pobj, self.addit, 0)

        self.pobj = flbt.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 60, 120, 30, "Insert")
        flba.fl_set_object_callback(self.pobj, self.insertit, 0)

        self.pobj = flbt.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 100, 120, 30, "Replace")
        flba.fl_set_object_callback(self.pobj, self.replaceit, 0)

        self.pobj = flbt.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 160, 120, 30, "Delete")
        flba.fl_set_object_callback(self.pobj, self.deleteit, 0)

        self.pobj = flbt.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 200, 120, 30, "Clear")
        flba.fl_set_object_callback(self.pobj, self.clearit, 0)

        self.pexitobj = flbt.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 370, 120, 30, "Exit")
        flba.fl_set_object_callback(self.pexitobj, self.exitcb, 0)

        flba.fl_end_form()



if __name__ == '__main__':
    BrowserOp(len(sys.argv), sys.argv)

