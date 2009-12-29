#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  select.c XForms demo, with some adaptations and modifications.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



def exitcb(pobj, data):
    xf.fl_hide_form(pform)
    xf.fl_finish()
    sys.exit()


def cb(pr):
    print ("CallBack: %s\n" % pr.contents.label)
    return 0


def create_form():

    global pform, preadyobj

    pform = xf.fl_bgn_form(xfc.FL_NO_BOX, 420, 360)

    xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 420, 360, "")

    xf.fl_add_input(xfc.FL_NORMAL_INPUT, 70, 300, 320, 30, "Name")
    xf.fl_add_input(xfc.FL_NORMAL_INPUT, 70, 260, 320, 30, "Address")
    xf.fl_add_input(xfc.FL_NORMAL_INPUT, 70, 220, 320, 30, "City")
    xf.fl_add_input(xfc.FL_NORMAL_INPUT, 70, 180, 320, 30, "Country")

    psexobj = xf.fl_add_select(xfc.FL_NORMAL_SELECT, 70, 130, 110, 30, "Sex")

    pmaleent = xf.fl_add_select_items(psexobj, "Male%SM")
    xf.fl_popup_entry_set_callback(pmaleent, cb)
    xf.fl_popup_entry_set_state(pmaleent, xfc.FL_POPUP_NONE)            # 0
    xf.fl_popup_entry_set_shortcut(pmaleent, "M")
    #pmaleent.contents.type = xfc.FL_POPUP_TOGGLE etc..

    pfemaleent = xf.fl_add_select_items(psexobj, "Female%SF")
    xf.fl_popup_entry_set_callback(pfemaleent, cb)
    xf.fl_popup_entry_set_state(pfemaleent, xfc.FL_POPUP_NONE)          # 0
    xf.fl_popup_entry_set_shortcut(pfemaleent, "F")

    xf.fl_set_object_shortcut(psexobj, "S", 1)

    pchildobj = xf.fl_add_select(xfc.FL_MENU_SELECT, 280, 130, 110, 30,
                                "Children")
    xf.fl_add_select_items(pchildobj, "Zero|One|Two|Three|Four|Many")
    xf.fl_set_object_shortcut(pchildobj, "C", 1)
    xf.fl_popup_set_title(xf.fl_get_select_popup(pchildobj), "Kids")

    plicenceobj = xf.fl_add_select(xfc.FL_NORMAL_SELECT, 280, 80, 110, 30, \
                                   "Licence")
    xf.fl_add_select_items(plicenceobj, "Yes|No")
    xf.fl_set_select_policy(plicenceobj, xfc.FL_POPUP_DRAG_SELECT)

    pmarriedobj = xf.fl_add_select(xfc.FL_DROPLIST_SELECT, 70, 80, 110, 27,
                                   "Married")
    xf.fl_add_select_items(pmarriedobj, "Yes|No")

    preadyobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 150, 20, 140, 30, \
                                "Quit")
    xf.fl_set_object_callback(preadyobj, exitcb, 0)

    xf.fl_end_form()



def main(lsysargv, sysargv):


    xf.fl_flip_yorigin()
    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    create_form()

    xf.fl_show_form(pform, xfc.FL_PLACE_CENTER | xfc.FL_FREE_SIZE, \
                    xfc.FL_TRANSIENT, "Select Object Demo")

    while True:
        pobj = xf.fl_do_forms()
        if xf.fl_is_same_object(pobj, preadyobj):
            break

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

