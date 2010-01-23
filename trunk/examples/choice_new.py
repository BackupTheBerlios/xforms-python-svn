#!/usr/bin/env python

#  This file is part of xforms-python, and it is a variation of
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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flinput import *
from xformslib.flmisc import *
from xformslib.flbutton import *
from xformslib.flselect import *
from xformslib.xfdata import *




class Choice(object):

    def __init__(self, lsysargv, sysargv):

        fl_flip_yorigin()
        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        self.create_form()
        fl_add_select_items(self.psexobj,"Male")
        fl_add_select_items(self.psexobj,"Female")
        fl_add_select_items(self.pchildobj, "Zero|One|Two|Three|Four|Many")
        fl_add_select_items(self.plicenceobj, "Yes")
        fl_add_select_items(self.plicenceobj, "No")
        fl_add_select_items(self.pmarriedobj, "Yes")
        fl_add_select_items(self.pmarriedobj, "No")

        fl_show_form(self.pform, FL_PLACE_CENTER | FL_FREE_SIZE, \
                    FL_TRANSIENT, "Choice(Select)Demo")

        while fl_do_forms():
            pass            # empty


    def exitcb(self, pobj, data):
        fl_hide_form(self.pform)
        fl_finish()
        sys.exit()


    def cb(self, pobj, data):
        pselitem = fl_get_select_item(pobj)
        print("CallBack: %d\n" % pselitem.contents.val)


    def create_form(self):
        self.pform = fl_bgn_form(FL_NO_BOX, 420, 360)

        fl_add_box(FL_UP_BOX, 0, 0, 420, 360, "")
        fl_add_input(FL_NORMAL_INPUT, 70, 300, 320, 30, "Name")
        fl_add_input(FL_NORMAL_INPUT, 70, 260, 320, 30, "Address")
        fl_add_input(FL_NORMAL_INPUT, 70, 220, 320, 30, "City")
        fl_add_input(FL_NORMAL_INPUT, 70, 180, 320, 30, "Country")

        self.psexobj = fl_add_select(FL_NORMAL_SELECT, 70, 130, 110, 30, \
                               "Sex")
        fl_set_object_shortcut(self.psexobj, "S", 1)

        self.pchildobj = fl_add_select(FL_MENU_SELECT, 280, 130, 110, 30,
                                 "Children")
        self.plicenceobj = fl_add_select(FL_NORMAL_SELECT, 280, 80, 110, 30, \
                                   "Licence")
        self.pmarriedobj = fl_add_select(FL_DROPLIST_SELECT, 70, 80, 110, 27,
                                   "Married")
        fl_set_object_boxtype(self.pmarriedobj, FL_UP_BOX)
        fl_set_object_callback(self.pmarriedobj, self.cb, 0)

        self.preadyobj = fl_add_button(FL_NORMAL_BUTTON, 150, 20, 140, 30, \
                                 "Quit")
        fl_set_object_callback(self.preadyobj, self.exitcb, 0)

        fl_end_form()




if __name__ == '__main__':
    appl = Choice(len(sys.argv), sys.argv)

