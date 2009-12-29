#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  scrollbar.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# scrollbar functionality check-out
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



# Forms and Objects

class FD_scb(object):
    scb = None
    vdata = None
    cdata = ""
    ldata = 0
    hor = None
    hor_thin = None
    hor_nice = None
    vert = None
    vert_thin = None
    hide = None
    deactivate = None
    vert_nice = None



def create_form_scb():

    fdui = FD_scb()

    fdui.scb = xf.fl_bgn_form(xfc.FL_NO_BOX, 470, 230)

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 470, 230, "")

    fdui.hor = xf.fl_add_scrollbar(xfc.FL_HOR_SCROLLBAR, 30, 15, 230, 17, "HOR_SCROLLBAR")
    xf.fl_set_object_lsize(fdui.hor, xfc.FL_TINY_SIZE)
    xf.fl_set_object_resize(fdui.hor, xfc.FL_RESIZE_ALL)
    xf.fl_set_object_callback(fdui.hor, noop_cb, 0)

    fdui.hor_thin = xf.fl_add_scrollbar(xfc.FL_HOR_THIN_SCROLLBAR, 30, 60, 230, 18, "HOR_THIN_SCROLLBAR")
    xf.fl_set_object_boxtype(fdui.hor_thin, xfc.FL_DOWN_BOX)
    xf.fl_set_object_lsize(fdui.hor_thin, xfc.FL_TINY_SIZE)
    xf.fl_set_object_resize(fdui.hor_thin, xfc.FL_RESIZE_ALL)
    xf.fl_set_object_callback(fdui.hor_thin, noop_cb, 0)
    xf.fl_set_scrollbar_value(fdui.hor_thin, 0.11)

    fdui.hor_nice = xf.fl_add_scrollbar(xfc.FL_HOR_NICE_SCROLLBAR, 30, 110, 230, 18, "HOR_NICE_SCROLLBAR")
    xf.fl_set_object_boxtype(fdui.hor_nice, xfc.FL_FRAME_BOX)
    xf.fl_set_object_lsize(fdui.hor_nice, xfc.FL_TINY_SIZE)
    xf.fl_set_object_resize(fdui.hor_nice, xfc.FL_RESIZE_ALL)
    xf.fl_set_object_callback(fdui.hor_nice, noop_cb, 0)

    fdui.vert = xf.fl_add_scrollbar(xfc.FL_VERT_SCROLLBAR, 300, 10, 17, 185, "")
    xf.fl_set_object_resize(fdui.vert, xfc.FL_RESIZE_ALL)
    xf.fl_set_object_callback(fdui.vert, noop_cb, 0)

    fdui.vert_thin = xf.fl_add_scrollbar(xfc.FL_VERT_THIN_SCROLLBAR, 338, 10, 17, 185, "")
    xf.fl_set_object_boxtype(fdui.vert_thin, xfc.FL_DOWN_BOX)
    xf.fl_set_object_resize(fdui.vert_thin, xfc.FL_RESIZE_ALL)
    xf.fl_set_object_callback(fdui.vert_thin, noop_cb, 0)

    fdui.hide = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 20, 195, 80, 25, "Hide")
    xf.fl_set_object_lalign(fdui.hide, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_callback(fdui.hide, hide_cb, 0)

    fdui.deactivate = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 100, 195, 80, 25, "Deactivate")
    xf.fl_set_object_lalign(fdui.deactivate, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_callback(fdui.deactivate, deactivate_cb, 0)

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 200, 195, 80, 25, "Done")
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_callback(pobj, done_cb, 0)

    fdui.vert_nice = xf.fl_add_scrollbar(xfc.FL_VERT_NICE_SCROLLBAR, 370, 10, 17, 185, "")
    xf.fl_set_object_boxtype(fdui.vert_nice, xfc.FL_FRAME_BOX)
    xf.fl_set_object_resize(fdui.vert_nice, xfc.FL_RESIZE_ALL)
    xf.fl_set_object_callback(fdui.vert_nice, noop_cb, 0)
    xf.fl_set_scrollbar_value(fdui.vert_nice, 1)

    pobj = xf.fl_add_scrollbar(xfc.FL_HOR_PLAIN_SCROLLBAR, 30, 155, 230, 18, "HOR_PLAIN_SCROLLBAR")
    xf.fl_set_object_boxtype(pobj, xfc.FL_DOWN_BOX)
    xf.fl_set_object_lsize(pobj, xfc.FL_TINY_SIZE)
    xf.fl_set_object_resize(pobj, xfc.FL_RESIZE_ALL)
    xf.fl_set_object_callback(pobj, noop_cb, 0)
    xf.fl_set_scrollbar_value(pobj, 0.77)
    xf.fl_set_scrollbar_size(pobj, 0.20)

    pobj = xf.fl_add_scrollbar(xfc.FL_VERT_PLAIN_SCROLLBAR, 410, 10, 17, 185, "")
    xf.fl_set_object_boxtype(pobj, xfc.FL_DOWN_BOX)
    xf.fl_set_object_resize(pobj, xfc.FL_RESIZE_ALL)
    xf.fl_set_object_callback(pobj, noop_cb, 0)
    xf.fl_set_scrollbar_value(pobj, 0.97)
    xf.fl_set_scrollbar_size(pobj, 0.20)

    xf.fl_end_form()

    return fdui



def hide_cb(pobj, data):

    if xf.fl_object_is_visible(fd_scb.hor_thin):
        xf.fl_set_object_label(fd_scb.hide, "Show")
        xf.fl_hide_object(fd_scb.hor_thin)
    else:
        xf.fl_set_object_label(fd_scb.hide, "Hide")
        xf.fl_show_object(fd_scb.hor_thin)



def deactivate_cb(pobj, data):

    if xf.fl_object_is_active(fd_scb.hor_thin):
        xf.fl_set_object_label(fd_scb.deactivate, "Activate")
        xf.fl_deactivate_object(fd_scb.hor_thin)
    else:
        xf.fl_set_object_label(fd_scb.deactivate, "Deactivate")
        xf.fl_activate_object(fd_scb.hor_thin)


def done_cb(pobj, data):
    xf.fl_finish()
    sys.exit(0)



def noop_cb(pobj, data):
    pass



def main(lsysargv, sysargv):
    global fd_scb

    xf.fl_initialize(lsysargv, sysargv, 0, 0, 0)
    fd_scb = create_form_scb()

    xf.fl_show_form(fd_scb.scb, xfc.FL_PLACE_CENTERFREE, xfc.FL_FULLBORDER, "form0")

    xf.fl_do_forms()
    xf.fl_finish()

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

