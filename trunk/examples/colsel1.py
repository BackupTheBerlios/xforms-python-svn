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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.xfdata import *



class Colsel1(object):
    def __init__(self, lsysargv, sysargv):

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        self.makeform()
        fl_scale_form(self.pform, 4.0, 4.0)
        fl_show_form(self.pform, FL_PLACE_FREE, FL_TRANSIENT, "colsel")

        while True:
            pret = fl_do_forms()
            if fl_is_same_object(pret, self.ptopbox):
                break

        fl_hide_form(self.pform)
        fl_finish()


    def change_color(self, pobj, color):
        fl_set_object_color(self.ptopbox, color, color)


    def makeform(self):
        self.pform = fl_bgn_form(FL_UP_BOX, 100, 100)

        for i in range(0, 8):
            for j in range(0, 8):
                strng = str(8 * j + i)
                pobj = fl_add_button(FL_RADIO_BUTTON, \
                                    11 + 10 * i, 15 + 10 * j, 8, 6, strng)
                fl_set_object_color(pobj, 8 * j + i, 8 * j + i)
                fl_set_object_lalign(pobj, FL_ALIGN_BOTTOM)
                fl_set_object_callback(pobj, self.change_color, 8 * j + i)

        self.ptopbox = fl_add_button(FL_NORMAL_BUTTON, 30, 5, 40, 8, "The Color Map")
        fl_set_object_lsize(self.ptopbox, FL_LARGE_SIZE)
        fl_set_object_lstyle(self.ptopbox, FL_BOLD_STYLE)

        fl_end_form()

        fl_adjust_form_size(self.pform)





if __name__ == '__main__':
    appl = Colsel1(len(sys.argv), sys.argv)

