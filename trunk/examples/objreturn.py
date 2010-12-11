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
import xformslib as xfl



# Forms and Objects
class FD_form0(object):
    form0 = None
    vdata = None
    ldata = 0
    pobj = [None] * 4
    br = None
    when = None


class Flobjreturn(object):
    def __init__(self, lsysargv, sysargv):

        self.mess = ["slider returned", "counter returned", \
                "input 1 returned", "input 2 returned"]

        xfl.fl_set_border_width(-2)

        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.fd_form0 = self.create_form_form0()

        # fill-in form initialization code
        self.set_when(0)
        xfl.fl_set_object_dblbuffer(self.fd_form0.br, 1)

        pitem1st = xfl.fl_add_select_items(self.fd_form0.when, "RETURN_NONE")
        xfl.fl_popup_entry_set_shortcut(pitem1st, xfl.FL_RETURN_NONE)

        pitem2nd = xfl.fl_insert_select_items(self.fd_form0.when, pitem1st, \
                "RETURN_CHANGED")
        xfl.fl_popup_entry_set_shortcut(pitem2nd, xfl.FL_RETURN_CHANGED)

        pitem3rd = xfl.fl_insert_select_items(self.fd_form0.when, pitem2nd, \
                "RETURN_END")
        xfl.fl_popup_entry_set_shortcut(pitem3rd, xfl.FL_RETURN_END)
        pitem4th = xfl.fl_insert_select_items(self.fd_form0.when, pitem3rd, \
                "RETURN_END_CHANGED")
        xfl.fl_popup_entry_set_shortcut(pitem4th, xfl.FL_RETURN_END_CHANGED)
        pitem5th = xfl.fl_insert_select_items(self.fd_form0.when, pitem4th, \
                "RETURN_ALWAYS")
        xfl.fl_popup_entry_set_shortcut(pitem5th, xfl.FL_RETURN_ALWAYS)

        # show the first form
        xfl.fl_show_form(self.fd_form0.form0, xfl.FL_PLACE_CENTER, \
                xfl.FL_FULLBORDER, "form0")

        xfl.fl_do_forms()


    # callbacks for form form0

    def return_cb(self, pobj, data):
        xfl.fl_addto_browser(self.fd_form0.br, self.mess[data])


    def set_when(self, n):
        xfl.fl_set_object_return(self.fd_form0.pobj[0], n)
        xfl.fl_set_object_return(self.fd_form0.pobj[1], n)
        xfl.fl_set_object_return(self.fd_form0.pobj[2], n)
        xfl.fl_set_object_return(self.fd_form0.pobj[3], n)


    def when_cb(self, pobj, data):
        self.set_when(xfl.fl_get_select_item(pobj).contents.val)


    def resetlog_cb(self, pobj, data):
        xfl.fl_clear_browser(self.fd_form0.br)


    def create_form_form0(self):

        fdui = FD_form0()

        fdui.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 321, 276)

        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 321, 276, "")

        fdui.pobj[0] = xfl.fl_add_valslider(xfl.FL_HOR_SLIDER, 12, 55, \
                138, 22, "")
        xfl.fl_set_object_lalign(fdui.pobj[0] , xfl.FL_ALIGN_BOTTOM | \
                xfl.FL_ALIGN_INSIDE)
        xfl.fl_set_object_callback(fdui.pobj[0], self.return_cb, 0)
        xfl.fl_set_object_return(fdui.pobj[0], xfl.FL_RETURN_CHANGED)

        fdui.pobj[1] = xfl.fl_add_counter(xfl.FL_NORMAL_COUNTER, 12, 85, \
                138, 22, "")
        xfl.fl_set_object_lalign(fdui.pobj[1], xfl.FL_ALIGN_BOTTOM | \
                xfl.FL_ALIGN_INSIDE)
        xfl.fl_set_object_callback(fdui.pobj[1], self.return_cb, 1)

        fdui.pobj[2] = xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 12, 150, \
                138, 25, "")
        xfl.fl_set_object_callback(fdui.pobj[2], self.return_cb, 2)

        fdui.br = xfl.fl_add_browser(xfl.FL_NORMAL_BROWSER, 170, 55, \
                140, 160, "")

        fdui.pobj[3] = xfl.fl_add_input(xfl.FL_INT_INPUT, 12, 187, 138, 25, "")
        xfl.fl_set_object_lalign(fdui.pobj[3], xfl.FL_ALIGN_LEFT | \
                xfl.FL_ALIGN_INSIDE)
        xfl.fl_set_object_callback(fdui.pobj[3], self.return_cb, 3)

        fdui.when = xfl.fl_add_select(xfl.FL_NORMAL_SELECT, 40, 12, \
                240, 27, "")
        xfl.fl_set_object_callback(fdui.when, self.when_cb, 0)

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 170, 239, \
                80, 25, "Done")

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 70, 239, \
                80, 25, "ResetLog")
        xfl.fl_set_object_callback(pobj, self.resetlog_cb, 0)

        xfl.fl_end_form()

        return fdui



if __name__ == '__main__':
    print("********* objreturn.py *********")
    appl = Flobjreturn(len(sys.argv), sys.argv)

