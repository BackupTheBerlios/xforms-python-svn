#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  cursor.c XForms demo, with some adaptations and modifications.
#
#  cursor.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Cursor routines demo.
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc


# converted from "bm1.xbm" file
bm1_width = 16
bm1_height = 16
bm1_bits = "\x00\x00\x00\x57\x7c\x72\xc4\x52\xc4\x00\x44\x01" \
           "\x44\x1f\xfc\x22\x40\x42\x40\x44\x40\x43\xc0\x40" \
           "\x70\x40\x8c\x20\x00\x1f\x00\x00"
# converted from "bm2.xbm" file
bm2_width = 16
bm2_height = 16
bm2_bits = "\x00\x00\x00\x57\x7c\x72\xfc\x52\xfc\x00\x7c\x01" \
           "\x7c\x1f\xfc\x22\x40\x42\x40\x44\x40\x43\xc0\x40" \
           "\x70\x40\x8c\x20\x00\x1f\x00\x00"


#curs = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\xff"
curslist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
curs = "".join([chr(x) for x in curslist])



class FD_cursor(object):
    cursor = None
    vdata = None
    cdata = ""
    ldata = 0



# callbacks for form cursor

def setcursor_cb(pobj, data):
    xf.fl_set_cursor(xf.FL_ObjWin(pobj), data)


def setbitmapcursor_cb(pobj, data):
    xf.fl_reset_cursor(xf.FL_ObjWin(pobj))      # back to default
    pbitmapcur = xf.fl_create_bitmap_cursor(bm1_bits, bm2_bits, \
                    bm1_width, bm1_height, bm1_width / 2, bm1_height / 2)
    xf.fl_set_cursor(xf.FL_ObjWin(pobj), pbitmapcur)


def setanimatedcursor_cb(pobj, data):
    xf.fl_set_cursor(xf.FL_ObjWin(pobj), panimated)


def done_cb(pobj, data):
    xf.fl_finish()
    sys.exit(0)



def main(lsysargv, sysarg):
    global panimated

    xf.fl_set_border_width(-2)
    xf.fl_initialize(lsysargv, sysarg, "FormDemo", 0, 0)
    fd_cursor = create_form_cursor()

    # fill-in form initialization code

    xf.fl_set_cursor_color(xfc.FL_BUSY_CURSOR, xfc.FL_BLACK, xfc.FL_RED)

    panimated = xf.fl_create_animated_cursor(curs, 200)

    xf.fl_show_form(fd_cursor.cursor, xfc.FL_PLACE_CENTER, xfc.FL_FULLBORDER, \
                    "cursor")
    xf.fl_do_forms()
    return 0



def create_form_cursor():

    fdui = FD_cursor()

    fdui.cursor = xf.fl_bgn_form(xfc.FL_NO_BOX, 325, 175)

    xf.fl_add_box(xfc.FL_UP_BOX, 0 ,0, 325, 175, "")
    xf.fl_add_frame(xfc.FL_EMBOSSED_FRAME, 10, 10, 305, 120, "")

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 20, 20, 50, 25, "Hand")
    xf.fl_set_object_callback(pobj, setcursor_cb, xfc.XC_hand2)

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 70, 20, 50, 25, "Watch")
    xf.fl_set_object_callback(pobj, setcursor_cb, xfc.FL_BUSY_CURSOR)

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 120, 20, 60, 25, "Invisible")
    xf.fl_set_object_callback(pobj, setcursor_cb, xfc.FL_INVISIBLE_CURSOR)

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 180, 20, 62, 25, "Animated")
    xf.fl_set_object_callback(pobj, setanimatedcursor_cb, 0)

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 242, 20, 62, 25, "BitmapCur")
    xf.fl_set_object_callback(pobj, setbitmapcursor_cb, 0)

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 90, 70, 140, 50, "DefaultCursor")
    xf.fl_set_button_shortcut(pobj, "Dd#d", 1)
    xf.fl_set_object_callback(pobj, setcursor_cb, xfc.FL_DEFAULT_CURSOR)

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 140, 60, 25, "Done")
    xf.fl_set_object_callback(pobj, done_cb, 0)

    xf.fl_end_form()

    xf.fl_adjust_form_size(fdui.cursor)

    return fdui


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

