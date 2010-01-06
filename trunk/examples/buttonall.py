#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  buttonall.c XForms demo, with some adaptations.
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
from xformslib import oldfunc as xfdepr


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


# callbacks for form buttform


def done_cb(pobj, data):
    xf.fl_finish()
    sys.exit(0)


def bw_cb(pobj, data):

    bws = [-4, -3, -2, -1, 1, 2, 3, 4]
    n = xfdepr.fl_get_choice(pobj) - 1

    xf.fl_freeze_form(pobj.contents.form)
    xf.fl_set_object_bw(fd_buttform.backface, bws[n])
    xf.fl_set_object_bw(fd_buttform.objsgroup, bws[n])
    xf.fl_set_object_bw(fd_buttform.done, bws[n])

    # redrawing the backface wipes out the done button. Redraw it

    xf.fl_redraw_object(fd_buttform.done)
    xf.fl_unfreeze_form(pobj.contents.form)



def main(lsysargv, sysargv):
    global fd_buttform

    xf.fl_initialize(lsysargv, sysargv, 0, 0, 0)
    fd_buttform = create_form_buttform()

    # fill-in form initialization code

    xf.fl_set_pixmapbutton_file(fd_buttform.pbutt, "crab45.xpm")
    xf.fl_set_bitmapbutton_file(fd_buttform.bbutt, "bm1.xbm")
    xfdepr.fl_addto_choice(fd_buttform.bw_obj,
                           " -4 | -3 | -2 | -1 |  1|  2|  3|  4")
    xfdepr.fl_set_choice(fd_buttform.bw_obj, 5)

    # show the first form

    xf.fl_show_form(fd_buttform.buttform, xfc.FL_PLACE_CENTER, \
                    xfc.FL_FULLBORDER, "buttform")
    while xf.fl_do_forms():
        pass    # empty

    return 0





def create_form_buttform():

    fdui = FD_buttform()

    fdui.buttform = xf.fl_bgn_form(xfc.FL_NO_BOX, 290, 260)

    fdui.backface = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 290, 260, "")

    fdui.done = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 185, 215, 90, 30, "Done")
    xf.fl_set_object_lalign(fdui.done, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_callback(fdui.done, done_cb, 0)

    fdui.objsgroup = xf.fl_bgn_group()

    pobj = xf.fl_add_frame(xfc.FL_ENGRAVED_FRAME, 175, 170, 100, 30, "")
    xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_GREEN)

    pobj = xf.fl_add_round3dbutton(xfc.FL_PUSH_BUTTON, 210, 170, 30, 30, "")
    xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_GREEN)

    fdui.bbutt = xf.fl_add_bitmapbutton(xfc.FL_NORMAL_BUTTON, 25, 85, 40, 40, \
                                        "bitmapbutton")
    xf.fl_set_object_color(fdui.bbutt, xfc.FL_COL1, xfc.FL_BLACK)

    fdui.pbutt = xf.fl_add_pixmapbutton(xfc.FL_NORMAL_BUTTON, 25, 25, 40, 40, \
                                        "pixmapbutton")
    xf.fl_set_object_color(fdui.pbutt, xfc.FL_COL1, xfc.FL_YELLOW)

    pobj = xf.fl_add_checkbutton(xfc.FL_RADIO_BUTTON, 100, 31, 70, 32, "Red")
    xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_RED)

    pobj = xf.fl_add_checkbutton(xfc.FL_RADIO_BUTTON, 100, 60, 70, 32, "Green")
    xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_GREEN)

    pobj = xf.fl_add_checkbutton(xfc.FL_RADIO_BUTTON, 100, 90, 70, 32, "Blue")
    xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_BLUE)

    pobj = xf.fl_add_lightbutton(xfc.FL_PUSH_BUTTON, 20, 170, 108, 30, "LightButton")
    xf.fl_set_button(pobj, 1)

    pobj = xf.fl_add_roundbutton(xfc.FL_PUSH_BUTTON, 200, 35, 75, 25, "Red")
    xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_RED)

    pobj = xf.fl_add_roundbutton(xfc.FL_PUSH_BUTTON, 200, 64, 75, 25, "Green")
    xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_GREEN)

    pobj = xf.fl_add_roundbutton(xfc.FL_PUSH_BUTTON, 200, 93, 75, 25, "Blue")
    xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_BLUE)

    pobj = xf.fl_add_round3dbutton(xfc.FL_PUSH_BUTTON, 180, 170, 30, 30, "")
    xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_RED)

    pobj = xf.fl_add_round3dbutton(xfc.FL_PUSH_BUTTON, 240, 170, 30, 30, "")
    xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_BLUE)

    pobj = xf.fl_add_button(xfc.FL_PUSH_BUTTON, 130, 210, 30, 30, "go")
    xf.fl_set_object_boxtype(pobj, xfc.FL_OVAL3D_UPBOX)
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_lstyle(pobj, xfc.FL_BOLD_STYLE)

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 20, 210, 90, 30, "Button")
    xf.fl_set_object_boxtype(pobj, xfc.FL_ROUNDED3D_UPBOX)
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_CENTER)

    fdui.bw_obj = xfdepr.fl_add_choice(xfdepr.FL_NORMAL_CHOICE2, 105, 135, \
                                       80, 30, "BW")
    xf.fl_set_object_callback(fdui.bw_obj, bw_cb, 0)

    pobj = xf.fl_add_labelframe(xfc.FL_ENGRAVED_FRAME, 190, 25, 85, 100, \
				"RoundButton")

    pobj = xf.fl_add_labelframe(xfc.FL_ENGRAVED_FRAME, 90, 25, 90, 100, \
				"CheckButton")

    xf.fl_end_group()

    xf.fl_end_form()

    #fdui.buttform.fdui = fdui

    return fdui



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

