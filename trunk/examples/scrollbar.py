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
import xformslib as xfl



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


class Flscrollbar(object):
    def __init__(self, lsysargv, sysargv):

        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.fd_scb = self.create_form_scb()
        xfl.fl_show_form(self.fd_scb.scb, xfl.FL_PLACE_CENTERFREE, \
                xfl.FL_FULLBORDER, "form0")
        xfl.fl_do_forms()
        xfl.fl_finish()


    def create_form_scb(self):

        fdui = FD_scb()

        fdui.scb = xfl.fl_bgn_form(xfl.FL_NO_BOX, 470, 230)

        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 470, 230, "")
        fdui.hor = xfl.fl_add_scrollbar(xfl.FL_HOR_SCROLLBAR, 30, 15, \
                230, 17, "HOR_SCROLLBAR")
        xfl.fl_set_object_lsize(fdui.hor, xfl.FL_TINY_SIZE)
        xfl.fl_set_object_resize(fdui.hor, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_callback(fdui.hor, self.noop_cb, 0)
        fdui.hor_thin = xfl.fl_add_scrollbar(xfl.FL_HOR_THIN_SCROLLBAR, \
                30, 60, 230, 18, "HOR_THIN_SCROLLBAR")
        xfl.fl_set_object_boxtype(fdui.hor_thin, xfl.FL_DOWN_BOX)
        xfl.fl_set_object_lsize(fdui.hor_thin, xfl.FL_TINY_SIZE)
        xfl.fl_set_object_resize(fdui.hor_thin, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_callback(fdui.hor_thin, self.noop_cb, 0)
        xfl.fl_set_scrollbar_value(fdui.hor_thin, 0.11)
        fdui.hor_nice = xfl.fl_add_scrollbar(xfl.FL_HOR_NICE_SCROLLBAR, \
                30, 110, 230, 18, "HOR_NICE_SCROLLBAR")
        xfl.fl_set_object_boxtype(fdui.hor_nice, xfl.FL_FRAME_BOX)
        xfl.fl_set_object_lsize(fdui.hor_nice, xfl.FL_TINY_SIZE)
        xfl.fl_set_object_resize(fdui.hor_nice, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_callback(fdui.hor_nice, self.noop_cb, 0)
        fdui.vert = xfl.fl_add_scrollbar(xfl.FL_VERT_SCROLLBAR, 300, 10, \
                17, 185, "")
        xfl.fl_set_object_resize(fdui.vert, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_callback(fdui.vert, self.noop_cb, 0)
        fdui.vert_thin = xfl.fl_add_scrollbar(xfl.FL_VERT_THIN_SCROLLBAR, \
                338, 10, 17, 185, "")
        xfl.fl_set_object_boxtype(fdui.vert_thin, xfl.FL_DOWN_BOX)
        xfl.fl_set_object_resize(fdui.vert_thin, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_callback(fdui.vert_thin, self.noop_cb, 0)
        fdui.hide = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 20, 195, \
                80, 25, "Hide")
        xfl.fl_set_object_lalign(fdui.hide, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_callback(fdui.hide, self.hide_cb, 0)
        fdui.deactivate = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 100, 195, \
                80, 25, "Deactivate")
        xfl.fl_set_object_lalign(fdui.deactivate, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_callback(fdui.deactivate, self.deactivate_cb, 0)
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 200, 195, \
                80, 25, "Done")
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_callback(pobj, self.done_cb, 0)
        fdui.vert_nice = xfl.fl_add_scrollbar(xfl.FL_VERT_NICE_SCROLLBAR, \
                370, 10, 17, 185, "")
        xfl.fl_set_object_boxtype(fdui.vert_nice, xfl.FL_FRAME_BOX)
        xfl.fl_set_object_resize(fdui.vert_nice, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_callback(fdui.vert_nice, self.noop_cb, 0)
        xfl.fl_set_scrollbar_value(fdui.vert_nice, 1)
        pobj = xfl.fl_add_scrollbar(xfl.FL_HOR_PLAIN_SCROLLBAR, 30, 155, \
                230, 18, "HOR_PLAIN_SCROLLBAR")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_DOWN_BOX)
        xfl.fl_set_object_lsize(pobj, xfl.FL_TINY_SIZE)
        xfl.fl_set_object_resize(pobj, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_callback(pobj, self.noop_cb, 0)
        xfl.fl_set_scrollbar_value(pobj, 0.77)
        xfl.fl_set_scrollbar_size(pobj, 0.20)
        pobj = xfl.fl_add_scrollbar(xfl.FL_VERT_PLAIN_SCROLLBAR, 410, 10, \
                17, 185, "")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_DOWN_BOX)
        xfl.fl_set_object_resize(pobj, xfl.FL_RESIZE_ALL)
        xfl.fl_set_object_callback(pobj, self.noop_cb, 0)
        xfl.fl_set_scrollbar_value(pobj, 0.97)
        xfl.fl_set_scrollbar_size(pobj, 0.20)

        xfl.fl_end_form()

        return fdui


    def hide_cb(self, pobj, data):
        if xfl.fl_object_is_visible(self.fd_scb.hor_thin):
            xfl.fl_set_object_label(self.fd_scb.hide, "Show")
            xfl.fl_hide_object(self.fd_scb.hor_thin)
        else:
            xfl.fl_set_object_label(self.fd_scb.hide, "Hide")
            xfl.fl_show_object(self.fd_scb.hor_thin)


    def deactivate_cb(self, pobj, data):
        if xfl.fl_object_is_active(self.fd_scb.hor_thin):
            xfl.fl_set_object_label(self.fd_scb.deactivate, "Activate")
            xfl.fl_deactivate_object(self.fd_scb.hor_thin)
        else:
            xfl.fl_set_object_label(self.fd_scb.deactivate, "Deactivate")
            xfl.fl_activate_object(self.fd_scb.hor_thin)


    def done_cb(self, pobj, data):
        xfl.fl_finish()
        sys.exit(0)


    def noop_cb(self, pobj, data):
        pass



if __name__ == '__main__':
    print ("********* scrollbar.py *********")
    Flscrollbar(len(sys.argv), sys.argv)

