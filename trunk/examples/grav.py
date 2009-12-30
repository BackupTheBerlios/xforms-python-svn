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
from xformslib import library as xf
from xformslib import xfdata as xfc



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


gd = []
for u in range(0, 9+1):
    gd.append(FD_grav_data())                   #FD_grav_data()*9

g = [xfc.FL_NorthWest, xfc.FL_North, xfc.FL_NorthEast, \
     xfc.FL_West, xfc.FL_NoGravity, xfc.FL_East, \
     xfc.FL_SouthWest, xfc.FL_South, xfc.FL_SouthEast]
w = 500
h = 400
bw = 200
bh = 200


def ULC_POS_LEFT_FIXED(pobj):
    if (pobj.contents.nwgravity == xfc.FL_NorthWest) or \
       (pobj.contents.nwgravity == xfc.FL_West) or \
       (pobj.contents.nwgravity == xfc.FL_SouthWest):
        return True
    else:
        return False

def ULC_POS_RIGHT_FIXED(pobj):
    if (pobj.contents.nwgravity == xfc.FL_NorthEast) or \
       (pobj.contents.nwgravity == xfc.FL_East) or \
       (pobj.contents.nwgravity == xfc.FL_SouthEast):
        return True
    else:
        return False

def LRC_POS_LEFT_FIXED(pobj):
    if (pobj.contents.segravity == xfc.FL_NorthWest) or \
       (pobj.contents.segravity == xfc.FL_West) or \
       (pobj.contents.segravity == xfc.FL_SouthWest):
        return True
    else:
        return False

def LRC_POS_RIGHT_FIXED(pobj):
    if (pobj.contents.segravity == xfc.FL_NorthEast) or \
       (pobj.contents.segravity == xfc.FL_East) or \
       (pobj.contents.segravity == xfc.FL_SouthEast):
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
    if (pobj.contents.nwgravity == xfc.FL_NorthWest) or \
       (pobj.contents.nwgravity == xfc.FL_North) or \
       (pobj.contents.nwgravity == xfc.FL_NorthEast):
        return True
    else:
        return False

def ULC_POS_BOTTOM_FIXED(pobj):
    if (pobj.contents.nwgravity == xfc.FL_SouthWest) or \
       (pobj.contents.nwgravity == xfc.FL_South) or \
       (pobj.contents.nwgravity == xfc.FL_SouthEast):
        return True
    else:
        return False

def LRC_POS_TOP_FIXED(pobj):
    if (pobj.contents.segravity == xfc.FL_NorthWest) or \
       (pobj.contents.segravity == xfc.FL_North) or \
       (pobj.contents.segravity == xfc.FL_NorthEast):
        return True
    else:
        return False

def LRC_POS_BOTTOM_FIXED(pobj):
    if (pobj.contents.segravity == xfc.FL_SouthWest) or \
       (pobj.contents.segravity == xfc.FL_South) or \
       (pobj.contents.segravity == xfc.FL_SouthEast):
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




def check_resize(g):

    xf.fl_set_button(g.rx, g.box.contents.resize & xfc.FL_RESIZE_X)
    xf.fl_set_button(g.ry, g.box.contents.resize & xfc.FL_RESIZE_Y)

    if HAS_FIXED_WIDTH(g.box):
        xf.fl_set_object_lcol(g.rx, xfc.FL_INACTIVE_COL)
    else:
        xf.fl_set_object_lcol(g.rx, xfc.FL_BLACK)

    if HAS_FIXED_HEIGHT(g.box):
        xf.fl_set_object_lcol(g.ry, xfc.FL_INACTIVE_COL)
    else:
        xf.fl_set_object_lcol(g.ry, xfc.FL_BLACK)



def nw_callback(obj, data):

    g = gd[data]           # FD_grav_data *g = (FD_grav_data * ) data
    xf.fl_set_object_gravity(g.box, g.grav, g.box.contents.segravity)
    check_resize(g)


def se_callback(obj, data):

    g = gd[data]            # FD_grav_data *g = (FD_grav_data * ) data
    xf.fl_set_object_gravity(g.box, g.box.contents.nwgravity, g.grav)
    check_resize(g)



def rx_callback(obj, data):

    g = gd[data]            # FD_grav_data *g = (FD_grav_data * ) data
    r = g.box.contents.resize

    if r & xfc.FL_RESIZE_X:
        r &= ~ xfc.FL_RESIZE_X
    else:
        r |= xfc.FL_RESIZE_X

    xf.fl_set_object_resize(g.box, r)


def ry_callback(obj, data):

    g = gd[data]            # FD_grav_data *g = (FD_grav_data * ) data
    r = g.box.contents.resize

    if r & xfc.FL_RESIZE_Y:
        r &= ~ xfc.FL_RESIZE_Y
    else:
        r |= xfc.FL_RESIZE_Y

    xf.fl_set_object_resize(g.box, r)



def reset_callback(obj, data):

    g = gd[data]            # FD_grav_data *g = (FD_grav_data * ) data
    xf.fl_set_form_size(g.box.contents.form, w, h)
    xf.fl_set_object_geometry(g.box, (w - bw) / 2, (h - bh) / 2, bw, bh)




def help_callback(obj, data):

    h = help_            #FD_help *h = (FD_help * ) data
    if not h.is_shown:
        xf.fl_show_form(h.help_, xfc.FL_PLACE_CENTER | xfc.FL_FREE_SIZE, \
                        xfc.FL_FULLBORDER, "Gravity Demo Help")
        h.is_shown = 1



def close_callback(obj, data):

    h = help_            #FD_help *h = (FD_help * ) data
    xf.fl_hide_form(h.help_)
    h.is_shown = 0



def create_form_gravity(help_):

    fdui = FD_gravity()
    label = ["NW", "N", "NE", "W", "-", "E", "SW", "S", "SE"]
    s = 25
    m = 5

    fdui.grav = xf.fl_bgn_form(xfc.FL_NO_BOX, 500, 400)

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, w, h, "")
    xf.fl_set_object_bw(pobj, -1)

    fdui.box = xf.fl_add_box(xfc.FL_FRAME_BOX, (w - bw ) / 2, (h - bh ) / 2,
                             bw, bh, "")
    xf.fl_set_object_color(fdui.box, xfc.FL_GREEN, xfc.FL_GREEN)

    xf.fl_bgn_group()
    for i in range(0, 9):
        pobj = xf.fl_add_button(xfc.FL_RADIO_BUTTON, s * (i % 3) + m, \
                                s * (i / 3 ) + m, s, s, label[i])
        xf.fl_set_object_bw(pobj, -1)
        xf.fl_set_object_resize(pobj, xfc.FL_RESIZE_NONE)
        xf.fl_set_object_gravity(pobj, xfc.FL_NorthWest, xfc.FL_NorthWest)
        xf.fl_set_object_callback(pobj, nw_callback, i)                         #gd[i])          # long gd+i
        xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_MCOL)
        if  fdui.box.contents.nwgravity == g[i]:
            boolval = True
        else:
            boolval = False
        xf.fl_set_button(pobj, boolval)

    xf.fl_end_group()

    xf.fl_bgn_group()
    for i in range (0, 9):
        pobj = xf.fl_add_button(xfc.FL_RADIO_BUTTON, s * (i % 3) + w - 3 * s - m, \
                                s * (i / 3) + h - 3 * s - m, s, s, label[i])
        xf.fl_set_object_bw(pobj, -1)
        xf.fl_set_object_resize(pobj, xfc.FL_RESIZE_NONE)
        xf.fl_set_object_gravity(pobj, xfc.FL_SouthEast, xfc.FL_SouthEast)
        xf.fl_set_object_callback(pobj, se_callback, i)                 #gd[i])          # long gd+i
        xf.fl_set_object_color(pobj, xfc.FL_COL1, xfc.FL_MCOL)
        if  fdui.box.contents.segravity == g[i]:
            boolval = True
        else:
            boolval = False
        xf.fl_set_button(pobj, boolval)


    xf.fl_end_group()

    fdui.rx = xf.fl_add_button(xfc.FL_PUSH_BUTTON, m, h - s - m, 80, s, \
                               "X Resize")
    xf.fl_set_object_bw(fdui.rx, -1)
    xf.fl_set_object_resize(fdui.rx, xfc.FL_RESIZE_NONE)
    xf.fl_set_object_gravity(fdui.rx, xfc.FL_SouthWest, xfc.FL_SouthWest)
    xf.fl_set_object_callback(fdui.rx, rx_callback, 0)                          #gd[0])             # long gd
    xf.fl_set_object_color(fdui.rx, xfc.FL_COL1, xfc.FL_MCOL)
    xf.fl_set_button(fdui.rx, fdui.box.contents.resize & xfc.FL_RESIZE_X)

    fdui.ry = xf.fl_add_button(xfc.FL_PUSH_BUTTON, 2 * m + 80, h - s - m, \
                               80, s, "Y Resize")
    xf.fl_set_object_bw(fdui.ry, -1)
    xf.fl_set_object_resize(fdui.ry, xfc.FL_RESIZE_NONE)
    xf.fl_set_object_gravity(fdui.ry, xfc.FL_SouthWest, xfc.FL_SouthWest)
    xf.fl_set_object_callback(fdui.ry, ry_callback, 0)                          #gd[0])         # long gd
    xf.fl_set_object_color(fdui.ry, xfc.FL_COL1, xfc.FL_MCOL)
    xf.fl_set_button(fdui.ry, fdui.box.contents.resize & xfc.FL_RESIZE_Y)

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, w - 85, 5, 80, s, "Help")
    xf.fl_set_object_bw(pobj, -1)
    xf.fl_set_object_gravity(pobj, xfc.FL_NorthEast, xfc.FL_NorthEast)
    xf.fl_set_object_callback(pobj, help_callback, 0)                   # long help_

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 200, h - s - m,
                            80, s, "Reset")
    xf.fl_set_object_bw(pobj, -1)
    xf.fl_set_object_resize(pobj, xfc.FL_RESIZE_NONE)
    xf.fl_set_object_gravity(pobj, xfc.FL_South, xfc.FL_South)
    xf.fl_set_object_callback(pobj, reset_callback, 0)                          #gd[0])  # long gd

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, m + 280, h - s - m, 80, s, \
                            "Quit")
    xf.fl_set_object_bw(pobj, -1)
    xf.fl_set_object_resize(pobj, xfc.FL_RESIZE_NONE)
    xf.fl_set_object_gravity(pobj, xfc.FL_South, xfc.FL_South)

    xf.fl_end_form()

    return fdui



def create_form_help():

    fdui = FD_help()
    #size_t i;
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

    fdui.help_ = xf.fl_bgn_form(xfc.FL_NO_BOX, 345, 325)

    fdui.is_shown = 0

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 345, 325, "")
    xf.fl_set_object_bw(pobj, -1)

    pobj = xf.fl_add_browser(xfc.FL_NORMAL_BROWSER, 5, 5, 335, 285, "")
    xf.fl_set_object_bw(pobj, -1)
    xf.fl_set_object_color(pobj, xfc.FL_WHITE, xfc.FL_WHITE)
    xf.fl_set_object_gravity(pobj, xfc.FL_NorthWest, xfc.FL_SouthEast)

    for i in range(0, len(text)):           # i < sizeof text / sizeof *text
        xf.fl_add_browser_line(pobj, text[i])

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 133, 295, 80, 25, "Close")
    xf.fl_set_object_bw(pobj, -1)
    xf.fl_set_object_gravity(pobj, xfc.FL_South, xfc.FL_South)
    xf.fl_set_object_resize(pobj, xfc.FL_RESIZE_NONE)
    xf.fl_set_object_callback(pobj, close_callback, 0)                # fdui

    xf.fl_end_form()

    return fdui




def main(lsysargv, sysargv):
    global grav, help_, gd

    #grav = FD_gravity()
    #help_ = FD_help()

    xf.fl_initialize(lsysargv, sysargv, "Gravity Demo", 0, 0)
    help_ = create_form_help()
    grav = create_form_gravity(help_)
    xf.fl_set_app_mainform(grav.grav)

    for i in range (0, 9):
        gd[i].box = grav.box
        gd[i].grav = g[i]
        gd[i].rx = grav.rx
        gd[i].ry = grav.ry

    xf.fl_show_form(grav.grav, xfc.FL_PLACE_CENTER | xfc.FL_FREE_SIZE,
                    xfc.FL_FULLBORDER, "Gravity Demo")

    xf.fl_do_forms()

    # xf.fl_hide_form(grav.grav)
    # xf.fl_free_form(grav.grav)

    # if (help->is_shown )
    #    xf.fl_hide_form(help_.help_)
    # xf.fl_free_form(help_.help_)

    xf.fl_finish()

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

