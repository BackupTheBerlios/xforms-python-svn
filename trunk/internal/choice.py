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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flinput import *
from xformslib.flmisc import *
from xformslib.flbutton import *
from xformslib.xfdata import *
from xformslib import deprecated



class Choice(object):

    def __init__(self, lsysargv, sysargv):

        fl_flip_yorigin()
        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        self.create_form()
        deprecated.fl_addto_choice(self.psexobj,"Male")
        deprecated.fl_addto_choice(self.psexobj,"Female")
        deprecated.fl_addto_choice(self.pchildobj, "Zero|One|Two|Three|Four|Many")
        deprecated.fl_addto_choice(self.plicenceobj, "Yes")
        deprecated.fl_addto_choice(self.plicenceobj, "No")
        deprecated.fl_addto_choice(self.pmarriedobj, "Yes")
        deprecated.fl_addto_choice(self.pmarriedobj, "No")

        fl_show_form(self.pform, FL_PLACE_CENTER | FL_FREE_SIZE, \
                    FL_TRANSIENT, "ChoiceDemo")

        while fl_do_forms():
            pass            # empty


    def exitcb(self, pobj, data):
        fl_hide_form(self.pform)
        fl_finish()
        sys.exit()


    def cb(self, pobj, data):
        print("CallBack: %d\n" % deprecated.fl_get_choice(pobj))


    def create_form(self):
        #global pform, psexobj, pchildobj, plicenceobj, pmarriedobj, preadyobj

        self.pform = fl_bgn_form(FL_NO_BOX, 420, 360)

        fl_add_box(FL_UP_BOX, 0, 0, 420, 360, "")
        fl_add_input(FL_NORMAL_INPUT, 70, 300, 320, 30, "Name")
        fl_add_input(FL_NORMAL_INPUT, 70, 260, 320, 30, "Address")
        fl_add_input(FL_NORMAL_INPUT, 70, 220, 320, 30, "City")
        fl_add_input(FL_NORMAL_INPUT, 70, 180, 320, 30, "Country")

        self.psexobj = deprecated.fl_add_choice(deprecated.FL_NORMAL_CHOICE, 70, 130, 110, 30, \
                               "Sex")
        deprecated.fl_set_choice_notitle(self.psexobj, 1)
        fl_set_object_shortcut(self.psexobj, "S", 1)

        self.pchildobj = deprecated.fl_add_choice(deprecated.FL_NORMAL_CHOICE2, 280, 130, 110, 30,
                                 "Children")
        self.plicenceobj = deprecated.fl_add_choice(deprecated.FL_NORMAL_CHOICE, 280, 80, 110, 30, \
                                   "Licence")
        self.pmarriedobj = deprecated.fl_add_choice(deprecated.FL_DROPLIST_CHOICE, 70, 80, 110, 27,
                                   "Married")
        fl_set_object_boxtype(self.pmarriedobj, FL_UP_BOX)
        fl_set_object_callback(self.pmarriedobj, self.cb, 0)

        self.preadyobj = fl_add_button(FL_NORMAL_BUTTON, 150, 20, 140, 30, \
                                 "Quit")
        fl_set_object_callback(self.preadyobj, self.exitcb, 0)

        fl_end_form()




if __name__ == '__main__':
    appl = Choice(len(sys.argv), sys.argv)

