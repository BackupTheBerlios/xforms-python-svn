#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  lalign.c XForms demo, with some adaptations.
#
#  lalign.c was written by M. Overmars and T.C. Zhao
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Different label alignments
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flbitmap import *
from xformslib.flmisc import *
from xformslib.xfdata import *



# Forms and Objects

#TEST_PIXMAP_ALIGN = False
TEST_PIXMAP_ALIGN = True


class FD_form0(object):
    form0 = None
    vdata = None
    ldata = None
    box = None
    inside = None
    center_ = None



class Flalignpixmap(object):
    def __init__(self, lsysargv, sysargv):

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.fd_form0 = self.create_form_form0()

        # fill-in form initialization code
        fl_set_form_dblbuffer(self.fd_form0.form0, 1)
        align = fl_get_object_lalign(self.fd_form0.box) | FL_ALIGN_INSIDE
        if align != fl_get_object_lalign(self.fd_form0.box):
            fl_set_button(self.fd_form0.inside, 1)

        # show the first form
        fl_show_form(self.fd_form0.form0, FL_PLACE_FREE, \
                        FL_FULLBORDER, "form0")

        fl_do_forms()


    def align_cb(self, pobj, n):

        if fl_get_button(self.fd_form0.inside):
            n |= FL_ALIGN_INSIDE

        if not TEST_PIXMAP_ALIGN:
            fl_set_object_lalign(self.fd_form0.box, n)
        else:
            fl_set_pixmap_align(self.fd_form0.box, n, 3, 3)


    def inside_cb(self, pobj, data):

        if fl_get_button(pobj):
            newalign = fl_get_object_lalign(self.fd_form0.box)
            newalign |= FL_ALIGN_INSIDE
            fl_set_object_lalign(self.fd_form0.box, newalign)
            #self.fd_form0.box.contents.align |= FL_ALIGN_INSIDE
        else:
            newalign = fl_get_object_lalign(self.fd_form0.box)
            newalign &= ~ FL_ALIGN_INSIDE
            fl_set_object_lalign(self.fd_form0.box, newalign)
            #self.fd_form0.box.contents.align &= ~FL_ALIGN_INSIDE

        if TEST_PIXMAP_ALIGN:
            fl_set_pixmap_align(self.fd_form0.box, fl_get_object_lalign(self.fd_form0.box), 3, 3)
        else:
            fl_redraw_form(self.fd_form0.form0)


    def create_form_form0(self):

        fdui = FD_form0()

        fdui.form0 = fl_bgn_form(FL_NO_BOX, 351, 180)
        pobj = fl_add_box(FL_UP_BOX, 0, 0, 351, 180, "")

        if not TEST_PIXMAP_ALIGN:
            fdui.box = fl_add_box(FL_UP_BOX, 190, 40, 90, 55,
                                 "This is\na label")
        else:
            fdui.box = fl_add_pixmap(FL_NORMAL_PIXMAP, 190, 35, 90, 60, "")
            fl_set_pixmap_file(fdui.box, "crab.xpm")
            fl_set_object_boxtype(fdui.box, FL_UP_BOX)

        fdui.inside = fl_add_lightbutton(FL_PUSH_BUTTON, 20, 125, 90, 30,
                                        "Inside")
        fl_set_object_callback(fdui.inside, self.inside_cb, 0)

        fl_bgn_group()

        pobj = fl_add_button(FL_RADIO_BUTTON, 20, 20, 30, 30, "@#7->")
        fl_set_object_lcol(pobj, FL_BLUE)
        fl_set_object_callback(pobj, self.align_cb, FL_ALIGN_LEFT_TOP)

        pobj = fl_add_button(FL_RADIO_BUTTON, 50, 20, 30, 30, "@#8->")
        fl_set_object_lcol(pobj, FL_BLUE)
        fl_set_object_callback(pobj, self.align_cb, FL_ALIGN_TOP)

        pobj = fl_add_button(FL_RADIO_BUTTON, 80, 20, 30, 30, "@#9->")
        fl_set_object_lcol(pobj, FL_BLUE)
        fl_set_object_callback(pobj, self.align_cb, FL_ALIGN_RIGHT_TOP)

        pobj = fl_add_button(FL_RADIO_BUTTON, 80, 50, 30, 30, "@#->")
        fl_set_object_lcol(pobj, FL_BLUE)
        fl_set_object_callback(pobj, self.align_cb, FL_ALIGN_RIGHT)

        fdui.center_ = fl_add_button(FL_RADIO_BUTTON, 50, 50, 30, 30,
                                       "@circle")
        fl_set_object_lcol(fdui.center_, FL_RED)
        fl_set_object_callback(fdui.center_, self.align_cb, FL_ALIGN_CENTER)

        pobj = fl_add_button(FL_RADIO_BUTTON, 20, 50, 30, 30, "@#<-")
        fl_set_object_lcol(pobj, FL_BLUE)
        fl_set_object_callback(pobj, self.align_cb, FL_ALIGN_LEFT)

        pobj = fl_add_button(FL_RADIO_BUTTON, 20, 80, 30, 30, "@#1->")
        fl_set_object_lcol(pobj, FL_BLUE)
        fl_set_object_callback(pobj, self.align_cb, FL_ALIGN_LEFT_BOTTOM)

        pobj = fl_add_button(FL_RADIO_BUTTON, 50, 80, 30, 30, "@#2->")
        fl_set_object_lcol(pobj, FL_BLUE)
        fl_set_object_callback(pobj, self.align_cb, FL_ALIGN_BOTTOM)

        pobj = fl_add_button(FL_RADIO_BUTTON, 80, 80, 30, 30, "@#3->")
        fl_set_object_lcol(pobj, FL_BLUE)
        fl_set_object_callback(pobj, self.align_cb, FL_ALIGN_RIGHT_BOTTOM)

        fl_end_group()

        pobj = fl_add_button(FL_NORMAL_BUTTON, 200, 135, 70, 30, "Done")

        fl_end_form()

        return fdui




if __name__ == '__main__':
    Flalignpixmap(len(sys.argv), sys.argv)

