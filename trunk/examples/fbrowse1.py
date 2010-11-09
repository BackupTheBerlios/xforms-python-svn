#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  fbrowse1.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a browser and xfl.fl_call_object_callback.
#

import sys
#sys.path.append("..")
import xformslib as xfl



class FLfbrowse1(object):
    def __init__(self, lsysargv, sysargv):

        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 130, 100)

        self.pbr = xfl.fl_add_browser(xfl.FL_NORMAL_BROWSER, 5, 5, 95, 90, "")
        pbut = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 105, 5, 20, 8, "Exit")
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 105, 75, 20, 8, "Load")
        xfl.fl_set_object_callback(pobj, self.load_file, 0)

        pobj = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 105, 60, 20, 8, \
                "Small")
        xfl.fl_set_object_callback(pobj, self.set_size, xfl.FL_SMALL_SIZE)
        xfl.fl_call_object_callback(pobj)
        xfl.fl_set_button(pobj, 1)

        pobj = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 105, 50, 20, 8, \
                "Normal")
        xfl.fl_set_object_callback(pobj, self.set_size, xfl.FL_NORMAL_SIZE)

        pobj = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 105, 40, 20, 8, \
                "Large")
        xfl.fl_set_object_callback(pobj, self.set_size, xfl.FL_LARGE_SIZE)

        xfl.fl_end_form()

        xfl.fl_scale_form(pform, 4.0, 4.0)
        xfl.fl_adjust_form_size(pform)

        xfl.fl_clear_browser(self.pbr)
        xfl.fl_add_browser_line(self.pbr, "LOAD A FILE.")

        xfl.fl_show_form(pform, xfl.FL_PLACE_FREE, xfl.FL_FULLBORDER, \
                "Browser")

        while True:
            pobj = xfl.fl_do_forms()
            if xfl.fl_is_same_object(pobj, pbut):
                break

        xfl.fl_hide_form(pform)
        xfl.fl_finish()


    def load_file(self, pobj, arg):
        if not xfl.fl_load_browser(self.pbr, \
         xfl.fl_show_input("Filename to load", "")):
            xfl.fl_add_browser_line(self.pbr, "NO SUCH FILE!")


    def set_size(self, pobj, arg):
        xfl.fl_set_browser_fontsize(self.pbr, arg)



if __name__ == '__main__':
    FLfbrowse1(len(sys.argv), sys.argv)
