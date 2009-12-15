#!/usr/bin/env python

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
from xformslib import library as xf
from xformslib import xfdata as xfc



def create_form_0():
    global form, readyobj

    form = xf.fl_bgn_form(xfc.FL_NO_BOX, 400, 470)

    obj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 400, 470, "")
    xf.fl_set_object_color(obj, xfc.FL_SLATEBLUE, xfc.FL_COL1)

    obj = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 140, 40, 120, 120,
                         "This is\na multi-line\nlabelT")
    xf.fl_set_object_boxtype(obj, xfc.FL_BORDER_BOX)
    xf.fl_set_object_lalign(obj, xfc.FL_ALIGN_TOP)

    obj = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 140, 160, 120, 120,
                         "This is\na multi-line\nlabelC")
    xf.fl_set_object_boxtype(obj, xfc.FL_BORDER_BOX)
    xf.fl_set_object_color(obj, xfc.FL_PALEGREEN, xfc.FL_COL1)
    xf.fl_set_object_lsize(obj, xfc.FL_LARGE_SIZE)
    xf.fl_set_object_lalign(obj, xfc.FL_ALIGN_CENTER)

    readyobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 280, 400, \
                                100, 50, "I am sure\nthat I am\nReady")
    xf.fl_set_object_lsize(readyobj, xfc.FL_SMALL_SIZE)
    readyobj[0].u_ldata = xfc.EXITVAL

    obj = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 260, 160, 120, 120,
                         "This is\na multi-line\nlabelR")
    xf.fl_set_object_boxtype(obj, xfc.FL_BORDER_BOX)
    xf.fl_set_object_lalign(obj, xfc.FL_ALIGN_RIGHT)

    obj = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 140, 280, 120, 120,
                         "This is\na multi-line\nlabelB")
    xf.fl_set_object_boxtype(obj, xfc.FL_BORDER_BOX)
    xf.fl_set_object_lalign(obj, xfc.FL_ALIGN_BOTTOM)

    obj = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 20, 160, 120, 120,
                         "This is\na multi-line\nlabelL")
    xf.fl_set_object_boxtype(obj, xfc.FL_BORDER_BOX)
    #xf.fl_set_object_lalign(obj, xfc.FL_ALIGN_LEFT)

    xf.fl_end_form()



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    create_form_0()

    xf.fl_show_form(form, xfc.FL_PLACE_CENTER, xfc.FL_NOBORDER, \
                    "Labels")

    while True:
        obj = xf.fl_do_forms()
        if obj[0].u_ldata == readyobj[0].u_ldata:
            break

    xf.fl_hide_form(form)
    xf.fl_finish()

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

