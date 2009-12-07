#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  pushbutton.c XForms demo, with some adaptation.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# A demo that shows the use of push buttons.
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc


abox = [0, 0, 0, 0, 0, 0, 0, 0]


def push_cb(ob, n):
    if xf.fl_get_button(ob):
        xf.fl_show_object(abox[n])
    else:
        xf.fl_hide_object(abox[n])


def makeform():
    global form

    form = xf.fl_bgn_form( xfc.FL_UP_BOX, 400, 400)

    for i in range(0, 8):
        obj = xf.fl_add_button(xfc.FL_PUSH_BUTTON, 40, 310 - 40 * i, \
                               80, 30, "")
        xf.fl_set_object_color(obj, xfc.FL_BLACK + i + 1, \
                               xfc.FL_BLACK + i + 1)
        xf.fl_set_object_callback(obj, push_cb, i)

        abox[i] = xf.fl_add_box(xfc.FL_DOWN_BOX, 150 + 30 * i, 40, \
                                25, 320, "")
        xf.fl_set_object_color(abox[i], xfc.FL_BLACK + i + 1, \
                               xfc.FL_BLACK + i + 1)
        xf.fl_hide_object(abox[i])

    xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 40, 350, 80, 30, "Exit")
    xf.fl_end_form()



def main(lsysarg, sysarg):

    xf.fl_initialize(lsysarg, sysarg, "FormDemo", 0, 0)
    makeform()

    xf.fl_show_form(form, xfc.FL_PLACE_CENTER, xfc.FL_NOBORDER, \
                    "Push Buttons")

    # xf.fl_do_forms will return only when Exit is pressed
    xf.fl_do_forms()
    xf.fl_finish()

    return 0


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

