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
import xformslib as xfl



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
#curs = ""
#for x in curslist:
#    curs += chr(x)
curs += hex(-1)         #"\xffffffff"


class FD_cursor(object):
    cursor = None
    vdata = None
    cdata = ""
    ldata = 0


class FLCursor(object):
    def __init__(self, lsysargv, sysarg):
        self.pbitmapcur = None
        xfl.fl_set_border_width(-2)
        xfl.fl_initialize(lsysargv, sysarg, "FormDemo", None, 0)
        self.fd_cursor = self.create_form_cursor()

        # fill-in form initialization code
        xfl.fl_set_cursor_color(xfl.FL_BUSY_CURSOR, xfl.FL_BLACK, xfl.FL_RED)

        self.panimated = xfl.fl_create_animated_cursor(curs, 150)

        xfl.fl_show_form(self.fd_cursor.cursor, xfl.FL_PLACE_CENTER, \
                xfl.FL_FULLBORDER, "cursor")
        xfl.fl_do_forms()


    # callbacks for form cursor

    def setcursor_cb(self, pobj, data):
        xfl.fl_set_cursor(xfl.FL_ObjWin(pobj), data)


    def setbitmapcursor_cb(self, pobj, data):
        if not self.pbitmapcur:
            self.pbitmapcur = xfl.fl_create_bitmap_cursor(bm1_bits, \
                    bm2_bits, bm1_width, bm1_height, bm1_width / 2, \
                    bm1_height / 2)

        xfl.fl_reset_cursor(xfl.FL_ObjWin(pobj))      # back to default
        xfl.fl_set_cursor(xfl.FL_ObjWin(pobj), self.pbitmapcur)
        xfl.fl_redraw_form(self.fd_cursor.cursor)


    def setanimatedcursor_cb(self, pobj, data):
        xfl.fl_reset_cursor(xfl.FL_ObjWin(pobj))      # back to default
        xfl.fl_set_cursor(xfl.FL_ObjWin(pobj), self.panimated)


    def done_cb(self, pobj, data):
        xfl.fl_finish()
        sys.exit(0)


    def create_form_cursor(self):

        fdui = FD_cursor()

        fdui.cursor = xfl.fl_bgn_form(xfl.FL_NO_BOX, 325, 175)

        xfl.fl_add_box(xfl.FL_UP_BOX, 0 ,0, 325, 175, "")
        xfl.fl_add_frame(xfl.FL_EMBOSSED_FRAME, 10, 10, 305, 120, "")

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 20, 20, 50, 25, "Hand")
        xfl.fl_set_object_callback(pobj, self.setcursor_cb, xfl.XC_hand2)

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 70, 20, 50, 25, "Watch")
        xfl.fl_set_object_callback(pobj, self.setcursor_cb, xfl.FL_BUSY_CURSOR)

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 120, 20, 60, 25, \
                "Invisible")
        xfl.fl_set_object_callback(pobj, self.setcursor_cb, \
                xfl.FL_INVISIBLE_CURSOR)

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 180, 20, 62, 25, \
                "Animated")
        xfl.fl_set_object_callback(pobj, self.setanimatedcursor_cb, 0)

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 242, 20, 62, 25, \
                "BitmapCur")
        xfl.fl_set_object_callback(pobj, self.setbitmapcursor_cb, 0)

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 90, 70, 140, 50, \
                "DefaultCursor")
        xfl.fl_set_button_shortcut(pobj, "Dd#d", 1)
        xfl.fl_set_object_callback(pobj, self.setcursor_cb, \
                xfl.FL_DEFAULT_CURSOR)

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 250, 140, 60, 25, \
                "Done")
        xfl.fl_set_object_callback(pobj, self.done_cb, 0)

        xfl.fl_end_form()

        xfl.fl_adjust_form_size(fdui.cursor)

        return fdui



if __name__ == '__main__':
    print("********* cursor.py *********")
    appl = FLCursor(len(sys.argv), sys.argv)
