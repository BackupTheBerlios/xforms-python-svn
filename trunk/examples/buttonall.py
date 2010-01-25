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
#from xformslib import *
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flbitmap import *
from xformslib.flmisc import *
from xformslib.xfdata import *
from xformslib import deprecated



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

        fl_initialize(lsysargv, sysargv, 0, 0, 0)
        self.fd_buttform = self.create_form_buttform()

        # fill-in form initialization code

        fl_set_pixmapbutton_file(self.fd_buttform.pbutt, "crab45.xpm")
        fl_set_bitmapbutton_file(self.fd_buttform.bbutt, "bm1.xbm")
        deprecated.fl_addto_choice(self.fd_buttform.bw_obj,
                                   " -4 | -3 | -2 | -1 |  1|  2|  3|  4")
        deprecated.fl_set_choice(self.fd_buttform.bw_obj, 5)

        # show the first form
        fl_show_form(self.fd_buttform.buttform, FL_PLACE_CENTER, \
                     FL_FULLBORDER, "buttform")
        while fl_do_forms():
            pass    # empty


    # callbacks for form buttform

    def done_cb(self, pobj, data):
        fl_finish()
        sys.exit(0)


    def bw_cb(self, pobj, data):

        bws = [-4, -3, -2, -1, 1, 2, 3, 4]
        n = deprecated.fl_get_choice(pobj) - 1

        fl_freeze_form(pobj.contents.form)
        fl_set_object_bw(self.fd_buttform.backface, bws[n])
        fl_set_object_bw(self.fd_buttform.objsgroup, bws[n])
        fl_set_object_bw(self.fd_buttform.done, bws[n])

        # redrawing the backface wipes out the done button. Redraw it
        fl_redraw_object(self.fd_buttform.done)
        fl_unfreeze_form(pobj.contents.form)


    def create_form_buttform(self):

        fdui = FD_buttform()

        fdui.buttform = fl_bgn_form(FL_NO_BOX, 290, 260)

        fdui.backface = fl_add_box(FL_UP_BOX, 0, 0, 290, 260, "")

        fdui.done = fl_add_button(FL_NORMAL_BUTTON, 185, 215, 90, 30, "Done")
        fl_set_object_lalign(fdui.done, FL_ALIGN_CENTER)
        fl_set_object_callback(fdui.done, self.done_cb, 0)

        fdui.objsgroup = fl_bgn_group()

        pobj = fl_add_frame(FL_ENGRAVED_FRAME, 175, 170, 100, 30, "")
        fl_set_object_color(pobj, FL_COL1, FL_GREEN)

        pobj = fl_add_round3dbutton(FL_PUSH_BUTTON, 210, 170, 30, 30, "")
        fl_set_object_color(pobj, FL_COL1, FL_GREEN)

        fdui.bbutt = fl_add_bitmapbutton(FL_NORMAL_BUTTON, 25, 85, 40, 40, \
                                        "bitmapbutton")
        fl_set_object_color(fdui.bbutt, FL_COL1, FL_BLACK)

        fdui.pbutt = fl_add_pixmapbutton(FL_NORMAL_BUTTON, 25, 25, 40, 40, \
                                        "pixmapbutton")
        fl_set_object_color(fdui.pbutt, FL_COL1, FL_YELLOW)

        pobj = fl_add_checkbutton(FL_RADIO_BUTTON, 100, 31, 70, 32, "Red")
        fl_set_object_color(pobj, FL_COL1, FL_RED)

        pobj = fl_add_checkbutton(FL_RADIO_BUTTON, 100, 60, 70, 32, "Green")
        fl_set_object_color(pobj, FL_COL1, FL_GREEN)

        pobj = fl_add_checkbutton(FL_RADIO_BUTTON, 100, 90, 70, 32, "Blue")
        fl_set_object_color(pobj, FL_COL1, FL_BLUE)

        pobj = fl_add_lightbutton(FL_PUSH_BUTTON, 20, 170, 108, 30, "LightButton")
        fl_set_button(pobj, 1)

        pobj = fl_add_roundbutton(FL_PUSH_BUTTON, 200, 35, 75, 25, "Red")
        fl_set_object_color(pobj, FL_COL1, FL_RED)

        pobj = fl_add_roundbutton(FL_PUSH_BUTTON, 200, 64, 75, 25, "Green")
        fl_set_object_color(pobj, FL_COL1, FL_GREEN)

        pobj = fl_add_roundbutton(FL_PUSH_BUTTON, 200, 93, 75, 25, "Blue")
        fl_set_object_color(pobj, FL_COL1, FL_BLUE)

        pobj = fl_add_round3dbutton(FL_PUSH_BUTTON, 180, 170, 30, 30, "")
        fl_set_object_color(pobj, FL_COL1, FL_RED)

        pobj = fl_add_round3dbutton(FL_PUSH_BUTTON, 240, 170, 30, 30, "")
        fl_set_object_color(pobj, FL_COL1, FL_BLUE)

        pobj = fl_add_button(FL_PUSH_BUTTON, 130, 210, 30, 30, "go")
        fl_set_object_boxtype(pobj, FL_OVAL3D_UPBOX)
        fl_set_object_lalign(pobj, FL_ALIGN_CENTER)
        fl_set_object_lstyle(pobj, FL_BOLD_STYLE)

        pobj = fl_add_button(FL_NORMAL_BUTTON, 20, 210, 90, 30, "Button")
        fl_set_object_boxtype(pobj, FL_ROUNDED3D_UPBOX)
        fl_set_object_lalign(pobj, FL_ALIGN_CENTER)

        fdui.bw_obj = deprecated.fl_add_choice(deprecated.FL_NORMAL_CHOICE2, \
                                               105, 135, 80, 30, "BW")
        fl_set_object_callback(fdui.bw_obj, self.bw_cb, 0)

        pobj = fl_add_labelframe(FL_ENGRAVED_FRAME, 190, 25, 85, 100, \
                                 "RoundButton")

        pobj = fl_add_labelframe(FL_ENGRAVED_FRAME, 90, 25, 90, 100, \
                                 "CheckButton")

        fl_end_group()
        fl_end_form()

        return fdui



if __name__ == '__main__':
    ButtonAll(len(sys.argv), sys.argv)

