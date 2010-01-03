#!/usr/bin/env python

#  This file is part of xforms-python, and it is a variation of nmenu
#  to show some fl_*_nmenu_items2 functions.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.


import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



def item1_cb(r):
    print "choice 1 added", xf.fl_get_nmenu_item_by_value(pmenu1, 1)
    return 0

def item2_cb(r):
    print "choice 2 added", xf.fl_get_nmenu_item_by_value(pmenu1, 2)
    return 0

def item3_cb(r):
    print "choice 3 inserted", xf.fl_get_nmenu_item_by_value(pmenu1, 3)
    return 0

def item4_cb(r):
    print "choice 4 inserted", xf.fl_get_nmenu_item_by_value(pmenu1, 4)
    return 0

def item5_cb(r):
    print "choice 5 added", xf.fl_get_nmenu_item_by_value(pmenu1, 5)
    return 0

def item6_cb(r):
    print "Choice 6 replace for choice 1", xf.fl_get_nmenu_item_by_value(pmenu1, 6)
    return 0

def item7_cb(r):
    print "Choice 7 replace for choice 2", xf.fl_get_nmenu_item_by_value(pmenu1, 7)
    return 0

def done_cb(r):
    xf.fl_finish()
    sys.exit(0)

def item9_cb(r):
    print "choice 9 added", xf.fl_get_nmenu_item_by_value(pmenu2, 9)
    return 0

def item10_cb(r):
    print "Choice 10 added", xf.fl_get_nmenu_item_by_value(pmenu2, 10)
    return 0

def item11_cb(r):
    print "Choice 11 added", xf.fl_get_nmenu_item_by_value(pmenu2, 11)
    return 0

def item12_cb(r):
    print "Choice 12 inserted", xf.fl_get_nmenu_item_by_value(pmenu2, 12)
    return 0



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    pform = create_form()

    # remember: it's a list of lists, but you can pass a single list, too.
    MypopupitemA = ["First item ADD", item1_cb, "F", xfc.FL_POPUP_NORMAL, xfc.FL_POPUP_NONE], \
                    ["Second item ADD", item2_cb, "E", xfc.FL_POPUP_NORMAL, xfc.FL_POPUP_NONE]

    ppopmenu1 = xf.make_pPopupItem_from_list(MypopupitemA)
    entry12 = xf.fl_add_nmenu_items2(pmenu1, ppopmenu1)

    MypopupitemB = ["Third item INS", item3_cb, "T", xfc.FL_POPUP_NORMAL, xfc.FL_POPUP_NONE], \
                    ["Fourth menu INS", item4_cb, "O", xfc.FL_POPUP_NORMAL, xfc.FL_POPUP_NONE]

    ppopmenu2 = xf.make_pPopupItem_from_list(MypopupitemB)
    entry34 = xf.fl_insert_nmenu_items2(pmenu1, None, ppopmenu2)

    MypopupitemC = ["Fifth item ADD", item5_cb, "I", xfc.FL_POPUP_NORMAL, xfc.FL_POPUP_NONE]

    ppopmenu3 = xf.make_pPopupItem_from_list(MypopupitemC)
    entry5 = xf.fl_add_nmenu_items2(pmenu1, ppopmenu3)

    MypopupitemD = ["Sixth item REPL", item6_cb, "S", xfc.FL_POPUP_NORMAL, xfc.FL_POPUP_NONE], \
                    ["Seventh menu REPL", item7_cb, "V", xfc.FL_POPUP_NORMAL, xfc.FL_POPUP_NONE]

    ppopmenu4 = xf.make_pPopupItem_from_list(MypopupitemD)
    entry67 = xf.fl_replace_nmenu_items2(pmenu1, entry12, ppopmenu4)

    MypopupitemE = ["Exit ADD", done_cb, "X", xfc.FL_POPUP_NORMAL, xfc.FL_POPUP_NONE]

    ppopmenu5 = xf.make_pPopupItem_from_list(MypopupitemE)
    entry8 = xf.fl_add_nmenu_items2(pmenu1, ppopmenu5)

    MypopupitemF = ["Ninth item ADD", item1_cb, "F", xfc.FL_POPUP_NORMAL, xfc.FL_POPUP_NONE], \
                    ["Tenth item ADD", item2_cb, "E", xfc.FL_POPUP_NORMAL, xfc.FL_POPUP_NONE]

    ppopmenu6 = xf.make_pPopupItem_from_list(MypopupitemF)
    entry910 = xf.fl_add_nmenu_items2(pmenu2, ppopmenu6)

    # currently dict is *only* for 1 item
    MypopupitemG = {'text' : "Eleventh item INS", 'callback' : item3_cb, 'shortcut' : "T", \
                    'type' : xfc.FL_POPUP_NORMAL, 'state' : xfc.FL_POPUP_NONE}

    ppopmenu7 = xf.make_pPopupItem_from_dict(MypopupitemG)
    entry910 = xf.fl_insert_nmenu_items2(pmenu2, entry910, ppopmenu7)



    xf.fl_show_form(pform, xfc.FL_PLACE_CENTER, xfc.FL_TRANSIENT, "Nmenu")

    while xf.fl_do_forms():
        pass

    return 0





def create_form():
    global pmenu1, pmenu2

    pform = xf.fl_bgn_form(xfc.FL_NO_BOX, 444, 380)

    pobj = xf.fl_add_box(xfc.FL_BORDER_BOX, 0, 0, 444, 380, "")
    xf.fl_set_object_color(pobj, xfc.FL_SLATEBLUE, xfc.FL_COL1)

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 444, 29, "")
    xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_COL1)

    pmenu1 = xf.fl_add_nmenu(xfc.FL_NORMAL_NMENU, 2, 2, 110, 25, "Menu 1")
    xf.fl_set_object_shortcut(pmenu1, "1#1", 1)

    pmenu2 = xf.fl_add_nmenu(xfc.FL_NORMAL_NMENU, 102, 2, 110, 25, "Menu 2")
    xf.fl_set_object_shortcut(pmenu2, "2#2", 2)

    xf.fl_end_form()

    return pform



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

