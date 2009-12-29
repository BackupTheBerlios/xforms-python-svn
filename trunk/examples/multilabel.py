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
    global pform, preadyobj

    pform = xf.fl_bgn_form(xfc.FL_NO_BOX, 400, 470)

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 400, 470, "")
    xf.fl_set_object_color(pobj, xfc.FL_SLATEBLUE, xfc.FL_COL1)

    pobj = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 140, 40, 120, 120,
                          "This is\na multi-line\nlabelT")
    xf.fl_set_object_boxtype(pobj, xfc.FL_BORDER_BOX)
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_TOP)

    pobj = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 140, 160, 120, 120,
                          "This is\na multi-line\nlabelC")
    xf.fl_set_object_boxtype(pobj, xfc.FL_BORDER_BOX)
    xf.fl_set_object_color(pobj, xfc.FL_PALEGREEN, xfc.FL_COL1)
    xf.fl_set_object_lsize(pobj, xfc.FL_LARGE_SIZE)
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_CENTER)

    preadyobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 280, 400, \
                                 100, 50, "I am sure\nthat I am\nReady")
    xf.fl_set_object_lsize(preadyobj, xfc.FL_SMALL_SIZE)
    preadyobj.contents.u_ldata = xfc.EXITVAL

    pobj = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 260, 160, 120, 120,
                          "This is\na multi-line\nlabelR")
    xf.fl_set_object_boxtype(pobj, xfc.FL_BORDER_BOX)
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_RIGHT)

    pobj = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 140, 280, 120, 120,
                          "This is\na multi-line\nlabelB")
    xf.fl_set_object_boxtype(pobj, xfc.FL_BORDER_BOX)
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_BOTTOM)

    pobj = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 20, 160, 120, 120,
                          "This is\na multi-line\nlabelL")
    xf.fl_set_object_boxtype(pobj, xfc.FL_BORDER_BOX)
    #xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_LEFT)

    xf.fl_end_form()



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    create_form_0()

    xf.fl_show_form(pform, xfc.FL_PLACE_CENTER, xfc.FL_NOBORDER, \
                    "Labels")

    while True:
        pobj = xf.fl_do_forms()
        if pobj.contents.u_ldata == preadyobj.contents.u_ldata:
            break

    xf.fl_hide_form(pform)
    xf.fl_finish()

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

