#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  fbrowse.c XForms demo, with some adaptations.
#
#  fbrowse.c was written by T.C. Zhao and M. Overmars
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a browser and a file selector.
# Good browser/scrollbar test
#

import sys
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flgoodies import *
from xformslib.flbrowser import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *



class Flfbrowse(object):

    def __init__(self, lsysarg, sysargv):

        fl_initialize(lsysarg, sysargv, "FormDemo", 0, 0)
        fdnew = self.create_form()

        fl_clear_browser(self.pbr)
        fl_add_browser_line(self.pbr, "LOAD A FILE.")
        fl_set_browser_fontstyle(self.pbr, FL_FIXED_STYLE)

        fl_show_form(fdnew, FL_PLACE_FREE, FL_FULLBORDER, \
                    "Browser")

        poret = fl_do_forms()

        if poret.contents.label:
            prndata = poret.contents.label
        else:
            prndata = ""
        print "%p %d %s\n" % poret.contents, poret.contents.objclass, prndata

        fl_hide_form(fdnew)
        fl_free_form(fdnew)

        fl_finish()


    def load_file(self, pobj, arg):
        fname = fl_show_file_selector("File To Load", "", "*", "")
        if fname:
            if not fl_load_browser(self.pbr, fname):
                fl_add_browser_line(self.pbr,"NO SUCH FILE!")


    def set_size(self, pobj, arg):
        fl_set_browser_fontsize(self.pbr, arg)


    def exit_program(self, pobj, data):
        fl_finish()
        sys.exit(0)


    def hide_show(self, pobj, data):
        if fl_object_is_visible(self.pbr):
            fl_hide_object(self.pbr)
        else:
            fl_show_object(self.pbr)


    def create_form(self):

        x = 20
        dx = 80
        dy = 28

        pform = fl_bgn_form(FL_NO_BOX, 590, 610)
        pobj1 = fl_add_box(FL_UP_BOX, 0, 0, 590, 610, "")

        self.pbr = fl_add_browser(FL_NORMAL_BROWSER, 20, 20, 550, 530, "")
        fl_set_object_boxtype(self.pbr, FL_EMBOSSED_BOX)

        pobj1 = fl_add_button(FL_NORMAL_BUTTON, x, 565, dx-5, dy, "Load")
        fl_set_object_callback(pobj1, self.load_file, 0)
        x += dx

        pobj2 = fl_add_lightbutton(FL_RADIO_BUTTON, x, 565, dx, dy, "Tiny")
        fl_set_object_callback(pobj2, self.set_size, FL_TINY_SIZE)
        x += dx

        pobj3 = fl_add_lightbutton(FL_RADIO_BUTTON, x , 565, dx, dy, "Small")
        fl_set_object_callback(pobj3, self.set_size, FL_SMALL_SIZE)
        fl_set_button(pobj3, FL_SMALL_SIZE == FL_BROWSER_FONTSIZE)
        x += dx

        pobj4 = fl_add_lightbutton(FL_RADIO_BUTTON, x , 565, dx, dy, "Normal")
        fl_set_object_callback(pobj4, self.set_size, FL_NORMAL_SIZE)
        fl_set_button(pobj4, FL_NORMAL_SIZE == FL_BROWSER_FONTSIZE)
        x += dx

        pobj5 = fl_add_lightbutton(FL_RADIO_BUTTON, x , 565, dx, dy, "Large")
        fl_set_object_callback(pobj5, self.set_size, FL_LARGE_SIZE)
        x += dx

        pobj6 = fl_add_button(FL_NORMAL_BUTTON, x, 565, dx, dy, "Hide/Show")
        fl_set_object_callback(pobj6, self.hide_show, 0)
        x += dx

        pobj7 = fl_add_button(FL_NORMAL_BUTTON, x, 565, dx, dy, "Exit")       #60->dx
        fl_set_object_callback(pobj7, self.exit_program, 0)

        fl_end_form()

        fl_adjust_form_size(pform)

        return pform






if __name__ == '__main__':
    Flfbrowse(len(sys.argv), sys.argv)

