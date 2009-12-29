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
from xformslib import library as xf
from xformslib import xfdata as xfc



def load_file(pobj, arg):
    fname = xf.fl_show_file_selector("File To Load", "", "*", "")
    if fname:
        if not xf.fl_load_browser(pbr, fname):
            xf.fl_add_browser_line(pbr,"NO SUCH FILE!")


def set_size(pobj, arg):
    xf.fl_set_browser_fontsize(pbr, arg)


def exit_program(pobj, data):
    xf.fl_finish()
    sys.exit(0)


def hide_show(pobj, data):
    print "visible", pbr.contents.visible
    if pbr.contents.visible:
        xf.fl_hide_object(pbr)
    else:
        xf.fl_show_object(pbr)


def create_form():
    global pbr

    x = 20
    dx = 80
    dy = 28

    pform = xf.fl_bgn_form(xfc.FL_NO_BOX, 590, 610)
    pobj1 = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 590, 610, "")

    pbr = xf.fl_add_browser(xfc.FL_NORMAL_BROWSER, 20, 20, 550, 530, "")
    xf.fl_set_object_boxtype(pbr, xfc.FL_EMBOSSED_BOX)

    pobj1 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, x, 565, dx-5, dy, "Load")
    xf.fl_set_object_callback(pobj1, load_file, 0)
    x += dx

    pobj2 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, x, 565, dx, dy, "Tiny")
    xf.fl_set_object_callback(pobj2, set_size, xfc.FL_TINY_SIZE)
    x += dx

    pobj3 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, x , 565, dx, dy, "Small")
    xf.fl_set_object_callback(pobj3, set_size, xfc.FL_SMALL_SIZE)
    xf.fl_set_button(pobj3, xfc.FL_SMALL_SIZE)           # == xfc.FL_BROWSER_FONTSIZE
    x += dx

    pobj4 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, x , 565, dx, dy, "Normal")
    xf.fl_set_object_callback(pobj4, set_size, xfc.FL_NORMAL_SIZE)
    xf.fl_set_button(pobj4, xfc.FL_NORMAL_SIZE)          # == xfc.FL_BROWSER_FONTSIZE
    x += dx

    pobj5 = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, x , 565, dx, dy, "Large")
    xf.fl_set_object_callback(pobj5, set_size, xfc.FL_LARGE_SIZE)
    x += dx

    pobj6 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, x, 565, dx, dy, "Hide/Show")
    xf.fl_set_object_callback(pobj6, hide_show, 0)
    x += dx

    pobj7 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, x, 565, dx, dy, "Exit")       #60->dx
    xf.fl_set_object_callback(pobj7, exit_program, 0)

    xf.fl_end_form()

    xf.fl_adjust_form_size(pform)

    return pform



def main(lsysarg, sysargv):

    global fdnew

    xf.fl_initialize(lsysarg, sysargv, "FormDemo", 0, 0)
    fdnew = create_form()

    xf.fl_clear_browser(pbr)
    xf.fl_add_browser_line(pbr, "LOAD A FILE.")
    xf.fl_set_browser_fontstyle(pbr, xfc.FL_FIXED_STYLE)

    xf.fl_show_form(fdnew, xfc.FL_PLACE_FREE, xfc.FL_FULLBORDER, \
                    "Browser")

    poret = xf.fl_do_forms()

    if poret.contents.label:
        prndata = oret.contents.label
    else:
        prndata = ""
    print "%p %d %s\n" % oret.contents, oret.contents.objclass, prndata

    xf.fl_hide_form(fdnew)
    xf.fl_free_form(fdnew)

    xf.fl_finish()
    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

