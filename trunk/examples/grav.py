#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  grav.c XForms demo, with some adaptations.
#
#  gravv.c was written by Jens Thoms Toerring <jt@toerring.de>
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flbrowser import *
from xformslib.flmisc import *
from xformslib.xfdata import *




# Forms and Objects

class FD_gravity(object):
    grav = None
    box = None
    rx = None
    ry = None

class FD_grav_data(object):
    box = None
    rx = None
    ry = None
    grav = 0

class FD_help(object):
    help_ = None
    is_shown = 0


def ULC_POS_LEFT_FIXED(pobj):
    if (pobj.contents.nwgravity == FL_NorthWest) or \
     (pobj.contents.nwgravity == FL_West) or \
     (pobj.contents.nwgravity == FL_SouthWest):
        return True
    else:
        return False

def ULC_POS_RIGHT_FIXED(pobj):
    if (pobj.contents.nwgravity == FL_NorthEast) or \
     (pobj.contents.nwgravity == FL_East) or \
     (pobj.contents.nwgravity == FL_SouthEast):
        return True
    else:
        return False

def LRC_POS_LEFT_FIXED(pobj):
    if (pobj.contents.segravity == FL_NorthWest) or \
     (pobj.contents.segravity == FL_West) or \
     (pobj.contents.segravity == FL_SouthWest):
        return True
    else:
        return False

def LRC_POS_RIGHT_FIXED(pobj):
    if (pobj.contents.segravity == FL_NorthEast) or \
     (pobj.contents.segravity == FL_East) or \
     (pobj.contents.segravity == FL_SouthEast):
        return True
    else:
        return False

def HAS_FIXED_HORI_ULC_POS(pobj):
    if ULC_POS_LEFT_FIXED(pobj) or ULC_POS_RIGHT_FIXED(pobj):
        return True
    else:
        return False

def HAS_FIXED_HORI_LRC_POS(pobj):
    if LRC_POS_LEFT_FIXED(pobj) or LRC_POS_RIGHT_FIXED(pobj):
        return True
    else:
        return False

def HAS_FIXED_WIDTH(pobj):
    if HAS_FIXED_HORI_ULC_POS(pobj) and HAS_FIXED_HORI_LRC_POS(pobj):
        return True
    else:
        return False

def ULC_POS_TOP_FIXED(pobj):
    if (pobj.contents.nwgravity == FL_NorthWest) or \
     (pobj.contents.nwgravity == FL_North) or \
     (pobj.contents.nwgravity == FL_NorthEast):
        return True
    else:
        return False

def ULC_POS_BOTTOM_FIXED(pobj):
    if (pobj.contents.nwgravity == FL_SouthWest) or \
     (pobj.contents.nwgravity == FL_South) or \
     (pobj.contents.nwgravity == FL_SouthEast):
        return True
    else:
        return False

def LRC_POS_TOP_FIXED(pobj):
    if (pobj.contents.segravity == FL_NorthWest) or \
     (pobj.contents.segravity == FL_North) or \
     (pobj.contents.segravity == FL_NorthEast):
        return True
    else:
        return False


def LRC_POS_BOTTOM_FIXED(pobj):
    if (pobj.contents.segravity == FL_SouthWest) or \
     (pobj.contents.segravity == FL_South) or \
     (pobj.contents.segravity == FL_SouthEast):
        return True
    else:
        return False


def HAS_FIXED_VERT_ULC_POS(pobj):
    if ULC_POS_TOP_FIXED(pobj) or ULC_POS_BOTTOM_FIXED(pobj):
        return True
    else:
        return False


def HAS_FIXED_VERT_LRC_POS(pobj):
    if LRC_POS_TOP_FIXED(pobj) or LRC_POS_BOTTOM_FIXED(pobj):
        return True
    else:
        return False


def HAS_FIXED_HEIGHT(pobj):
    if HAS_FIXED_VERT_ULC_POS(pobj) and HAS_FIXED_VERT_LRC_POS(pobj):
        return True
    else:
        return False


class Flgrav(object):
    def __init__(self, lsysargv, sysargv):

        self.gd = []
        for u in range(0, 9+1):
            self.gd.append(FD_grav_data())                   #FD_grav_data()*9

        self.gr = [FL_NorthWest, FL_North, FL_NorthEast, \
             FL_West, FL_NoGravity, FL_East, \
             FL_SouthWest, FL_South, FL_SouthEast]
        self.w = 500
        self.h = 400
        self.bw = 200
        self.bh = 200
        #grav = FD_gravity()
        #help_ = FD_help()

        fl_initialize(lsysargv, sysargv, "Gravity Demo", 0, 0)
        self.help_ = self.create_form_help()
        self.grav = self.create_form_gravity(self.help_)
        fl_set_app_mainform(self.grav.grav)

        for i in range (0, 9):
            self.gd[i].box = self.grav.box
            self.gd[i].grav = self.gr[i]
            self.gd[i].rx = self.grav.rx
            self.gd[i].ry = self.grav.ry

        fl_show_form(self.grav.grav, FL_PLACE_CENTER | FL_FREE_SIZE,
                     FL_FULLBORDER, "Gravity Demo")

        fl_do_forms()

        # fl_hide_form(self.grav.grav)
        # fl_free_form(self.grav.grav)

        # if (self.help_->is_shown )
        #    fl_hide_form(self.help_.help_)
        # fl_free_form(self.help_.help_)

        fl_finish()


    def check_resize(self, g):

        fl_set_button(g.rx, g.box.contents.resize & FL_RESIZE_X)
        fl_set_button(g.ry, g.box.contents.resize & FL_RESIZE_Y)

        if HAS_FIXED_WIDTH(g.box):
            fl_set_object_lcol(g.rx, FL_INACTIVE_COL)
        else:
            fl_set_object_lcol(g.rx, FL_BLACK)

        if HAS_FIXED_HEIGHT(g.box):
            fl_set_object_lcol(g.ry, FL_INACTIVE_COL)
        else:
            fl_set_object_lcol(g.ry, FL_BLACK)


    def nw_callback(self, obj, data):

        g = self.gd[data]           # FD_grav_data *g = (FD_grav_data * ) data
        fl_set_object_gravity(g.box, g.grav, g.box.contents.segravity)
        self.check_resize(g)


    def se_callback(self, obj, data):

        g = self.gd[data]            # FD_grav_data *g = (FD_grav_data * ) data
        fl_set_object_gravity(g.box, g.box.contents.nwgravity, g.grav)
        self.check_resize(g)


    def rx_callback(self, obj, data):

        g = self.gd[data]            # FD_grav_data *g = (FD_grav_data * ) data
        r = g.box.contents.resize

        if r & FL_RESIZE_X:
            r &= ~ FL_RESIZE_X
        else:
            r |= FL_RESIZE_X

        fl_set_object_resize(g.box, r)


    def ry_callback(self, obj, data):

        g = self.gd[data]            # FD_grav_data *g = (FD_grav_data * ) data
        r = g.box.contents.resize

        if r & FL_RESIZE_Y:
            r &= ~ FL_RESIZE_Y
        else:
            r |= FL_RESIZE_Y

        fl_set_object_resize(g.box, r)


    def reset_callback(self, obj, data):

        g = self.gd[data]            # FD_grav_data *g = (FD_grav_data * ) data
        fl_set_form_size(g.box.contents.form, self.w, self.h)
        fl_set_object_geometry(g.box, (self.w - self.bw) / 2, \
            (self.h - self.bh) / 2, self.bw, self.bh)


    def help_callback(self, obj, data):

        self.h = self.help_            #FD_help *h = (FD_help * ) data
        if not self.h.is_shown:
            fl_show_form(self.h.help_, FL_PLACE_CENTER | FL_FREE_SIZE, \
                        FL_FULLBORDER, "Gravity Demo Help")
            self.h.is_shown = 1


    def close_callback(self, obj, data):

        self.h = self.help_            #FD_help *h = (FD_help * ) data
        fl_hide_form(self.h.help_)
        self.h.is_shown = 0


    def create_form_gravity(self, help_):

        fdui = FD_gravity()
        label = ["NW", "N", "NE", "W", "-", "E", "SW", "S", "SE"]
        s = 25
        m = 5

        fdui.grav = fl_bgn_form(FL_NO_BOX, 500, 400)

        pobj = fl_add_box(FL_UP_BOX, 0, 0, self.w, self.h, "")
        fl_set_object_bw(pobj, -1)

        fdui.box = fl_add_box(FL_FRAME_BOX, (self.w - self.bw ) / 2, \
            (self.h - self.bh ) / 2, self.bw, self.bh, "")
        fl_set_object_color(fdui.box, FL_GREEN, FL_GREEN)

        fl_bgn_group()
        for i in range(0, 9):
            pobj = fl_add_button(FL_RADIO_BUTTON, s * (i % 3) + m, \
                                s * (i / 3 ) + m, s, s, label[i])
            fl_set_object_bw(pobj, -1)
            fl_set_object_resize(pobj, FL_RESIZE_NONE)
            fl_set_object_gravity(pobj, FL_NorthWest, FL_NorthWest)
            fl_set_object_callback(pobj, self.nw_callback, i)         # long gd+i
            fl_set_object_color(pobj, FL_COL1, FL_MCOL)
            if  fdui.box.contents.nwgravity == self.gr[i]:
                boolval = True
            else:
                boolval = False
            fl_set_button(pobj, boolval)

        fl_end_group()

        fl_bgn_group()
        for i in range (0, 9):
            pobj = fl_add_button(FL_RADIO_BUTTON, s * (i % 3) + self.w - 3 * s \
                - m, s * (i / 3) + self.h - 3 * s - m, s, s, label[i])
            fl_set_object_bw(pobj, -1)
            fl_set_object_resize(pobj, FL_RESIZE_NONE)
            fl_set_object_gravity(pobj, FL_SouthEast, FL_SouthEast)
            fl_set_object_callback(pobj, self.se_callback, i)         # long gd+i
            fl_set_object_color(pobj, FL_COL1, FL_MCOL)
            if fdui.box.contents.segravity == self.gr[i]:
                boolval = True
            else:
                boolval = False
            fl_set_button(pobj, boolval)

        fl_end_group()

        fdui.rx = fl_add_button(FL_PUSH_BUTTON, m, self.h - s - m, 80, s, \
                               "X Resize")
        fl_set_object_bw(fdui.rx, -1)
        fl_set_object_resize(fdui.rx, FL_RESIZE_NONE)
        fl_set_object_gravity(fdui.rx, FL_SouthWest, FL_SouthWest)
        fl_set_object_callback(fdui.rx, self.rx_callback, 0)          # long gd
        fl_set_object_color(fdui.rx, FL_COL1, FL_MCOL)
        fl_set_button(fdui.rx, fdui.box.contents.resize & FL_RESIZE_X)

        fdui.ry = fl_add_button(FL_PUSH_BUTTON, 2 * m + 80, self.h - s - m, \
                               80, s, "Y Resize")
        fl_set_object_bw(fdui.ry, -1)
        fl_set_object_resize(fdui.ry, FL_RESIZE_NONE)
        fl_set_object_gravity(fdui.ry, FL_SouthWest, FL_SouthWest)
        fl_set_object_callback(fdui.ry, self.ry_callback, 0)                          #gd[0])         # long gd
        fl_set_object_color(fdui.ry, FL_COL1, FL_MCOL)
        fl_set_button(fdui.ry, fdui.box.contents.resize & FL_RESIZE_Y)

        pobj = fl_add_button(FL_NORMAL_BUTTON, self.w - 85, 5, 80, s, "Help")
        fl_set_object_bw(pobj, -1)
        fl_set_object_gravity(pobj, FL_NorthEast, FL_NorthEast)
        fl_set_object_callback(pobj, self.help_callback, 0)      # long help_

        pobj = fl_add_button(FL_NORMAL_BUTTON, 200, self.h - s - m,
                            80, s, "Reset")
        fl_set_object_bw(pobj, -1)
        fl_set_object_resize(pobj, FL_RESIZE_NONE)
        fl_set_object_gravity(pobj, FL_South, FL_South)
        fl_set_object_callback(pobj, self.reset_callback, 0)             # long gd

        pobj = fl_add_button(FL_NORMAL_BUTTON, m + 280, self.h - s - m, 80, \
                             s, "Quit")
        fl_set_object_bw(pobj, -1)
        fl_set_object_resize(pobj, FL_RESIZE_NONE)
        fl_set_object_gravity(pobj, FL_South, FL_South)

        fl_end_form()

        return fdui


    def create_form_help(self):

        fdui = FD_help()
        text = ["Gravity and resize settings demonstration",
            "",
            "The interaction between gravity and resize settings",
            "can somtimes be difficult to understand  This pro-",
            "gram allows you to test some of the effects.",
            "",
            "With the sets of buttons in the upper left hand and",
            "lower right hand corner you can set the gravity for",
            "the corresponding corners of the green rectangle.",
            "",
            "With the buttons labeled 'X Resize' and 'Y Resize'",
            "you can set if the rectangle may be scaled in x-",
            "and/or y-direction. Please note that for several",
            "combinations of gravity settings the resizing",
            "settings are not taken into account by XForms. In",
            "these cases the corresponding buttons are grayed",
            "out (but not deactivated)."]

        fdui.help_ = fl_bgn_form(FL_NO_BOX, 345, 325)

        fdui.is_shown = 0

        pobj = fl_add_box(FL_UP_BOX, 0, 0, 345, 325, "")
        fl_set_object_bw(pobj, -1)

        pobj = fl_add_browser(FL_NORMAL_BROWSER, 5, 5, 335, 285, "")
        fl_set_object_bw(pobj, -1)
        fl_set_object_color(pobj, FL_WHITE, FL_WHITE)
        fl_set_object_gravity(pobj, FL_NorthWest, FL_SouthEast)

        for i in range(0, len(text)):           # i < sizeof text / sizeof *text
            fl_add_browser_line(pobj, text[i])

        pobj = fl_add_button(FL_NORMAL_BUTTON, 133, 295, 80, 25, "Close")
        fl_set_object_bw(pobj, -1)
        fl_set_object_gravity(pobj, FL_South, FL_South)
        fl_set_object_resize(pobj, FL_RESIZE_NONE)
        fl_set_object_callback(pobj, self.close_callback, 0)            # fdui

        fl_end_form()

        return fdui




if __name__ == '__main__':
    Flgrav(len(sys.argv), sys.argv)

