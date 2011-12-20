#!/usr/bin/env python

#  This file is part of xforms-python, and it is a variant of
#  buttonall.c XForms demo, not using deprecated functions, with
#  some adaptations.
#
#  buttonall.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# All button classes
#

import sys
#sys.path.append("..")
import xformslib as xfl


# Forms and Objects

class FD_buttform(object):
    buttform = None
    vdata = None
    cdata = ""
    ldata = 0
    backface = None
    done = None
    objsgroup = None
    bbutt = None
    pbutt = None
    bw_obj = None


class ButtonAll(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, "", 0, 0)
        self.fd_buttform = self.create_form_buttform()

        # fill-in form initialization code

        xfl.fl_set_pixmapbutton_file(self.fd_buttform.pbutt, "crab45.xpm")
        xfl.fl_set_bitmapbutton_file(self.fd_buttform.bbutt, "bm1.xbm")
        xfl.fl_add_select_items(self.fd_buttform.bw_obj,
                                   " -4| -3 | -2| -1|  1|  2|  3|  4")
        #xfl.fl_set_select(self.fd_buttform.bw_obj, 5)

        # show the first form
        xfl.fl_show_form(self.fd_buttform.buttform, xfl.FL_PLACE_CENTER, \
                     xfl.FL_FULLBORDER, "buttform")
        while xfl.fl_do_forms():
            pass    # empty

    # callbacks for form buttform

    def done_cb(self, pobj, data):
        xfl.fl_finish()
        sys.exit(0)


    def bw_cb(self, pobj, data):
        bws = [-4, -3, -2, -1, 1, 2, 3, 4]
        n = xfl.fl_get_select_item(pobj).contents.val - 1
        # xfl.FL_POPUP_RETURN

        xfl.fl_freeze_form(pobj.contents.form)
        xfl.fl_set_object_bw(self.fd_buttform.backface, bws[n])
        xfl.fl_set_object_bw(self.fd_buttform.objsgroup, bws[n])
        xfl.fl_set_object_bw(self.fd_buttform.done, bws[n])

        # redrawing the backface wipes out the done button. Redraw it
        #xfl.fl_redraw_object(self.fd_buttform.done)
        xfl.fl_unfreeze_form(pobj.contents.form)


    def create_form_buttform(self):
        fdui = FD_buttform()

        fdui.buttform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 290, 260)

        fdui.backface = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 290, \
                260, "")

        fdui.done = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 185, \
                215, 90, 30, "Done")
        xfl.fl_set_object_lalign(fdui.done, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_callback(fdui.done, self.done_cb, 0)

        fdui.objsgroup = xfl.fl_bgn_group()

        pobj = xfl.fl_add_frame(xfl.FL_ENGRAVED_FRAME, 175, 170, \
                100, 30, "")
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_GREEN)

        pobj = xfl.fl_add_round3dbutton(xfl.FL_PUSH_BUTTON, 210, 170, \
                30, 30, "")
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_GREEN)

        fdui.bbutt = xfl.fl_add_bitmapbutton(xfl.FL_NORMAL_BUTTON, \
                25, 85, 40, 40, "bitmapbutton")
        xfl.fl_set_object_color(fdui.bbutt, xfl.FL_COL1, \
                xfl.FL_BLACK)

        fdui.pbutt = xfl.fl_add_pixmapbutton(xfl.FL_NORMAL_BUTTON, \
                25, 25, 40, 40, "pixmapbutton")
        xfl.fl_set_object_color(fdui.pbutt, xfl.FL_COL1, \
                xfl.FL_YELLOW)

        pobj = xfl.fl_add_checkbutton(xfl.FL_RADIO_BUTTON, 100, 31, \
                70, 32, "Red")
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_RED)

        pobj = xfl.fl_add_checkbutton(xfl.FL_RADIO_BUTTON, 100, 60, \
                70, 32, "Green")
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_GREEN)

        pobj = xfl.fl_add_checkbutton(xfl.FL_RADIO_BUTTON, 100, 90, \
                70, 32, "Blue")
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_BLUE)

        pobj = xfl.fl_add_lightbutton(xfl.FL_PUSH_BUTTON, 20, 170, \
                108, 30, "LightButton")
        xfl.fl_set_button(pobj, 1)

        pobj = xfl.fl_add_roundbutton(xfl.FL_PUSH_BUTTON, 200, 35, \
                75, 25, "Red")
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_RED)

        pobj = xfl.fl_add_roundbutton(xfl.FL_PUSH_BUTTON, 200, 64, \
                75, 25, "Green")
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_GREEN)

        pobj = xfl.fl_add_roundbutton(xfl.FL_PUSH_BUTTON, 200, 93, \
                75, 25, "Blue")
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_BLUE)

        pobj = xfl.fl_add_round3dbutton(xfl.FL_PUSH_BUTTON, 180, 170, \
                30, 30, "")
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_RED)

        pobj = xfl.fl_add_round3dbutton(xfl.FL_PUSH_BUTTON, 240, 170, \
                30, 30, "")
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_BLUE)

        pobj = xfl.fl_add_button(xfl.FL_PUSH_BUTTON, 130, 210, 30, 30, "go")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_OVAL3D_UPBOX)
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(pobj, xfl.FL_BOLD_STYLE)

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 20, 210, \
                90, 30, "Button")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_ROUNDED3D_UPBOX)
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_CENTER)

        fdui.bw_obj = xfl.fl_add_select(xfl.FL_NORMAL_SELECT, 105, 135, \
                80, 30, "BW")
        xfl.fl_set_object_callback(fdui.bw_obj, self.bw_cb, 0)

        pobj = xfl.fl_add_labelframe(xfl.FL_ENGRAVED_FRAME, 190, 25, \
                85, 100, "RoundButton")

        pobj = xfl.fl_add_labelframe(xfl.FL_ENGRAVED_FRAME, 90, 25, \
                90, 100, "CheckButton")

        xfl.fl_end_group()
        xfl.fl_end_form()

        return fdui


if __name__ == '__main__':
    print("********* buttonall_new.py *********")
    ButtonAll(len(sys.argv), sys.argv)
