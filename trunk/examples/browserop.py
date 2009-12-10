#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  browserop.c XForms demo, with some adaptations.
#
#  browserop.c was written by M. Overmars and T.C. Zhao (1997)
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the basic browsers browsers
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc




def addit(ob, data):
    # append and show the last line. Don't use this if you just want
    # to add some lines. use xf.fl_add_browser_line
    xf.fl_addto_browser(browserobj, xf.fl_get_input(inputobj))


def insertit(ob, arg):
    xf.fl_insert_browser_line(browserobj, xf.fl_get_browser(browserobj), \
                              xf.fl_get_input(inputobj))


def replaceit(obj, arg):

    n = xf.fl_get_browser(browserobj)
    if n:
        xf.fl_replace_browser_line(browserobj, n, xf.fl_get_input(inputobj))


def deleteit(obj, arg):

    n = xf.fl_get_browser(browserobj)
    if n:
        xf.fl_delete_browser_line(browserobj, n)


def clearit(obj, arg):
    xf.fl_clear_browser(browserobj)


def exitcb(obj, arg):
    xf.fl_finish()
    sys.exit(0)


def create_form():
    global form, browserobj, inputobj, exitobj

    form = xf.fl_bgn_form(xfc.FL_UP_BOX, 390, 420)

    browserobj = xf.fl_add_browser(xfc.FL_HOLD_BROWSER, 20, 20, 210, 330, "")
    xf.fl_set_object_dblbuffer(browserobj, 1)

    inputobj = xf.fl_add_input(xfc.FL_NORMAL_INPUT, 20, 370, 210, 30, "")

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 20, 120, 30, "Add")
    xf.fl_set_object_callback(obj, addit, 0)

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 60, 120, 30, "Insert")
    xf.fl_set_object_callback(obj, insertit, 0)

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 100, 120, 30, "Replace")
    xf.fl_set_object_callback(obj, replaceit, 0)

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 160, 120, 30, "Delete")
    xf.fl_set_object_callback(obj, deleteit, 0)

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 200, 120, 30, "Clear")
    xf.fl_set_object_callback(obj, clearit, 0)

    exitobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 370, 120, 30, "Exit")
    xf.fl_set_object_callback(exitobj, exitcb, 0)

    xf.fl_end_form()



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    create_form()
    xf.fl_show_form(form, xfc.FL_PLACE_CENTER, xfc.FL_TRANSIENT, "Browser Op")

    while xf.fl_do_forms():
        pass

    xf.fl_hide_form(form)
    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

