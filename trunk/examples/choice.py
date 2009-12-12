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


def exitcb(ob, data):
    xf.fl_hide_form(form)
    xf.fl_finish()
    sys.exit()


def cb(ob, data):
    print("CallBack: %d\n" % xf.fl_get_choice(ob))


def create_form():
    global form, sexobj, childobj, licenceobj, marriedobj, readyobj

    form = xf.fl_bgn_form(xfc.FL_NO_BOX, 420, 360)

    xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 420, 360, "")
    xf.fl_add_input(xfc.FL_NORMAL_INPUT, 70, 300, 320, 30, "Name")
    xf.fl_add_input(xfc.FL_NORMAL_INPUT, 70, 260, 320, 30, "Address")
    xf.fl_add_input(xfc.FL_NORMAL_INPUT, 70, 220, 320, 30, "City")
    xf.fl_add_input(xfc.FL_NORMAL_INPUT, 70, 180, 320, 30, "Country")

    sexobj = xf.fl_add_choice(xfc.FL_NORMAL_CHOICE, 70, 130, 110, 30, \
                              "Sex")
    xf.fl_set_choice_notitle(sexobj, 1)
    xf.fl_set_object_shortcut(sexobj, "S", 1)

    childobj = xf.fl_add_choice(xfc.FL_NORMAL_CHOICE2, 280, 130, 110, 30,
                                "Children")
    licenceobj = xf.fl_add_choice(xfc.FL_NORMAL_CHOICE, 280, 80, 110, 30, \
                                  "Licence")
    marriedobj = xf.fl_add_choice(xfc.FL_DROPLIST_CHOICE, 70, 80, 110, 27,
                                  "Married")
    xf.fl_set_object_boxtype(marriedobj, xfc.FL_UP_BOX)
    xf.fl_set_object_callback(marriedobj, cb, 0)

    readyobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 150, 20, 140, 30, \
                                "Quit")
    xf.fl_set_object_callback(readyobj, exitcb, 0)

    xf.fl_end_form()


def main(lsysargv, sysargv):

    obj = None

    xf.fl_flip_yorigin()
    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    create_form()
    xf.fl_addto_choice(sexobj,"Male")
    xf.fl_addto_choice(sexobj,"Female")
    xf.fl_addto_choice(childobj, "Zero|One|Two|Three|Four|Many")
    xf.fl_addto_choice(licenceobj, "Yes")
    xf.fl_addto_choice(licenceobj, "No")
    xf.fl_addto_choice(marriedobj, "Yes")
    xf.fl_addto_choice(marriedobj, "No")

    xf.fl_show_form(form, xfc.FL_PLACE_CENTER | xfc.FL_FREE_SIZE, \
                    xfc.FL_TRANSIENT, "ChoiceDemo")

    while xf.fl_do_forms():
        pass            # empty


    return 0


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

