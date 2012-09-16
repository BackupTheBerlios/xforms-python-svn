#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  nmenu.c XForms demo, with some adaptations and modifications.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of all four types of nmenu's.
#

import sys
#sys.path.append("..")
import xformslib as xfl

#pmenu1 = pmenu2 = pmenu3 = pmenu4 = None

class Flnmenu(object):
    def __init__(self, lsysargv, sysargv):
        self.pabox = [None] * 4
        self.set = [0] * 4
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        pform = self.create_form()
        self.add_items_to_menu1()
        xfl.fl_popup_entry_set_state(xfl.fl_get_nmenu_item_by_value( \
                self.pmenu1, 0), xfl.FL_POPUP_CHECKED)
        self.set[0] = 0
        xfl.fl_set_object_color(self.pabox[0], xfl.FL_RED + self.set[0], \
                xfl.FL_BLACK)
        self.add_items_to_menu2()
        xfl.fl_popup_entry_set_state(xfl.fl_get_nmenu_item_by_value( \
                self.pmenu2, 1), xfl.FL_POPUP_CHECKED)
        self.set[1] = 1
        xfl.fl_set_object_color(self.pabox[1], xfl.FL_RED + self.set[1], \
                xfl.FL_BLACK)
        self.add_items_to_menu3()
        xfl.fl_popup_entry_set_state(xfl.fl_get_nmenu_item_by_value( \
                self.pmenu3, 2), xfl.FL_POPUP_CHECKED)
        self.set[2] = 2
        xfl.fl_set_object_color(self.pabox[2], xfl.FL_RED + self.set[2], \
                xfl.FL_BLACK)
        self.add_items_to_menu4()
        xfl.fl_popup_entry_set_state(xfl.fl_get_nmenu_item_by_value( \
                self.pmenu4, 3), xfl.FL_POPUP_CHECKED)
        self.set[3] = 3
        xfl.fl_set_object_color(self.pabox[3], xfl.FL_RED + self.set[3], \
                xfl.FL_BLACK)
        xfl.fl_show_form(pform, xfl.FL_PLACE_CENTER, xfl.FL_TRANSIENT, "Nmenu")
        xfl.fl_do_forms()
        xfl.fl_hide_form(pform)
        xfl.fl_finish()


    def create_form(self):
        pform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 444, 380)
        pobj = xfl.fl_add_box(xfl.FL_BORDER_BOX, 0, 0, 444, 380, "")
        xfl.fl_set_object_color(pobj, xfl.FL_SLATEBLUE, xfl.FL_COL1)
        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 444, 29, "")
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_COL1)
        self.pmenu1 = xfl.fl_add_nmenu(xfl.FL_NORMAL_NMENU, 2, 2, \
                110, 25, "Color 1")
        xfl.fl_set_object_shortcut(self.pmenu1, "1#1", 1)
        xfl.fl_set_object_callback(self.pmenu1, self.menu_cb, 0)
        self.pmenu2 = xfl.fl_add_nmenu(xfl.FL_NORMAL_TOUCH_NMENU, 112, 2, \
                110, 25, "Color 2")
        xfl.fl_set_object_shortcut(self.pmenu2, "2#2", 1)
        xfl.fl_set_object_callback(self.pmenu2, self.menu_cb, 1)
        self.pmenu3 = xfl.fl_add_nmenu(xfl.FL_BUTTON_NMENU, 222, 2, \
                110, 25, "Color 3")
        xfl.fl_set_object_shortcut(self.pmenu3, "3#3", 1)
        xfl.fl_set_object_callback(self.pmenu3, self.menu_cb, 2)
        self.pmenu4 = xfl.fl_add_nmenu(xfl.FL_BUTTON_TOUCH_NMENU, 332, 2, \
                110, 25, "Color 4")
        xfl.fl_set_object_shortcut(self.pmenu4, "4#4", 1)
        xfl.fl_set_object_callback(self.pmenu4, self.menu_cb, 3)
        self.pabox[0] = xfl.fl_add_box(xfl.FL_SHADOW_BOX,  20, 80, 70, 230, "")
        self.pabox[1] = xfl.fl_add_box(xfl.FL_SHADOW_BOX, 130, 80, 70, 230, "")
        self.pabox[2] = xfl.fl_add_box(xfl.FL_SHADOW_BOX, 240, 80, 70, 230, "")
        self.pabox[3] = xfl.fl_add_box(xfl.FL_SHADOW_BOX, 350, 80, 70, 230, "")
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 310, 330, \
                110, 30, "Quit")
        xfl.fl_set_object_shortcut(pobj, "Q#Q", 1)
        xfl.fl_set_object_callback(pobj, self.done_cb, 0)
        xfl.fl_end_form()
        return pform


    def add_items_to_menu1(self):
        pitem1menu1 = xfl.fl_add_nmenu_items(self.pmenu1, "Red%SR")
        pitem1menu1.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem1menu1, "Rr#R#r")
        xfl.fl_popup_entry_set_state(pitem1menu1, xfl.FL_POPUP_DISABLED)
        pitem2menu1 = xfl.fl_insert_nmenu_items(self.pmenu1, pitem1menu1, \
                "Green%SG")
        pitem2menu1.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem2menu1, "Gg#G#g")
        xfl.fl_popup_entry_set_state(pitem2menu1, xfl.FL_POPUP_DISABLED)
        pitem3menu1 = xfl.fl_insert_nmenu_items(self.pmenu1, pitem2menu1, \
                "Yellow%SY")
        pitem3menu1.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem3menu1, "Yy#Y#y")
        xfl.fl_popup_entry_set_state(pitem3menu1, xfl.FL_POPUP_DISABLED)
        pitem4menu1 = xfl.fl_insert_nmenu_items(self.pmenu1, pitem3menu1, \
                "Blue%SB")
        pitem4menu1.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem4menu1, "Bb#B#b")
        xfl.fl_popup_entry_set_state(pitem4menu1, xfl.FL_POPUP_DISABLED)
        pitem5menu1 = xfl.fl_insert_nmenu_items(self.pmenu1, pitem4menu1, \
                "Purple%SP")
        pitem5menu1.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem5menu1, "Pp#P#p")
        xfl.fl_popup_entry_set_state(pitem5menu1, xfl.FL_POPUP_NONE)
        pitem6menu1 = xfl.fl_insert_nmenu_items(self.pmenu1, pitem5menu1, \
                "Cyan%SC")
        pitem6menu1.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem6menu1, "Cc#C#c")
        xfl.fl_popup_entry_set_state(pitem6menu1, xfl.FL_POPUP_NONE)
        pitem7menu1 = xfl.fl_insert_nmenu_items(self.pmenu1, pitem6menu1, \
                "White%SW")
        pitem7menu1.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem7menu1, "Ww#W#w")
        xfl.fl_popup_entry_set_state(pitem7menu1, xfl.FL_POPUP_NONE)


    def add_items_to_menu2(self):
        pitem1menu2 = xfl.fl_add_nmenu_items(self.pmenu2, "Red%SR")
        pitem1menu2.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem1menu2, "Rr#R#r")
        xfl.fl_popup_entry_set_state(pitem1menu2, xfl.FL_POPUP_DISABLED)
        pitem2menu2 = xfl.fl_insert_nmenu_items(self.pmenu2, pitem1menu2, \
                "Green%SG")
        pitem2menu2.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem2menu2, "Gg#G#g")
        xfl.fl_popup_entry_set_state(pitem2menu2, xfl.FL_POPUP_DISABLED)
        pitem3menu2 = xfl.fl_insert_nmenu_items(self.pmenu2, pitem2menu2, \
                "Yellow%SY")
        pitem3menu2.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem3menu2, "Yy#Y#y")
        xfl.fl_popup_entry_set_state(pitem3menu2, xfl.FL_POPUP_DISABLED)
        pitem4menu2 = xfl.fl_insert_nmenu_items(self.pmenu2, pitem3menu2, \
                "Blue%SB")
        pitem4menu2.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem4menu2, "Bb#B#b")
        xfl.fl_popup_entry_set_state(pitem4menu2, xfl.FL_POPUP_DISABLED)
        pitem5menu2 = xfl.fl_insert_nmenu_items(self.pmenu2, pitem4menu2, \
                "Purple%SP")
        pitem5menu2.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem5menu2, "Pp#P#p")
        xfl.fl_popup_entry_set_state(pitem5menu2, xfl.FL_POPUP_NONE)
        pitem6menu2 = xfl.fl_insert_nmenu_items(self.pmenu2, pitem5menu2, \
                "Cyan%SC")
        pitem6menu2.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem6menu2, "Cc#C#c")
        xfl.fl_popup_entry_set_state(pitem6menu2, xfl.FL_POPUP_NONE)
        pitem7menu2 = xfl.fl_insert_nmenu_items(self.pmenu2, pitem6menu2, \
                "White%SW")
        pitem7menu2.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem7menu2, "Ww#W#w")
        xfl.fl_popup_entry_set_state(pitem7menu2, xfl.FL_POPUP_NONE)


    def add_items_to_menu3(self):
        pitem1menu3 = xfl.fl_add_nmenu_items(self.pmenu3, "Red%SR")
        pitem1menu3.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem1menu3, "Rr#R#r")
        xfl.fl_popup_entry_set_state(pitem1menu3, xfl.FL_POPUP_DISABLED)
        pitem2menu3 = xfl.fl_insert_nmenu_items(self.pmenu3, pitem1menu3, \
                "Green%SG")
        pitem2menu3.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem2menu3, "Gg#G#g")
        xfl.fl_popup_entry_set_state(pitem2menu3, xfl.FL_POPUP_DISABLED)
        pitem3menu3 = xfl.fl_insert_nmenu_items(self.pmenu3, pitem2menu3, \
                "Yellow%SY")
        pitem3menu3.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem3menu3, "Yy#Y#y")
        xfl.fl_popup_entry_set_state(pitem3menu3, xfl.FL_POPUP_DISABLED)
        pitem4menu3 = xfl.fl_insert_nmenu_items(self.pmenu3, pitem3menu3, \
                "Blue%SB")
        pitem4menu3.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem4menu3, "Bb#B#b")
        xfl.fl_popup_entry_set_state(pitem4menu3, xfl.FL_POPUP_DISABLED)
        pitem5menu3 = xfl.fl_insert_nmenu_items(self.pmenu3, pitem4menu3, \
                "Purple%SP")
        pitem5menu3.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem5menu3, "Pp#P#p")
        xfl.fl_popup_entry_set_state(pitem5menu3, xfl.FL_POPUP_NONE)
        pitem6menu3 = xfl.fl_insert_nmenu_items(self.pmenu3, pitem5menu3, \
                "Cyan%SC")
        pitem6menu3.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem6menu3, "Cc#C#c")
        xfl.fl_popup_entry_set_state(pitem6menu3, xfl.FL_POPUP_NONE)
        pitem7menu3 = xfl.fl_insert_nmenu_items(self.pmenu3, pitem6menu3, \
                "White%SW")
        pitem7menu3.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem7menu3, "Ww#W#w")
        xfl.fl_popup_entry_set_state(pitem7menu3, xfl.FL_POPUP_NONE)


    def add_items_to_menu4(self):
        pitem1menu4 = xfl.fl_add_nmenu_items(self.pmenu4, "Red%SR")
        pitem1menu4.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem1menu4, "Rr#R#r")
        xfl.fl_popup_entry_set_state(pitem1menu4, xfl.FL_POPUP_DISABLED)
        pitem2menu4 = xfl.fl_insert_nmenu_items(self.pmenu4, pitem1menu4, \
                "Green%SG")
        pitem2menu4.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem2menu4, "Gg#G#g")
        xfl.fl_popup_entry_set_state(pitem2menu4, xfl.FL_POPUP_DISABLED)
        pitem3menu4 = xfl.fl_insert_nmenu_items(self.pmenu4, pitem2menu4, \
                "Yellow%SY")
        pitem3menu4.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem3menu4, "Yy#Y#y")
        xfl.fl_popup_entry_set_state(pitem3menu4, xfl.FL_POPUP_DISABLED)
        pitem4menu4 = xfl.fl_insert_nmenu_items(self.pmenu4, pitem3menu4, \
                "Blue%SB")
        pitem4menu4.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem4menu4, "Bb#B#b")
        xfl.fl_popup_entry_set_state(pitem4menu4, xfl.FL_POPUP_DISABLED)
        pitem5menu4 = xfl.fl_insert_nmenu_items(self.pmenu4, pitem4menu4, \
                "Purple%SP")
        pitem5menu4.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem5menu4, "Pp#P#p")
        xfl.fl_popup_entry_set_state(pitem5menu4, xfl.FL_POPUP_NONE)
        pitem6menu4 = xfl.fl_insert_nmenu_items(self.pmenu4, pitem5menu4, \
                "Cyan%SC")
        pitem6menu4.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem6menu4, "Cc#C#c")
        xfl.fl_popup_entry_set_state(pitem6menu4, xfl.FL_POPUP_NONE)
        pitem7menu4 = xfl.fl_insert_nmenu_items(self.pmenu4, pitem6menu4, \
                "White%SW")
        pitem7menu4.contents.type = xfl.FL_POPUP_RADIO
        xfl.fl_popup_entry_set_shortcut(pitem7menu4, "Ww#W#w")
        xfl.fl_popup_entry_set_state(pitem7menu4, xfl.FL_POPUP_NONE)


    def menu_cb(self, pobj, m):
        # m is the menu index 0 - 3
        pr = xfl.fl_get_nmenu_item(pobj)
        if self.set[m] == pr.contents.val:
            return
        if m == 0:
            # enable the old selected color for other menus
            xfl.fl_popup_entry_set_state(xfl.fl_get_nmenu_item_by_value( \
                    self.pmenu1,  self.set[m]), xfl.FL_POPUP_NONE)
            # disable the currently selected color for other menus
            xfl.fl_popup_entry_set_state(xfl.fl_get_nmenu_item_by_value( \
                    self.pmenu1, pr.contents.val), xfl.FL_POPUP_DISABLED)
        elif m == 1:
            xfl.fl_popup_entry_set_state(xfl.fl_get_nmenu_item_by_value( \
                    self.pmenu2, self.set[m]), xfl.FL_POPUP_NONE)
            xfl.fl_popup_entry_set_state(xfl.fl_get_nmenu_item_by_value( \
                    self.pmenu2, pr.contents.val), xfl.FL_POPUP_DISABLED)
        elif m == 2:
            xfl.fl_popup_entry_set_state(xfl.fl_get_nmenu_item_by_value( \
                    self.pmenu3, self.set[m]), xfl.FL_POPUP_NONE)
            xfl.fl_popup_entry_set_state(xfl.fl_get_nmenu_item_by_value( \
                    self.pmenu3, pr.contents.val), xfl.FL_POPUP_DISABLED)
        elif m == 3:
            xfl.fl_popup_entry_set_state(xfl.fl_get_nmenu_item_by_value( \
                    self.pmenu4, self.set[m]), xfl.FL_POPUP_NONE)
            xfl.fl_popup_entry_set_state(xfl.fl_get_nmenu_item_by_value( \
                    self.pmenu4, pr.contents.val), xfl.FL_POPUP_DISABLED)
        self.set[m] = pr.contents.val
        xfl.fl_set_object_color(self.pabox[m], xfl.FL_RED + pr.contents.val, \
                xfl.FL_BLACK)


    def done_cb(self, pobj, data):
        xfl.fl_finish()
        sys.exit(0)


if __name__ == '__main__':
    print ("********* nmenu.py *********")
    Flnmenu(len(sys.argv), sys.argv)
