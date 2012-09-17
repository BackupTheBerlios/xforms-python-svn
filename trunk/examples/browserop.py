#!/usr/bin/env python3

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
import xformslib as xfl


class BrowserOp(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.create_form()
        xfl.fl_show_form(self.pform, xfl.FL_PLACE_CENTER, \
                xfl.FL_TRANSIENT, "Browser Op")
        while not xfl.fl_is_same_object(xfl.fl_do_forms(), self.pexitobj):
            pass
        #xfl.fl_hide_form(self.pform)
        xfl.fl_finish()
        sys.exit(0)


    def addit(self, pobj, data):
        # append and show the last line. Don't use this if you just want
        # to add some lines. use fl_add_browser_line
        xfl.fl_addto_browser(self.pbrowserobj, \
                xfl.fl_get_input(self.pinputobj))


    def insertit(self, pobj, arg):
        xfl.fl_insert_browser_line(self.pbrowserobj, \
                xfl.fl_get_browser(self.pbrowserobj), \
                xfl.fl_get_input(self.pinputobj))


    def replaceit(self, pobj, arg):
        n = xfl.fl_get_browser(self.pbrowserobj)
        if n:
            xfl.fl_replace_browser_line(self.pbrowserobj, n, \
                    xfl.fl_get_input(self.pinputobj))


    def deleteit(self, pobj, arg):
        n = xfl.fl_get_browser(self.pbrowserobj)
        if n:
            xfl.fl_delete_browser_line(self.pbrowserobj, n)


    def clearit(self, pobj, arg):
        xfl.fl_clear_browser(self.pbrowserobj)


    #def exitcb(self, pobj, arg):
    #    xfl.fl_finish()
    #    sys.exit(0)


    def create_form(self):
        self.pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 390, 420)

        self.pbrowserobj = xfl.fl_add_browser(xfl.FL_HOLD_BROWSER, \
                20, 20, 210, 330, "")
        xfl.fl_set_object_dblbuffer(self.pbrowserobj, 1)

        self.pinputobj = xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 20, 370, \
                210, 30, "")
        xfl.fl_set_object_return(self.pinputobj, xfl.FL_RETURN_CHANGED)
        self.pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 250, 20, \
                120, 30, "Add")
        xfl.fl_set_object_callback(self.pobj, self.addit, 0)

        self.pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 250, 60, \
                120, 30, "Insert")
        xfl.fl_set_object_callback(self.pobj, self.insertit, 0)

        self.pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 250, 100, \
                120, 30, "Replace")
        xfl.fl_set_object_callback(self.pobj, self.replaceit, 0)

        self.pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 250, 160, \
                120, 30, "Delete")
        xfl.fl_set_object_callback(self.pobj, self.deleteit, 0)

        self.pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 250, 200, \
                120, 30, "Clear")
        xfl.fl_set_object_callback(self.pobj, self.clearit, 0)

        self.pexitobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 250, 370, \
                120, 30, "Exit")
        #xfl.fl_set_object_callback(self.pexitobj, self.exitcb, 0)

        xfl.fl_end_form()



if __name__ == '__main__':
    print("********* browserop.py *********")
    BrowserOp(len(sys.argv), sys.argv)
