#!/usr/bin/env python

#  This file is part of xforms-python, and it is originally created.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows an implementation of Waclaw Sierpinski's fractal triangle.
#

import sys
import random
#sys.path.append("..")
import xformslib as xfl


def main(lsysargv, sysargv):

    msg = "Fractal processing in progress (it will take some time before " \
            "you can close the window) ..."
    print(msg)
    xfl.fl_initialize(lsysargv, sysargv, "Fractals", None, 0)

    pform = xfl.fl_bgn_form(xfl.FL_DOWN_BOX, 635, 655)

    pbut = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 0, 0, 50, 25, "Close")
    xfl.fl_set_object_callback(pbut, close_cb, 0)

    pfree = xfl.fl_add_free(xfl.FL_NORMAL_FREE, 5, 35, 600, 600, "myfree", \
            drawing_cb)

    xfl.fl_end_form()

    xfl.fl_show_form(pform, xfl.FL_PLACE_CENTER, xfl.FL_FULLBORDER, \
            "Sierpinski's Triangle")

    xfl.fl_set_object_focus(pform, pbut)

    while xfl.fl_do_forms():
        pass


def close_cb(pobj, data):
    xfl.fl_finish()
    sys.exit(0)


def drawing_cb(pobj, evt, mx, my, key, pxev):

    xfl.fl_reset_focus_object(pobj)
    x = 40
    y = 50
    for i in range(1, 20000):
        r = random.randint(0, 3) + 1
        if r == 1:
            x = (600 + x) / 2
            y = (600 + y) / 2
        elif r == 2:
            x = (300 + x) / 2
            y = (50 + y) / 2
        elif r == 3:
            x = x / 2
            y = (600 + y) / 2

        if i > 0:
            xfl.fl_point(int(x), int(y), xfl.FL_YELLOW)

    return 0


if __name__ == '__main__':
    print("********* sierpinskitriangle_new.py *********")
    main(len(sys.argv), sys.argv)

