#!/usr/bin/env python3

#  This file is part of xforms-python, and it has been ported from
#  grav.c XForms demo, with some adaptations.
#
#  gravv.c was written by Jens Thoms Toerring <jt@toerring.de>
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#

import sys
#sys.path.append("..")
import xformslib as xfl


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
    if (pobj.contents.nwgravity == xfl.FL_NorthWest) or \
            (pobj.contents.nwgravity == xfl.FL_West) or \
            (pobj.contents.nwgravity == xfl.FL_SouthWest):
        return True
    else:
        return False

def ULC_POS_RIGHT_FIXED(pobj):
    if (pobj.contents.nwgravity == xfl.FL_NorthEast) or \
            (pobj.contents.nwgravity == xfl.FL_East) or \
            (pobj.contents.nwgravity == xfl.FL_SouthEast):
        return True
    else:
        return False

def LRC_POS_LEFT_FIXED(pobj):
    if (pobj.contents.segravity == xfl.FL_NorthWest) or \
            (pobj.contents.segravity == xfl.FL_West) or \
            (pobj.contents.segravity == xfl.FL_SouthWest):
        return True
    else:
        return False

def LRC_POS_RIGHT_FIXED(pobj):
    if (pobj.contents.segravity == xfl.FL_NorthEast) or \
            (pobj.contents.segravity == xfl.FL_East) or \
            (pobj.contents.segravity == xfl.FL_SouthEast):
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
    if (pobj.contents.nwgravity == xfl.FL_NorthWest) or \
            (pobj.contents.nwgravity == xfl.FL_North) or \
            (pobj.contents.nwgravity == xfl.FL_NorthEast):
        return True
    else:
        return False

def ULC_POS_BOTTOM_FIXED(pobj):
    if (pobj.contents.nwgravity == xfl.FL_SouthWest) or \
            (pobj.contents.nwgravity == xfl.FL_South) or \
            (pobj.contents.nwgravity == xfl.FL_SouthEast):
        return True
    else:
        return False

def LRC_POS_TOP_FIXED(pobj):
    if (pobj.contents.segravity == xfl.FL_NorthWest) or \
            (pobj.contents.segravity == xfl.FL_North) or \
            (pobj.contents.segravity == xfl.FL_NorthEast):
        return True
    else:
        return False

def LRC_POS_BOTTOM_FIXED(pobj):
    if (pobj.contents.segravity == xfl.FL_SouthWest) or \
            (pobj.contents.segravity == xfl.FL_South) or \
            (pobj.contents.segravity == xfl.FL_SouthEast):
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
            self.gd.append(FD_grav_data())    #FD_grav_data()*9
        self.gr = [xfl.FL_NorthWest, xfl.FL_North, xfl.FL_NorthEast, \
             xfl.FL_West, xfl.FL_NoGravity, xfl.FL_East, \
             xfl.FL_SouthWest, xfl.FL_South, xfl.FL_SouthEast]
        self.w = 500
        self.h = 400
        self.bw = 200
        self.bh = 200
        #grav = FD_gravity()
        #help_ = FD_help()
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.help_ = self.create_form_help()
        self.grav = self.create_form_gravity(self.help_.help_)
        xfl.fl_set_app_mainform(self.grav.grav)
        for i in range (0, 9):
            self.gd[i].box = self.grav.box
            self.gd[i].grav = self.gr[i]
            self.gd[i].rx = self.grav.rx
            self.gd[i].ry = self.grav.ry
        xfl.fl_show_form(self.grav.grav, \
                xfl.FL_PLACE_CENTER | xfl.FL_FREE_SIZE, xfl.FL_FULLBORDER, \
                "Gravity Demo")
        xfl.fl_do_forms()
        # xfl.fl_hide_form(self.grav.grav)
        # xfl.fl_free_form(self.grav.grav)
        # if (self.help_->is_shown )
        #    xfl.fl_hide_form(self.help_.help_)
        # xfl.fl_free_form(self.help_.help_)
        xfl.fl_finish()
        sys.exit(0)


    def check_resize(self, g):
        xfl.fl_set_button(g.rx, g.box.contents.resize & xfl.FL_RESIZE_X)
        xfl.fl_set_button(g.ry, g.box.contents.resize & xfl.FL_RESIZE_Y)
        if HAS_FIXED_WIDTH(g.box):
            xfl.fl_set_object_lcol(g.rx, xfl.FL_INACTIVE_COL)
        else:
            xfl.fl_set_object_lcol(g.rx, xfl.FL_BLACK)

        if HAS_FIXED_HEIGHT(g.box):
            xfl.fl_set_object_lcol(g.ry, xfl.FL_INACTIVE_COL)
        else:
            xfl.fl_set_object_lcol(g.ry, xfl.FL_BLACK)


    def nw_callback(self, obj, data):
        g = self.gd[data]       # FD_grav_data *g = (FD_grav_data * ) data
        xfl.fl_set_object_gravity(g.box, g.grav, g.box.contents.segravity)
        self.check_resize(g)


    def se_callback(self, obj, data):
        g = self.gd[data]       # FD_grav_data *g = (FD_grav_data * ) data
        xfl.fl_set_object_gravity(g.box, g.box.contents.nwgravity, g.grav)
        self.check_resize(g)


    def rx_callback(self, obj, data):
        g = self.gd[data]       # FD_grav_data *g = (FD_grav_data * ) data
        r = g.box.contents.resize
        if r & xfl.FL_RESIZE_X:
            r &= ~ xfl.FL_RESIZE_X
        else:
            r |= xfl.FL_RESIZE_X
        xfl.fl_set_object_resize(g.box, r)


    def ry_callback(self, obj, data):
        g = self.gd[data]       # FD_grav_data *g = (FD_grav_data * ) data
        r = g.box.contents.resize
        if r & xfl.FL_RESIZE_Y:
            r &= ~ xfl.FL_RESIZE_Y
        else:
            r |= xfl.FL_RESIZE_Y
        xfl.fl_set_object_resize(g.box, r)


    def reset_callback(self, obj, data):
        g = self.gd[data]       # FD_grav_data *g = (FD_grav_data * ) data
        xfl.fl_set_form_size(g.box.contents.form, self.w, self.h)
        xfl.fl_set_object_geometry(g.box, (self.w - self.bw) / 2, \
            (self.h - self.bh) / 2, self.bw, self.bh)


    def help_callback(self, obj, data):
        if not self.help_.is_shown:
            xfl.fl_show_form(self.help_.help_, \
                    xfl.FL_PLACE_CENTER | xfl.FL_FREE_SIZE, \
                    xfl.FL_FULLBORDER, "Gravity Demo Help")
            self.help_.is_shown = 1


    def close_callback(self, obj, data):
        xfl.fl_hide_form(self.help_.help_)
        self.help_.is_shown = 0


    def create_form_gravity(self, help_):
        fdui = FD_gravity()
        label = ["NW", "N", "NE", "W", "-", "E", "SW", "S", "SE"]
        s = 25
        m = 5
        fdui.grav = xfl.fl_bgn_form(xfl.FL_FLAT_BOX, 500, 400)
        xfl.fl_fl_set_form_background_color(fdui.grav, xfl.FL_DARKER_COLOR)
        fdui.box = xfl.fl_add_box(xfl.FL_FRAME_BOX, (self.w - self.bw ) / 2, \
                (self.h - self.bh ) / 2, self.bw, self.bh, "")
        xfl.fl_set_object_color(fdui.box, xfl.FL_GREEN, xfl.FL_GREEN)
        xfl.fl_bgn_group()
        for i in range(0, 9):
            pobj = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, s * (i % 3) + m, \
                    s * (i / 3 ) + m, s, s, label[i])
            xfl.fl_set_object_bw(pobj, -1)
            xfl.fl_set_object_resize(pobj, xfl.FL_RESIZE_NONE)
            xfl.fl_set_object_gravity(pobj, xfl.FL_NorthWest, xfl.FL_NorthWest)
            xfl.fl_set_object_callback(pobj, self.nw_callback, i)   # long gd+i
            xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_MCOL)
            if fdui.box.contents.nwgravity == self.gr[i]:
                boolval = True
            else:
                boolval = False
            xfl.fl_set_button(pobj, boolval)
        xfl.fl_end_group()
        xfl.fl_bgn_group()
        for i in range (0, 9):
            pobj = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, \
                    s * (i % 3) + self.w - 3 * s - m, \
                    s * (i / 3) + self.h - 3 * s - m, s, s, label[i])
            xfl.fl_set_object_bw(pobj, -1)
            xfl.fl_set_object_resize(pobj, xfl.FL_RESIZE_NONE)
            xfl.fl_set_object_gravity(pobj, xfl.FL_SouthEast, xfl.FL_SouthEast)
            xfl.fl_set_object_callback(pobj, self.se_callback, i)   # long gd+i
            xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_MCOL)
            if fdui.box.contents.segravity == self.gr[i]:
                boolval = True
            else:
                boolval = False
            xfl.fl_set_button(pobj, boolval)
        xfl.fl_end_group()
        fdui.rx = xfl.fl_add_button(xfl.FL_PUSH_BUTTON, m, self.h - s - m, \
                80, s, "X Resize")
        xfl.fl_set_object_bw(fdui.rx, -1)
        xfl.fl_set_object_resize(fdui.rx, xfl.FL_RESIZE_NONE)
        xfl.fl_set_object_gravity(fdui.rx, xfl.FL_SouthWest, xfl.FL_SouthWest)
        xfl.fl_set_object_callback(fdui.rx, self.rx_callback, 0)    # long gd
        xfl.fl_set_object_color(fdui.rx, xfl.FL_COL1, xfl.FL_MCOL)
        xfl.fl_set_button(fdui.rx, fdui.box.contents.resize & xfl.FL_RESIZE_X)
        fdui.ry = xfl.fl_add_button(xfl.FL_PUSH_BUTTON, 2 * m + 80, \
                self.h - s - m, 80, s, "Y Resize")
        xfl.fl_set_object_bw(fdui.ry, -1)
        xfl.fl_set_object_resize(fdui.ry, xfl.FL_RESIZE_NONE)
        xfl.fl_set_object_gravity(fdui.ry, xfl.FL_SouthWest, xfl.FL_SouthWest)
        xfl.fl_set_object_callback(fdui.ry, self.ry_callback, 0)                          #gd[0])         # long gd
        xfl.fl_set_object_color(fdui.ry, xfl.FL_COL1, xfl.FL_MCOL)
        xfl.fl_set_button(fdui.ry, fdui.box.contents.resize & xfl.FL_RESIZE_Y)
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, self.w - 85, 5, 80, \
                s, "Help")
        xfl.fl_set_object_bw(pobj, -1)
        xfl.fl_set_object_gravity(pobj, xfl.FL_NorthEast, xfl.FL_NorthEast)
        xfl.fl_set_object_callback(pobj, self.help_callback, 0)   # long help_
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 200, self.h - s - m,
                80, s, "Reset")
        xfl.fl_set_object_bw(pobj, -1)
        xfl.fl_set_object_resize(pobj, xfl.FL_RESIZE_NONE)
        xfl.fl_set_object_gravity(pobj, xfl.FL_South, xfl.FL_South)
        xfl.fl_set_object_callback(pobj, self.reset_callback, 0)   # long gd
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, m + 280, \
                self.h - s - m, 80, s, "Quit")
        xfl.fl_set_object_bw(pobj, -1)
        xfl.fl_set_object_resize(pobj, xfl.FL_RESIZE_NONE)
        xfl.fl_set_object_gravity(pobj, xfl.FL_South, xfl.FL_South)
        xfl.fl_end_form()
        return fdui


    def create_form_help(self):
        fdui = FD_help()
        text = ["Gravity and resize settings demonstration", "",
            "The interaction between gravity and resize settings",
            "can sometimes be difficult to understand  This pro-",
            "gram allows you to test some of the effects.", "",
            "With the sets of buttons in the upper left hand and",
            "lower right hand corner you can set the gravity for",
            "the corresponding corners of the green rectangle.", "",
            "With the buttons labeled 'X Resize' and 'Y Resize'",
            "you can set if the rectangle may be scaled in x-",
            "and/or y-direction. Please note that for several",
            "combinations of gravity settings the resizing",
            "settings are not taken into account by XForms. In",
            "these cases the corresponding buttons are grayed",
            "out (but not deactivated)."]
        fdui.help_ = xfl.fl_bgn_form(xfl.FL_FLAT_BOX, 345, 325)
        fdui.is_shown = 0
        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 345, 325, "")
        xfl.fl_set_object_bw(pobj, -1)
        pobj = xfl.fl_add_browser(xfl.FL_NORMAL_BROWSER, 5, 5, 335, 285, "")
        xfl.fl_set_object_bw(pobj, -1)
        xfl.fl_set_object_color(pobj, xfl.FL_WHITE, xfl.FL_WHITE)
        xfl.fl_set_object_gravity(pobj, xfl.FL_NorthWest, xfl.FL_SouthEast)
        for i in range(0, len(text)):   # i < sizeof text / sizeof *text
            xfl.fl_add_browser_line(pobj, text[i])
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 133, 295, 80, 25, \
                "Close")
        xfl.fl_set_object_bw(pobj, -1)
        xfl.fl_set_object_gravity(pobj, xfl.FL_South, xfl.FL_South)
        xfl.fl_set_object_resize(pobj, xfl.FL_RESIZE_NONE)
        xfl.fl_set_object_callback(pobj, self.close_callback, 0)   # fdui
        xfl.fl_end_form()
        return fdui


if __name__ == '__main__':
    print("********* grav.py *********")
    Flgrav(len(sys.argv), sys.argv)
