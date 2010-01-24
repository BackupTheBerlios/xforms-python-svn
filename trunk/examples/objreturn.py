#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  objreturn.c XForms demo, with some adaptation.
#
#  objreturn.c was written by M. Overmars and T.C. Zhao
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# demo showing the choices when to return object. Note this program,
# strictly speaking, is illegal in the usage of user data parameter
# in the callback function.
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbrowser import *
from xformslib.flpopup import *
from xformslib.flinput import *
from xformslib.flselect import *
from xformslib.flslider import *
from xformslib.flcounter import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *



# Forms and Objects

class FD_form0(object):
    form0 = None
    vdata = None
    ldata = 0
    pobj = [None, None, None, None]
    br = None
    when = None



class Flobjreturn(object):
    def __init__(self, lsysargv, sysargv):

        self.mess = ["slider returned", "counter returned", \
                "input 1 returned", "input 2 returned"]

        fl_set_border_width(-2)

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.fd_form0 = self.create_form_form0()

        # fill-in form initialization code
        self.set_when(0)
        fl_set_object_dblbuffer(self.fd_form0.br, 1)

        pitem1st = fl_add_select_items(self.fd_form0.when, "RETURN_NONE")
        fl_popup_entry_set_shortcut(pitem1st, FL_RETURN_NONE)

        pitem2nd = fl_insert_select_items(self.fd_form0.when, pitem1st, \
                                         "RETURN_CHANGED")
        fl_popup_entry_set_shortcut(pitem2nd, FL_RETURN_CHANGED)

        pitem3rd = fl_insert_select_items(self.fd_form0.when, pitem2nd, \
                                         "RETURN_END")
        fl_popup_entry_set_shortcut(pitem3rd, FL_RETURN_END)
        pitem4th = fl_insert_select_items(self.fd_form0.when, pitem3rd, \
                                         "RETURN_END_CHANGED")
        fl_popup_entry_set_shortcut(pitem4th, FL_RETURN_END_CHANGED)
        pitem5th = fl_insert_select_items(self.fd_form0.when, pitem4th, \
                                         "RETURN_ALWAYS")
        fl_popup_entry_set_shortcut(pitem5th, FL_RETURN_ALWAYS)

        # show the first form
        fl_show_form(self.fd_form0.form0, FL_PLACE_CENTER, FL_FULLBORDER, \
                     "form0")

        fl_do_forms()


    # callbacks for form form0

    def return_cb(self, pobj, data):
        fl_addto_browser(self.fd_form0.br, self.mess[data])


    def set_when(self, n):
        fl_set_object_return(self.fd_form0.pobj[0], n)
        fl_set_object_return(self.fd_form0.pobj[1], n)
        fl_set_object_return(self.fd_form0.pobj[2], n)
        fl_set_object_return(self.fd_form0.pobj[3], n)


    def when_cb(self, pobj, data):
        self.set_when(fl_get_select_item(pobj).contents.val)


    def resetlog_cb(self, pobj, data):
        fl_clear_browser(self.fd_form0.br)


    def create_form_form0(self):

        fdui = FD_form0()

        fdui.form0 = fl_bgn_form(FL_NO_BOX, 321, 276)

        pobj = fl_add_box(FL_UP_BOX, 0, 0, 321, 276, "")

        fdui.pobj[0] = fl_add_valslider(FL_HOR_SLIDER, 12, 55, 138, 22, "")
        fl_set_object_lalign(fdui.pobj[0] ,FL_ALIGN_BOTTOM| FL_ALIGN_INSIDE)
        fl_set_object_callback(fdui.pobj[0], self.return_cb, 0)
        fl_set_object_return(fdui.pobj[0], FL_RETURN_CHANGED)

        fdui.pobj[1] = fl_add_counter(FL_NORMAL_COUNTER, 12, 85, 138, 22, "")
        fl_set_object_lalign(fdui.pobj[1], FL_ALIGN_BOTTOM | FL_ALIGN_INSIDE)
        fl_set_object_callback(fdui.pobj[1], self.return_cb, 1)

        fdui.pobj[2] = fl_add_input(FL_NORMAL_INPUT, 12, 150, 138, 25, "")
        fl_set_object_callback(fdui.pobj[2], self.return_cb, 2)

        fdui.br = fl_add_browser(FL_NORMAL_BROWSER, 170, 55, 140, 160, "")

        fdui.pobj[3] = fl_add_input(FL_INT_INPUT, 12, 187, 138, 25, "")
        fl_set_object_lalign(fdui.pobj[3], FL_ALIGN_LEFT | FL_ALIGN_INSIDE)
        fl_set_object_callback(fdui.pobj[3], self.return_cb, 3)

        fdui.when = fl_add_select(FL_NORMAL_SELECT, 40, 12, 240, 27, "")
        fl_set_object_callback(fdui.when, self.when_cb, 0)

        pobj = fl_add_button(FL_NORMAL_BUTTON, 170, 239, 80, 25, "Done")

        pobj = fl_add_button(FL_NORMAL_BUTTON, 70, 239, 80, 25, "ResetLog")
        fl_set_object_callback(pobj, self.resetlog_cb, 0)

        fl_end_form()

        return fdui





if __name__ == '__main__':
    Flobjreturn(len(sys.argv), sys.argv)

