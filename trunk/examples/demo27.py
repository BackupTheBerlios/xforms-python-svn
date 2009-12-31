#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  demo27.c XForms demo, with some adaptations.
#
#  demo27.c was written by M. Overmars and T.C. Zhao
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of event callbacks and form callbacks.
# purposesly mixed form callback, object callback and event callback
# to show the flexibility of Forms Library's event handling (and
# test if they actually work together).
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc


pcolorform = None    # placeholder

# Color Part
r = 128
g = 128
b = 128


# color form callback routine

def color_callback(pobj, d):
    global r, g, b
    r = int(255 * xf.fl_get_slider_value(predsl))
    g = int(255 * xf.fl_get_slider_value(pgreensl))
    b = int(255 * xf.fl_get_slider_value(pbluesl))
    xf.fl_mapcolor(xfc.FL_FREE_COL1, r, g, b)
    xf.fl_redraw_object(pcolorobj)



def create_colorform():
    global pcolorform, pcolorobj, pbluesl, predsl, pgreensl

    if pcolorform:
        return

    pcolorform = xf.fl_bgn_form(xfc.FL_NO_BOX, 315, 190)

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 315, 190, "")

    pbluesl = xf.fl_add_slider(xfc.FL_HOR_SLIDER, 20, 25, 220, 35, "")
    xf.fl_set_object_color(pbluesl, xfc.FL_COL1, xfc.FL_BLUE)

    predsl = xf.fl_add_slider(xfc.FL_HOR_SLIDER, 20, 135, 220, 35, "")
    xf.fl_set_object_color(predsl, xfc.FL_COL1, xfc.FL_RED)

    pgreensl = xf.fl_add_slider(xfc.FL_HOR_SLIDER, 20, 80, 220, 35, "")
    xf.fl_set_object_color(pgreensl, xfc.FL_COL1, xfc.FL_GREEN)

    pcolorobj = xf.fl_add_box(xfc.FL_BORDER_BOX, 250, 25, 50, 145, "")
    xf.fl_set_object_color(pcolorobj, xfc.FL_FREE_COL1, xfc.FL_FREE_COL1)

    xf.fl_end_form()



# initializes the color part

def init_colorpart():
    global pcolorform

    create_colorform()
    xf.fl_set_form_callback(pcolorform, color_callback, 0)
    xf.fl_set_form_position(pcolorform, 20, -300 - pcolorform.contents.h)
    xf.fl_show_form(pcolorform, xfc.FL_PLACE_GEOMETRY, xfc.FL_TRANSIENT, \
                    "Color")
    xf.fl_mapcolor(xfc.FL_FREE_COL1, r, g, b)
    xf.fl_redraw_object(pcolorobj)



# Control Part

curobj = 1
cursize = 20



def select_object(pobj, which):
    global curobj
    curobj = which



# control form callback routine

def control_callback(pobj, d):
    global cursize

    if xf.fl_is_same_object(pobj, psizeobj):
        cursize = int(40 * xf.fl_get_slider_value(psizeobj))
    elif xf.fl_is_same_object(pobj, pexitobj):
        xf.fl_finish()
        sys.exit(0)



def create_controlform():
    global pcontrolform, psquareobj, pexitobj, psizeobj

    pcontrolform = xf.fl_bgn_form(xfc.FL_UP_BOX, 260, 230)

    xf.fl_bgn_group()

    psquareobj = xf.fl_add_button(xfc.FL_RADIO_BUTTON, 20, 150, 60, 60,
                                 "@square")
    xf.fl_set_object_lcol(psquareobj, xfc.FL_YELLOW)
    xf.fl_set_object_callback(psquareobj, select_object, 1)

    pobj = xf.fl_add_button(xfc.FL_RADIO_BUTTON, 20, 90, 60, 60,
                            "@circle")
    xf.fl_set_object_lcol(pobj, xfc.FL_YELLOW)
    xf.fl_set_object_callback(pobj, select_object, 2)

    pobj = xf.fl_add_button(xfc.FL_RADIO_BUTTON, 20, 30, 60, 60, 
                            "@8>")
    xf.fl_set_object_lcol(pobj, xfc.FL_YELLOW)
    xf.fl_set_object_callback(pobj, select_object, 3)

    xf.fl_end_group()

    pexitobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 160, 30, 80, 30, "Exit")

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 160, 180, 80, 30, "Clear")
    xf.fl_set_object_callback(pobj, clearit, 0)

    psizeobj = xf.fl_add_slider(xfc.FL_VERT_SLIDER, 100, 30, 40, 180, "size")
    xf.fl_set_slider_bounds(psizeobj, 0.025, 1.0)

    xf.fl_end_form()



# initializes the control part

def init_controlpart():

    create_controlform()
    xf.fl_set_form_callback(pcontrolform, control_callback, 0)
    xf.fl_set_button(psquareobj, 1)
    xf.fl_set_form_geometry(pcontrolform, 20, -pcontrolform.contents.h - 40,
                            pcontrolform.contents.w, pcontrolform.contents.h)
    xf.fl_show_form(pcontrolform, xfc.FL_PLACE_SIZE, xfc.FL_TRANSIENT, \
                    "Control")



# Main part

class OBJ(object):
    type = 0
    r = 0
    g = 0
    b = 0
    x = 0
    y = 0
    size = 0


global structob
structob = []
for a in range(0, 10000):
    structob.append(OBJ())              # ob[ 10000 ]

global onumb
onumb = 0


def drawit(stobj):

    xf.fl_winset(main_win)
    xf.fl_mapcolor(xfc.FL_FREE_COL1, stobj.r, \
                   stobj.g, stobj.b)

    if stobj.type == 1:
        xf.fl_rectf(stobj.x.value - stobj.size, \
                    stobj.y.value - stobj.size, 2 * stobj.size, \
                    2 * stobj.size, xfc.FL_FREE_COL1)
    elif stobj.type == 2:
        xf.fl_circf(stobj.x.value, stobj.y.value, stobj.size, \
                    xfc.FL_FREE_COL1)
    elif stobj.type == 3:
        point = (xfc.FL_POINT * 3)()          # point[ 3 ]

        #for pt in point:
        point[0].x = stobj.x.value - stobj.size
        point[0].y = stobj.y.value + stobj.size
        point[1].x = stobj.x.value + stobj.size
        point[1].y = stobj.y.value + stobj.size
        point[2].x = stobj.x.value
        point[2].y = stobj.y.value - stobj.size
        xf.fl_polyf(point, 3, xfc.FL_FREE_COL1)



#draws a particular object

def drawobject():
    global onumb, structob

    cur_obj = structob[onumb]                # OBJ *
    win_notused, x0, y0, km = xf.fl_get_win_mouse(main_win)
    cur_obj.x = x0
    cur_obj.y = y0
    cur_obj.r = r
    cur_obj.g = g
    cur_obj.b = b
    cur_obj.type = curobj
    cur_obj.size = cursize
    drawit(cur_obj)
    onumb += onumb



def redrawit():

    #xf.XClearWindow(xfc.fl_display, main_win)
    xf.fl_redraw_form(pcontrolform)
    for i in range(0, onumb):
        drawit(structob + i)




def clearit(pobj, data):
    onumb = 0
    xf.fl_winbackground(main_win, xf.fl_get_flcolor(xfc.FL_COL1))
    redrawit()



# Event callback routine

def main_callback(pxev, p):

    xf.fl_winset(main_win)

    if pxev.contents.type == xfc.Expose:
        redrawit()
    elif pxev.contents.type == xfc.ButtonPress:
        drawobject()
    return 0



def init_mainpart():
    global main_win

    xf.fl_pref_wingeometry(400, 300, 400, 400)
    xf.fl_pref_winsize(400, 400)
    xf.fl_winbackground(0, xf.fl_get_flcolor(xfc.FL_COL1))
    main_win = xf.fl_winopen("Drawing")
    xf.fl_set_event_callback(main_callback, 0)



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    init_colorpart()
    init_controlpart()
    init_mainpart()
    color_callback(pcolorobj, 0)

    while xf.fl_do_forms():
        pass

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

