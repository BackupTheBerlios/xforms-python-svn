#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  fonts.c XForms demo, with some adaptations.
#
#  fonts.c was written by M. Overmars and T.C. Zhao
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Demo, showing the different fonts in different sizes.
#

import sys
import xformslib as xfl


class FD_fontsform(object):
    fontsform = None
    vdata = None
    cdata = None
    ldata = None
    fontobj = None
    sizeobj = None
    textobj = None


class Flfonts(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_set_border_width(-3)
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.ui = self.create_form_fontsform()
        xfl.fl_scale_form(self.ui.pfontsform, 1.1, 1.2)
        xfl.fl_set_object_dblbuffer(self.ui.ptextobj, 1)
        xfl.fl_set_object_bw(self.ui.ptextobj, 5)
        xfl.fl_enumerate_fonts(self.addit, 1)
        xfl.fl_select_browser_line(self.ui.pfontobj, 1)
        xfl.fl_addto_browser(self.ui.psizeobj, "8  (tiny)")
        xfl.fl_addto_browser(self.ui.psizeobj, "10 (small)")
        xfl.fl_addto_browser(self.ui.psizeobj, "11 (scaled)")
        xfl.fl_addto_browser(self.ui.psizeobj, "12 (normal)")
        xfl.fl_addto_browser(self.ui.psizeobj, "13 (scaled)")
        xfl.fl_addto_browser(self.ui.psizeobj, "14 (medium)")
        xfl.fl_addto_browser(self.ui.psizeobj, "18 (large)")
        xfl.fl_addto_browser(self.ui.psizeobj, "24 (Huge)")
        xfl.fl_addto_browser(self.ui.psizeobj, "30 (scaled)")
        xfl.fl_select_browser_line(self.ui.psizeobj, 2)
        xfl.fl_set_object_lstyle(self.ui.ptextobj, xfl.FL_NORMAL_STYLE)
        xfl.fl_call_object_callback(self.ui.pfontobj)
        xfl.fl_call_object_callback(self.ui.psizeobj)
        xfl.fl_show_form(self.ui.pfontsform, xfl.FL_PLACE_CENTER, \
                xfl.FL_TRANSIENT, "Fonts")
        xfl.fl_do_forms()


    def done_cb(self, pobj, arg):
        xfl.fl_finish()
        sys.exit(0)


    def style_cb(self, pobj, arg):
        xfl.fl_set_object_lstyle(self.ui.ptextobj, \
                xfl.fl_get_browser(pobj) - 1)


    def size_cb(self, pobj, arg):
        sizes = [8, 10, 11, 12, 13, 14, 18, 24, 30]
        xfl.fl_set_object_lsize(self.ui.ptextobj, \
                sizes[xfl.fl_get_browser(pobj) - 1 ])


    def addit(self, txtstr):
        xfl.fl_add_browser_line(self.ui.pfontobj, txtstr)


    def create_form_fontsform(self):
        fdui = FD_fontsform()
        fdui.pfontsform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 371, 296)
        pobj = xfl.fl_add_box(xfl.FL_FLAT_BOX, 0, 0, 371, 296, "")
        xfl.fl_set_object_color(pobj, xfl.FL_SLATEBLUE, xfl.FL_COL1)
        fdui.pfontobj = xfl.fl_add_browser(xfl.FL_HOLD_BROWSER, 10, 145, \
                195, 135, "")
        xfl.fl_set_object_lalign(fdui.pfontobj, \
                xfl.FL_ALIGN_BOTTOM | xfl.FL_ALIGN_INSIDE)
        xfl.fl_set_object_callback(fdui.pfontobj, self.style_cb, 0)
        fdui.psizeobj = xfl.fl_add_browser(xfl.FL_HOLD_BROWSER, 215, 145, \
                145, 135, "")
        xfl.fl_set_object_lalign(fdui.psizeobj, \
                xfl.FL_ALIGN_BOTTOM | xfl.FL_ALIGN_INSIDE)
        xfl.fl_set_object_callback(fdui.psizeobj, self.size_cb, 0)
        fdui.ptextobj = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 10, 5, 351, \
                125, "The quick brown\nfox jumps over\nthe lazy dog.")
        xfl.fl_set_object_boxtype(fdui.ptextobj, xfl.FL_FRAME_BOX)
        xfl.fl_set_object_lalign(fdui.ptextobj, xfl.FL_ALIGN_CENTER)
        pobj = xfl.fl_add_button(xfl.FL_HIDDEN_BUTTON, 0, 0, 370, 140, \
                "Button")
        xfl.fl_set_button_shortcut(pobj, "^[qQ", 1)
        xfl.fl_set_object_callback(pobj, self.done_cb, 0)
        xfl.fl_end_form()
        return fdui


if __name__ == '__main__':
    print("********* fonts.py *********")
    Flfonts(len(sys.argv), sys.argv)
