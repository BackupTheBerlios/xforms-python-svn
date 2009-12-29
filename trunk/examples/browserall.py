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



pbr = [0, 0, 0, 0]
bnames = ["NORMAL_BROWSER", "SELECT_BROWSER", "HOLD_BROWSER", \
          "MULTI_BROWSER"]


def create_form():
    global pform, pbr, preadout

    pform = xf.fl_bgn_form(xfc.FL_UP_BOX, 700, 570)

    preadout = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 50, 30, 600, 50, "")
    xf.fl_set_object_lsize(preadout, xfc.FL_NORMAL_SIZE)
    xf.fl_set_object_lalign(preadout, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_lstyle(preadout, xfc.FL_BOLD_STYLE)
    xf.fl_set_object_boxtype(preadout, xfc.FL_UP_BOX)
    xf.fl_set_object_color(preadout, xfc.FL_MAGENTA, xfc.FL_MAGENTA)

    pbr[0] = xf.fl_add_browser(xfc.FL_NORMAL_BROWSER, 20, 120, 150, 290,
                               bnames[0])
    xf.fl_set_object_callback(pbr[0], br_callback, 0)

    pbr[1] = xf.fl_add_browser(xfc.FL_SELECT_BROWSER, 190, 120, 150, 290,
                               bnames[1])
    xf.fl_set_object_callback(pbr[1], br_callback, 1)

    pbr[2] = xf.fl_add_browser(xfc.FL_HOLD_BROWSER, 360, 120, 150, 290,
                               bnames[2])
    xf.fl_set_object_color(pbr[2], xfc.FL_WHITE, xfc.FL_GREEN)
    xf.fl_set_object_callback(pbr[2], br_callback, 2)

    pbr[3] = xf.fl_add_browser(xfc.FL_MULTI_BROWSER, 530, 120, 150, 290,
                               bnames[3])
    xf.fl_set_object_color(pbr[3],xfc.FL_WHITE, xfc.FL_CYAN)
    xf.fl_set_object_callback(pbr[3], br_callback, 3)

    pexitobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 560, 510, 120, 30, "Exit")

    pobj1 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 560, 460, 120, 30, "Deselect")
    xf.fl_set_object_callback(pobj1, deselect, 0)

    xf.fl_bgn_group()

    pobj2 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 20, 500, 100, 30, "Tiny")
    xf.fl_set_object_lsize(pobj2, xfc.FL_TINY_SIZE)
    xf.fl_set_object_callback(pobj2, set_size, xf.fl_get_object_lsize(pobj2))

    pobj3 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 130, 500, 100, 30, "Small")
    xf.fl_set_object_lsize(pobj3, xfc.FL_SMALL_SIZE)
    xf.fl_set_object_callback(pobj3, set_size, xf.fl_get_object_lsize(pobj3))
    xf.fl_set_button(pobj3, 1)

    pobj4 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 240, 500, 100, 30, "Normal")
    xf.fl_set_object_lsize(pobj4, xfc.FL_NORMAL_SIZE)
    xf.fl_set_object_callback(pobj4, set_size, xf.fl_get_object_lsize(pobj4))

    pobj5 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 350, 500, 100, 30, "Large")
    xf.fl_set_object_lsize(pobj5, xfc.FL_LARGE_SIZE)
    xf.fl_set_object_callback(pobj5, set_size, xf.fl_get_object_lsize(pobj5))

    pobj6 = xf.fl_add_button(xfc.FL_BUTTON, 470, 510, 45,30, "Link")
    xf.fl_set_object_callback(pobj6, link_browsers, 0)

    xf.fl_end_group()

    xf.fl_bgn_group()

    pobj7 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 20, 450, 100, 30, \
                                  "Normal")
    xf.fl_set_object_callback(pobj7, set_style, xfc.FL_NORMAL_STYLE)
    xf.fl_set_button(pobj7, 1)

    pobj8 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 120, 450, 100, 30, \
                                  "Bold")
    xf.fl_set_object_callback(pobj8, set_style, xfc.FL_BOLD_STYLE)

    pobj9 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 220, 450, 100, 30, \
                                  "Italic")
    xf.fl_set_object_callback(pobj9, set_style, xfc.FL_ITALIC_STYLE)

    pobj10 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 320, 450, 100, 30,
                                   "BoldItalic")
    xf.fl_set_object_callback(pobj10, set_style, xfc.FL_BOLDITALIC_STYLE)

    pobj11 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 420, 450, 100, 30, \
                                   "Fixed")
    xf.fl_set_object_callback(pobj11, set_style, xfc.FL_FIXED_STYLE)

    xf.fl_end_group()

    xf.fl_end_form()



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    create_form()
    fill_browsers()
    xf.fl_show_form(pform,xfc.FL_PLACE_CENTER | xfc.FL_FREE_SIZE, \
                    xfc.FL_TRANSIENT, "All Browsers")
    xf.fl_do_forms()
    xf.fl_hide_form(pform)
    return 0



def deselect(pobj, arg):
    for i in range(0, 4):
        xf.fl_deselect_browser(pbr[i])



def set_size(pobj, arg):
    for i in range(0, 4):
        xf.fl_set_browser_fontsize(pbr[i], arg)



def set_style(pobj, arg):
    for i in range(0, 4):
        xf.fl_set_browser_fontstyle(pbr[i], arg)



def br_callback(pobj, arg):

    mb = ["left", "middle", "right", "scroll-up", "scroll-down"]

    i = xf.fl_mouse_button()
    if i >= xfc.FL_LEFT_MOUSE and i <= xfc.FL_SCROLLDOWN_MOUSE:
        buf = "In %s [%s]: " % (bnames[arg], mb[i - xfc.FL_LEFT_MOUSE])
    else:
        buf = "In %s: " % bnames[arg]

    i = xf.fl_get_browser(pobj)
    if i:
        if i > 0:
            ii = i
            txtsel = "was selected."
        else:
            ii = -i
            txtsel = "was deselected."
        buf += xf.fl_get_browser_line(pobj, ii)
        buf += txtsel

    xf.fl_set_object_label(preadout, buf)



def vcallback(pobj, topline, data):

    yoffset = xf.fl_get_browser_yoffset(pbr[0])
    for i in range(0, 4):
        xf.fl_set_browser_yoffset(pbr[i], yoffset)


def donothing(pobj, topline, data):
    pass        # placeholder for disabled vcallback



def link_browsers(pobj, data):

    sync = xf.fl_get_button(pobj)
    if sync:
        linktxt = "Unlink"
    else:
        linktxt = "Link"
    xf.fl_set_object_label(pobj, linktxt)

    if sync:
        yoffset = xf.fl_get_browser_yoffset(pbr[0])
        for i in range(1, 4):
            xf.fl_set_browser_vscrollbar(pbr[i], xfc.FL_OFF)
            xf.fl_set_browser_yoffset(pbr[i], yoffset)
        xf.fl_set_browser_vscroll_callback(pbr[0], vcallback, 0)
    else:
        for i in range(1, 4):
            xf.fl_set_browser_vscrollbar(pbr[i], xfc.FL_ON)
        xf.fl_set_browser_vscroll_callback(pbr[0], donothing, 0)




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

            xf.fl_add_browser_line(pbr[i], buf)




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

