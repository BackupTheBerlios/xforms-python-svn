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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flnmenu import *
from xformslib.flpopup import *
from xformslib.flmisc import *
from xformslib.flbutton import *
from xformslib.xfdata import *



#pmenu1 = pmenu2 = pmenu3 = pmenu4 = None



class Flnmenu(object):
    def __init__(self, lsysargv, sysargv):

        self.pabox = [None, None, None, None]
        self.set = [0, 0, 0, 0]
        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        pform = self.create_form()

        self.add_items_to_menu1()
        fl_popup_entry_set_state(fl_get_nmenu_item_by_value(self.pmenu1, 0), FL_POPUP_CHECKED)
        self.set[0] = 0
        fl_set_object_color(self.pabox[0], FL_RED + self.set[0], FL_BLACK)

        self.add_items_to_menu2()
        fl_popup_entry_set_state(fl_get_nmenu_item_by_value(self.pmenu2, 1), FL_POPUP_CHECKED)
        self.set[1] = 1
        fl_set_object_color(self.pabox[1], FL_RED + self.set[1], FL_BLACK)

        self.add_items_to_menu3()
        fl_popup_entry_set_state(fl_get_nmenu_item_by_value(self.pmenu3, 2), FL_POPUP_CHECKED)
        self.set[2] = 2
        fl_set_object_color(self.pabox[2], FL_RED + self.set[2], FL_BLACK)

        self.add_items_to_menu4()
        fl_popup_entry_set_state(fl_get_nmenu_item_by_value(self.pmenu4, 3), FL_POPUP_CHECKED)
        self.set[3] = 3
        fl_set_object_color(self.pabox[3], FL_RED + self.set[3], FL_BLACK)

        fl_show_form(pform, FL_PLACE_CENTER, FL_TRANSIENT, "Nmenu")

        fl_do_forms()
        fl_hide_form(pform)

        fl_finish()


    def create_form(self):

        pform = fl_bgn_form(FL_NO_BOX, 444, 380)

        pobj = fl_add_box(FL_BORDER_BOX, 0, 0, 444, 380, "")
        fl_set_object_color(pobj, FL_SLATEBLUE, FL_COL1)

        pobj = fl_add_box(FL_UP_BOX, 0, 0, 444, 29, "")
        fl_set_object_color(pobj, FL_COL1, FL_COL1)

        self.pmenu1 = fl_add_nmenu(FL_NORMAL_NMENU, 2, 2, 110, 25, "Color 1")
        fl_set_object_shortcut(self.pmenu1, "1#1", 1)
        fl_set_object_callback(self.pmenu1, self.menu_cb, 0)

        self.pmenu2 = fl_add_nmenu(FL_NORMAL_TOUCH_NMENU, 112, 2, 110, 25,
                                      "Color 2")
        fl_set_object_shortcut(self.pmenu2, "2#2", 1)
        fl_set_object_callback(self.pmenu2, self.menu_cb, 1)

        self.pmenu3 = fl_add_nmenu(FL_BUTTON_NMENU, 222, 2, 110, 25, "Color 3")
        fl_set_object_shortcut(self.pmenu3, "3#3", 1)
        fl_set_object_callback(self.pmenu3, self.menu_cb, 2)

        self.pmenu4 = fl_add_nmenu(FL_BUTTON_TOUCH_NMENU, 332, 2, 110, 25,
                                      "Color 4")
        fl_set_object_shortcut(self.pmenu4, "4#4", 1)
        fl_set_object_callback(self.pmenu4, self.menu_cb, 3)

        self.pabox[0] = fl_add_box(FL_SHADOW_BOX,  20, 80, 70, 230, "")
        self.pabox[1] = fl_add_box(FL_SHADOW_BOX, 130, 80, 70, 230, "")
        self.pabox[2] = fl_add_box(FL_SHADOW_BOX, 240, 80, 70, 230, "")
        self.pabox[3] = fl_add_box(FL_SHADOW_BOX, 350, 80, 70, 230, "")

        pobj = fl_add_button(FL_NORMAL_BUTTON, 310, 330, 110, 30, "Quit")
        fl_set_object_shortcut(pobj, "Q#Q", 1)
        fl_set_object_callback(pobj, self.done_cb, 0)

        fl_end_form()

        return pform


    def add_items_to_menu1(self):

        pitem1menu1 = fl_add_nmenu_items(self.pmenu1, "Red%SR")
        pitem1menu1.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem1menu1, "Rr#R#r")
        fl_popup_entry_set_state(pitem1menu1, FL_POPUP_DISABLED)

        pitem2menu1 = fl_insert_nmenu_items(self.pmenu1, pitem1menu1, "Green%SG")
        pitem2menu1.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem2menu1, "Gg#G#g")
        fl_popup_entry_set_state(pitem2menu1, FL_POPUP_DISABLED)

        pitem3menu1 = fl_insert_nmenu_items(self.pmenu1, pitem2menu1, "Yellow%SY")
        pitem3menu1.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem3menu1, "Yy#Y#y")
        fl_popup_entry_set_state(pitem3menu1, FL_POPUP_DISABLED)

        pitem4menu1 = fl_insert_nmenu_items(self.pmenu1, pitem3menu1, "Blue%SB")
        pitem4menu1.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem4menu1, "Bb#B#b")
        fl_popup_entry_set_state(pitem4menu1, FL_POPUP_DISABLED)

        pitem5menu1 = fl_insert_nmenu_items(self.pmenu1, pitem4menu1, "Purple%SP")
        pitem5menu1.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem5menu1, "Pp#P#p")
        fl_popup_entry_set_state(pitem5menu1, FL_POPUP_NONE)

        pitem6menu1 = fl_insert_nmenu_items(self.pmenu1, pitem5menu1, "Cyan%SC")
        pitem6menu1.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem6menu1, "Cc#C#c")
        fl_popup_entry_set_state(pitem6menu1, FL_POPUP_NONE)

        pitem7menu1 = fl_insert_nmenu_items(self.pmenu1, pitem6menu1, "White%SW")
        pitem7menu1.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem7menu1, "Ww#W#w")
        fl_popup_entry_set_state(pitem7menu1, FL_POPUP_NONE)


    def add_items_to_menu2(self):

        pitem1menu2 = fl_add_nmenu_items(self.pmenu2, "Red%SR")
        pitem1menu2.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem1menu2, "Rr#R#r")
        fl_popup_entry_set_state(pitem1menu2, FL_POPUP_DISABLED)

        pitem2menu2 = fl_insert_nmenu_items(self.pmenu2, pitem1menu2, "Green%SG")
        pitem2menu2.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem2menu2, "Gg#G#g")
        fl_popup_entry_set_state(pitem2menu2, FL_POPUP_DISABLED)

        pitem3menu2 = fl_insert_nmenu_items(self.pmenu2, pitem2menu2, "Yellow%SY")
        pitem3menu2.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem3menu2, "Yy#Y#y")
        fl_popup_entry_set_state(pitem3menu2, FL_POPUP_DISABLED)

        pitem4menu2 = fl_insert_nmenu_items(self.pmenu2, pitem3menu2, "Blue%SB")
        pitem4menu2.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem4menu2, "Bb#B#b")
        fl_popup_entry_set_state(pitem4menu2, FL_POPUP_DISABLED)

        pitem5menu2 = fl_insert_nmenu_items(self.pmenu2, pitem4menu2, "Purple%SP")
        pitem5menu2.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem5menu2, "Pp#P#p")
        fl_popup_entry_set_state(pitem5menu2, FL_POPUP_NONE)

        pitem6menu2 = fl_insert_nmenu_items(self.pmenu2, pitem5menu2, "Cyan%SC")
        pitem6menu2.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem6menu2, "Cc#C#c")
        fl_popup_entry_set_state(pitem6menu2, FL_POPUP_NONE)

        pitem7menu2 = fl_insert_nmenu_items(self.pmenu2, pitem6menu2, "White%SW")
        pitem7menu2.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem7menu2, "Ww#W#w")
        fl_popup_entry_set_state(pitem7menu2, FL_POPUP_NONE)


    def add_items_to_menu3(self):

        pitem1menu3 = fl_add_nmenu_items(self.pmenu3, "Red%SR")
        pitem1menu3.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem1menu3, "Rr#R#r")
        fl_popup_entry_set_state(pitem1menu3, FL_POPUP_DISABLED)

        pitem2menu3 = fl_insert_nmenu_items(self.pmenu3, pitem1menu3, "Green%SG")
        pitem2menu3.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem2menu3, "Gg#G#g")
        fl_popup_entry_set_state(pitem2menu3, FL_POPUP_DISABLED)

        pitem3menu3 = fl_insert_nmenu_items(self.pmenu3, pitem2menu3, "Yellow%SY")
        pitem3menu3.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem3menu3, "Yy#Y#y")
        fl_popup_entry_set_state(pitem3menu3, FL_POPUP_DISABLED)

        pitem4menu3 = fl_insert_nmenu_items(self.pmenu3, pitem3menu3, "Blue%SB")
        pitem4menu3.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem4menu3, "Bb#B#b")
        fl_popup_entry_set_state(pitem4menu3, FL_POPUP_DISABLED)

        pitem5menu3 = fl_insert_nmenu_items(self.pmenu3, pitem4menu3, "Purple%SP")
        pitem5menu3.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem5menu3, "Pp#P#p")
        fl_popup_entry_set_state(pitem5menu3, FL_POPUP_NONE)

        pitem6menu3 = fl_insert_nmenu_items(self.pmenu3, pitem5menu3, "Cyan%SC")
        pitem6menu3.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem6menu3, "Cc#C#c")
        fl_popup_entry_set_state(pitem6menu3, FL_POPUP_NONE)

        pitem7menu3 = fl_insert_nmenu_items(self.pmenu3, pitem6menu3, "White%SW")
        pitem7menu3.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem7menu3, "Ww#W#w")
        fl_popup_entry_set_state(pitem7menu3, FL_POPUP_NONE)


    def add_items_to_menu4(self):

        pitem1menu4 = fl_add_nmenu_items(self.pmenu4, "Red%SR")
        pitem1menu4.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem1menu4, "Rr#R#r")
        fl_popup_entry_set_state(pitem1menu4, FL_POPUP_DISABLED)

        pitem2menu4 = fl_insert_nmenu_items(self.pmenu4, pitem1menu4, "Green%SG")
        pitem2menu4.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem2menu4, "Gg#G#g")
        fl_popup_entry_set_state(pitem2menu4, FL_POPUP_DISABLED)

        pitem3menu4 = fl_insert_nmenu_items(self.pmenu4, pitem2menu4, "Yellow%SY")
        pitem3menu4.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem3menu4, "Yy#Y#y")
        fl_popup_entry_set_state(pitem3menu4, FL_POPUP_DISABLED)

        pitem4menu4 = fl_insert_nmenu_items(self.pmenu4, pitem3menu4, "Blue%SB")
        pitem4menu4.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem4menu4, "Bb#B#b")
        fl_popup_entry_set_state(pitem4menu4, FL_POPUP_DISABLED)

        pitem5menu4 = fl_insert_nmenu_items(self.pmenu4, pitem4menu4, "Purple%SP")
        pitem5menu4.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem5menu4, "Pp#P#p")
        fl_popup_entry_set_state(pitem5menu4, FL_POPUP_NONE)

        pitem6menu4 = fl_insert_nmenu_items(self.pmenu4, pitem5menu4, "Cyan%SC")
        pitem6menu4.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem6menu4, "Cc#C#c")
        fl_popup_entry_set_state(pitem6menu4, FL_POPUP_NONE)

        pitem7menu4 = fl_insert_nmenu_items(self.pmenu4, pitem6menu4, "White%SW")
        pitem7menu4.contents.type = FL_POPUP_RADIO
        fl_popup_entry_set_shortcut(pitem7menu4, "Ww#W#w")
        fl_popup_entry_set_state(pitem7menu4, FL_POPUP_NONE)


    def menu_cb(self, pobj, m):
        # m is the menu index 0 - 3
        pr = fl_get_nmenu_item(pobj)
        if self.set[m] == pr.contents.val:
            return

        if m == 0:
            # enable the old selected color for other menus
            fl_popup_entry_set_state(fl_get_nmenu_item_by_value(self.pmenu1, \
                                     self.set[m]), FL_POPUP_NONE)
            # disable the currently selected color for other menus
            fl_popup_entry_set_state(fl_get_nmenu_item_by_value(self.pmenu1, \
                                     pr.contents.val), FL_POPUP_DISABLED)
        elif m == 1:
            fl_popup_entry_set_state(fl_get_nmenu_item_by_value(self.pmenu2, \
                                     self.set[m]), FL_POPUP_NONE)
            fl_popup_entry_set_state(fl_get_nmenu_item_by_value(self.pmenu2, \
                                     pr.contents.val), FL_POPUP_DISABLED)
        elif m == 2:
            fl_popup_entry_set_state(fl_get_nmenu_item_by_value(self.pmenu3, \
                                     self.set[m]), FL_POPUP_NONE)
            fl_popup_entry_set_state(fl_get_nmenu_item_by_value(self.pmenu3, \
                                     pr.contents.val), FL_POPUP_DISABLED)
        elif m == 3:
            fl_popup_entry_set_state(fl_get_nmenu_item_by_value(self.pmenu4, \
                                     self.set[m]), FL_POPUP_NONE)
            fl_popup_entry_set_state(fl_get_nmenu_item_by_value(self.pmenu4, \
                                     pr.contents.val), FL_POPUP_DISABLED)

        self.set[m] = pr.contents.val
        fl_set_object_color(self.pabox[m], FL_RED + pr.contents.val, FL_BLACK)


    def done_cb(self, pobj, data):
        fl_finish()
        sys.exit(0)





if __name__ == '__main__':
    Flnmenu(len(sys.argv), sys.argv)

