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
from xformslib import flbasic as flba
from xformslib import flxbasic as flxb
from xformslib import flmisc as flms
from xformslib import flbutton as flbt
from xformslib import flbrowser as flbr
from xformslib import xfdata as xfc




class BrowserAll(object):

    def __init__(self, lsysargv, sysargv):

        self.pbr = [0, 0, 0, 0]
        self.bnames = ["NORMAL_BROWSER", "SELECT_BROWSER", "HOLD_BROWSER", \
                  "MULTI_BROWSER"]

        flxb.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.create_form()
        self.fill_browsers()
        flba.fl_show_form(self.pform, xfc.FL_PLACE_CENTER | xfc.FL_FREE_SIZE, \
                          xfc.FL_TRANSIENT, "All Browsers")
        flba.fl_do_forms()
        flba.fl_hide_form(self.pform)


    def create_form(self):
        self.pform = flba.fl_bgn_form(xfc.FL_UP_BOX, 700, 570)
        self.preadout = flms.fl_add_text(xfc.FL_NORMAL_TEXT, 50, 30, 600, 50, "")
        flba.fl_set_object_lsize(self.preadout, xfc.FL_NORMAL_SIZE)
        flba.fl_set_object_lalign(self.preadout, xfc.FL_ALIGN_CENTER)
        flba.fl_set_object_lstyle(self.preadout, xfc.FL_BOLD_STYLE)
        flba.fl_set_object_boxtype(self.preadout, xfc.FL_UP_BOX)
        flba.fl_set_object_color(self.preadout, xfc.FL_MAGENTA, xfc.FL_MAGENTA)
        self.pbr[0] = flbr.fl_add_browser(xfc.FL_NORMAL_BROWSER, 20, 120, 150, 290,
                                     self.bnames[0])
        flba.fl_set_object_callback(self.pbr[0], self.br_callback, 0)
        self.pbr[1] = flbr.fl_add_browser(xfc.FL_SELECT_BROWSER, 190, 120, 150, 290,
                                     self.bnames[1])
        flba.fl_set_object_callback(self.pbr[1], self.br_callback, 1)
        self.pbr[2] = flbr.fl_add_browser(xfc.FL_HOLD_BROWSER, 360, 120, 150, 290,
                                     self.bnames[2])
        flba.fl_set_object_color(self.pbr[2], xfc.FL_WHITE, xfc.FL_GREEN)
        flba.fl_set_object_callback(self.pbr[2], self.br_callback, 2)
        self.pbr[3] = flbr.fl_add_browser(xfc.FL_MULTI_BROWSER, 530, 120, 150, 290,
                                     self.bnames[3])
        flba.fl_set_object_color(self.pbr[3],xfc.FL_WHITE, xfc.FL_CYAN)
        flba.fl_set_object_callback(self.pbr[3], self.br_callback, 3)
        self.pexitobj = flbt.fl_add_button(xfc.FL_NORMAL_BUTTON, 560, 510, 120, 30, "Exit")
        self.pobj1 = flbt.fl_add_button(xfc.FL_NORMAL_BUTTON, 560, 460, 120, 30, "Deselect")
        flba.fl_set_object_callback(self.pobj1, self.deselect, 0)

        flba.fl_bgn_group()
        self.pobj2 = flbt.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 20, 500, 100, 30, "Tiny")
        flba.fl_set_object_lsize(self.pobj2, xfc.FL_TINY_SIZE)
        flba.fl_set_object_callback(self.pobj2, self.set_size, flba.fl_get_object_lsize(self.pobj2))
        self.pobj3 = flbt.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 130, 500, 100, 30, "Small")
        flba.fl_set_object_lsize(self.pobj3, xfc.FL_SMALL_SIZE)
        flba.fl_set_object_callback(self.pobj3, self.set_size, flba.fl_get_object_lsize(self.pobj3))
        flbt.fl_set_button(self.pobj3, 1)
        self.pobj4 = flbt.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 240, 500, 100, 30, "Normal")
        flba.fl_set_object_lsize(self.pobj4, xfc.FL_NORMAL_SIZE)
        flba.fl_set_object_callback(self.pobj4, self.set_size, flba.fl_get_object_lsize(self.pobj4))
        self.pobj5 = flbt.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 350, 500, 100, 30, "Large")
        flba.fl_set_object_lsize(self.pobj5, xfc.FL_LARGE_SIZE)
        flba.fl_set_object_callback(self.pobj5, self.set_size, flba.fl_get_object_lsize(self.pobj5))
        self.pobj6 = flbt.fl_add_button(xfc.FL_BUTTON, 470, 510, 45,30, "Link")
        flba.fl_set_object_callback(self.pobj6, self.link_browsers, 0)
        flba.fl_end_group()

        flba.fl_bgn_group()
        self.pobj7 = flbt.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 20, 450, 100, 30, \
                                        "Normal")
        flba.fl_set_object_callback(self.pobj7, self.set_style, xfc.FL_NORMAL_STYLE)
        flbt.fl_set_button(self.pobj7, 1)
        self.pobj8 = flbt.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 120, 450, 100, 30, \
                                        "Bold")
        flba.fl_set_object_callback(self.pobj8, self.set_style, xfc.FL_BOLD_STYLE)
        self.pobj9 = flbt.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 220, 450, 100, 30, \
                                        "Italic")
        flba.fl_set_object_callback(self.pobj9, self.set_style, xfc.FL_ITALIC_STYLE)
        self.pobj10 = flbt.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 320, 450, 100, 30,
                                         "BoldItalic")
        flba.fl_set_object_callback(self.pobj10, self.set_style, xfc.FL_BOLDITALIC_STYLE)
        self.pobj11 = flbt.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 420, 450, 100, 30, \
                                         "Fixed")
        flba.fl_set_object_callback(self.pobj11, self.set_style, xfc.FL_FIXED_STYLE)
        flba.fl_end_group()

        flba.fl_end_form()


    def deselect(self, pobj, arg):
        for i in range(0, 4):
            flbr.fl_deselect_browser(self.pbr[i])


    def set_size(self, pobj, arg):
        for i in range(0, 4):
            flbr.fl_set_browser_fontsize(self.pbr[i], arg)


    def set_style(self, pobj, arg):
        for i in range(0, 4):
            flbr.fl_set_browser_fontstyle(self.pbr[i], arg)


    def br_callback(self, pobj, arg):

        mb = ["left", "middle", "right", "scroll-up", "scroll-down"]
        i = flba.fl_mouse_button()
        if i >= xfc.FL_LEFT_MOUSE and i <= xfc.FL_SCROLLDOWN_MOUSE:
            buf = "In %s [%s]: " % (self.bnames[arg], mb[i - xfc.FL_LEFT_MOUSE])
        else:
            buf = "In %s: " % self.bnames[arg]

        i = flbr.fl_get_browser(pobj)
        if i:
            if i > 0:
                ii = i
                txtsel = "was selected."
            else:
                ii = -i
                txtsel = "was deselected."
            buf += flbr.fl_get_browser_line(pobj, ii)
            buf += txtsel

        flba.fl_set_object_label(self.preadout, buf)


    def vcallback(self, pobj, topline, data):

        yoffset = flbr.fl_get_browser_yoffset(self.pbr[0])
        for i in range(0, 4):
            flbr.fl_set_browser_yoffset(self.pbr[i], yoffset)


    def donothing(self, pobj, topline, data):
        pass        # placeholder for disabled vcallback


    def link_browsers(self, pobj, data):

        sync = flbt.fl_get_button(pobj)
        if sync:
            linktxt = "Unlink"
        else:
            linktxt = "Link"
        flba.fl_set_object_label(pobj, linktxt)

        if sync:
            yoffset = flbr.fl_get_browser_yoffset(self.pbr[0])
            for i in range(1, 4):
                flbr.fl_set_browser_vscrollbar(self.pbr[i], xfc.FL_OFF)
                flbr.fl_set_browser_yoffset(self.pbr[i], yoffset)
            flbr.fl_set_browser_vscroll_callback(self.pbr[0], self.vcallback, 0)
        else:
            for i in range(1, 4):
                flbr.fl_set_browser_vscrollbar(self.pbr[i], xfc.FL_ON)
            flbr.fl_set_browser_vscroll_callback(self.pbr[0], self.donothing, 0)


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
                flbr.fl_add_browser_line(self.pbr[i], buf)




if __name__ == '__main__':
    BrowserAll(len(sys.argv), sys.argv)

