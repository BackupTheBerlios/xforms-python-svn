#!/usr/bin/env python

#  This file is part of xforms-python, and it is a variation of nmenu
#  to show some xfl.fl_*_nmenu_items2 functions.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.


import sys
#sys.path.append("..")
import xformslib as xfl
from xformslib import library as libr



class Flnmenumin(object):
    def __init__(self, lsysargv, sysargv):

        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        pform = self.create_form()

        # remember: it's a list of lists, but you can pass a single list, too.
        MypopupitemA = ["First item ADD", self.item1_cb, "F", \
                xfl.FL_POPUP_NORMAL, xfl.FL_POPUP_NONE], \
                ["Second item ADD", self.item2_cb, "E", \
                xfl.FL_POPUP_NORMAL, xfl.FL_POPUP_NONE]

        ppopmenu1 = libr.create_pPopupItem_from_list(MypopupitemA)
        entry12 = xfl.fl_add_nmenu_items2(self.pmenu1, ppopmenu1)

        MypopupitemB = ["Third item INS", self.item3_cb, "T", \
                xfl.FL_POPUP_NORMAL, xfl.FL_POPUP_NONE], \
                ["Fourth menu INS", self.item4_cb, "O", \
                xfl.FL_POPUP_NORMAL, xfl.FL_POPUP_NONE]

        ppopmenu2 = libr.create_pPopupItem_from_list(MypopupitemB)
        entry34 = xfl.fl_insert_nmenu_items2(self.pmenu1, None, ppopmenu2)

        MypopupitemC = ["Fifth item ADD", self.item5_cb, "I", \
                xfl.FL_POPUP_NORMAL, xfl.FL_POPUP_NONE]

        ppopmenu3 = libr.create_pPopupItem_from_list(MypopupitemC)
        entry5 = xfl.fl_add_nmenu_items2(self.pmenu1, ppopmenu3)

        MypopupitemD = ["Sixth item REPL", self.item6_cb, "S", \
                xfl.FL_POPUP_NORMAL, xfl.FL_POPUP_NONE], \
                ["Seventh menu REPL", self.item7_cb, "V", \
                xfl.FL_POPUP_NORMAL, xfl.FL_POPUP_NONE]

        ppopmenu4 = libr.create_pPopupItem_from_list(MypopupitemD)
        entry67 = xfl.fl_replace_nmenu_items2(self.pmenu1, entry12, ppopmenu4)

        MypopupitemE = ["Exit ADD", self.done_cb, "X", \
                xfl.FL_POPUP_NORMAL, xfl.FL_POPUP_NONE]

        ppopmenu5 = libr.create_pPopupItem_from_list(MypopupitemE)
        entry8 = xfl.fl_add_nmenu_items2(self.pmenu1, ppopmenu5)

        MypopupitemF = ["Ninth item ADD", self.item1_cb, "F", \
                xfl.FL_POPUP_NORMAL, xfl.FL_POPUP_NONE], \
                ["Tenth item ADD", self.item2_cb, "E", \
                xfl.FL_POPUP_NORMAL, xfl.FL_POPUP_NONE]

        ppopmenu6 = libr.create_pPopupItem_from_list(MypopupitemF)
        entry910 = xfl.fl_add_nmenu_items2(self.pmenu2, ppopmenu6)

        # currently dict is *only* for 1 item
        MypopupitemG = {'text' : "Eleventh item INS", \
                'callback' : self.item3_cb, 'shortcut' : "T", \
                'type' : xfl.FL_POPUP_NORMAL, 'state' : xfl.FL_POPUP_NONE}

        ppopmenu7 = libr.create_pPopupItem_from_dict(MypopupitemG)
        entry910 = xfl.fl_insert_nmenu_items2(self.pmenu2, entry910, ppopmenu7)

        xfl.fl_show_form(pform, xfl.FL_PLACE_CENTER, xfl.FL_TRANSIENT, "Nmenu")

        while xfl.fl_do_forms():
            pass


    def create_form(self):

        pform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 444, 380)

        pobj = xfl.fl_add_box(xfl.FL_BORDER_BOX, 0, 0, 444, 380, "")
        xfl.fl_set_object_color(pobj, xfl.FL_SLATEBLUE, xfl.FL_COL1)
        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 444, 29, "")
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_COL1)
        self.pmenu1 = xfl.fl_add_nmenu(xfl.FL_NORMAL_NMENU, 2, 2, \
                110, 25, "Menu 1")
        xfl.fl_set_object_shortcut(self.pmenu1, "1#1", 1)
        self.pmenu2 = xfl.fl_add_nmenu(xfl.FL_NORMAL_NMENU, 102, 2, \
                110, 25, "Menu 2")
        xfl.fl_set_object_shortcut(self.pmenu2, "2#2", 2)

        xfl.fl_end_form()

        return pform


    def item1_cb(self, r):
        print "choice 1 added", xfl.fl_get_nmenu_item_by_value(self.pmenu1, 1)
        return 0

    def item2_cb(self, r):
        print "choice 2 added", xfl.fl_get_nmenu_item_by_value(self.pmenu1, 2)
        return 0

    def item3_cb(self, r):
        print "choice 3 inserted", \
                xfl.fl_get_nmenu_item_by_value(self.pmenu1, 3)
        return 0

    def item4_cb(self, r):
        print "choice 4 inserted", \
                xfl.fl_get_nmenu_item_by_value(self.pmenu1, 4)
        return 0

    def item5_cb(self, r):
        print "choice 5 added", xfl.fl_get_nmenu_item_by_value(self.pmenu1, 5)
        return 0

    def item6_cb(self, r):
        print "choice 6 replace for choice 1", \
                xfl.fl_get_nmenu_item_by_value(self.pmenu1, 6)
        return 0

    def item7_cb(self, r):
        print "choice 7 replace for choice 2", \
                xfl.fl_get_nmenu_item_by_value(self.pmenu1, 7)
        return 0

    def done_cb(self, r):
        xfl.fl_finish()
        sys.exit(0)

    def item9_cb(self, r):
        print "choice 9 added", xfl.fl_get_nmenu_item_by_value(self.pmenu2, 9)
        return 0

    def item10_cb(self, r):
        print "choice 10 added", \
                xfl.fl_get_nmenu_item_by_value(self.pmenu2, 10)
        return 0

    def item11_cb(self, r):
        print "Choice 11 added", \
                xfl.fl_get_nmenu_item_by_value(self.pmenu2, 11)
        return 0

    def item12_cb(self, r):
        print "Choice 12 inserted", \
                xfl.fl_get_nmenu_item_by_value(self.pmenu2, 12)
        return 0



if __name__ == '__main__':
    Flnmenumin(len(sys.argv), sys.argv)
