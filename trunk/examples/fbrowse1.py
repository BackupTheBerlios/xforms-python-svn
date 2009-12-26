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



def load_file(ob, arg):
    if not xf.fl_load_browser(br, xf.fl_show_input("Filename to load", "")):
        xf.fl_add_browser_line(br, "NO SUCH FILE!")



def set_size(ob, arg):
    xf.fl_set_browser_fontsize(br, arg)



def main(lsysargv, sysargv):
    global br

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    form = xf.fl_bgn_form(xfc.FL_UP_BOX, 130, 100)

    br = xf.fl_add_browser(xfc.FL_NORMAL_BROWSER, 5, 5, 95, 90, "")

    but = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 105, 5, 20, 8, "Exit")
    but[0].u_ldata = xfc.EXITVAL

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 105, 75, 20, 8, "Load")
    xf.fl_set_object_callback(obj, load_file, 0)

    obj = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 105, 60, 20, 8, "Small")
    xf.fl_set_object_callback(obj, set_size, xfc.FL_SMALL_SIZE)
    xf.fl_call_object_callback(obj)
    xf.fl_set_button(obj, 1)

    obj = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 105, 50, 20, 8, "Normal")
    xf.fl_set_object_callback(obj, set_size, xfc.FL_NORMAL_SIZE)

    obj = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 105, 40, 20, 8, "Large")
    xf.fl_set_object_callback(obj, set_size, xfc.FL_LARGE_SIZE)

    xf.fl_end_form()

    xf.fl_scale_form(form, 4.0, 4.0)
    xf.fl_adjust_form_size(form)

    xf.fl_clear_browser(br)
    xf.fl_add_browser_line(br, "LOAD A FILE.")

    xf.fl_show_form(form,xfc.FL_PLACE_FREE, xfc.FL_FULLBORDER, "Browser")

    while True:
        obj = xf.fl_do_forms()
        if obj[0].u_ldata == but[0].u_ldata:
            break

    xf.fl_hide_form(form)
    xf.fl_finish()

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

