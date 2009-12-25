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
    obj = [None, None, None, None]
    br = None
    when = None



# callbacks for form form0

mess = ["slider returned", "counter returned", \
        "input 1 returned", "input 2 returned"]


def return_cb(ob, data):
    xf.fl_addto_browser(fd_form0.br, mess[data])



def set_when(n):
    xf.fl_set_object_return(fd_form0.obj[0], n)
    xf.fl_set_object_return(fd_form0.obj[1], n)
    xf.fl_set_object_return(fd_form0.obj[2], n)
    xf.fl_set_object_return(fd_form0.obj[3], n)



def when_cb(ob, data):
    set_when(xf.fl_get_select_item(ob)[0].val)



def resetlog_cb(ob, data):
    xf.fl_clear_browser(fd_form0.br)



def main(lsysargv, sysargv):
    global fd_form0

    xf.fl_set_border_width(-2)

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    fd_form0 = create_form_form0()

    # fill-in form initialization code
    set_when(0)
    xf.fl_set_object_dblbuffer(fd_form0.br, 1)

    item1st = xf.fl_add_select_items(fd_form0.when, "RETURN_NONE")
    xf.fl_popup_entry_set_shortcut(item1st, xfc.FL_RETURN_NONE)

    item2nd = xf.fl_insert_select_items(fd_form0.when, item1st, \
                                        "RETURN_CHANGED")
    xf.fl_popup_entry_set_shortcut(item2nd, xfc.FL_RETURN_CHANGED)

    item3rd = xf.fl_insert_select_items(fd_form0.when, item2nd, \
                                        "RETURN_END")
    xf.fl_popup_entry_set_shortcut(item3rd,  xfc.FL_RETURN_END)
    item4th = xf.fl_insert_select_items(fd_form0.when, item3rd, \
                                        "RETURN_END_CHANGED")
    xf.fl_popup_entry_set_shortcut(item4th, xfc.FL_RETURN_END_CHANGED)
    item5th = xf.fl_insert_select_items(fd_form0.when, item4th, \
                                        "RETURN_ALWAYS")
    xf.fl_popup_entry_set_shortcut(item5th, xfc.FL_RETURN_ALWAYS)

    # show the first form
    xf.fl_show_form(fd_form0.form0, xfc.FL_PLACE_CENTER, xfc.FL_FULLBORDER, \
                    "form0")

    xf.fl_do_forms()

    return 0



def create_form_form0():

    fdui = FD_form0()

    fdui.form0 = xf.fl_bgn_form(xfc.FL_NO_BOX, 321, 276)

    obj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 321, 276, "")

    fdui.obj[0] = xf.fl_add_valslider(xfc.FL_HOR_SLIDER, 12, 55, 138, 22, "")
    xf.fl_set_object_lalign(fdui.obj[0] ,xfc.FL_ALIGN_BOTTOM| xfc.FL_ALIGN_INSIDE)
    xf.fl_set_object_callback(fdui.obj[0], return_cb, 0)
    xf.fl_set_slider_return(fdui.obj[0], xfc.FL_RETURN_CHANGED)

    fdui.obj[1] = xf.fl_add_counter(xfc.FL_NORMAL_COUNTER, 12, 85, 138, 22, "")
    xf.fl_set_object_lalign(fdui.obj[1], xfc.FL_ALIGN_BOTTOM | xfc.FL_ALIGN_INSIDE)
    xf.fl_set_object_callback(fdui.obj[1], return_cb, 1)

    fdui.obj[2] = xf.fl_add_input(xfc.FL_NORMAL_INPUT, 12, 150, 138, 25, "")
    xf.fl_set_object_callback(fdui.obj[2], return_cb, 2)

    fdui.br = xf.fl_add_browser(xfc.FL_NORMAL_BROWSER, 170, 55, 140, 160, "")

    fdui.obj[3] = xf.fl_add_input(xfc.FL_INT_INPUT, 12, 187, 138, 25, "")
    xf.fl_set_object_lalign(fdui.obj[3], xfc.FL_ALIGN_LEFT | xfc.FL_ALIGN_INSIDE)
    xf.fl_set_object_callback(fdui.obj[3], return_cb, 3)

    fdui.when = xf.fl_add_select(xfc.FL_NORMAL_SELECT, 40, 12, 240, 27, "")
    xf.fl_set_object_callback(fdui.when, when_cb, 0)

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 170, 239, 80, 25, "Done")

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 70, 239, 80, 25, "ResetLog")
    xf.fl_set_object_callback(obj, resetlog_cb, 0)

    xf.fl_end_form()

    return fdui




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

