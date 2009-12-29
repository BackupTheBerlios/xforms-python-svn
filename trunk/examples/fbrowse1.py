#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  fbrowse1.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a browser and fl_call_object_callback.
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



def load_file(pobj, arg):
    if not xf.fl_load_browser(pbr, xf.fl_show_input("Filename to load", "")):
        xf.fl_add_browser_line(pbr, "NO SUCH FILE!")



def set_size(pobj, arg):
    xf.fl_set_browser_fontsize(pbr, arg)



def main(lsysargv, sysargv):
    global pbr

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    pform = xf.fl_bgn_form(xfc.FL_UP_BOX, 130, 100)

    pbr = xf.fl_add_browser(xfc.FL_NORMAL_BROWSER, 5, 5, 95, 90, "")

    pbut = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 105, 5, 20, 8, "Exit")
    pbut.contents.u_ldata = xfc.EXITVAL

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 105, 75, 20, 8, "Load")
    xf.fl_set_object_callback(pobj, load_file, 0)

    pobj = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 105, 60, 20, 8, "Small")
    xf.fl_set_object_callback(pobj, set_size, xfc.FL_SMALL_SIZE)
    xf.fl_call_object_callback(pobj)
    xf.fl_set_button(pobj, 1)

    pobj = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 105, 50, 20, 8, "Normal")
    xf.fl_set_object_callback(pobj, set_size, xfc.FL_NORMAL_SIZE)

    pobj = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 105, 40, 20, 8, "Large")
    xf.fl_set_object_callback(pobj, set_size, xfc.FL_LARGE_SIZE)

    xf.fl_end_form()

    xf.fl_scale_form(pform, 4.0, 4.0)
    xf.fl_adjust_form_size(pform)

    xf.fl_clear_browser(pbr)
    xf.fl_add_browser_line(pbr, "LOAD A FILE.")

    xf.fl_show_form(pform, xfc.FL_PLACE_FREE, xfc.FL_FULLBORDER, "Browser")

    while True:
        pobj = xf.fl_do_forms()
        if pobj.contents.u_ldata == pbut.contents.u_ldata:
            break

    xf.fl_hide_form(pform)
    xf.fl_finish()

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

