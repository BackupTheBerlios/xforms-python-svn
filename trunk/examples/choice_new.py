#!/usr/bin/env python

#  This file is part of xforms-python, and it is a variant of
#  choice.c XForms demo, not using deprecated functions, with some
#  adaptations.
#
#  choice.c was written by M. Overmars and T.C. Zhao (1997)
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
#  This demo shows the use of choice objects.
#

import sys
#sys.path.append("..")
import xformslib as xfl



class Choice(object):

    def __init__(self, lsysargv, sysargv):

        xfl.fl_flip_yorigin()
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)

        self.create_form()
        xfl.fl_add_select_items(self.psexobj,"Male")
        xfl.fl_add_select_items(self.psexobj,"Female")
        xfl.fl_add_select_items(self.pchildobj, "Zero|One|Two|Three|Four|Many")
        xfl.fl_add_select_items(self.plicenceobj, "Yes")
        xfl.fl_add_select_items(self.plicenceobj, "No")
        xfl.fl_add_select_items(self.pmarriedobj, "Yes")
        xfl.fl_add_select_items(self.pmarriedobj, "No")

        xfl.fl_show_form(self.pform, xfl.FL_PLACE_CENTER | xfl.FL_FREE_SIZE, \
                xfl.FL_TRANSIENT, "Choice(Select)Demo")

        while xfl.fl_do_forms():
            pass            # empty


    def exitcb(self, pobj, data):
        xfl.fl_hide_form(self.pform)
        xfl.fl_finish()
        sys.exit()


    def cb(self, pobj, data):
        pselitem = xfl.fl_get_select_item(pobj)
        message = "CallBack: %d\n" % pselitem.contents.val
        print(message)


    def create_form(self):
        self.pform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 420, 360)

        xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 420, 360, "")
        xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 70, 300, 320, 30, "Name")
        xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 70, 260, 320, 30, "Address")
        xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 70, 220, 320, 30, "City")
        xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 70, 180, 320, 30, "Country")

        self.psexobj = xfl.fl_add_select(xfl.FL_NORMAL_SELECT, 70, 130, \
                110, 30, "Sex")
        xfl.fl_set_object_shortcut(self.psexobj, "S", 1)

        self.pchildobj = xfl.fl_add_select(xfl.FL_MENU_SELECT, 280, 130, \
                110, 30, "Children")
        self.plicenceobj = xfl.fl_add_select(xfl.FL_NORMAL_SELECT, 280, 80, \
                110, 30, "Licence")
        self.pmarriedobj = xfl.fl_add_select(xfl.FL_DROPLIST_SELECT, 70, 80, \
                110, 27, "Married")
        xfl.fl_set_object_boxtype(self.pmarriedobj, xfl.FL_UP_BOX)
        xfl.fl_set_object_callback(self.pmarriedobj, self.cb, 0)

        self.preadyobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 150, 20, \
                140, 30, "Quit")
        xfl.fl_set_object_callback(self.preadyobj, self.exitcb, 0)

        xfl.fl_end_form()



if __name__ == '__main__':
    print("********* choice_new.py *********")
    appl = Choice(len(sys.argv), sys.argv)

