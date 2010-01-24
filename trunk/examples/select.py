#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  select.c XForms demo, with some adaptations and modifications.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flinput import *
from xformslib.flbutton import *
from xformslib.flpopup import *
from xformslib.flselect import *
from xformslib.flmisc import *
from xformslib.xfdata import *




class Flselect(object):
    def __init__(self, lsysargv, sysargv):

        fl_flip_yorigin()
        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        self.create_form()

        fl_show_form(self.pform, FL_PLACE_CENTER | FL_FREE_SIZE, \
                        FL_TRANSIENT, "Select Object Demo")
        while True:
            pobj = fl_do_forms()
            if fl_is_same_object(pobj, self.preadyobj):
                break


    def exitcb(self, pobj, data):
        fl_hide_form(self.pform)
        fl_finish()
        sys.exit()


    def cb(self, pr):
        print ("CallBack: %s\n" % pr.contents.label)
        return 0


    def create_form(self):

        self.pform = fl_bgn_form(FL_NO_BOX, 420, 360)

        fl_add_box(FL_UP_BOX, 0, 0, 420, 360, "")

        fl_add_input(FL_NORMAL_INPUT, 70, 300, 320, 30, "Name")
        fl_add_input(FL_NORMAL_INPUT, 70, 260, 320, 30, "Address")
        fl_add_input(FL_NORMAL_INPUT, 70, 220, 320, 30, "City")
        fl_add_input(FL_NORMAL_INPUT, 70, 180, 320, 30, "Country")

        psexobj = fl_add_select(FL_NORMAL_SELECT, 70, 130, \
                                   110, 30, "Sex")

        pmaleent = fl_add_select_items(psexobj, "Male%SM")
        fl_popup_entry_set_callback(pmaleent, self.cb)
        fl_popup_entry_set_state(pmaleent, FL_POPUP_NONE)        # 0
        fl_popup_entry_set_shortcut(pmaleent, "M")

        pfemaleent = fl_add_select_items(psexobj, "Female%SF")
        fl_popup_entry_set_callback(pfemaleent, self.cb)
        fl_popup_entry_set_state(pfemaleent, FL_POPUP_NONE)      # 0
        fl_popup_entry_set_shortcut(pfemaleent, "F")

        fl_set_object_shortcut(psexobj, "S", 1)

        pchildobj = fl_add_select(FL_MENU_SELECT, 280, 130, 110, 30,
                                    "Children")
        fl_add_select_items(pchildobj, "Zero|One|Two|Three|Four|Many")
        fl_set_object_shortcut(pchildobj, "C", 1)
        fl_popup_set_title(fl_get_select_popup(pchildobj), "Kids")

        plicenceobj = fl_add_select(FL_NORMAL_SELECT, 280, 80, \
                                       110, 30, "Licence")
        fl_add_select_items(plicenceobj, "Yes|No")
        fl_set_select_policy(plicenceobj, FL_POPUP_DRAG_SELECT)

        pmarriedobj = fl_add_select(FL_DROPLIST_SELECT, 70, 80, \
                                       110, 27, "Married")
        fl_add_select_items(pmarriedobj, "Yes|No")

        self.preadyobj = fl_add_button(FL_NORMAL_BUTTON, 150, 20, \
                                          140, 30, "Quit")
        fl_set_object_callback(self.preadyobj, self.exitcb, 0)

        fl_end_form()




if __name__ == '__main__':
    Flselect(len(sys.argv), sys.argv)

