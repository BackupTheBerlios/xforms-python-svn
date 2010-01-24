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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flscrollbar import *
from xformslib.flmisc import *
from xformslib.xfdata import *



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

        fl_initialize(lsysargv, sysargv, 0, 0, 0)
        self.fd_scb = self.create_form_scb()

        fl_show_form(self.fd_scb.scb, FL_PLACE_CENTERFREE, \
                        FL_FULLBORDER, "form0")

        fl_do_forms()
        fl_finish()


    def create_form_scb(self):

        fdui = FD_scb()

        fdui.scb = fl_bgn_form(FL_NO_BOX, 470, 230)

        pobj = fl_add_box(FL_UP_BOX, 0, 0, 470, 230, "")

        fdui.hor = fl_add_scrollbar(FL_HOR_SCROLLBAR, 30, 15, 230, 17, \
                                    "HOR_SCROLLBAR")
        fl_set_object_lsize(fdui.hor, FL_TINY_SIZE)
        fl_set_object_resize(fdui.hor, FL_RESIZE_ALL)
        fl_set_object_callback(fdui.hor, self.noop_cb, 0)

        fdui.hor_thin = fl_add_scrollbar(FL_HOR_THIN_SCROLLBAR, 30, 60, \
                                         230, 18, "HOR_THIN_SCROLLBAR")
        fl_set_object_boxtype(fdui.hor_thin, FL_DOWN_BOX)
        fl_set_object_lsize(fdui.hor_thin, FL_TINY_SIZE)
        fl_set_object_resize(fdui.hor_thin, FL_RESIZE_ALL)
        fl_set_object_callback(fdui.hor_thin, self.noop_cb, 0)
        fl_set_scrollbar_value(fdui.hor_thin, 0.11)

        fdui.hor_nice = fl_add_scrollbar(FL_HOR_NICE_SCROLLBAR, 30, 110, \
                                         230, 18, "HOR_NICE_SCROLLBAR")
        fl_set_object_boxtype(fdui.hor_nice, FL_FRAME_BOX)
        fl_set_object_lsize(fdui.hor_nice, FL_TINY_SIZE)
        fl_set_object_resize(fdui.hor_nice, FL_RESIZE_ALL)
        fl_set_object_callback(fdui.hor_nice, self.noop_cb, 0)

        fdui.vert = fl_add_scrollbar(FL_VERT_SCROLLBAR, 300, 10, 17, 185, "")
        fl_set_object_resize(fdui.vert, FL_RESIZE_ALL)
        fl_set_object_callback(fdui.vert, self.noop_cb, 0)

        fdui.vert_thin = fl_add_scrollbar(FL_VERT_THIN_SCROLLBAR, 338, 10, \
                                          17, 185, "")
        fl_set_object_boxtype(fdui.vert_thin, FL_DOWN_BOX)
        fl_set_object_resize(fdui.vert_thin, FL_RESIZE_ALL)
        fl_set_object_callback(fdui.vert_thin, self.noop_cb, 0)

        fdui.hide = fl_add_button(FL_NORMAL_BUTTON, 20, 195, 80, 25, "Hide")
        fl_set_object_lalign(fdui.hide, FL_ALIGN_CENTER)
        fl_set_object_callback(fdui.hide, self.hide_cb, 0)

        fdui.deactivate = fl_add_button(FL_NORMAL_BUTTON, 100, 195, \
                                        80, 25, "Deactivate")
        fl_set_object_lalign(fdui.deactivate, FL_ALIGN_CENTER)
        fl_set_object_callback(fdui.deactivate, self.deactivate_cb, 0)

        pobj = fl_add_button(FL_NORMAL_BUTTON, 200, 195, 80, 25, "Done")
        fl_set_object_lalign(pobj, FL_ALIGN_CENTER)
        fl_set_object_callback(pobj, self.done_cb, 0)

        fdui.vert_nice = fl_add_scrollbar(FL_VERT_NICE_SCROLLBAR, 370, 10, \
                                          17, 185, "")
        fl_set_object_boxtype(fdui.vert_nice, FL_FRAME_BOX)
        fl_set_object_resize(fdui.vert_nice, FL_RESIZE_ALL)
        fl_set_object_callback(fdui.vert_nice, self.noop_cb, 0)
        fl_set_scrollbar_value(fdui.vert_nice, 1)

        pobj = fl_add_scrollbar(FL_HOR_PLAIN_SCROLLBAR, 30, 155, \
                                230, 18, "HOR_PLAIN_SCROLLBAR")
        fl_set_object_boxtype(pobj, FL_DOWN_BOX)
        fl_set_object_lsize(pobj, FL_TINY_SIZE)
        fl_set_object_resize(pobj, FL_RESIZE_ALL)
        fl_set_object_callback(pobj, self.noop_cb, 0)
        fl_set_scrollbar_value(pobj, 0.77)
        fl_set_scrollbar_size(pobj, 0.20)

        pobj = fl_add_scrollbar(FL_VERT_PLAIN_SCROLLBAR, 410, 10, 17, \
                                185, "")
        fl_set_object_boxtype(pobj, FL_DOWN_BOX)
        fl_set_object_resize(pobj, FL_RESIZE_ALL)
        fl_set_object_callback(pobj, self.noop_cb, 0)
        fl_set_scrollbar_value(pobj, 0.97)
        fl_set_scrollbar_size(pobj, 0.20)

        fl_end_form()

        return fdui


    def hide_cb(self, pobj, data):

        if fl_object_is_visible(self.fd_scb.hor_thin):
            fl_set_object_label(self.fd_scb.hide, "Show")
            fl_hide_object(self.fd_scb.hor_thin)
        else:
            fl_set_object_label(self.fd_scb.hide, "Hide")
            fl_show_object(self.fd_scb.hor_thin)


    def deactivate_cb(self, pobj, data):

        if fl_object_is_active(self.fd_scb.hor_thin):
            fl_set_object_label(self.fd_scb.deactivate, "Activate")
            fl_deactivate_object(self.fd_scb.hor_thin)
        else:
            fl_set_object_label(self.fd_scb.deactivate, "Deactivate")
            fl_activate_object(self.fd_scb.hor_thin)


    def done_cb(self, pobj, data):
        fl_finish()
        sys.exit(0)


    def noop_cb(self, pobj, data):
        pass





if __name__ == '__main__':
    Flscrollbar(len(sys.argv), sys.argv)

