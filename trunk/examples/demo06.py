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
import xformslib as xfl



class FLDemo06(object):
    def __init__(self, lsysargv, sysargv):

        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.make_form1()
        xfl.fl_show_form(self.pform, xfl.FL_PLACE_CENTER, xfl.FL_NOBORDER, \
                "Demo06")

        while True:
            pobj = xfl.fl_do_forms()
            if xfl.fl_is_same_object(pobj, self.pbut):
                if xfl.fl_show_question("Do you really want to Quit?", 0):
                    xfl.fl_finish()
                    sys.exit(0)


    def make_form1(self):
        self.pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 500, 400)

        xfl.fl_bgn_group()
        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 150, 295, 300, 65, "Children  ")
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_LEFT)
        xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 175, 310, 50, 35, "1")
        xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 241, 310, 50, 35, "2")
        xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 308, 310, 50, 35, "3")
        xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 375, 310, 50, 35, "4")
        xfl.fl_end_group()

        xfl.fl_bgn_group()
        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 150, 230, 300, 65, "Married  ")
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_LEFT)
        xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 175, 245, 100, 35, "Yes")
        xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 325, 245, 100, 35, "No")
        xfl.fl_end_group()

        xfl.fl_bgn_group()
        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 150, 165, 300, 65, "Sex  ")
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_LEFT)
        xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 175, 180, 100, 35, "Male")
        xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, 325, 180, 100, 35, \
                "Female")
        xfl.fl_end_group()

        xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 150, 30, 300, 30, "Name  ")
        xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 150, 75, 300, 30, "Address  ")
        xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 150, 120, 300, 30, "City  ")

        self.pbut = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 25, 360, \
                75, 30, "OK")

        xfl.fl_end_form()



if __name__ == '__main__':
    print("********* demo06.py *********")
    appl = FLDemo06(len(sys.argv), sys.argv)
