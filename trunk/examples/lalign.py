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
from xformslib import library as xf
from xformslib import xfdata as xfc


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



def main(lsysargv, sysargv):
    global fd_form0

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    fd_form0 = create_form_form0()

    # fill-in form initialization code

    xf.fl_set_form_dblbuffer(fd_form0.form0, 1)
    align = fd_form0.box.contents.align | xfc.FL_ALIGN_INSIDE
    if align != fd_form0.box.contents.align:
        xf.fl_set_button(fd_form0.inside, 1)

    # show the first form
    xf.fl_show_form(fd_form0.form0, xfc.FL_PLACE_FREE, \
                    xfc.FL_FULLBORDER, "form0")

    xf.fl_do_forms()
    return 0



def align_cb(pobj, n):

    if xf.fl_get_button(fd_form0.inside):
        n |= xfc.FL_ALIGN_INSIDE

    if TEST_PIXMAP_ALIGN:
        xf.fl_set_object_lalign(fd_form0.box, n)
    else:
        xf.fl_set_pixmap_align(fd_form0.box, n, 3, 3)



def inside_cb(pobj, data):

    if xf.fl_get_button(pobj):
        fd_form0.box.contents.align |= xfc.FL_ALIGN_INSIDE
    else:
        fd_form0.box.contents.align &= ~xfc.FL_ALIGN_INSIDE

    if TEST_PIXMAP_ALIGN:
        xf.fl_set_pixmap_align(fd_form0.box, fd_form0.box.contents.align, 3, 3)
    else:
        xf.fl_redraw_form(fd_form0.form0)



def create_form_form0():

    fdui = FD_form0()

    fdui.form0 = xf.fl_bgn_form(xfc.FL_NO_BOX, 351, 180)

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 351, 180, "")

    if TEST_PIXMAP_ALIGN:
        fdui.box = xf.fl_add_box(xfc.FL_UP_BOX, 190, 40, 90, 55,
                                 "This is\na label")
    else:
        fdui.box = xf.fl_add_pixmap(xfc.FL_NORMAL_PIXMAP, 190, 35, 90, 60, "")
        xf.fl_set_pixmap_file(fdui.box, "crab.xpm")
        xf.fl_set_object_boxtype(fdui.box, xfc.FL_UP_BOX)

    fdui.inside = xf.fl_add_lightbutton(xfc.FL_PUSH_BUTTON, 20, 125, 90, 30,
                                        "Inside")
    xf.fl_set_object_callback(fdui.inside, inside_cb, 0)

    xf.fl_bgn_group()

    pobj = xf.fl_add_button(xfc.FL_RADIO_BUTTON, 20, 20, 30, 30, "@#7->")
    xf.fl_set_object_lcol(pobj, xfc.FL_BLUE)
    xf.fl_set_object_callback(pobj, align_cb, xfc.FL_ALIGN_LEFT_TOP)

    pobj = xf.fl_add_button(xfc.FL_RADIO_BUTTON, 50, 20, 30, 30, "@#8->")
    xf.fl_set_object_lcol(pobj, xfc.FL_BLUE)
    xf.fl_set_object_callback(pobj, align_cb, xfc.FL_ALIGN_TOP)

    pobj = xf.fl_add_button(xfc.FL_RADIO_BUTTON, 80, 20, 30, 30, "@#9->")
    xf.fl_set_object_lcol(pobj, xfc.FL_BLUE)
    xf.fl_set_object_callback(pobj, align_cb, xfc.FL_ALIGN_RIGHT_TOP)

    pobj = xf.fl_add_button(xfc.FL_RADIO_BUTTON, 80, 50, 30, 30, "@#->")
    xf.fl_set_object_lcol(pobj, xfc.FL_BLUE)
    xf.fl_set_object_callback(pobj, align_cb, xfc.FL_ALIGN_RIGHT)

    fdui.center_ = xf.fl_add_button(xfc.FL_RADIO_BUTTON, 50, 50, 30, 30,
                                   "@circle")
    xf.fl_set_object_lcol(fdui.center_, xfc.FL_RED)
    xf.fl_set_object_callback(fdui.center_, align_cb, xfc.FL_ALIGN_CENTER)

    pobj = xf.fl_add_button(xfc.FL_RADIO_BUTTON, 20, 50, 30, 30, "@#<-")
    xf.fl_set_object_lcol(pobj, xfc.FL_BLUE)
    xf.fl_set_object_callback(pobj, align_cb, xfc.FL_ALIGN_LEFT)

    pobj = xf.fl_add_button(xfc.FL_RADIO_BUTTON, 20, 80, 30, 30, "@#1->")
    xf.fl_set_object_lcol(pobj, xfc.FL_BLUE)
    xf.fl_set_object_callback(pobj, align_cb, xfc.FL_ALIGN_LEFT_BOTTOM)

    pobj = xf.fl_add_button(xfc.FL_RADIO_BUTTON, 50, 80, 30, 30, "@#2->")
    xf.fl_set_object_lcol(pobj, xfc.FL_BLUE)
    xf.fl_set_object_callback(pobj, align_cb, xfc.FL_ALIGN_BOTTOM)

    pobj = xf.fl_add_button(xfc.FL_RADIO_BUTTON, 80, 80, 30, 30, "@#3->")
    xf.fl_set_object_lcol(pobj, xfc.FL_BLUE)
    xf.fl_set_object_callback(pobj, align_cb, xfc.FL_ALIGN_RIGHT_BOTTOM)

    xf.fl_end_group()

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 200, 135, 70, 30, "Done")

    xf.fl_end_form()

    return fdui



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

