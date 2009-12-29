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
from xformslib import library as xf
from xformslib import xfdata as xfc



# Forms and Objects

class FD_form0(object):
    form0 = None
    vdata = None
    ldata = 0
    pobj = [None, None, None, None]
    br = None
    when = None



# callbacks for form form0

mess = ["slider returned", "counter returned", \
        "input 1 returned", "input 2 returned"]


def return_cb(pobj, data):
    xf.fl_addto_browser(fd_form0.br, mess[data])



def set_when(n):
    xf.fl_set_object_return(fd_form0.pobj[0], n)
    xf.fl_set_object_return(fd_form0.pobj[1], n)
    xf.fl_set_object_return(fd_form0.pobj[2], n)
    xf.fl_set_object_return(fd_form0.pobj[3], n)



def when_cb(pobj, data):
    set_when(xf.fl_get_select_item(pobj).contents.val)



def resetlog_cb(pobj, data):
    xf.fl_clear_browser(fd_form0.br)



def main(lsysargv, sysargv):
    global fd_form0

    xf.fl_set_border_width(-2)

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    fd_form0 = create_form_form0()

    # fill-in form initialization code
    set_when(0)
    xf.fl_set_object_dblbuffer(fd_form0.br, 1)

    pitem1st = xf.fl_add_select_items(fd_form0.when, "RETURN_NONE")
    xf.fl_popup_entry_set_shortcut(pitem1st, xfc.FL_RETURN_NONE)

    pitem2nd = xf.fl_insert_select_items(fd_form0.when, pitem1st, \
                                         "RETURN_CHANGED")
    xf.fl_popup_entry_set_shortcut(pitem2nd, xfc.FL_RETURN_CHANGED)

    pitem3rd = xf.fl_insert_select_items(fd_form0.when, pitem2nd, \
                                         "RETURN_END")
    xf.fl_popup_entry_set_shortcut(pitem3rd,  xfc.FL_RETURN_END)
    pitem4th = xf.fl_insert_select_items(fd_form0.when, pitem3rd, \
                                         "RETURN_END_CHANGED")
    xf.fl_popup_entry_set_shortcut(pitem4th, xfc.FL_RETURN_END_CHANGED)
    pitem5th = xf.fl_insert_select_items(fd_form0.when, pitem4th, \
                                         "RETURN_ALWAYS")
    xf.fl_popup_entry_set_shortcut(pitem5th, xfc.FL_RETURN_ALWAYS)

    # show the first form
    xf.fl_show_form(fd_form0.form0, xfc.FL_PLACE_CENTER, xfc.FL_FULLBORDER, \
                    "form0")

    xf.fl_do_forms()

    return 0



def create_form_form0():

    fdui = FD_form0()

    fdui.form0 = xf.fl_bgn_form(xfc.FL_NO_BOX, 321, 276)

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 321, 276, "")

    fdui.pobj[0] = xf.fl_add_valslider(xfc.FL_HOR_SLIDER, 12, 55, 138, 22, "")
    xf.fl_set_object_lalign(fdui.pobj[0] ,xfc.FL_ALIGN_BOTTOM| xfc.FL_ALIGN_INSIDE)
    xf.fl_set_object_callback(fdui.pobj[0], return_cb, 0)
    xf.fl_set_slider_return(fdui.pobj[0], xfc.FL_RETURN_CHANGED)

    fdui.pobj[1] = xf.fl_add_counter(xfc.FL_NORMAL_COUNTER, 12, 85, 138, 22, "")
    xf.fl_set_object_lalign(fdui.pobj[1], xfc.FL_ALIGN_BOTTOM | xfc.FL_ALIGN_INSIDE)
    xf.fl_set_object_callback(fdui.pobj[1], return_cb, 1)

    fdui.pobj[2] = xf.fl_add_input(xfc.FL_NORMAL_INPUT, 12, 150, 138, 25, "")
    xf.fl_set_object_callback(fdui.pobj[2], return_cb, 2)

    fdui.br = xf.fl_add_browser(xfc.FL_NORMAL_BROWSER, 170, 55, 140, 160, "")

    fdui.pobj[3] = xf.fl_add_input(xfc.FL_INT_INPUT, 12, 187, 138, 25, "")
    xf.fl_set_object_lalign(fdui.pobj[3], xfc.FL_ALIGN_LEFT | xfc.FL_ALIGN_INSIDE)
    xf.fl_set_object_callback(fdui.pobj[3], return_cb, 3)

    fdui.when = xf.fl_add_select(xfc.FL_NORMAL_SELECT, 40, 12, 240, 27, "")
    xf.fl_set_object_callback(fdui.when, when_cb, 0)

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 170, 239, 80, 25, "Done")

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 70, 239, 80, 25, "ResetLog")
    xf.fl_set_object_callback(pobj, resetlog_cb, 0)

    xf.fl_end_form()

    return fdui




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

