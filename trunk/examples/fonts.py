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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbrowser import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *



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

        fl_set_border_width(-3)
        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        self.ui = self.create_form_fontsform()
        fl_scale_form(self.ui.pfontsform, 1.1, 1.2)
        fl_set_object_dblbuffer(self.ui.ptextobj, 1)
        fl_set_object_bw(self.ui.ptextobj, 5)

        fl_enumerate_fonts(self.addit, 1)
        fl_select_browser_line(self.ui.pfontobj, 1)
        fl_addto_browser(self.ui.psizeobj, "8  (tiny)")
        fl_addto_browser(self.ui.psizeobj, "10 (small)")
        fl_addto_browser(self.ui.psizeobj, "11 (scaled)")
        fl_addto_browser(self.ui.psizeobj, "12 (normal)")
        fl_addto_browser(self.ui.psizeobj, "13 (scaled)")
        fl_addto_browser(self.ui.psizeobj, "14 (medium)")
        fl_addto_browser(self.ui.psizeobj, "18 (large)")
        fl_addto_browser(self.ui.psizeobj, "24 (Huge)")
        fl_addto_browser(self.ui.psizeobj, "30 (scaled)")
        fl_select_browser_line(self.ui.psizeobj, 2)
        fl_set_object_lstyle(self.ui.ptextobj, FL_NORMAL_STYLE)
        fl_call_object_callback(self.ui.pfontobj)
        fl_call_object_callback(self.ui.psizeobj)
        fl_show_form(self.ui.pfontsform, FL_PLACE_CENTER, FL_TRANSIENT, "Fonts")

        fl_do_forms()


    def done_cb(self, pobj, arg):
        fl_finish()
        sys.exit(0)


    def style_cb(self, pobj, arg):
        fl_set_object_lstyle(self.ui.ptextobj, fl_get_browser(pobj) - 1)


    def size_cb(self, pobj, arg):
        sizes = [8, 10, 11, 12, 13, 14, 18, 24, 30]
        fl_set_object_lsize(self.ui.ptextobj, sizes[fl_get_browser(pobj) - 1 ])


    def addit(self, txtstr):
        fl_add_browser_line(self.ui.pfontobj, txtstr)


    def create_form_fontsform(self):

        fdui = FD_fontsform()

        fdui.pfontsform = fl_bgn_form(FL_NO_BOX, 371, 296)

        pobj = fl_add_box(FL_FLAT_BOX, 0, 0, 371, 296, "")
        fl_set_object_color(pobj, FL_SLATEBLUE, FL_COL1)

        fdui.pfontobj = fl_add_browser(FL_HOLD_BROWSER, 10, 145, 195, 135, "")
        fl_set_object_lalign(fdui.pfontobj, FL_ALIGN_BOTTOM | FL_ALIGN_INSIDE)
        fl_set_object_callback(fdui.pfontobj, self.style_cb, 0)

        fdui.psizeobj = fl_add_browser(FL_HOLD_BROWSER, 215, 145, 145, 135, "")
        fl_set_object_lalign(fdui.psizeobj, FL_ALIGN_BOTTOM | FL_ALIGN_INSIDE)
        fl_set_object_callback(fdui.psizeobj, self.size_cb, 0)

        fdui.ptextobj = fl_add_text(FL_NORMAL_TEXT, 10, 5, 351, 125, \
                               "The quick brown\nfox jumps over\n" \
                               "the lazy dog.")
        fl_set_object_boxtype(fdui.ptextobj, FL_FRAME_BOX)
        fl_set_object_lalign(fdui.ptextobj, FL_ALIGN_CENTER)

        pobj = fl_add_button(FL_HIDDEN_BUTTON, 0, 0, 370, 140, "Button")
        fl_set_button_shortcut(pobj, "^[qQ", 1)
        fl_set_object_callback(pobj, self.done_cb, 0)

        fl_end_form()

        return fdui



if __name__ == '__main__':
    Flfonts(len(sys.argv), sys.argv)

