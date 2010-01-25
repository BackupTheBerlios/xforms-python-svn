#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  fbrowse1.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a browser and fl_call_object_callback.
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbrowser import *
from xformslib.flbutton import *
from xformslib.flgoodies import *
from xformslib.xfdata import *



class Flfbrowse1(object):
    def __init__(self, lsysargv, sysargv):

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        pform = fl_bgn_form(FL_UP_BOX, 130, 100)

        self.pbr = fl_add_browser(FL_NORMAL_BROWSER, 5, 5, 95, 90, "")

        pbut = fl_add_button(FL_NORMAL_BUTTON, 105, 5, 20, 8, "Exit")

        pobj = fl_add_button(FL_NORMAL_BUTTON, 105, 75, 20, 8, "Load")
        fl_set_object_callback(pobj, self.load_file, 0)

        pobj = fl_add_lightbutton(FL_RADIO_BUTTON, 105, 60, 20, 8, "Small")
        fl_set_object_callback(pobj, self.set_size, FL_SMALL_SIZE)
        fl_call_object_callback(pobj)
        fl_set_button(pobj, 1)

        pobj = fl_add_lightbutton(FL_RADIO_BUTTON, 105, 50, 20, 8, "Normal")
        fl_set_object_callback(pobj, self.set_size, FL_NORMAL_SIZE)

        pobj = fl_add_lightbutton(FL_RADIO_BUTTON, 105, 40, 20, 8, "Large")
        fl_set_object_callback(pobj, self.set_size, FL_LARGE_SIZE)

        fl_end_form()

        fl_scale_form(pform, 4.0, 4.0)
        fl_adjust_form_size(pform)

        fl_clear_browser(self.pbr)
        fl_add_browser_line(self.pbr, "LOAD A FILE.")

        fl_show_form(pform, FL_PLACE_FREE, FL_FULLBORDER, "Browser")

        while True:
            pobj = fl_do_forms()
            if fl_is_same_object(pobj, pbut):
                break

        fl_hide_form(pform)
        fl_finish()


    def load_file(self, pobj, arg):
        if not fl_load_browser(self.pbr, \
         fl_show_input("Filename to load", "")):
            fl_add_browser_line(self.pbr, "NO SUCH FILE!")


    def set_size(self, pobj, arg):
        fl_set_browser_fontsize(self.pbr, arg)





if __name__ == '__main__':
    Flfbrowse1(len(sys.argv), sys.argv)

