#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  buttonall.c XForms demo, with some adaptation.
#
#  buttonall.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# All button classes
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc


# Forms and Objects

class FD_buttform(object):
    buttform = None
    vdata = None
    cdata = None
    ldata = None
    backface = None
    done = None
    objsgroup = None
    bbutt = None
    pbutt = None
    bw_obj = None


# callbacks for form buttform


def done_cb(ob, data):
    xf.fl_finish()
    sys.exit(0)


def bw_cb(ob, data):

    bws = [-4, -3, -2, -1, 1, 2, 3, 4]
    n = xf.fl_get_choice(ob) - 1

    xf.fl_freeze_form(ob[0].form)
    xf.fl_set_object_bw(fdui.backface, bws[n])
    xf.fl_set_object_bw(fdui.objsgroup, bws[n])
    xf.fl_set_object_bw(fdui.done, bws[n])

    # redrawing the backface wipes out the done button. Redraw it

    xf.fl_redraw_object(fdui.done)
    xf.fl_unfreeze_form(ob[0].form)



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, 0, 0, 0)
    fd_buttform = create_form_buttform()

    # fill-in form initialization code

    xf.fl_set_pixmapbutton_file(fd_buttform.pbutt,"crab45.xpm")
    xf.fl_set_bitmapbutton_file(fd_buttform.bbutt,"bm1.xbm")
    xf.fl_addto_choice(fd_buttform.bw_obj,
		       " -4 | -3 | -2 | -1 |  1|  2|  3|  4")
    xf.fl_set_choice(fd_buttform.bw_obj, 5)

    # show the first form

    xf.fl_show_form(fd_buttform.buttform, xfc.FL_PLACE_CENTER, \
                    xfc.FL_FULLBORDER, "buttform")
    while xf.fl_do_forms():
        pass    # empty

    return 0





def create_form_buttform():

    global fdui
    fdui = FD_buttform()

    fdui.vdata = fdui.cdata = None
    fdui.ldata = 0

    fdui.buttform = xf.fl_bgn_form(xfc.FL_NO_BOX, 290, 260)

    fdui.backface = obj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 290, 260, "")

    fdui.done = obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 185, 215, 90, 30, "Done")
    xf.fl_set_object_lalign(obj, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_callback(obj, done_cb, 0)

    fdui.objsgroup = xf.fl_bgn_group()

    obj = xf.fl_add_frame(xfc.FL_ENGRAVED_FRAME, 175, 170, 100, 30, "")
    xf.fl_set_object_color(obj, xfc.FL_COL1, xfc.FL_GREEN)

    obj = xf.fl_add_round3dbutton(xfc.FL_PUSH_BUTTON, 210, 170, 30, 30, "")
    xf.fl_set_object_color(obj, xfc.FL_COL1, xfc.FL_GREEN)

    fdui.bbutt = obj = xf.fl_add_bitmapbutton(xfc.FL_NORMAL_BUTTON, 25, 85, 40, 40, "bitmapbutton")
    xf.fl_set_object_color(obj, xfc.FL_COL1, xfc.FL_BLACK)

    fdui.pbutt = obj = xf.fl_add_pixmapbutton(xfc.FL_NORMAL_BUTTON, 25, 25, 40, 40, "pixmapbutton")
    xf.fl_set_object_color(obj, xfc.FL_COL1, xfc.FL_YELLOW)

    obj = xf.fl_add_checkbutton(xfc.FL_RADIO_BUTTON, 100, 31, 70, 32, "Red")
    xf.fl_set_object_color(obj, xfc.FL_COL1, xfc.FL_RED)

    obj = xf.fl_add_checkbutton(xfc.FL_RADIO_BUTTON, 100, 60, 70, 32, "Green")
    xf.fl_set_object_color(obj, xfc.FL_COL1, xfc.FL_GREEN)

    obj = xf.fl_add_checkbutton(xfc.FL_RADIO_BUTTON, 100, 90, 70, 32, "Blue")
    xf.fl_set_object_color(obj, xfc.FL_COL1, xfc.FL_BLUE)

    obj = xf.fl_add_lightbutton(xfc.FL_PUSH_BUTTON, 20, 170, 108, 30, "LightButton")
    xf.fl_set_button(obj, 1)

    obj = xf.fl_add_roundbutton(xfc.FL_PUSH_BUTTON, 200, 35, 75, 25, "Red")
    xf.fl_set_object_color(obj, xfc.FL_COL1, xfc.FL_RED)

    obj = xf.fl_add_roundbutton(xfc.FL_PUSH_BUTTON, 200, 64, 75, 25, "Green")
    xf.fl_set_object_color(obj, xfc.FL_COL1, xfc.FL_GREEN)

    obj = xf.fl_add_roundbutton(xfc.FL_PUSH_BUTTON, 200, 93, 75, 25, "Blue")
    xf.fl_set_object_color(obj, xfc.FL_COL1, xfc.FL_BLUE)

    obj = xf.fl_add_round3dbutton(xfc.FL_PUSH_BUTTON, 180, 170, 30, 30, "")
    xf.fl_set_object_color(obj, xfc.FL_COL1, xfc.FL_RED)

    obj = xf.fl_add_round3dbutton(xfc.FL_PUSH_BUTTON, 240, 170, 30, 30, "")
    xf.fl_set_object_color(obj, xfc.FL_COL1, xfc.FL_BLUE)

    obj = xf.fl_add_button(xfc.FL_PUSH_BUTTON, 130, 210, 30, 30, "go")
    xf.fl_set_object_boxtype(obj, xfc.FL_OVAL3D_UPBOX)
    xf.fl_set_object_lalign(obj, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_lstyle(obj, xfc.FL_BOLD_STYLE)

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 20, 210, 90, 30, "Button")
    xf.fl_set_object_boxtype(obj, xfc.FL_ROUNDED3D_UPBOX)
    xf.fl_set_object_lalign(obj, xfc.FL_ALIGN_CENTER)

    fdui.bw_obj = obj = xf.fl_add_choice(xfc.FL_NORMAL_CHOICE2, 105, 135, 80, 30, "BW")
    xf.fl_set_object_callback(obj, bw_cb, 0)

    obj = xf.fl_add_labelframe(xfc.FL_ENGRAVED_FRAME, 190, 25, 85, 100, "RoundButton")

    obj = xf.fl_add_labelframe(xfc.FL_ENGRAVED_FRAME, 90, 25, 90, 100, "CheckButton")
    xf.fl_end_group()

    xf.fl_end_form()

    #fdui.buttform.fdui = fdui

    return fdui



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

