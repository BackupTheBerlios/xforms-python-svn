#!/usr/bin/env python3

#  This file is part of xforms-python, and it has been ported from
#  xyplotall.c XForms demo, with some adaptations.
#
#  xyplotover.c was written by M. Overmars and T.C. Zhao.
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# test screen/world conversion in addition to showing the xyplot styles
#

import sys
import math
#sys.path.append("..")
import xformslib as xfl


xytype = [ {'type':xfl.FL_NORMAL_XYPLOT, 'name':"FL_NORMAL_XYPLOT", \
        'color':xfl.FL_BLACK}, \
        {'type':xfl.FL_SQUARE_XYPLOT, 'name':"FL_SQUARE_XYPLOT", \
        'color':xfl.FL_BLACK}, \
        {'type':xfl.FL_CIRCLE_XYPLOT, 'name':"FL_CIRCLE_XYPLOT", \
        'color':xfl.FL_BLACK}, \
        {'type':xfl.FL_FILL_XYPLOT, 'name':"FL_FILL_XYPLOT", \
        'color':xfl.FL_BLACK}, \
        {'type':xfl.FL_POINTS_XYPLOT, 'name':"FL_POINTS_XYPLOT", \
        'color':xfl.FL_BLACK}, \
        {'type':xfl.FL_LINEPOINTS_XYPLOT, 'name':"FL_LINEPOINTS_XYPLOT", \
        'color':xfl.FL_BLACK}, \
        {'type':xfl.FL_DASHED_XYPLOT, 'name':"FL_DASHED_XYPLOT", \
        'color':xfl.FL_BLACK}, \
        {'type':xfl.FL_DOTTED_XYPLOT, 'name':"FL_DOTTED_XYPLOT", \
        'color':xfl.FL_BLACK}, \
        {'type':xfl.FL_DOTDASHED_XYPLOT, 'name':"FL_DOTDASHED_XYPLOT", \
        'color':xfl.FL_BLACK}, \
        {'type':xfl.FL_IMPULSE_XYPLOT, 'name':"FL_IMPULSE_XYPLOT", \
        'color':xfl.FL_BLACK}, \
        {'type':xfl.FL_ACTIVE_XYPLOT, 'name':"FL_ACTIVE_XYPLOT", \
        'color':xfl.FL_BLACK}, \
        {'type':xfl.FL_EMPTY_XYPLOT, 'name':"FL_EMPTY_XYPLOT", \
        'color':xfl.FL_BLACK} ]

N = len(xytype)
xyplot = [None] * N

fxyplot = None

x = [[0.0] * 21] * N    #static float x[ N ][ 21 ],
y = [[0.0] * 21] * N    # y[ N ][ 21 ];


def done_xyplot(pobj, q):

    xfl.fl_hide_form(pobj.contents.form)
    xfl.fl_finish()
    sys.exit(0)


def post(pobj, ev, mx, my, key, pxev):

    if ev == xfl.FL_PUSH or ev == xfl.FL_MOTION:
        wx, wy = xfl.fl_xyplot_s2w(pobj, mx, my)
        buf = "x=%d y=%d wx=%.1f wy=%.1f" % (mx, my, wx, wy)
        xfl.fl_show_oneliner(buf, pobj.contents.x + \
                pobj.contents.form.contents.x + 5, pobj.contents.y + \
                pobj.contents.form.contents.y)
        #  xfl.fl_object_ps_dump(pobj, "test.ps")
        pobj.contents.wantkey = xfl.FL_KEY_ALL
        pobj.contents.input = 1
    elif ev == xfl.FL_RELEASE:
        xfl.fl_hide_oneliner()
    elif ev == xfl.FL_KEYPRESS:
        keytxt = "key=%d\n" % key
        print(keytxt)

    return 0


def create_form_xyplot():
    global fxyplot, xyplot

    xy = 0         #XYType *xy  = xytype;
    dx = 180
    dy = 160
    i = 0
    if N % 3:
        tmpval = 1
    else:
        tmpval = 0
    j = N / 3 + tmpval

    if fxyplot:
        return

    fxyplot = xfl.fl_bgn_form(xfl.FL_NO_BOX, 3 * (dx + 20) + 20, \
            j * (dy + 30) + 120)

    xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, \
            3 * (dx + 20) + 20, j * (dy + 30) + 120, "")

    for j in range(0, N):
        try:
            u = xytype[xy]
        except IndexError:      # end of xytype list
            break
        for i in range(0, 3):
            try:
                u = xytype[xy]
            except IndexError:      # end of xytype list
                break
            xyplot[3 * j + i] = pobj = xfl.fl_add_xyplot(xytype[xy]["type"], \
                    i * (dx + 20) + 20, j * (dy + 30) + 60, dx, dy, \
                    xytype[xy]["name"])
            xfl.fl_set_object_lsize(pobj, xfl.FL_TINY_SIZE)
            xfl.fl_set_object_color(pobj, xfl.FL_COL1, xytype[xy]["color"])
            xy += 1
        i = 0

    pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, \
            (3 * (dx + 20) + 20) / 2 - 50, j * (dy + 30) + 60, 100, 30, "Exit")
    xfl.fl_set_object_callback(pobj, done_xyplot, 0)

    pobj = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, (3 * (dx + 20) + 20) / 2 - 90, \
            15, 240, 30, "FL_XYPLOT")
    xfl.fl_set_object_lcol(pobj, xfl.FL_SLATEBLUE)
    xfl.fl_set_object_lsize(pobj, xfl.FL_HUGE_SIZE)
    xfl.fl_set_object_lstyle(pobj, xfl.FL_BOLD_STYLE|xfl.FL_EMBOSSED_STYLE)
    xfl.fl_set_object_boxtype(pobj, xfl.FL_FLAT_BOX)

    xfl.fl_end_form()


def main(lsysargv, sysargv):
    global xyplot

    xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
    create_form_xyplot()

    # Make sure double buffer also works

    for i in range(0, N):

        xfl.fl_set_object_dblbuffer(xyplot[i], 1)

        for j in range(0, 21):
            x[i][j] = j * 3.1415 / 10 + 0.2
            y[i][j] = math.sin(2 * x[i][j]) + math.cos(x[i][j])

        xfl.fl_set_xyplot_data(xyplot[i], x[i], y[i], 21, "TestTitle", \
                "X-axis", "Y|axis")
        if i == 0:
            xfl.fl_add_xyplot_text(xyplot[i], x[i][15], 0.1, \
                    "@2->", xfl.FL_ALIGN_TOP, xfl.FL_BLUE)
        else:
            xfl.fl_add_xyplot_text(xyplot[i], x[i][8], 1.4, \
                    "Text Inset", xfl.FL_ALIGN_CENTER, xfl.FL_BLUE)

        if i == 3:
            xfl.fl_set_xyplot_xgrid(xyplot[i], xfl.FL_GRID_MAJOR)
            xfl.fl_set_xyplot_xgrid(xyplot[i], xfl.FL_GRID_MINOR)
        elif i == 0:
            xfl.fl_set_xyplot_xtics(xyplot[i], 7, 2)
            xfl.fl_set_xyplot_xbounds(xyplot[i], 6, 0)
        elif i == 1:
            xfl.fl_set_xyplot_ytics(xyplot[i], 5, 2)
            xfl.fl_set_xyplot_ybounds(xyplot[i], 2.4, -2.4)

        xfl.fl_set_object_posthandler(xyplot[i], post)

    xfl.fl_show_form( fxyplot, xfl.FL_PLACE_MOUSE | xfl.FL_FREE_SIZE, \
            xfl.FL_TRANSIENT, "XYplot")

    while xfl.fl_do_forms():
        pass

    return 0




if __name__ == '__main__':
    print("********* xyplotall.py *********")
    main(len(sys.argv), sys.argv)

