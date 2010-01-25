#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  browserall.c XForms demo, with some adaptations.
#
#  browserall.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This is a demo that shows the different types of browsers.
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flmisc import *
from xformslib.flbutton import *
from xformslib.flbrowser import *
from xformslib.xfdata import *




class BrowserAll(object):

    def __init__(self, lsysargv, sysargv):

        self.pbr = [0, 0, 0, 0]
        self.bnames = ["NORMAL_BROWSER", "SELECT_BROWSER", "HOLD_BROWSER", \
                  "MULTI_BROWSER"]

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.create_form()
        self.fill_browsers()
        fl_show_form(self.pform, FL_PLACE_CENTER | FL_FREE_SIZE, \
                             FL_TRANSIENT, "All Browsers")
        fl_do_forms()
        fl_hide_form(self.pform)


    def create_form(self):
        self.pform = fl_bgn_form(FL_UP_BOX, 700, 570)
        self.preadout = fl_add_text(FL_NORMAL_TEXT, 50, 30, 600, 50, "")
        fl_set_object_lsize(self.preadout, FL_NORMAL_SIZE)
        fl_set_object_lalign(self.preadout, FL_ALIGN_CENTER)
        fl_set_object_lstyle(self.preadout, FL_BOLD_STYLE)
        fl_set_object_boxtype(self.preadout, FL_UP_BOX)
        fl_set_object_color(self.preadout, FL_MAGENTA, FL_MAGENTA)
        self.pbr[0] = fl_add_browser(FL_NORMAL_BROWSER, 20, 120, 150, 290,
                                     self.bnames[0])
        fl_set_object_callback(self.pbr[0], self.br_callback, 0)
        self.pbr[1] = fl_add_browser(FL_SELECT_BROWSER, 190, 120, 150, 290,
                                     self.bnames[1])
        fl_set_object_callback(self.pbr[1], self.br_callback, 1)
        self.pbr[2] = fl_add_browser(FL_HOLD_BROWSER, 360, 120, 150, 290,
                                     self.bnames[2])
        fl_set_object_color(self.pbr[2], FL_WHITE, FL_GREEN)
        fl_set_object_callback(self.pbr[2], self.br_callback, 2)
        self.pbr[3] = fl_add_browser(FL_MULTI_BROWSER, 530, 120, 150, 290,
                                     self.bnames[3])
        fl_set_object_color(self.pbr[3],FL_WHITE, FL_CYAN)
        fl_set_object_callback(self.pbr[3], self.br_callback, 3)
        self.pexitobj = fl_add_button(FL_NORMAL_BUTTON, 560, 510, 120, 30, "Exit")
        self.pobj1 = fl_add_button(FL_NORMAL_BUTTON, 560, 460, 120, 30, "Deselect")
        fl_set_object_callback(self.pobj1, self.deselect, 0)

        fl_bgn_group()
        self.pobj2 = fl_add_lightbutton(FL_RADIO_BUTTON, 20, 500, 100, 30, "Tiny")
        fl_set_object_lsize(self.pobj2, FL_TINY_SIZE)
        fl_set_object_callback(self.pobj2, self.set_size, fl_get_object_lsize(self.pobj2))
        self.pobj3 = fl_add_lightbutton(FL_RADIO_BUTTON, 130, 500, 100, 30, "Small")
        fl_set_object_lsize(self.pobj3, FL_SMALL_SIZE)
        fl_set_object_callback(self.pobj3, self.set_size, fl_get_object_lsize(self.pobj3))
        fl_set_button(self.pobj3, 1)
        self.pobj4 = fl_add_lightbutton(FL_RADIO_BUTTON, 240, 500, 100, 30, "Normal")
        fl_set_object_lsize(self.pobj4, FL_NORMAL_SIZE)
        fl_set_object_callback(self.pobj4, self.set_size, fl_get_object_lsize(self.pobj4))
        self.pobj5 = fl_add_lightbutton(FL_RADIO_BUTTON, 350, 500, 100, 30, "Large")
        fl_set_object_lsize(self.pobj5, FL_LARGE_SIZE)
        fl_set_object_callback(self.pobj5, self.set_size, fl_get_object_lsize(self.pobj5))
        self.pobj6 = fl_add_button(FL_BUTTON, 470, 510, 45,30, "Link")
        fl_set_object_callback(self.pobj6, self.link_browsers, 0)
        fl_end_group()

        fl_bgn_group()
        self.pobj7 = fl_add_lightbutton(FL_RADIO_BUTTON, 20, 450, 100, 30, \
                                        "Normal")
        fl_set_object_callback(self.pobj7, self.set_style, FL_NORMAL_STYLE)
        fl_set_button(self.pobj7, 1)
        self.pobj8 = fl_add_lightbutton(FL_RADIO_BUTTON, 120, 450, 100, 30, \
                                        "Bold")
        fl_set_object_callback(self.pobj8, self.set_style, FL_BOLD_STYLE)
        self.pobj9 = fl_add_lightbutton(FL_RADIO_BUTTON, 220, 450, 100, 30, \
                                        "Italic")
        fl_set_object_callback(self.pobj9, self.set_style, FL_ITALIC_STYLE)
        self.pobj10 = fl_add_lightbutton(FL_RADIO_BUTTON, 320, 450, 100, 30,
                                         "BoldItalic")
        fl_set_object_callback(self.pobj10, self.set_style, FL_BOLDITALIC_STYLE)
        self.pobj11 = fl_add_lightbutton(FL_RADIO_BUTTON, 420, 450, 100, 30, \
                                         "Fixed")
        fl_set_object_callback(self.pobj11, self.set_style, FL_FIXED_STYLE)
        fl_end_group()

        fl_end_form()


    def deselect(self, pobj, arg):
        for i in range(0, 4):
            fl_deselect_browser(self.pbr[i])


    def set_size(self, pobj, arg):
        for i in range(0, 4):
            fl_set_browser_fontsize(self.pbr[i], arg)


    def set_style(self, pobj, arg):
        for i in range(0, 4):
            fl_set_browser_fontstyle(self.pbr[i], arg)


    def br_callback(self, pobj, arg):

        mb = ["left", "middle", "right", "scroll-up", "scroll-down"]
        i = fl_mouse_button()
        if i >= FL_LEFT_MOUSE and i <= FL_SCROLLDOWN_MOUSE:
            buf = "In %s [%s]: " % (self.bnames[arg], mb[i - FL_LEFT_MOUSE])
        else:
            buf = "In %s: " % self.bnames[arg]

        i = fl_get_browser(pobj)
        if i:
            if i > 0:
                ii = i
                txtsel = "was selected."
            else:
                ii = -i
                txtsel = "was deselected."
            buf += fl_get_browser_line(pobj, ii)
            buf += txtsel

        fl_set_object_label(self.preadout, buf)


    def vcallback(self, pobj, topline, data):

        yoffset = fl_get_browser_yoffset(self.pbr[0])
        for i in range(0, 4):
            fl_set_browser_yoffset(self.pbr[i], yoffset)


    def donothing(self, pobj, topline, data):
        pass        # placeholder for disabled vcallback


    def link_browsers(self, pobj, data):

        sync = fl_get_button(pobj)
        if sync:
            linktxt = "Unlink"
        else:
            linktxt = "Link"
        fl_set_object_label(pobj, linktxt)

        if sync:
            yoffset = fl_get_browser_yoffset(self.pbr[0])
            for i in range(1, 4):
                fl_set_browser_vscrollbar(self.pbr[i], FL_OFF)
                fl_set_browser_yoffset(self.pbr[i], yoffset)
            fl_set_browser_vscroll_callback(self.pbr[0], self.vcallback, 0)
        else:
            for i in range(1, 4):
                fl_set_browser_vscrollbar(self.pbr[i], FL_ON)
            fl_set_browser_vscroll_callback(self.pbr[0], self.donothing, 0)


    def fill_browsers(self):

        for i in range(0, 4):
            for j in range(1, 100+1):
                if j == 5 or j == 6:
                    buf = "@NLine with qb %3d" % j
                elif j == 10:
                    buf = "@-trailing text should be ignored"
                elif j == 40:
                    buf = "@mLine with qb %3d" % j
                else:
                    buf = "Line with qb %3d" % j
                fl_add_browser_line(self.pbr[i], buf)




if __name__ == '__main__':
    BrowserAll(len(sys.argv), sys.argv)

