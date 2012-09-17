#!/usr/bin/env python3

#  This file is part of xforms-python, and it has been ported from
#  select.c XForms demo, with some adaptations and modifications.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#

import sys
#sys.path.append("..")
import xformslib as xfl


class Flselect(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_flip_yorigin()
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.create_form()
        xfl.fl_show_form(self.pform, xfl.FL_PLACE_CENTER | xfl.FL_FREE_SIZE, \
                xfl.FL_TRANSIENT, "Select Object Demo")
        while True:
            pobj = xfl.fl_do_forms()
            if xfl.fl_is_same_object(pobj, self.preadyobj):
                break


    def exitcb(self, pobj, data):
        xfl.fl_hide_form(self.pform)
        xfl.fl_finish()
        sys.exit()


    def cb(self, pr):
        message = "CallBack: %s" % pr.contents.label
        print(message)
        return 0


    def create_form(self):
        self.pform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 420, 360)
        xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 420, 360, "")
        xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 70, 300, 320, 30, "Name")
        xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 70, 260, 320, 30, "Address")
        xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 70, 220, 320, 30, "City")
        xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 70, 180, 320, 30, "Country")
        psexobj = xfl.fl_add_select(xfl.FL_NORMAL_SELECT, 70, 130, \
                110, 30, "Sex")
        pmaleent = xfl.fl_add_select_items(psexobj, "Male%SM")
        xfl.fl_popup_entry_set_callback(pmaleent, self.cb)
        xfl.fl_popup_entry_set_state(pmaleent, xfl.FL_POPUP_NONE)    # 0
        xfl.fl_popup_entry_set_shortcut(pmaleent, "M")
        pfemaleent = xfl.fl_add_select_items(psexobj, "Female%SF")
        xfl.fl_popup_entry_set_callback(pfemaleent, self.cb)
        xfl.fl_popup_entry_set_state(pfemaleent, xfl.FL_POPUP_NONE)    # 0
        xfl.fl_popup_entry_set_shortcut(pfemaleent, "F")
        xfl.fl_set_object_shortcut(psexobj, "S", 1)
        pchildobj = xfl.fl_add_select(xfl.FL_MENU_SELECT, 280, 130, 110, 30, \
                "Children")
        xfl.fl_add_select_items(pchildobj, "Zero|One|Two|Three|Four|Many")
        xfl.fl_set_object_shortcut(pchildobj, "C", 1)
        xfl.fl_popup_set_title(xfl.fl_get_select_popup(pchildobj), "Kids")
        plicenceobj = xfl.fl_add_select(xfl.FL_NORMAL_SELECT, 280, 80, \
                110, 30, "Licence")
        xfl.fl_add_select_items(plicenceobj, "Yes|No")
        xfl.fl_set_select_policy(plicenceobj, xfl.FL_POPUP_DRAG_SELECT)
        pmarriedobj = xfl.fl_add_select(xfl.FL_DROPLIST_SELECT, 70, 80, \
                110, 27, "Married")
        xfl.fl_add_select_items(pmarriedobj, "Yes|No")
        self.preadyobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 150, 20, \
                140, 30, "Quit")
        xfl.fl_set_object_callback(self.preadyobj, self.exitcb, 0)
        xfl.fl_end_form()


if __name__ == '__main__':
    print ("********* select.py *********")
    Flselect(len(sys.argv), sys.argv)
