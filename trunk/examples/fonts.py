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
from xformslib import library as xf
from xformslib import xfdata as xfc


class FD_fontsform(object):
    fontsform = None
    vdata = None
    cdata = None
    ldata = None
    fontobj = None
    sizeobj = None
    textobj = None


def done_cb(pobj, arg):
    xf.fl_finish()
    sys.exit(0)


def style_cb(pobj, arg):
    xf.fl_set_object_lstyle(ui.ptextobj, xf.fl_get_browser(pobj) - 1)


def size_cb(pobj, arg):
    sizes = [8, 10, 11, 12, 13, 14, 18, 24, 30]
    xf.fl_set_object_lsize(ui.ptextobj, sizes[xf.fl_get_browser(pobj) - 1 ])


def addit(txtstr):
    xf.fl_add_browser_line(ui.pfontobj, txtstr)




def main(lsysargv, sysargv):
    global ui

    xf.fl_set_border_width(-3)
    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    ui = create_form_fontsform()
    xf.fl_scale_form(ui.pfontsform, 1.1, 1.2)
    xf.fl_set_object_dblbuffer(ui.ptextobj, 1)
    xf.fl_set_object_bw(ui.ptextobj, 5)

    xf.fl_enumerate_fonts(addit, 1)
    xf.fl_select_browser_line(ui.pfontobj, 1)
    xf.fl_addto_browser(ui.psizeobj, "8  (tiny)")
    xf.fl_addto_browser(ui.psizeobj, "10 (small)")
    xf.fl_addto_browser(ui.psizeobj, "11 (scaled)")
    xf.fl_addto_browser(ui.psizeobj, "12 (normal)")
    xf.fl_addto_browser(ui.psizeobj, "13 (scaled)")
    xf.fl_addto_browser(ui.psizeobj, "14 (medium)")
    xf.fl_addto_browser(ui.psizeobj, "18 (large)")
    xf.fl_addto_browser(ui.psizeobj, "24 (Huge)")
    xf.fl_addto_browser(ui.psizeobj, "30 (scaled)")
    xf.fl_select_browser_line(ui.psizeobj, 2)
    xf.fl_set_object_lstyle(ui.ptextobj, xfc.FL_NORMAL_STYLE)
    xf.fl_call_object_callback(ui.pfontobj)
    xf.fl_call_object_callback(ui.psizeobj)
    xf.fl_show_form(ui.pfontsform, xfc.FL_PLACE_CENTER, xfc.FL_TRANSIENT, "Fonts")

    xf.fl_do_forms()

    return 0



def create_form_fontsform():

    fdui = FD_fontsform()

    fdui.pfontsform = xf.fl_bgn_form(xfc.FL_NO_BOX, 371, 296)

    pobj = xf.fl_add_box(xfc.FL_FLAT_BOX, 0, 0, 371, 296, "")
    xf.fl_set_object_color(pobj, xfc.FL_SLATEBLUE, xfc.FL_COL1)

    fdui.pfontobj = xf.fl_add_browser(xfc.FL_HOLD_BROWSER, 10, 145, 195, 135, "")
    xf.fl_set_object_lalign(fdui.pfontobj, xfc.FL_ALIGN_BOTTOM | xfc.FL_ALIGN_INSIDE)
    xf.fl_set_object_callback(fdui.pfontobj, style_cb, 0)

    fdui.psizeobj = xf.fl_add_browser(xfc.FL_HOLD_BROWSER, 215, 145, 145, 135, "")
    xf.fl_set_object_lalign(fdui.psizeobj, xfc.FL_ALIGN_BOTTOM | xfc.FL_ALIGN_INSIDE)
    xf.fl_set_object_callback(fdui.psizeobj, size_cb, 0)

    fdui.ptextobj = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 10, 5, 351, 125, \
                               "The quick brown\nfox jumps over\n" \
                               "the lazy dog.")
    xf.fl_set_object_boxtype(fdui.ptextobj, xfc.FL_FRAME_BOX)
    xf.fl_set_object_lalign(fdui.ptextobj, xfc.FL_ALIGN_CENTER)

    pobj = xf.fl_add_button(xfc.FL_HIDDEN_BUTTON, 0, 0, 370, 140, "Button")
    xf.fl_set_button_shortcut(pobj, "^[qQ", 1)
    xf.fl_set_object_callback(pobj, done_cb, 0)

    xf.fl_end_form()

    return fdui



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

