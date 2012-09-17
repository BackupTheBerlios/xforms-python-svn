#!/usr/bin/env python3

#  This file is part of xforms-python, and it has been ported from
#  multilabel.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Multiline labels.
#

import sys
#sys.path.append("..")
import xformslib as xfl


class Flmultilabel(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.create_form_0()
        xfl.fl_show_form(self.pform, xfl.FL_PLACE_CENTER, xfl.FL_NOBORDER, \
                "Labels")
        while True:
            pobj = xfl.fl_do_forms()
            if xfl.fl_is_same_object(pobj, self.preadyobj):
                break
        xfl.fl_hide_form(self.pform)
        xfl.fl_finish()
        sys.exit(0)


    def create_form_0(self):
        self.pform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 400, 470)
        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 400, 470, "")
        xfl.fl_set_object_color(pobj, xfl.FL_SLATEBLUE, xfl.FL_COL1)
        pobj = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 140, 40, 120, 120,
                "This is\na multi-line\nlabelT")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_BORDER_BOX)
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_TOP)
        pobj = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 140, 160, 120, 120,
                "This is\na multi-line\nlabelC")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_BORDER_BOX)
        xfl.fl_set_object_color(pobj, xfl.FL_PALEGREEN, xfl.FL_COL1)
        xfl.fl_set_object_lsize(pobj, xfl.FL_LARGE_SIZE)
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_CENTER)
        self.preadyobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 280, 400, \
                100, 50, "I am sure\nthat I am\nReady")
        xfl.fl_set_object_lsize(self.preadyobj, xfl.FL_SMALL_SIZE)
        pobj = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 260, 160, 120, 120,
                "This is\na multi-line\nlabelR")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_BORDER_BOX)
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_RIGHT)
        pobj = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 140, 280, 120, 120,
                "This is\na multi-line\nlabelB")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_BORDER_BOX)
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_BOTTOM)
        pobj = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 20, 160, 120, 120,
                "This is\na multi-line\nlabelL")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_BORDER_BOX)
        xfl.fl_end_form()


if __name__ == '__main__':
    print("********* multilabel.py *********")
    Flmultilabel(len(sys.argv), sys.argv)
