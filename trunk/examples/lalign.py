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
import xformslib as xfl


# Forms and Objects
TEST_PIXMAP_ALIGN = False
#TEST_PIXMAP_ALIGN = True


class FD_form0(object):
    form0 = None
    vdata = None
    ldata = None
    box = None
    inside = None
    center_ = None


class Flalign(object):

    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.fd_form0 = self.create_form_form0()

        # fill-in form initialization code
        xfl.fl_set_form_dblbuffer(self.fd_form0.form0, 1)
        align = xfl.fl_get_object_lalign(self.fd_form0.box) | \
                xfl.FL_ALIGN_INSIDE
        if align != xfl.fl_get_object_lalign(self.fd_form0.box):
            xfl.fl_set_button(self.fd_form0.inside, 1)

        # show the first form
        xfl.fl_show_form(self.fd_form0.form0, xfl.FL_PLACE_FREE, \
                     xfl.FL_FULLBORDER, "form0")

        xfl.fl_do_forms()


    def align_cb(self, pobj, n):
        if xfl.fl_get_button(self.fd_form0.inside):
            n |= xfl.FL_ALIGN_INSIDE
        if not TEST_PIXMAP_ALIGN:
            xfl.fl_set_object_lalign(self.fd_form0.box, n)
        else:
            xfl.fl_set_pixmap_align(self.fd_form0.box, n, 3, 3)


    def inside_cb(self, pobj, data):

        if xfl.fl_get_button(pobj):
            newalign = xfl.fl_get_object_lalign(self.fd_form0.box)
            newalign |= xfl.FL_ALIGN_INSIDE
            xfl.fl_set_object_lalign(self.fd_form0.box, newalign)
            #fd_form0.box.contents.align |= xfl.FL_ALIGN_INSIDE
        else:
            newalign = xfl.fl_get_object_lalign(self.fd_form0.box)
            newalign &= ~xfl.FL_ALIGN_INSIDE
            xfl.fl_set_object_lalign(self.fd_form0.box, newalign)
            #fd_form0.box.contents.align &= ~xfl.FL_ALIGN_INSIDE

        if TEST_PIXMAP_ALIGN:
            xfl.fl_set_pixmap_align(self.fd_form0.box, \
                    xfl.fl_get_object_lalign(self.fd_form0.box), 3, 3)
        else:
            xfl.fl_redraw_form(self.fd_form0.form0)



    def create_form_form0(self):

        fdui = FD_form0()

        fdui.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 351, 180)

        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 351, 180, "")

        if not TEST_PIXMAP_ALIGN:
            fdui.box = xfl.fl_add_box(xfl.FL_UP_BOX, 190, 40, 90, 55,
                                  "This is\na label")
        else:
            fdui.box = xfl.fl_add_pixmap(xfl.FL_NORMAL_PIXMAP, 190, 35, \
                    90, 60, "")
            xfl.fl_set_pixmap_file(fdui.box, "crab.xpm")
            xfl.fl_set_object_boxtype(fdui.box, xfl.FL_UP_BOX)

        fdui.inside = xfl.fl_add_lightbutton(xfl.FL_PUSH_BUTTON, 20, 125, \
                90, 30, "Inside")
        xfl.fl_set_object_callback(fdui.inside, self.inside_cb, 0)

        xfl.fl_bgn_group()

        pobj = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 20, 20, 30, 30, "@#7->")
        xfl.fl_set_object_lcol(pobj, xfl.FL_BLUE)
        xfl.fl_set_object_callback(pobj, self.align_cb, xfl.FL_ALIGN_LEFT_TOP)

        pobj = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 50, 20, 30, 30, "@#8->")
        xfl.fl_set_object_lcol(pobj, xfl.FL_BLUE)
        xfl.fl_set_object_callback(pobj, self.align_cb, xfl.FL_ALIGN_TOP)

        pobj = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 80, 20, 30, 30, "@#9->")
        xfl.fl_set_object_lcol(pobj, xfl.FL_BLUE)
        xfl.fl_set_object_callback(pobj, self.align_cb, xfl.FL_ALIGN_RIGHT_TOP)

        pobj = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 80, 50, 30, 30, "@#->")
        xfl.fl_set_object_lcol(pobj, xfl.FL_BLUE)
        xfl.fl_set_object_callback(pobj, self.align_cb, xfl.FL_ALIGN_RIGHT)

        fdui.center_ = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 50, 50, 30, 30,
                                   "@circle")
        xfl.fl_set_object_lcol(fdui.center_, xfl.FL_RED)
        xfl.fl_set_object_callback(fdui.center_, self.align_cb, \
                xfl.FL_ALIGN_CENTER)

        pobj = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 20, 50, 30, 30, "@#<-")
        xfl.fl_set_object_lcol(pobj, xfl.FL_BLUE)
        xfl.fl_set_object_callback(pobj, self.align_cb, xfl.FL_ALIGN_LEFT)

        pobj = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 20, 80, 30, 30, "@#1->")
        xfl.fl_set_object_lcol(pobj, xfl.FL_BLUE)
        xfl.fl_set_object_callback(pobj, self.align_cb, \
                xfl.FL_ALIGN_LEFT_BOTTOM)

        pobj = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 50, 80, 30, 30, "@#2->")
        xfl.fl_set_object_lcol(pobj, xfl.FL_BLUE)
        xfl.fl_set_object_callback(pobj, self.align_cb, xfl.FL_ALIGN_BOTTOM)

        pobj = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 80, 80, 30, 30, "@#3->")
        xfl.fl_set_object_lcol(pobj, xfl.FL_BLUE)
        xfl.fl_set_object_callback(pobj, self.align_cb, \
                xfl.FL_ALIGN_RIGHT_BOTTOM)

        xfl.fl_end_group()

        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 200, 135, 70, 30, \
                "Done")

        xfl.fl_end_form()

        return fdui



if __name__ == '__main__':
    print("********* lalign.py *********")
    appl = Flalign(len(sys.argv), sys.argv)

