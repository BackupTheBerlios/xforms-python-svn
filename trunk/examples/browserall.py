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
from xformslib import flbasic, flxbasic, flmisc, flbutton, flbrowser, xfdata




class BrowserAll(object):

    def __init__(self, lsysargv, sysargv):

        self.pbr = [0, 0, 0, 0]
        self.bnames = ["NORMAL_BROWSER", "SELECT_BROWSER", "HOLD_BROWSER", \
                  "MULTI_BROWSER"]

        flxbasic.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.create_form()
        self.fill_browsers()
        flbasic.fl_show_form(self.pform, xfdata.FL_PLACE_CENTER | xfdata.FL_FREE_SIZE, \
                             xfdata.FL_TRANSIENT, "All Browsers")
        flbasic.fl_do_forms()
        flbasic.fl_hide_form(self.pform)
        return 0


    def create_form(self):
        self.pform = flbasic.fl_bgn_form(xfdata.FL_UP_BOX, 700, 570)
        self.preadout = flmisc.fl_add_text(xfdata.FL_NORMAL_TEXT, 50, 30, 600, 50, "")
        flbasic.fl_set_object_lsize(self.preadout, xfdata.FL_NORMAL_SIZE)
        flbasic.fl_set_object_lalign(self.preadout, xfdata.FL_ALIGN_CENTER)
        flbasic.fl_set_object_lstyle(self.preadout, xfdata.FL_BOLD_STYLE)
        flbasic.fl_set_object_boxtype(self.preadout, xfdata.FL_UP_BOX)
        flbasic.fl_set_object_color(self.preadout, xfdata.FL_MAGENTA, xfdata.FL_MAGENTA)
        self.pbr[0] = browserfn.fl_add_browser(xfdata.FL_NORMAL_BROWSER, 20, 120, 150, 290,
                                               self.bnames[0])
        flbasic.fl_set_object_callback(self.pbr[0], self.br_callback, 0)
        self.pbr[1] = browserfn.fl_add_browser(xfdata.FL_SELECT_BROWSER, 190, 120, 150, 290,
                                               self.bnames[1])
        flbasic.fl_set_object_callback(self.pbr[1], self.br_callback, 1)
        self.pbr[2] = browserfn.fl_add_browser(xfdata.FL_HOLD_BROWSER, 360, 120, 150, 290,
                                               self.bnames[2])
        flbasic.fl_set_object_color(self.pbr[2], xfdata.FL_WHITE, xfdata.FL_GREEN)
        flbasic.fl_set_object_callback(self.pbr[2], self.br_callback, 2)
        self.pbr[3] = browserfn.fl_add_browser(xfdata.FL_MULTI_BROWSER, 530, 120, 150, 290,
                                               self.bnames[3])
        flbasic.fl_set_object_color(self.pbr[3],xfdata.FL_WHITE, xfdata.FL_CYAN)
        flbasic.fl_set_object_callback(self.pbr[3], self.br_callback, 3)
        self.pexitobj = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 560, 510, 120, 30, "Exit")
        self.pobj1 = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 560, 460, 120, 30, "Deselect")
        flbasic.fl_set_object_callback(self.pobj1, self.deselect, 0)

        flbasic.fl_bgn_group()
        self.pobj2 = flbutton.fl_add_lightbutton(xfdata.FL_RADIO_BUTTON, 20, 500, 100, 30, "Tiny")
        flbasic.fl_set_object_lsize(self.pobj2, xfdata.FL_TINY_SIZE)
        flbasic.fl_set_object_callback(self.pobj2, self.set_size, flbasic.fl_get_object_lsize(self.pobj2))
        self.pobj3 = flbutton.fl_add_lightbutton(xfdata.FL_RADIO_BUTTON, 130, 500, 100, 30, "Small")
        flbasic.fl_set_object_lsize(self.pobj3, xfdata.FL_SMALL_SIZE)
        flbasic.fl_set_object_callback(self.pobj3, self.set_size, flbasic.fl_get_object_lsize(self.pobj3))
        flbutton.fl_set_button(self.pobj3, 1)
        self.pobj4 = flbutton.fl_add_lightbutton(xfdata.FL_RADIO_BUTTON, 240, 500, 100, 30, "Normal")
        flbasic.fl_set_object_lsize(self.pobj4, xfdata.FL_NORMAL_SIZE)
        flbasic.fl_set_object_callback(self.pobj4, self.set_size, flbasic.fl_get_object_lsize(self.pobj4))
        self.pobj5 = flbutton.fl_add_lightbutton(xfdata.FL_RADIO_BUTTON, 350, 500, 100, 30, "Large")
        flbasic.fl_set_object_lsize(self.pobj5, xfdata.FL_LARGE_SIZE)
        flbasic.fl_set_object_callback(self.pobj5, self.set_size, flbasic.fl_get_object_lsize(self.pobj5))
        self.pobj6 = flbutton.fl_add_button(xfdata.FL_BUTTON, 470, 510, 45,30, "Link")
        flbasic.fl_set_object_callback(self.pobj6, self.link_browsers, 0)
        flbasic.fl_end_group()

        flbasic.fl_bgn_group()
        self.pobj7 = flbutton.fl_add_lightbutton(xfdata.FL_RADIO_BUTTON, 20, 450, 100, 30, \
                                        "Normal")
        flbasic.fl_set_object_callback(self.pobj7, self.set_style, xfdata.FL_NORMAL_STYLE)
        flbutton.fl_set_button(self.pobj7, 1)
        self.pobj8 = flbutton.fl_add_lightbutton(xfdata.FL_RADIO_BUTTON, 120, 450, 100, 30, \
                                                 "Bold")
        flbasic.fl_set_object_callback(self.pobj8, self.set_style, xfdata.FL_BOLD_STYLE)
        self.pobj9 = flbutton.fl_add_lightbutton(xfdata.FL_RADIO_BUTTON, 220, 450, 100, 30, \
                                        "Italic")
        flbasic.fl_set_object_callback(self.pobj9, self.set_style, xfdata.FL_ITALIC_STYLE)
        self.pobj10 = flbutton.fl_add_lightbutton(xfdata.FL_RADIO_BUTTON, 320, 450, 100, 30,
                                         "BoldItalic")
        flbasic.fl_set_object_callback(self.pobj10, self.set_style, xfdata.FL_BOLDITALIC_STYLE)
        self.pobj11 = flbutton.fl_add_lightbutton(xfdata.FL_RADIO_BUTTON, 420, 450, 100, 30, \
                                         "Fixed")
        flbasic.fl_set_object_callback(self.pobj11, self.set_style, xfdata.FL_FIXED_STYLE)
        flbasic.fl_end_group()

        flbasic.fl_end_form()


    def deselect(self, pobj, arg):
        for i in range(0, 4):
            browserfn.fl_deselect_browser(self.pbr[i])


    def set_size(self, pobj, arg):
        for i in range(0, 4):
            browserfn.fl_set_browser_fontsize(self.pbr[i], arg)


    def set_style(self, pobj, arg):
        for i in range(0, 4):
            browserfn.fl_set_browser_fontstyle(self.pbr[i], arg)


    def br_callback(self, pobj, arg):

        mb = ["left", "middle", "right", "scroll-up", "scroll-down"]
        i = flbasic.fl_mouse_button()
        if i >= xfdata.FL_LEFT_MOUSE and i <= xfdata.FL_SCROLLDOWN_MOUSE:
            buf = "In %s [%s]: " % (self.bnames[arg], mb[i - xfdata.FL_LEFT_MOUSE])
        else:
            buf = "In %s: " % self.bnames[arg]

        i = browserfn.fl_get_browser(pobj)
        if i:
            if i > 0:
                ii = i
                txtsel = "was selected."
            else:
                ii = -i
                txtsel = "was deselected."
            buf += browserfn.fl_get_browser_line(pobj, ii)
            buf += txtsel

        flbasic.fl_set_object_label(self.preadout, buf)


    def vcallback(self, pobj, topline, data):

        yoffset = browserfn.fl_get_browser_yoffset(self.pbr[0])
        for i in range(0, 4):
            browserfn.fl_set_browser_yoffset(self.pbr[i], yoffset)


    def donothing(self, pobj, topline, data):
        pass        # placeholder for disabled vcallback


    def link_browsers(self, pobj, data):

        sync = flbutton.fl_get_button(pobj)
        if sync:
            linktxt = "Unlink"
        else:
            linktxt = "Link"
        flbasic.fl_set_object_label(pobj, linktxt)

        if sync:
            yoffset = browserfn.fl_get_browser_yoffset(self.pbr[0])
            for i in range(1, 4):
                browserfn.fl_set_browser_vscrollbar(self.pbr[i], xfdata.FL_OFF)
                browserfn.fl_set_browser_yoffset(self.pbr[i], yoffset)
            browserfn.fl_set_browser_vscroll_callback(self.pbr[0], self.vcallback, 0)
        else:
            for i in range(1, 4):
                browserfn.fl_set_browser_vscrollbar(self.pbr[i], xfdata.FL_ON)
            browserfn.fl_set_browser_vscroll_callback(self.pbr[0], self.donothing, 0)


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

                browserfn.fl_add_browser_line(self.pbr[i], buf)




if __name__ == '__main__':
    appl = BrowserAll(len(sys.argv), sys.argv)

