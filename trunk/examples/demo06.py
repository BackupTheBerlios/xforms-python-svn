#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  demo06.c XForms demo, with some adaptations.
#
#  demo06.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# A demo of the forms library using light buttons for
#   radio buttons and input fields.
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



def make_form1():
    global pform, pbut

    pform = xf.fl_bgn_form(xfc.FL_UP_BOX, 500, 400)

    xf.fl_bgn_group()

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 150, 295, 300, 65, "Children  ")
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_LEFT)
    xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 175, 310, 50, 35, "1")
    xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 241, 310, 50, 35, "2")
    xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 308, 310, 50, 35, "3")
    xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 375, 310, 50, 35, "4")

    xf.fl_end_group()

    xf.fl_bgn_group()

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 150, 230, 300, 65, "Married  ")
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_LEFT)
    xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 175, 245, 100, 35, "Yes")
    xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 325, 245, 100, 35, "No")

    xf.fl_end_group()

    xf.fl_bgn_group()

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 150, 165, 300, 65, "Sex  ")
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_LEFT)
    xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 175, 180, 100, 35, "Male")
    xf.fl_add_lightbutton(xfc.FL_RADIO_BUTTON, 325, 180, 100, 35, "Female")

    xf.fl_end_group()

    xf.fl_add_input(xfc.FL_NORMAL_INPUT, 150, 30, 300, 30, "Name  ")

    xf.fl_add_input(xfc.FL_NORMAL_INPUT, 150, 75, 300, 30, "Address  ")

    xf.fl_add_input(xfc.FL_NORMAL_INPUT, 150, 120, 300, 30, "City  ")

    pbut = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 25, 360, 75, 30, "OK")
    pbut.contents.u_ldata = 255

    xf.fl_end_form()



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    make_form1()
    xf.fl_show_form(pform, xfc.FL_PLACE_CENTER, xfc.FL_NOBORDER, "Demo06")

    while True:
        pobj = xf.fl_do_forms()
        if pobj.contents.u_ldata == pbut.contents.u_ldata:    # temporary trick to compare 2 objects
            if xf.fl_show_question("Do you really want to Quit?", 0):
                xf.fl_finish()
                sys.exit(0)

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

