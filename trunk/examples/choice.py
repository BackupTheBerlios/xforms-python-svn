#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  choice.c XForms demo, with some adaptations.
#
#  choice.c was written by M. Overmars and T.C. Zhao (1997)
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
#  This demo shows the use of choice objects.
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc
from xformslib import oldfunc as xfdepr

def exitcb(pobj, data):
    xf.fl_hide_form(pform)
    xf.fl_finish()
    sys.exit()


def cb(pobj, data):
    print("CallBack: %d\n" % xfdepr.fl_get_choice(pobj))


def create_form():
    global pform, psexobj, pchildobj, plicenceobj, pmarriedobj, preadyobj

    pform = xf.fl_bgn_form(xfc.FL_NO_BOX, 420, 360)

    xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 420, 360, "")
    xf.fl_add_input(xfc.FL_NORMAL_INPUT, 70, 300, 320, 30, "Name")
    xf.fl_add_input(xfc.FL_NORMAL_INPUT, 70, 260, 320, 30, "Address")
    xf.fl_add_input(xfc.FL_NORMAL_INPUT, 70, 220, 320, 30, "City")
    xf.fl_add_input(xfc.FL_NORMAL_INPUT, 70, 180, 320, 30, "Country")

    psexobj = xfdepr.fl_add_choice(xfdepr.FL_NORMAL_CHOICE, 70, 130, 110, 30, \
                               "Sex")
    xfdepr.fl_set_choice_notitle(psexobj, 1)
    xfdepr.fl_set_object_shortcut(psexobj, "S", 1)

    pchildobj = xfdepr.fl_add_choice(xfdepr.FL_NORMAL_CHOICE2, 280, 130, 110, 30,
                                 "Children")
    plicenceobj = xfdepr.fl_add_choice(xfdepr.FL_NORMAL_CHOICE, 280, 80, 110, 30, \
                                   "Licence")
    pmarriedobj = xfdepr.fl_add_choice(xfdepr.FL_DROPLIST_CHOICE, 70, 80, 110, 27,
                                   "Married")
    xf.fl_set_object_boxtype(pmarriedobj, xfc.FL_UP_BOX)
    xf.fl_set_object_callback(pmarriedobj, cb, 0)

    preadyobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 150, 20, 140, 30, \
                                 "Quit")
    xf.fl_set_object_callback(preadyobj, exitcb, 0)

    xf.fl_end_form()


def main(lsysargv, sysargv):

    xf.fl_flip_yorigin()
    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    create_form()
    xfdepr.fl_addto_choice(psexobj,"Male")
    xfdepr.fl_addto_choice(psexobj,"Female")
    xfdepr.fl_addto_choice(pchildobj, "Zero|One|Two|Three|Four|Many")
    xfdepr.fl_addto_choice(plicenceobj, "Yes")
    xfdepr.fl_addto_choice(plicenceobj, "No")
    xfdepr.fl_addto_choice(pmarriedobj, "Yes")
    xfdepr.fl_addto_choice(pmarriedobj, "No")

    xf.fl_show_form(pform, xfc.FL_PLACE_CENTER | xfc.FL_FREE_SIZE, \
                    xfc.FL_TRANSIENT, "ChoiceDemo")

    while xf.fl_do_forms():
        pass            # empty


    return 0


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

