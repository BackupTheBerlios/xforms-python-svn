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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flmisc import *
from xformslib.flbutton import *
from xformslib.xfdata import *




class Flmultilabel(object):

    def __init__(self, lsysargv, sysargv):

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.create_form_0()

        fl_show_form(self.pform, FL_PLACE_CENTER, FL_NOBORDER, \
                     "Labels")

        while True:
            pobj = fl_do_forms()
            if fl_is_same_object(pobj, self.preadyobj):
                break

        fl_hide_form(self.pform)
        fl_finish()


    def create_form_0(self):

        self.pform = fl_bgn_form(FL_NO_BOX, 400, 470)

        pobj = fl_add_box(FL_UP_BOX, 0, 0, 400, 470, "")
        fl_set_object_color(pobj, FL_SLATEBLUE, FL_COL1)

        pobj = fl_add_text(FL_NORMAL_TEXT, 140, 40, 120, 120,
                           "This is\na multi-line\nlabelT")
        fl_set_object_boxtype(pobj, FL_BORDER_BOX)
        fl_set_object_lalign(pobj, FL_ALIGN_TOP)

        pobj = fl_add_text(FL_NORMAL_TEXT, 140, 160, 120, 120,
                          "This is\na multi-line\nlabelC")
        fl_set_object_boxtype(pobj, FL_BORDER_BOX)
        fl_set_object_color(pobj, FL_PALEGREEN, FL_COL1)
        fl_set_object_lsize(pobj, FL_LARGE_SIZE)
        fl_set_object_lalign(pobj, FL_ALIGN_CENTER)

        self.preadyobj = fl_add_button(FL_NORMAL_BUTTON, 280, 400, \
                                       100, 50, "I am sure\nthat I am\nReady")
        fl_set_object_lsize(self.preadyobj, FL_SMALL_SIZE)

        pobj = fl_add_text(FL_NORMAL_TEXT, 260, 160, 120, 120,
                           "This is\na multi-line\nlabelR")
        fl_set_object_boxtype(pobj, FL_BORDER_BOX)
        fl_set_object_lalign(pobj, FL_ALIGN_RIGHT)

        pobj = fl_add_text(FL_NORMAL_TEXT, 140, 280, 120, 120,
                          "This is\na multi-line\nlabelB")
        fl_set_object_boxtype(pobj, FL_BORDER_BOX)
        fl_set_object_lalign(pobj, FL_ALIGN_BOTTOM)

        pobj = fl_add_text(FL_NORMAL_TEXT, 20, 160, 120, 120,
                          "This is\na multi-line\nlabelL")
        fl_set_object_boxtype(pobj, FL_BORDER_BOX)
        #fl_set_object_lalign(pobj, FL_ALIGN_LEFT)

        fl_end_form()





if __name__ == '__main__':
    Flmultilabel(len(sys.argv), sys.argv)

