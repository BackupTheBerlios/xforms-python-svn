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
from xformslib import library as xf
from xformslib import xfdata as xfc


pmenu1 = pmenu2 = pmenu3 = pmenu4 = None
pabox = [None, None, None, None]
set = [0, 0, 0, 0]



def add_items_to_menu1():

    pitem1menu1 = xf.fl_add_nmenu_items(pmenu1, "Red%SR")
    pitem1menu1.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem1menu1, "Rr#R#r")
    xf.fl_popup_entry_set_state(pitem1menu1, xfc.FL_POPUP_DISABLED)

    pitem2menu1 = xf.fl_insert_nmenu_items(pmenu1, pitem1menu1, "Green%SG")
    pitem2menu1.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem2menu1, "Gg#G#g")
    xf.fl_popup_entry_set_state(pitem2menu1, xfc.FL_POPUP_DISABLED)

    pitem3menu1 = xf.fl_insert_nmenu_items(pmenu1, pitem2menu1, "Yellow%SY")
    pitem3menu1.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem3menu1, "Yy#Y#y")
    xf.fl_popup_entry_set_state(pitem3menu1, xfc.FL_POPUP_DISABLED)

    pitem4menu1 = xf.fl_insert_nmenu_items(pmenu1, pitem3menu1, "Blue%SB")
    pitem4menu1.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem4menu1, "Bb#B#b")
    xf.fl_popup_entry_set_state(pitem4menu1, xfc.FL_POPUP_DISABLED)

    pitem5menu1 = xf.fl_insert_nmenu_items(pmenu1, pitem4menu1, "Purple%SP")
    pitem5menu1.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem5menu1, "Pp#P#p")
    xf.fl_popup_entry_set_state(pitem5menu1, xfc.FL_POPUP_NONE)

    pitem6menu1 = xf.fl_insert_nmenu_items(pmenu1, pitem5menu1, "Cyan%SC")
    pitem6menu1.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem6menu1, "Cc#C#c")
    xf.fl_popup_entry_set_state(pitem6menu1, xfc.FL_POPUP_NONE)

    pitem7menu1 = xf.fl_insert_nmenu_items(pmenu1, pitem6menu1, "White%SW")
    pitem7menu1.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem7menu1, "Ww#W#w")
    xf.fl_popup_entry_set_state(pitem7menu1, xfc.FL_POPUP_NONE)


def add_items_to_menu2():

    pitem1menu2 = xf.fl_add_nmenu_items(pmenu2, "Red%SR")
    pitem1menu2.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem1menu2, "Rr#R#r")
    xf.fl_popup_entry_set_state(pitem1menu2, xfc.FL_POPUP_DISABLED)

    pitem2menu2 = xf.fl_insert_nmenu_items(pmenu2, pitem1menu2, "Green%SG")
    pitem2menu2.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem2menu2, "Gg#G#g")
    xf.fl_popup_entry_set_state(pitem2menu2, xfc.FL_POPUP_DISABLED)

    pitem3menu2 = xf.fl_insert_nmenu_items(pmenu2, pitem2menu2, "Yellow%SY")
    pitem3menu2.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem3menu2, "Yy#Y#y")
    xf.fl_popup_entry_set_state(pitem3menu2, xfc.FL_POPUP_DISABLED)

    pitem4menu2 = xf.fl_insert_nmenu_items(pmenu2, pitem3menu2, "Blue%SB")
    pitem4menu2.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem4menu2, "Bb#B#b")
    xf.fl_popup_entry_set_state(pitem4menu2, xfc.FL_POPUP_DISABLED)

    pitem5menu2 = xf.fl_insert_nmenu_items(pmenu2, pitem4menu2, "Purple%SP")
    pitem5menu2.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem5menu2, "Pp#P#p")
    xf.fl_popup_entry_set_state(pitem5menu2, xfc.FL_POPUP_NONE)

    pitem6menu2 = xf.fl_insert_nmenu_items(pmenu2, pitem5menu2, "Cyan%SC")
    pitem6menu2.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem6menu2, "Cc#C#c")
    xf.fl_popup_entry_set_state(pitem6menu2, xfc.FL_POPUP_NONE)

    pitem7menu2 = xf.fl_insert_nmenu_items(pmenu2, pitem6menu2, "White%SW")
    pitem7menu2.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem7menu2, "Ww#W#w")
    xf.fl_popup_entry_set_state(pitem7menu2, xfc.FL_POPUP_NONE)



def add_items_to_menu3():

    pitem1menu3 = xf.fl_add_nmenu_items(pmenu3, "Red%SR")
    pitem1menu3.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem1menu3, "Rr#R#r")
    xf.fl_popup_entry_set_state(pitem1menu3, xfc.FL_POPUP_DISABLED)

    pitem2menu3 = xf.fl_insert_nmenu_items(pmenu3, pitem1menu3, "Green%SG")
    pitem2menu3.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem2menu3, "Gg#G#g")
    xf.fl_popup_entry_set_state(pitem2menu3, xfc.FL_POPUP_DISABLED)

    pitem3menu3 = xf.fl_insert_nmenu_items(pmenu3, pitem2menu3, "Yellow%SY")
    pitem3menu3.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem3menu3, "Yy#Y#y")
    xf.fl_popup_entry_set_state(pitem3menu3, xfc.FL_POPUP_DISABLED)

    pitem4menu3 = xf.fl_insert_nmenu_items(pmenu3, pitem3menu3, "Blue%SB")
    pitem4menu3.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem4menu3, "Bb#B#b")
    xf.fl_popup_entry_set_state(pitem4menu3, xfc.FL_POPUP_DISABLED)

    pitem5menu3 = xf.fl_insert_nmenu_items(pmenu3, pitem4menu3, "Purple%SP")
    pitem5menu3.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem5menu3, "Pp#P#p")
    xf.fl_popup_entry_set_state(pitem5menu3, xfc.FL_POPUP_NONE)

    pitem6menu3 = xf.fl_insert_nmenu_items(pmenu3, pitem5menu3, "Cyan%SC")
    pitem6menu3.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem6menu3, "Cc#C#c")
    xf.fl_popup_entry_set_state(pitem6menu3, xfc.FL_POPUP_NONE)

    pitem7menu3 = xf.fl_insert_nmenu_items(pmenu3, pitem6menu3, "White%SW")
    pitem7menu3.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem7menu3, "Ww#W#w")
    xf.fl_popup_entry_set_state(pitem7menu3, xfc.FL_POPUP_NONE)


def add_items_to_menu4():

    pitem1menu4 = xf.fl_add_nmenu_items(pmenu4, "Red%SR")
    pitem1menu4.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem1menu4, "Rr#R#r")
    xf.fl_popup_entry_set_state(pitem1menu4, xfc.FL_POPUP_DISABLED)

    pitem2menu4 = xf.fl_insert_nmenu_items(pmenu4, pitem1menu4, "Green%SG")
    pitem2menu4.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem2menu4, "Gg#G#g")
    xf.fl_popup_entry_set_state(pitem2menu4, xfc.FL_POPUP_DISABLED)

    pitem3menu4 = xf.fl_insert_nmenu_items(pmenu4, pitem2menu4, "Yellow%SY")
    pitem3menu4.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem3menu4, "Yy#Y#y")
    xf.fl_popup_entry_set_state(pitem3menu4, xfc.FL_POPUP_DISABLED)

    pitem4menu4 = xf.fl_insert_nmenu_items(pmenu4, pitem3menu4, "Blue%SB")
    pitem4menu4.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem4menu4, "Bb#B#b")
    xf.fl_popup_entry_set_state(pitem4menu4, xfc.FL_POPUP_DISABLED)

    pitem5menu4 = xf.fl_insert_nmenu_items(pmenu4, pitem4menu4, "Purple%SP")
    pitem5menu4.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem5menu4, "Pp#P#p")
    xf.fl_popup_entry_set_state(pitem5menu4, xfc.FL_POPUP_NONE)

    pitem6menu4 = xf.fl_insert_nmenu_items(pmenu4, pitem5menu4, "Cyan%SC")
    pitem6menu4.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem6menu4, "Cc#C#c")
    xf.fl_popup_entry_set_state(pitem6menu4, xfc.FL_POPUP_NONE)

    pitem7menu4 = xf.fl_insert_nmenu_items(pmenu4, pitem6menu4, "White%SW")
    pitem7menu4.contents.type = xfc.FL_POPUP_RADIO
    xf.fl_popup_entry_set_shortcut(pitem7menu4, "Ww#W#w")
    xf.fl_popup_entry_set_state(pitem7menu4, xfc.FL_POPUP_NONE)




def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    pform = create_form()

    add_items_to_menu1()
    xf.fl_popup_entry_set_state(xf.fl_get_nmenu_item_by_value(pmenu1, 0), xfc.FL_POPUP_CHECKED)
    set[0] = 0
    xf.fl_set_object_color(pabox[0], xfc.FL_RED + set[0], xfc.FL_BLACK)

    add_items_to_menu2()
    xf.fl_popup_entry_set_state(xf.fl_get_nmenu_item_by_value(pmenu2, 1), xfc.FL_POPUP_CHECKED)
    set[1] = 1
    xf.fl_set_object_color(pabox[1], xfc.FL_RED + set[1], xfc.FL_BLACK)

    add_items_to_menu3()
    xf.fl_popup_entry_set_state(xf.fl_get_nmenu_item_by_value(pmenu3, 2), xfc.FL_POPUP_CHECKED)
    set[2] = 2
    xf.fl_set_object_color(pabox[2], xfc.FL_RED + set[2], xfc.FL_BLACK)

    add_items_to_menu4()
    xf.fl_popup_entry_set_state(xf.fl_get_nmenu_item_by_value(pmenu4, 3), xfc.FL_POPUP_CHECKED)
    set[3] = 3
    xf.fl_set_object_color(pabox[3], xfc.FL_RED + set[3], xfc.FL_BLACK)


    xf.fl_show_form(pform, xfc.FL_PLACE_CENTER, xfc.FL_TRANSIENT, "Nmenu")

    xf.fl_do_forms()
    xf.fl_hide_form(pform)

    return 0



# m is the menu index 0 - 3

def menu_cb(pobj, m):

    pr = xf.fl_get_nmenu_item(pobj)
    if set[m] == pr.contents.val:
        return

    if m == 0:
        # enable the old selected color for other menus
        xf.fl_popup_entry_set_state(xf.fl_get_nmenu_item_by_value(pmenu1, \
                                    set[m]), xfc.FL_POPUP_NONE)
        # disable the currently selected color for other menus
        xf.fl_popup_entry_set_state(xf.fl_get_nmenu_item_by_value(pmenu1, \
                                    pr.contents.val), xfc.FL_POPUP_DISABLED)
    elif m == 1:
        xf.fl_popup_entry_set_state(xf.fl_get_nmenu_item_by_value(pmenu2, \
                                    set[m]), xfc.FL_POPUP_NONE)
        xf.fl_popup_entry_set_state(xf.fl_get_nmenu_item_by_value(pmenu2, \
                                    pr.contents.val), xfc.FL_POPUP_DISABLED)
    elif m == 2:
        xf.fl_popup_entry_set_state(xf.fl_get_nmenu_item_by_value(pmenu3, \
                                    set[m]), xfc.FL_POPUP_NONE)
        xf.fl_popup_entry_set_state(xf.fl_get_nmenu_item_by_value(pmenu3, \
                                    pr.contents.val), xfc.FL_POPUP_DISABLED)
    elif m == 3:
        xf.fl_popup_entry_set_state(xf.fl_get_nmenu_item_by_value(pmenu4, \
                                    set[m]), xfc.FL_POPUP_NONE)
        xf.fl_popup_entry_set_state(xf.fl_get_nmenu_item_by_value(pmenu4, \
                                    pr.contents.val), xfc.FL_POPUP_DISABLED)

    set[m] = pr.contents.val
    xf.fl_set_object_color(pabox[m], xfc.FL_RED + pr.contents.val, xfc.FL_BLACK)



def done_cb(pobj, data):
    xf.fl_finish()
    sys.exit(0)



def create_form():
    global pmenu1, pmenu2, pmenu3, pmenu4

    pform = xf.fl_bgn_form(xfc.FL_NO_BOX, 444, 380)

    pobj = xf.fl_add_box(xfc.FL_BORDER_BOX, 0, 0, 444, 380, "")
    xf.fl_set_object_color(pobj, xfc.FL_SLATEBLUE, xfc.FL_COL1)

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 444, 29, "")
    xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_COL1)

    pmenu1 = xf.fl_add_nmenu(xfc.FL_NORMAL_NMENU, 2, 2, 110, 25, "Color 1")
    xf.fl_set_object_shortcut(pmenu1, "1#1", 1)
    xf.fl_set_object_callback(pmenu1, menu_cb, 0)

    pmenu2 = xf.fl_add_nmenu(xfc.FL_NORMAL_TOUCH_NMENU, 112, 2, 110, 25,
                             "Color 2")
    xf.fl_set_object_shortcut(pmenu2, "2#2", 1)
    xf.fl_set_object_callback(pmenu2, menu_cb, 1)

    pmenu3 = xf.fl_add_nmenu(xfc.FL_BUTTON_NMENU, 222, 2, 110, 25, "Color 3")
    xf.fl_set_object_shortcut(pmenu3, "3#3", 1)
    xf.fl_set_object_callback(pmenu3, menu_cb, 2)

    pmenu4 = xf.fl_add_nmenu(xfc.FL_BUTTON_TOUCH_NMENU, 332, 2, 110, 25,
                             "Color 4")
    xf.fl_set_object_shortcut(pmenu4, "4#4", 1)
    xf.fl_set_object_callback(pmenu4, menu_cb, 3)

    pabox[0] = xf.fl_add_box(xfc.FL_SHADOW_BOX,  20, 80, 70, 230, "")
    pabox[1] = xf.fl_add_box(xfc.FL_SHADOW_BOX, 130, 80, 70, 230, "")
    pabox[2] = xf.fl_add_box(xfc.FL_SHADOW_BOX, 240, 80, 70, 230, "")
    pabox[3] = xf.fl_add_box(xfc.FL_SHADOW_BOX, 350, 80, 70, 230, "")

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 310, 330, 110, 30, "Quit")
    xf.fl_set_object_shortcut(pobj, "Q#Q", 1)
    xf.fl_set_object_callback(pobj, done_cb, 0)

    xf.fl_end_form()

    return pform



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

