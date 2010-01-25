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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flcursor import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *



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



class FD_cursor(object):
    cursor = None
    vdata = None
    cdata = ""
    ldata = 0



class FLCursor(object):
    def __init__(self, lsysargv, sysarg):

        #curs = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\xff"
        curslist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        curs = "".join([chr(x) for x in curslist])

        fl_set_border_width(-2)
        fl_initialize(lsysargv, sysarg, "FormDemo", 0, 0)
        self.fd_cursor = self.create_form_cursor()

        # fill-in form initialization code
        fl_set_cursor_color(FL_BUSY_CURSOR, FL_BLACK, FL_RED)

        self.panimated = fl_create_animated_cursor(curs, 200)

        fl_show_form(self.fd_cursor.cursor, FL_PLACE_CENTER, FL_FULLBORDER, \
                    "cursor")
        fl_do_forms()


    # callbacks for form cursor

    def setcursor_cb(self, pobj, data):
        fl_set_cursor(FL_ObjWin(pobj), data)


    def setbitmapcursor_cb(self, pobj, data):
        fl_reset_cursor(FL_ObjWin(pobj))      # back to default
        pbitmapcur = fl_create_bitmap_cursor(bm1_bits, bm2_bits, \
                    bm1_width, bm1_height, bm1_width / 2, bm1_height / 2)
        fl_set_cursor(FL_ObjWin(pobj), pbitmapcur)
        fl_redraw_form(self.fd_cursor.cursor)


    def setanimatedcursor_cb(self, pobj, data):
        fl_set_cursor(FL_ObjWin(pobj), self.panimated)


    def done_cb(self, pobj, data):
        fl_finish()
        sys.exit(0)


    def create_form_cursor(self):

        fdui = FD_cursor()

        fdui.cursor = fl_bgn_form(FL_NO_BOX, 325, 175)

        fl_add_box(FL_UP_BOX, 0 ,0, 325, 175, "")
        fl_add_frame(FL_EMBOSSED_FRAME, 10, 10, 305, 120, "")

        pobj = fl_add_button(FL_NORMAL_BUTTON, 20, 20, 50, 25, "Hand")
        fl_set_object_callback(pobj, self.setcursor_cb, XC_hand2)

        pobj = fl_add_button(FL_NORMAL_BUTTON, 70, 20, 50, 25, "Watch")
        fl_set_object_callback(pobj, self.setcursor_cb, FL_BUSY_CURSOR)

        pobj = fl_add_button(FL_NORMAL_BUTTON, 120, 20, 60, 25, "Invisible")
        fl_set_object_callback(pobj, self.setcursor_cb, FL_INVISIBLE_CURSOR)

        pobj = fl_add_button(FL_NORMAL_BUTTON, 180, 20, 62, 25, "Animated")
        fl_set_object_callback(pobj, self.setanimatedcursor_cb, 0)

        pobj = fl_add_button(FL_NORMAL_BUTTON, 242, 20, 62, 25, "BitmapCur")
        fl_set_object_callback(pobj, self.setbitmapcursor_cb, 0)

        pobj = fl_add_button(FL_NORMAL_BUTTON, 90, 70, 140, 50, "DefaultCursor")
        fl_set_button_shortcut(pobj, "Dd#d", 1)
        fl_set_object_callback(pobj, self.setcursor_cb, FL_DEFAULT_CURSOR)

        pobj = fl_add_button(FL_NORMAL_BUTTON, 250, 140, 60, 25, "Done")
        fl_set_object_callback(pobj, self.done_cb, 0)

        fl_end_form()

        fl_adjust_form_size(fdui.cursor)

        return fdui




if __name__ == '__main__':
    FLCursor(len(sys.argv), sys.argv)

