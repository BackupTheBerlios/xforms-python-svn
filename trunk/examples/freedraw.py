#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  arrowbutton.c XForms demo, with some adaptations.
#
#  arrowbutton.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Demo showing the use of a free obejct
#

import sys
#sys.path.append("..")
import xformslib as xfl



# Forms and Objects
class FD_drawfree(object):
    drawfree = None
    vdata = None
    cdata = ""
    ldata = 0
    freeobj = None
    figgrp = None
    colgrp = None
    colorobj = None
    rsli = None
    gsli = None
    bsli = None
    miscgrp = None
    sizegrp = None
    hsli = None
    wsli = None
    drobj = [None] * 3

max_w = 150
max_h = 150
#static Display *dpy;


def main(lsysargv, sysargv):
    global drawui
    dpy = xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
    gctx = xfl.fl_gc()       #xfl.fl_state[xfl.fl_get_vclass()].gc[0]
    xfl.fl_set_background(gctx, xfl.FL_GRAY)
    drawui = create_form_drawfree()
    xfl.fl_set_object_color(drawui.colorobj, xfl.FL_FREE_COL1, xfl.FL_FREE_COL1)
    draw_initialize(drawui)
    xfl.fl_show_form(drawui.drawfree, xfl.FL_PLACE_CENTER | xfl.FL_FREE_SIZE, \
            xfl.FL_FULLBORDER, "FreeObject")
    xfl.fl_do_forms()
    xfl.fl_finish()

    return 0


# Structure mantainace

def draw_triangle(fill, x, y, w, h, colr):

    mylistpoint = [ {'x':int(x), 'y':int(y + h - 1)}, \
            {'x':int(x + w / 2), 'y':int(y)}, \
            {'x':int(x + w - 1), 'y':int(y + h - 1)} ]
    pxpoint = xfl.fls_make_ptr_flpoint(mylistpoint)

    #gctx = xfl.fl_gc()       #xfl.fl_state[xfl.fl_get_vclass()].gc[0]
    #xfl.fl_set_foreground(gctx, xfl.fl_get_flcolor(colr))

    if fill:
        xfl.fl_polyf(pxpoint, 3, colr)
    else:
        xfl.fl_polygon(0, pxpoint, 3, colr)


drawfunc = [xfl.fl_oval, xfl.fl_rectangle, draw_triangle]

class DrawFigure(object):
    drawit = None
    x = 0
    y = 0
    w = 0
    h = 0
    fill = 0
    c = [0] * 3
    newfig = 0
    col = 0

#static DrawFigure saved_figure[ 800 ],
#                  *cur_fig;
saved_figure = [DrawFigure()] * 800
cur_fig = saved_figure


def draw_initialize(ui):
    global cur_fig

    xfl.fl_set_form_minsize(ui.drawfree, 530, 490)
    xfl.fl_set_object_gravity(ui.colgrp, xfl.FL_West, xfl.FL_West)
    xfl.fl_set_object_gravity(ui.sizegrp, xfl.FL_SouthWest, xfl.FL_SouthWest)
    xfl.fl_set_object_gravity(ui.figgrp, xfl.FL_NorthWest, xfl.FL_NorthWest)
    xfl.fl_set_object_gravity(ui.miscgrp, xfl.FL_South, xfl.FL_South)
    xfl.fl_set_object_resize(ui.miscgrp, xfl.FL_RESIZE_NONE)

    cur_fig = saved_figure[0]
    cur_fig.c[0] = cur_fig.c[1] = cur_fig.c[2] = 127
    cur_fig.w = cur_fig.h = 30
    cur_fig.drawit = xfl.fl_oval
    cur_fig.fill = 1
    cur_fig.col = xfl.FL_FREE_COL1 + 1

    xfl.fl_mapcolor(xfl.FL_FREE_COL1, \
            cur_fig.c[0], cur_fig.c[1], cur_fig.c[2])
    xfl.fl_mapcolor(cur_fig.col, \
            cur_fig.c[0], cur_fig.c[1], cur_fig.c[2])

    xfl.fl_set_slider_bounds(ui.wsli, 1, max_w)
    xfl.fl_set_slider_bounds(ui.hsli, 1, max_h)
    xfl.fl_set_slider_precision(ui.wsli, 0)
    xfl.fl_set_slider_precision(ui.hsli, 0)
    xfl.fl_set_slider_value(ui.wsli, cur_fig.w)
    xfl.fl_set_slider_value(ui.hsli, cur_fig.h)

    # color sliders
    xfl.fl_set_slider_bounds(ui.rsli, 1.0, 0)
    xfl.fl_set_slider_bounds(ui.gsli, 1.0, 0)
    xfl.fl_set_slider_bounds(ui.bsli, 1.0, 0)

    # initial drawing function
    xfl.fl_set_button(ui.drobj[0], 1)

    # setup the color slider so we can find out colorobject from
    # the callback functions. This is not necessary as drawui
    # is static, this is done to show how to access other objects
    # from an object callback function
    #ui.rsli.contents.u_vdata = ui
    #ui.gsli.contents.u_vdata = ui
    #ui.bsli.contents.u_vdata = ui


def switch_object(pobj, which):
    global cur_fig
    cur_fig.drawit = drawfunc[which]


def change_color(pobj, which):
    global cur_fig
    cur_fig.c[which] = xfl.fl_get_slider_value(pobj) * 255.01
    xfl.fl_mapcolor(cur_fig.col, cur_fig.c[0], cur_fig.c[1], cur_fig.c[2])
    xfl.fl_mapcolor(xfl.FL_FREE_COL1, cur_fig.c[0], cur_fig.c[1], cur_fig.c[2])
    xfl.fl_redraw_object(drawui.colorobj)


def fill_cb(pobj, notused):
    global cur_fig
    cur_fig.fill = not xfl.fl_get_button(pobj)


def change_size(pobj, which):
    global cur_fig
    if which == 0:
        cur_fig.w = xfl.fl_get_slider_value(pobj)
    else:
        cur_fig.h = xfl.fl_get_slider_value(pobj)


def refresh_cb(pobj, which):
    xfl.fl_redraw_object(drawui.freeobj)


def clear_cb(pobj, notused):
    global cur_fig
    #saved_figure[ 0 ] = *cur_fig;
    saved_figure[0] = cur_fig
    cur_fig = saved_figure[0]
    xfl.fl_redraw_object(drawui.freeobj)


# The routine that does drawing
def freeobject_handler(pobj, event, mx, my, key, pxev):
    #DrawFigure *dr;
    if event == xfl.FL_DRAW:
        if cur_fig.newfig == 1:
            cur_fig.drawit(cur_fig.fill, cur_fig.x + pobj.contents.x, \
                    cur_fig.y + pobj.contents.y, cur_fig.w, cur_fig.h, \
                    cur_fig.col)
        else:
            xfl.fl_drw_box(pobj.contents.boxtype, pobj.contents.x, \
                    pobj.contents.y, pobj.contents.w, pobj.contents.h, \
                    pobj.contents.col1, pobj.contents.bw)
            #for ( dr = saved_figure; dr < cur_fig; dr++ )
            ndr = 0
            for ndr in range(0, len(saved_figure)):
                if saved_figure[ndr] < cur_fig:
                    saved_figure[ndr].drawit(saved_figure[ndr].fill, \
                            saved_figure[ndr].x + pobj.contents.x, \
                            saved_figure[ndr].y + pobj.contents.y, \
                            saved_figure[ndr].w, saved_figure[ndr].h, \
                            saved_figure[ndr].col)
        cur_fig.newfig = 0

    elif event == xfl.FL_PUSH:
        if key != 2:
            cur_fig.x = mx - cur_fig.w / 2
            cur_fig.y = my - cur_fig.h / 2
            # convert position to relative to the free object
            cur_fig.x -= pobj.contents.x
            cur_fig.y -= pobj.contents.y
            cur_fig.newfig = 1
            xfl.fl_redraw_object(pobj)
            #*(cur_fig+1) = *cur_fig;
            xfl.fl_mapcolor(cur_fig.col + 1, cur_fig.c[0], cur_fig.c[1], \
                    cur_fig.c[2])
            #cur_fig++
            #cur_fig.col++
            #cur_fig.col += 1 ??
    return 0


def create_form_drawfree():

    #gctx = xfl.fl_gc()       #xfl.fl_state[xfl.fl_get_vclass()].gc[0]
    #xfl.fl_set_background(gctx, xfl.FL_BLACK)

    fdui = FD_drawfree()

    fdui.drawfree = xfl.fl_bgn_form(xfl.FL_NO_BOX, 530, 490)

    pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 530, 490, "")

    pobj = xfl.fl_add_frame(xfl.FL_DOWN_FRAME, 145, 30, 370, 405, "")
    xfl.fl_set_object_gravity(pobj, xfl.FL_NorthWest, xfl.FL_SouthEast)

    fdui.freeobj = xfl.fl_add_free(xfl.FL_NORMAL_FREE, 145, 30, \
            370, 405, "", freeobject_handler)
    xfl.fl_set_object_gravity(fdui.freeobj, xfl.FL_NorthWest, \
            xfl.FL_SouthEast)
    xfl.fl_set_object_color(fdui.freeobj, xfl.FL_WHITE, xfl.FL_BLACK)

    pobj = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 15, 25, 100, 35, \
            "Outline")
    xfl.fl_set_object_color(pobj, xfl.FL_MCOL, xfl.FL_BLUE)
    xfl.fl_set_object_gravity(pobj, xfl.FL_NorthWest, xfl.FL_NorthWest)
    xfl.fl_set_object_callback(pobj, fill_cb, 0)

    fdui.figgrp = xfl.fl_bgn_group()

    fdui.drobj[0] = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 10, 60, 40, 40, \
            "@#circle")
    xfl.fl_set_object_lcol(fdui.drobj[0], xfl.FL_YELLOW)
    xfl.fl_set_object_callback(fdui.drobj[0], switch_object, 0)

    fdui.drobj[1] = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 50, 60, 40, 40, \
            "@#square")
    xfl.fl_set_object_lcol(fdui.drobj[1], xfl.FL_YELLOW)
    xfl.fl_set_object_callback(fdui.drobj[1], switch_object, 1)

    fdui.drobj[2] = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 90, 60, 40, 40, \
            "@#8>")
    xfl.fl_set_object_lcol(fdui.drobj[2], xfl.FL_YELLOW)
    xfl.fl_set_object_callback(fdui.drobj[2], switch_object, 2)
    xfl.fl_end_group()

    fdui.colgrp = xfl.fl_bgn_group()

    fdui.colorobj = xfl.fl_add_box(xfl.FL_BORDER_BOX, 25, 140, 90, 25, "")

    fdui.rsli = xfl.fl_add_slider(xfl.FL_VERT_FILL_SLIDER, 25, 170, \
            30, 125, "")
    xfl.fl_set_object_color(fdui.rsli, xfl.FL_COL1, xfl.FL_RED)
    xfl.fl_set_object_callback(fdui.rsli, change_color, 0)
    xfl.fl_set_object_return(fdui.rsli, xfl.FL_RETURN_CHANGED)

    fdui.gsli = xfl.fl_add_slider(xfl.FL_VERT_FILL_SLIDER, 55, 170, \
            30, 125, "")
    xfl.fl_set_object_color(fdui.gsli, xfl.FL_COL1, xfl.FL_GREEN)
    xfl.fl_set_object_callback(fdui.gsli, change_color, 1)
    xfl.fl_set_object_return(fdui.gsli, xfl.FL_RETURN_CHANGED)

    fdui.bsli = xfl.fl_add_slider(xfl.FL_VERT_FILL_SLIDER, 85, 170, \
            30, 125, "")
    xfl.fl_set_object_color(fdui.bsli, xfl.FL_COL1, xfl.FL_BLUE)
    xfl.fl_set_object_callback(fdui.bsli, change_color, 2)
    xfl.fl_set_object_return(fdui.bsli, xfl.FL_RETURN_CHANGED)

    xfl.fl_end_group()

    fdui.miscgrp = xfl.fl_bgn_group()

    pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 420, 455, 105, 30, "Quit")
    xfl.fl_set_button_shortcut(pobj, "Qq#q", 1)

    pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 280, 445, 105, 30, "Refresh")
    xfl.fl_set_object_callback(pobj, refresh_cb, 0)

    pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 165, 445, 105, 30, "Clear")
    xfl.fl_set_object_callback(pobj, clear_cb, 0)

    xfl.fl_end_group()

    fdui.sizegrp = xfl.fl_bgn_group()

    fdui.hsli = xfl.fl_add_valslider(xfl.FL_HOR_SLIDER, 15, 410, 120, 25, \
            "Height")
    xfl.fl_set_object_lalign(fdui.hsli, xfl.FL_ALIGN_TOP)
    xfl.fl_set_object_callback(fdui.hsli, change_size, 1)
    xfl.fl_set_object_return(fdui.hsli, xfl.FL_RETURN_CHANGED)

    fdui.wsli = xfl.fl_add_valslider(xfl.FL_HOR_SLIDER, 15, 370, \
            120, 25, "Width")
    xfl.fl_set_object_lalign(fdui.wsli, xfl.FL_ALIGN_TOP)
    xfl.fl_set_object_callback(fdui.wsli, change_size, 0)
    xfl.fl_set_object_return(fdui.wsli, xfl.FL_RETURN_CHANGED)

    xfl.fl_end_group()

    xfl.fl_end_form()

    return fdui



if __name__ == '__main__':
    print("********* freedraw.py *********")
    main(len(sys.argv), sys.argv)

