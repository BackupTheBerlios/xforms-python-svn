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
from xformslib import flbasic, flxbasic, flbrowser, flbutton, flinput, xfdata




class BrowserOp(object):

    def __init__(self, lsysargv, sysargv):

        flxbasic.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.create_form()
        flbasic.fl_show_form(self.pform, xfdata.FL_PLACE_CENTER, xfdata.FL_TRANSIENT, "Browser Op")

        while flbasic.fl_do_forms():
            pass

        flbasic.fl_hide_form(self.pform)
        return 0


    def addit(self, pobj, data):
        # append and show the last line. Don't use this if you just want
        # to add some lines. use fl_add_browser_line
        browserfn.fl_addto_browser(self.pbrowserobj, inputfn.fl_get_input(self.pinputobj))


    def insertit(self, pobj, arg):
        browserfn.fl_insert_browser_line(self.pbrowserobj, browserfn.fl_get_browser(self.pbrowserobj), \
                                         inputfn.fl_get_input(self.pinputobj))


    def replaceit(self, pobj, arg):
        n = browserfn.fl_get_browser(self.pbrowserobj)
        if n:
            browserfn.fl_replace_browser_line(self.pbrowserobj, n, inputfn.fl_get_input(self.pinputobj))


    def deleteit(self, pobj, arg):
        n = browserfn.fl_get_browser(self.pbrowserobj)
        if n:
            browserfn.fl_delete_browser_line(self.pbrowserobj, n)


    def clearit(self, pobj, arg):
        browserfn.fl_clear_browser(self.pbrowserobj)


    def exitcb(self, pobj, arg):
        flxbasic.fl_finish()
        sys.exit(0)


    def create_form(self):
        #global pform, pbrowserobj, pinputobj, pexitobj

        self.pform = flbasic.fl_bgn_form(xfdata.FL_UP_BOX, 390, 420)

        self.pbrowserobj = browserfn.fl_add_browser(xfdata.FL_HOLD_BROWSER, 20, 20, 210, 330, "")
        flbasic.fl_set_object_dblbuffer(self.pbrowserobj, 1)

        self.pinputobj = inputfn.fl_add_input(xfdata.FL_NORMAL_INPUT, 20, 370, 210, 30, "")

        self.pobj = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 250, 20, 120, 30, "Add")
        flbasic.fl_set_object_callback(self.pobj, self.addit, 0)

        self.pobj = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 250, 60, 120, 30, "Insert")
        flbasic.fl_set_object_callback(self.pobj, self.insertit, 0)

        self.pobj = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 250, 100, 120, 30, "Replace")
        flbasic.fl_set_object_callback(self.pobj, self.replaceit, 0)

        self.pobj = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 250, 160, 120, 30, "Delete")
        flbasic.fl_set_object_callback(self.pobj, self.deleteit, 0)

        self.pobj = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 250, 200, 120, 30, "Clear")
        flbasic.fl_set_object_callback(self.pobj, self.clearit, 0)

        self.pexitobj = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 250, 370, 120, 30, "Exit")
        flbasic.fl_set_object_callback(self.pexitobj, self.exitcb, 0)

        flbasic.fl_end_form()



if __name__ == '__main__':
    appl = BrowserOp(len(sys.argv), sys.argv)

