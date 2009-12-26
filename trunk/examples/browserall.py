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
from xformslib import library as xf
from xformslib import xfdata as xfc



br = [0, 0, 0, 0]
bnames = ["NORMAL_BROWSER", "SELECT_BROWSER", "HOLD_BROWSER", \
          "MULTI_BROWSER"]


def create_form():
    global form, br, readout

    form = xf.fl_bgn_form(xfc.FL_UP_BOX, 700, 570)

    readout = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 50, 30, 600, 50, "")
    xf.fl_set_object_lsize(readout, xfc.FL_NORMAL_SIZE)
    xf.fl_set_object_lalign(readout, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_lstyle(readout, xfc.FL_BOLD_STYLE)
    xf.fl_set_object_boxtype(readout, xfc.FL_UP_BOX)
    xf.fl_set_object_color(readout, xfc.FL_MAGENTA, xfc.FL_MAGENTA)

    br[0] = xf.fl_add_browser(xfc.FL_NORMAL_BROWSER, 20, 120, 150, 290,
                              bnames[0])
    xf.fl_set_object_callback(br[0], br_callback, 0)

    br[1] = xf.fl_add_browser(xfc.FL_SELECT_BROWSER, 190, 120, 150, 290,
                              bnames[1])
    xf.fl_set_object_callback(br[1], br_callback, 1)

    br[2] = xf.fl_add_browser(xfc.FL_HOLD_BROWSER, 360, 120, 150, 290,
                              bnames[2])
    xf.fl_set_object_color(br[2], xfc.FL_WHITE, xfc.FL_GREEN)
    xf.fl_set_object_callback(br[2], br_callback, 2)

    br[3] = xf.fl_add_browser(xfc.FL_MULTI_BROWSER, 530, 120, 150, 290,
                              bnames[3])
    xf.fl_set_object_color(br[3],xfc.FL_WHITE, xfc.FL_CYAN)
    xf.fl_set_object_callback(br[3], br_callback, 3)

    exitobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 560, 510, 120, 30, "Exit")

    obj1 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 560, 460, 120, 30, "Deselect")
    xf.fl_set_object_callback(obj1, deselect, 0)

    xf.fl_bgn_group()

    obj2 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 20, 500, 100, 30, "Tiny")
    xf.fl_set_object_lsize(obj2, xfc.FL_TINY_SIZE)
    xf.fl_set_object_callback(obj2, set_size, xfc.FL_TINY_SIZE)

    obj3 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 130, 500, 100, 30, "Small")
    xf.fl_set_object_lsize(obj3, xfc.FL_SMALL_SIZE)
    xf.fl_set_object_callback(obj3, set_size, xfc.FL_SMALL_SIZE)
    xf.fl_set_button(obj3, 1)

    obj4 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 240, 500, 100, 30, "Normal")
    xf.fl_set_object_lsize(obj4, xfc.FL_NORMAL_SIZE)
    xf.fl_set_object_callback(obj4, set_size, xfc.FL_NORMAL_SIZE)

    obj5 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 350, 500, 100, 30, "Large")
    xf.fl_set_object_lsize(obj5, xfc.FL_LARGE_SIZE)
    xf.fl_set_object_callback(obj5, set_size, xfc.FL_LARGE_SIZE)

    obj6 = xf.fl_add_button(xfc.FL_BUTTON, 470, 510, 45,30, "Link")
    xf.fl_set_object_callback(obj6, link_browsers, 0)

    xf.fl_end_group()

    xf.fl_bgn_group()

    obj7 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 20, 450, 100, 30, \
                                 "Normal")
    xf.fl_set_object_callback(obj7, set_style, xfc.FL_NORMAL_STYLE)
    xf.fl_set_button(obj7, 1)

    obj8 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 120, 450, 100, 30, \
                                 "Bold")
    xf.fl_set_object_callback(obj8, set_style, xfc.FL_BOLD_STYLE)

    obj9 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 220, 450, 100, 30, \
                                "Italic")
    xf.fl_set_object_callback(obj9, set_style, xfc.FL_ITALIC_STYLE)

    obj10 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 320, 450, 100, 30,
                                "BoldItalic")
    xf.fl_set_object_callback(obj10, set_style, xfc.FL_BOLDITALIC_STYLE)

    obj11 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 420, 450, 100, 30, \
                                "Fixed")
    xf.fl_set_object_callback(obj11, set_style, xfc.FL_FIXED_STYLE)

    xf.fl_end_group()

    xf.fl_end_form()



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    create_form()
    fill_browsers()
    xf.fl_show_form(form,xfc.FL_PLACE_CENTER | xfc.FL_FREE_SIZE, \
                    xfc.FL_TRANSIENT, "All Browsers")
    xf.fl_do_forms()
    xf.fl_hide_form(form)
    return 0



def deselect(obj, arg):
    for i in range(0, 4):
        xf.fl_deselect_browser(br[i])



def set_size(obj, arg):
    for i in range(0, 4):
        xf.fl_set_browser_fontsize(br[i], arg)



def set_style(obj, arg):
    for i in range(0, 4):
        xf.fl_set_browser_fontstyle(br[i], arg)



def br_callback(ob, arg):

    mb = ["left", "middle", "right", "scroll-up", "scroll-down"]

    i = xf.fl_mouse_button()
    if i >= xfc.FL_LEFT_MOUSE and i <= xfc.FL_SCROLLDOWN_MOUSE:
        buf = "In %s [%s]: " % (bnames[arg], mb[i - xfc.FL_LEFT_MOUSE])
    else:
        buf = "In %s: " % bnames[arg]

    i = xf.fl_get_browser(ob)
    if i:
        if i > 0:
            ii = i
            txtsel = "was selected."
        else:
            ii = -i
            txtsel = "was deselected."
        buf += xf.fl_get_browser_line(ob, ii)
        buf += txtsel

    xf.fl_set_object_label(readout, buf)



def vcallback(ob, topline, data):

    yoffset = xf.fl_get_browser_yoffset(br[0])
    for i in range(0, 4):
        xf.fl_set_browser_yoffset(br[i], yoffset)


def donothing(ob, topline, data):
    pass        # placeholder for disabled vcallback



def link_browsers(ob, data):

    sync = xf.fl_get_button(ob)
    if sync:
        linktxt = "Unlink"
    else:
        linktxt = "Link"
    xf.fl_set_object_label(ob, linktxt)

    if sync:
        yoffset = xf.fl_get_browser_yoffset(br[0])
        for i in range(1, 4):
            xf.fl_set_browser_vscrollbar(br[i], xfc.FL_OFF)
            xf.fl_set_browser_yoffset(br[i], yoffset)
        xf.fl_set_browser_vscroll_callback(br[0], vcallback, 0)
    else:
        for i in range(1, 4):
            xf.fl_set_browser_vscrollbar(br[i], xfc.FL_ON)
        xf.fl_set_browser_vscroll_callback(br[0], donothing, 0)




def fill_browsers():

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

            xf.fl_add_browser_line(br[i], buf)




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

