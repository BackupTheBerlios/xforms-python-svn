#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  objinactive.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Demo showing activating and deactivating objects
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



def exit_cb(ob, data):
    xf.fl_finish()
    sys.exit( 0)


def setit(obj, val):

    if val:
        xf.fl_set_object_lcol(obj, xfc.FL_BLACK)
        xf.fl_activate_object(obj)
    else:
        xf.fl_set_object_lcol(obj, xfc.FL_INACTIVE)
        xf.fl_deactivate_object(obj)


def doit(b1, b2, b3, b4):

    setit(button1, b1)
    setit(button2, b2)
    setit(button3, b3)
    setit(button4, b4)



def set_active(ob, arg):

    if arg == 0:
        doit(1, 1, 1, 1)
    elif arg == 1:
        doit(0, 0, 0, 0)
    elif arg == 2:
        doit(0, 1, 0, 1)
    elif arg == 3:
        doit(1, 0, 1, 0)



def create_form():
    global firstbut, form, button1, button2, button3, button4

    form = xf.fl_bgn_form(xfc.FL_NO_BOX, 420, 230)

    obj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 420, 230, "")
    xf.fl_set_object_color(obj, xfc.FL_SLATEBLUE, xfc.FL_COL1)

    button1 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 20, 170, 150, 40,
                                     "Button 1")
    xf.fl_set_object_lsize(button1 ,xfc.FL_LARGE_SIZE)
    xf.fl_set_button_shortcut(button1, "1", 1)

    button2 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 20, 120, 150, 40,
                               "Button 2")
    xf.fl_set_object_lsize(button2, xfc.FL_LARGE_SIZE)
    xf.fl_set_button_shortcut(button2, "2", 1)

    button3 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 20, 70, 150, 40,
                               "Button 3")
    xf.fl_set_object_lsize(button3, xfc.FL_LARGE_SIZE)
    xf.fl_set_button_shortcut(button3, "3", 1)

    button4 = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 20, 20, 150, 40,
                               "Button 4")
    xf.fl_set_button_shortcut(button4, "4", 1)
    xf.fl_set_object_lsize(button4,xfc.FL_LARGE_SIZE)

    group = xf.fl_bgn_group()

    firstbut = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 260, 180, 140, 30,
                                     "All active")
    xf.fl_set_object_callback(firstbut, set_active, 0)

    obj = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 260, 150, 140, 30,
                                "Non active")
    xf.fl_set_object_callback(obj, set_active, 1)

    obj = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 260, 120, 140 ,30,
                                "Even active")
    xf.fl_set_object_callback(obj, set_active, 2)

    obj = xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 260, 90, 140, 30, \
                                "Odd active")
    xf.fl_set_object_callback(obj, set_active, 3)

    xf.fl_end_group()

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 270, 20, 130, 30, "Quit")
    xf.fl_set_object_callback(obj, exit_cb, 0)

    xf.fl_end_form()




def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    create_form()

    xf.fl_set_button(firstbut, 1)

    xf.fl_show_form(form, xfc.FL_PLACE_CENTER, xfc.FL_NOBORDER, None)

    while xf.fl_do_forms():
        pass            # empty

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

