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
import xformslib as xfl


class BrowserAll(object):

    def __init__(self, lsysargv, sysargv):

        self.pbr = [0, 0, 0, 0]
        self.bnames = ["NORMAL_BROWSER", "SELECT_BROWSER", "HOLD_BROWSER", \
                "MULTI_BROWSER"]
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.create_form()
        self.fill_browsers()
        xfl.fl_show_form(self.pform, xfl.FL_PLACE_CENTER | xfl.FL_FREE_SIZE, \
                xfl.FL_TRANSIENT, "All Browsers")
        xfl.fl_do_forms()
        xfl.fl_hide_form(self.pform)


    def create_form(self):
        self.pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 700, 570)
        self.preadout = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 50, 30, \
                600, 50, "")
        xfl.fl_set_object_lsize(self.preadout, xfl.FL_NORMAL_SIZE)
        xfl.fl_set_object_lalign(self.preadout, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(self.preadout, xfl.FL_BOLD_STYLE)
        xfl.fl_set_object_boxtype(self.preadout, xfl.FL_UP_BOX)
        xfl.fl_set_object_color(self.preadout, xfl.FL_MAGENTA, \
                xfl.FL_MAGENTA)
        self.pbr[0] = xfl.fl_add_browser(xfl.FL_NORMAL_BROWSER, 20, 120, \
                150, 290, self.bnames[0])
        xfl.fl_set_object_callback(self.pbr[0], self.br_callback, 0)
        self.pbr[1] = xfl.fl_add_browser(xfl.FL_SELECT_BROWSER, 190, 120, \
                150, 290, self.bnames[1])
        xfl.fl_set_object_callback(self.pbr[1], self.br_callback, 1)
        self.pbr[2] = xfl.fl_add_browser(xfl.FL_HOLD_BROWSER, 360, 120, \
                150, 290, self.bnames[2])
        xfl.fl_set_object_color(self.pbr[2], xfl.FL_WHITE, xfl.FL_GREEN)
        xfl.fl_set_object_callback(self.pbr[2], self.br_callback, 2)
        self.pbr[3] = xfl.fl_add_browser(xfl.FL_MULTI_BROWSER, 530, 120, \
                150, 290, self.bnames[3])
        xfl.fl_set_object_color(self.pbr[3],xfl.FL_WHITE, xfl.FL_CYAN)
        xfl.fl_set_object_callback(self.pbr[3], self.br_callback, 3)
        self.pexitobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 560, 510, \
                120, 30, "Exit")
        self.pobj1 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 560, 460, \
                120, 30, "Deselect")
        xfl.fl_set_object_callback(self.pobj1, self.deselect, 0)

        xfl.fl_bgn_group()
        self.pobj2 = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 20, 500, \
                100, 30, "Tiny")
        xfl.fl_set_object_lsize(self.pobj2, xfl.FL_TINY_SIZE)
        xfl.fl_set_object_callback(self.pobj2, self.set_size, \
                xfl.fl_get_object_lsize(self.pobj2))
        self.pobj3 = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 130, 500, \
                100, 30, "Small")
        xfl.fl_set_object_lsize(self.pobj3, xfl.FL_SMALL_SIZE)
        xfl.fl_set_object_callback(self.pobj3, self.set_size, \
                xfl.fl_get_object_lsize(self.pobj3))
        xfl.fl_set_button(self.pobj3, 1)
        self.pobj4 = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 240, 500, \
                100, 30, "Normal")
        xfl.fl_set_object_lsize(self.pobj4, xfl.FL_NORMAL_SIZE)
        xfl.fl_set_object_callback(self.pobj4, self.set_size, \
                xfl.fl_get_object_lsize(self.pobj4))
        self.pobj5 = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 350, 500, \
                100, 30, "Large")
        xfl.fl_set_object_lsize(self.pobj5, xfl.FL_LARGE_SIZE)
        xfl.fl_set_object_callback(self.pobj5, self.set_size, \
                xfl.fl_get_object_lsize(self.pobj5))
        self.pobj6 = xfl.fl_add_button(xfl.FL_BUTTON, 470, 510, 45, 30, \
                "Link")
        xfl.fl_set_object_callback(self.pobj6, self.link_browsers, 0)
        xfl.fl_end_group()

        xfl.fl_bgn_group()
        self.pobj7 = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 20, 450, \
                100, 30, "Normal")
        xfl.fl_set_object_callback(self.pobj7, self.set_style, \
                xfl.FL_NORMAL_STYLE)
        xfl.fl_set_button(self.pobj7, 1)
        self.pobj8 = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 120, 450, \
                100, 30, "Bold")
        xfl.fl_set_object_callback(self.pobj8, self.set_style, \
                xfl.FL_BOLD_STYLE)
        self.pobj9 = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 220, 450, \
                100, 30, "Italic")
        xfl.fl_set_object_callback(self.pobj9, self.set_style, \
                xfl.FL_ITALIC_STYLE)
        self.pobj10 = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 320, 450, \
                100, 30, "BoldItalic")
        xfl.fl_set_object_callback(self.pobj10, self.set_style, \
                xfl.FL_BOLDITALIC_STYLE)
        self.pobj11 = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 420, 450, \
                100, 30, "Fixed")
        xfl.fl_set_object_callback(self.pobj11, self.set_style, \
                xfl.FL_FIXED_STYLE)
        xfl.fl_end_group()

        xfl.fl_end_form()


    def deselect(self, pobj, arg):
        for i in range(0, 4):
            xfl.fl_deselect_browser(self.pbr[i])


    def set_size(self, pobj, arg):
        for i in range(0, 4):
            xfl.fl_set_browser_fontsize(self.pbr[i], arg)


    def set_style(self, pobj, arg):
        for i in range(0, 4):
            xfl.fl_set_browser_fontstyle(self.pbr[i], arg)


    def br_callback(self, pobj, arg):

        mb = ["left", "middle", "right", "scroll-up", "scroll-down"]
        i = xfl.fl_mouse_button()
        if i >= xfl.FL_LEFT_MOUSE and i <= xfl.FL_SCROLLDOWN_MOUSE:
            buf = "In %s [%s]: " % (self.bnames[arg], \
                    mb[i - xfl.FL_LEFT_MOUSE])
        else:
            buf = "In %s: " % self.bnames[arg]

        i = xfl.fl_get_browser(pobj)
        if i:
            if i > 0:
                ii = i
                txtsel = " was selected."
            else:
                ii = -i
                txtsel = " was deselected."
            buf += xfl.fl_get_browser_line(pobj, ii)
            buf += txtsel

        xfl.fl_set_object_label(self.preadout, buf)


    def vcallback(self, pobj, topline, pvdata):
        ldata = xfl.convert_ptrvoid_to_ptrlongc(pvdata).contents.value
        print("ldata", ldata)
        yoffset = xfl.fl_get_browser_yoffset(self.pbr[0])
        for i in range(0, 4):
            xfl.fl_set_browser_yoffset(self.pbr[i], yoffset)


    def donothing(self, pobj, topline, pvdata):
        print "pvdata", pvdata
        ldata = xfl.convert_ptrvoid_to_ptrlongc(pvdata).contents.value
        print "ldata", ldata
        pass        # placeholder for disabled vcallback


    def link_browsers(self, pobj, data):

        sync = xfl.fl_get_button(pobj)
        if sync:
            linktxt = "Unlink"
        else:
            linktxt = "Link"
        xfl.fl_set_object_label(pobj, linktxt)

        if sync:
            yoffset = xfl.fl_get_browser_yoffset(self.pbr[0])
            for i in range(1, 4):
                xfl.fl_set_browser_vscrollbar(self.pbr[i], xfl.FL_OFF)
                xfl.fl_set_browser_yoffset(self.pbr[i], yoffset)
            xfl.fl_set_browser_vscroll_callback(self.pbr[0], \
                    self.vcallback, 11)          # 0
        else:
            for i in range(1, 4):
                xfl.fl_set_browser_vscrollbar(self.pbr[i], xfl.FL_ON)
            xfl.fl_set_browser_vscroll_callback(self.pbr[0], \
                    self.donothing, 12)          # 0


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
                xfl.fl_add_browser_line(self.pbr[i], buf)



if __name__ == '__main__':
    print("********* browserall.py *********")
    BrowserAll(len(sys.argv), sys.argv)

