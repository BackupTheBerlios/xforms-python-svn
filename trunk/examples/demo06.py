#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  demo06.c XForms demo, with some adaptations.
#
#  demo06.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# A demo of the forms library using light buttons for
# radio buttons and input fields.
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flinput import *
from xformslib.flmisc import *
from xformslib.flgoodies import *
from xformslib.xfdata import *




class FLDemo06(object):
    def __init__(self, lsysargv, sysargv):

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.make_form1()
        fl_show_form(self.pform, FL_PLACE_CENTER, FL_NOBORDER, "Demo06")

        while True:
            pobj = fl_do_forms()
            if fl_is_same_object(pobj, self.pbut):
                if fl_show_question("Do you really want to Quit?", 0):
                    fl_finish()
                    sys.exit(0)


    def make_form1(self):
        self.pform = fl_bgn_form(FL_UP_BOX, 500, 400)

        fl_bgn_group()
        pobj = fl_add_box(FL_UP_BOX, 150, 295, 300, 65, "Children  ")
        fl_set_object_lalign(pobj, FL_ALIGN_LEFT)
        fl_add_lightbutton(FL_RADIO_BUTTON, 175, 310, 50, 35, "1")
        fl_add_lightbutton(FL_RADIO_BUTTON, 241, 310, 50, 35, "2")
        fl_add_lightbutton(FL_RADIO_BUTTON, 308, 310, 50, 35, "3")
        fl_add_lightbutton(FL_RADIO_BUTTON, 375, 310, 50, 35, "4")
        fl_end_group()

        fl_bgn_group()
        pobj = fl_add_box(FL_UP_BOX, 150, 230, 300, 65, "Married  ")
        fl_set_object_lalign(pobj, FL_ALIGN_LEFT)
        fl_add_lightbutton(FL_RADIO_BUTTON, 175, 245, 100, 35, "Yes")
        fl_add_lightbutton(FL_RADIO_BUTTON, 325, 245, 100, 35, "No")
        fl_end_group()

        fl_bgn_group()
        pobj = fl_add_box(FL_UP_BOX, 150, 165, 300, 65, "Sex  ")
        fl_set_object_lalign(pobj, FL_ALIGN_LEFT)
        fl_add_lightbutton(FL_RADIO_BUTTON, 175, 180, 100, 35, "Male")
        fl_add_lightbutton(FL_RADIO_BUTTON, 325, 180, 100, 35, "Female")
        fl_end_group()

        fl_add_input(FL_NORMAL_INPUT, 150, 30, 300, 30, "Name  ")
        fl_add_input(FL_NORMAL_INPUT, 150, 75, 300, 30, "Address  ")
        fl_add_input(FL_NORMAL_INPUT, 150, 120, 300, 30, "City  ")

        self.pbut = fl_add_button(FL_NORMAL_BUTTON, 25, 360, 75, 30, "OK")

        fl_end_form()




if __name__ == '__main__':
    FLDemo06(len(sys.argv), sys.argv)

