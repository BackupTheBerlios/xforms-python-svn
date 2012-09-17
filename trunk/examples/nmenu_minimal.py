#!/usr/bin/env python3

#  This file is part of xforms-python, and it is a variant of nmenu
#  to show some xfl.fl_*_nmenu_items2 functions.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#

import sys
#sys.path.append("..")
import xformslib as xfl


class Flnmenumin(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        pform = self.create_form()
        MypopupitemA = \
                [{'text' : "First item ADD", 'callback' : self.item1_cb, \
                'shortcut' : "F", 'type' : xfl.FL_POPUP_NORMAL, \
                'state' : xfl.FL_POPUP_NONE}, \
                {'text' : "Second item ADD", 'callback' : self.item2_cb, \
                'shortcut' : "n", 'type' : xfl.FL_POPUP_NORMAL, \
                'state' : xfl.FL_POPUP_NONE}]
        ppopmenu1 = xfl.fls_make_ptr_flpopupitem(MypopupitemA)
        entry12 = xfl.fl_add_nmenu_items2(self.pmenu1, ppopmenu1)
        MypopupitemB = \
                [{'text' : "Third item INS", 'callback' : self.item3_cb, \
                'shortcut' : "r", 'type' : xfl.FL_POPUP_NORMAL, \
                'state' : xfl.FL_POPUP_NONE}, \
                {'text' : "Fourth item INS", 'callback' : self.item4_cb, \
                'shortcut' : "h", 'type' : xfl.FL_POPUP_NORMAL, \
                'state' : xfl.FL_POPUP_NONE}]
        ppopmenu2 = xfl.fls_make_ptr_flpopupitem(MypopupitemB)
        entry34 = xfl.fl_insert_nmenu_items2(self.pmenu1, None, ppopmenu2)
        MypopupitemC = {'text' : "Fifth item ADD", 'callback' : self.item5_cb,
                'shortcut' : "f", 'type' : xfl.FL_POPUP_NORMAL,
                'state' : xfl.FL_POPUP_NONE}
        ppopmenu3 = xfl.fls_make_ptr_flpopupitem(MypopupitemC)
        entry5 = xfl.fl_add_nmenu_items2(self.pmenu1, ppopmenu3)
        MypopupitemD = \
                [{'text' : "Sixth item REPL", 'callback' : self.item6_cb, \
                'shortcut' : "S", 'type' : xfl.FL_POPUP_NORMAL, \
                'state' : xfl.FL_POPUP_NONE}, \
                {'text' : "Seventh menu REPL", 'callback' : self.item7_cb, \
                'shortcut' : "v", 'type' : xfl.FL_POPUP_NORMAL, \
                'state' : xfl.FL_POPUP_NONE}]
        ppopmenu4 = xfl.fls_make_ptr_flpopupitem(MypopupitemD)
        entry67 = xfl.fl_replace_nmenu_items2(self.pmenu1, entry12, ppopmenu4)
        MypopupitemE = {'text' : "Exit ADD", 'callback' : self.done_cb, \
                'shortcut' : "x", 'type' : xfl.FL_POPUP_NORMAL, \
                'state' : xfl.FL_POPUP_NONE}
        ppopmenu5 = xfl.fls_make_ptr_flpopupitem(MypopupitemE)
        entry8 = xfl.fl_add_nmenu_items2(self.pmenu1, ppopmenu5)
        MypopupitemF = \
                [{'text' : "Ninth item ADD", 'callback' : self.item1_cb, \
                'shortcut' : "N", 'type' : xfl.FL_POPUP_NORMAL, \
                'state' : xfl.FL_POPUP_NONE}, \
                {'text' : "Tenth item ADD", 'callback' : self.item2_cb, \
                'shortcut' : "T", 'type' : xfl.FL_POPUP_NORMAL, \
                'state' : xfl.FL_POPUP_NONE}]
        ppopmenu6 = xfl.fls_make_ptr_flpopupitem(MypopupitemF)
        entry910 = xfl.fl_add_nmenu_items2(self.pmenu2, ppopmenu6)
        MypopupitemG = {'text' : "Eleventh item INS", \
                'callback' : self.item3_cb, 'shortcut' : "E", \
                'type' : xfl.FL_POPUP_NORMAL, 'state' : xfl.FL_POPUP_NONE}
        ppopmenu7 = xfl.fls_make_ptr_flpopupitem(MypopupitemG)
        entry910 = xfl.fl_insert_nmenu_items2(self.pmenu2, entry910, \
                ppopmenu7)
        xfl.fl_show_form(pform, xfl.FL_PLACE_CENTER, xfl.FL_TRANSIENT, \
                "Nmenu")
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
        xfl.fl_set_object_shortcut(self.pmenu2, "2#2", 1)
        xfl.fl_end_form()
        return pform


    def item1_cb(self, r):
        print("choice 1 added", xfl.fl_get_nmenu_item_by_value( \
                self.pmenu1, 1))
        return 0


    def item2_cb(self, r):
        print("choice 2 added", xfl.fl_get_nmenu_item_by_value( \
                self.pmenu1, 2))
        return 0


    def item3_cb(self, r):
        print("choice 3 inserted", \
                xfl.fl_get_nmenu_item_by_value(self.pmenu1, 3))
        return 0


    def item4_cb(self, r):
        print("choice 4 inserted", \
                xfl.fl_get_nmenu_item_by_value(self.pmenu1, 4))
        return 0


    def item5_cb(self, r):
        print("choice 5 added", xfl.fl_get_nmenu_item_by_value(self.pmenu1, 5))
        return 0


    def item6_cb(self, r):
        print("choice 6 replace for choice 1", \
                xfl.fl_get_nmenu_item_by_value(self.pmenu1, 6))
        return 0


    def item7_cb(self, r):
        print("choice 7 replace for choice 2", \
                xfl.fl_get_nmenu_item_by_value(self.pmenu1, 7))
        return 0


    def done_cb(self, r):
        xfl.fl_finish()
        sys.exit(0)


    def item9_cb(self, r):
        print("choice 9 added", xfl.fl_get_nmenu_item_by_value( \
                self.pmenu2, 9))
        return 0


    def item10_cb(self, r):
        print("choice 10 added", \
                xfl.fl_get_nmenu_item_by_value(self.pmenu2, 10))
        return 0


    def item11_cb(self, r):
        print("Choice 11 added", \
                xfl.fl_get_nmenu_item_by_value(self.pmenu2, 11))
        return 0


    def item12_cb(self, r):
        print("Choice 12 inserted", \
                xfl.fl_get_nmenu_item_by_value(self.pmenu2, 12))
        return 0


if __name__ == '__main__':
    print ("********* nmenu_minimal.py *********")
    Flnmenumin(len(sys.argv), sys.argv)
