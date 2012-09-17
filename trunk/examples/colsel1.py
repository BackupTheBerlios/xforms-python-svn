#!/usr/bin/env python3

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
import xformslib as xfl


class Colsel1(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.makeform()
        xfl.fl_scale_form(self.pform, 4.0, 4.0)
        xfl.fl_show_form(self.pform, xfl.FL_PLACE_FREE, \
                xfl.FL_TRANSIENT, "colsel")
        while True:
            pret = xfl.fl_do_forms()
            if xfl.fl_is_same_object(pret, self.ptopbox):
                break
        xfl.fl_hide_form(self.pform)
        xfl.fl_finish()
        sys.exit(0)


    def change_color(self, pobj, color):
        xfl.fl_set_object_color(self.ptopbox, color, color)


    def makeform(self):
        self.pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 100, 100)
        for i in range(0, 8):
            for j in range(0, 8):
                strng = str(8 * j + i)
                pobj = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, \
                        11 + 10 * i, 15 + 10 * j, 8, 6, strng)
                xfl.fl_set_object_color(pobj, 8 * j + i, 8 * j + i)
                xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_BOTTOM)
                xfl.fl_set_object_callback(pobj, self.change_color, \
                        8 * j + i)
        self.ptopbox = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 30, 5, \
                40, 8, "The Color Map")
        xfl.fl_set_object_lsize(self.ptopbox, xfl.FL_LARGE_SIZE)
        xfl.fl_set_object_lstyle(self.ptopbox, xfl.FL_BOLD_STYLE)
        xfl.fl_end_form()
        xfl.fl_adjust_form_size(self.pform)


if __name__ == '__main__':
    print("********* colsel1.py *********")
    Colsel1(len(sys.argv), sys.argv)
