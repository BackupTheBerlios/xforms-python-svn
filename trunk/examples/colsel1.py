#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  colsel1.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# show the use of setting object colors and call-back routines.
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



def change_color(pobj, color):
    xf.fl_set_object_color(ptopbox, color, color)



def makeform():
    global ptopbox, pform

    pform = xf.fl_bgn_form(xfc.FL_UP_BOX, 100, 100)

    for i in range(0, 8):
        for j in range(0, 8):
            strng = str(8 * j + i)
            pobj = xf.fl_add_button(xfc.FL_RADIO_BUTTON, \
                                    11 + 10 * i, 15 + 10 * j, 8, 6, strng)
            xf.fl_set_object_color(pobj, 8 * j + i, 8 * j + i)
            xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_BOTTOM)
            xf.fl_set_object_callback(pobj, change_color, 8 * j + i)

    ptopbox = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 30, 5, 40, 8, "The Color Map")
    xf.fl_set_object_lsize(ptopbox, xfc.FL_LARGE_SIZE)
    xf.fl_set_object_lstyle(ptopbox, xfc.FL_BOLD_STYLE)

    xf.fl_end_form()

    xf.fl_adjust_form_size(pform)



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    makeform()
    xf.fl_scale_form(pform, 4.0, 4.0)
    xf.fl_show_form(pform, xfc.FL_PLACE_FREE, xfc.FL_TRANSIENT, "colsel")

    while True:
        pret = xf.fl_do_forms()
        if pret.contents != ptopbox.contents:
            break

    xf.fl_hide_form(pform)
    xf.fl_finish()

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

