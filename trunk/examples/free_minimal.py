#!/usr/bin/env python

#  This file is part of xforms-python, and it has been originally
#  created.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of drawing routines in a free flobject.
#

import sys
#sys.path.append("..")
import xformslib as xfl


def freehandler(pobj, evt, mx, my, key, pxev):

    mypoint1 = [{'x':25, 'y':14}, {'x':14, 'y':25}, {'x':50, 'y':70}]
    ppoint1 = xfl.make_ptr_flpoint(mypoint1)
    xfl.fl_lines(ppoint1, 3, xfl.FL_RED)

    xfl.fl_line(90, 90, 150, 90, xfl.FL_GREEN)

    xfl.fl_linestyle(xfl.FL_LONGDASH)

    xfl.fl_line(95, 80, 140, 80, xfl.FL_YELLOW)

    xfl.fl_linestyle(xfl.FL_SOLID)

    xfl.fl_point(75, 52, xfl.FL_BLUE)

    mypoint2 = [{'x':70, 'y':70}, {'x':70, 'y':75}, {'x':75, 'y':80}, \
        {'x':80, 'y':75}]
    ppoint2 = xfl.make_ptr_flpoint(mypoint2)
    xfl.fl_points(ppoint2, 4, xfl.FL_MAGENTA)

    xfl.fl_diagline(180, 90, 25, 20, xfl.FL_CYAN)

    xfl.fl_linewidth(3)

    xfl.fl_line(75, 10, 85, 15, xfl.FL_WHITE)

    xfl.fl_linewidth(0)

    xfl.fl_oval(0, 125, 30, 45, 32, xfl.FL_TOMATO)

    xfl.fl_ovalbound(150, 90, 40, 80, xfl.FL_SLATEBLUE)

    xfl.fl_ovalarc(1, 400, 10, 40, 80, 65, 270, xfl.FL_PALEGREEN)

    xfl.fl_ovalf(15, 90, 40, 80, xfl.FL_INDIANRED)

    xfl.fl_ovall(250, 10, 40, 80, xfl.FL_DARKGOLD)

    xfl.fl_circf(200, 35, 20, xfl.FL_ORCHID)

    xfl.fl_circ(300, 35, 20, xfl.FL_DARKCYAN)

    xfl.fl_pieslice(1, 180, 60, 82, 117, 0, 90, xfl.FL_DARKTOMATO)

    xfl.fl_pieslice(0, 220, 40, 100, 300, 10, 150, xfl.FL_WHEAT)

    xfl.fl_arcf(350, 20, 120, 0, 80, xfl.FL_DARKORANGE)

    xfl.fl_arc(400, 80, 120, 0, 80, xfl.FL_DEEPPINK)

    xfl.fl_rectangle(0, 10, 200, 80, 20, xfl.FL_CHARTREUSE)

    xfl.fl_rectbound(100, 200, 20, 20, xfl.FL_DARKVIOLET)

    xfl.fl_rectf(160, 200, 40, 20, xfl.FL_SPRINGGREEN)

    xfl.fl_rect(205, 200, 40, 20, xfl.FL_DODGERBLUE)

    xfl.fl_roundrectangle(0, 260, 200, 80, 20, xfl.FL_ALICEBLUE)

    xfl.fl_roundrectangle(1, 350, 180, 70, 30, xfl.FL_ANTIQUEWHITE)

    xfl.fl_roundrectf(10, 250, 70, 15, xfl.FL_AQUA)

    xfl.fl_roundrect(90, 250, 50, 25, xfl.FL_AQUAMARINE)

    mypoint3 = [{'x':10, 'y':300}, {'x':50, 'y':310}, {'x':40, 'y':350}, \
            {'x':70, 'y':360}, {'x':20, 'y':370}]
    ppoint3 = xfl.make_ptr_flpoint(mypoint3)
    xfl.fl_polygon(0, ppoint3, 5, xfl.FL_AZURE)

    mypoint4 = [{'x':90, 'y':280}, {'x':130, 'y':310}, {'x':140, 'y':300}, \
            {'x':170, 'y':360}, {'x':180, 'y':370}, {'x':160, 'y':300}]
    ppoint4 = xfl.make_ptr_flpoint(mypoint4)
    xfl.fl_polygon(1, ppoint4, 6, xfl.FL_BEIGE)

    mypoint5 = [{'x':200, 'y':280}, {'x':210, 'y':280}, {'x':220, 'y':300}, \
            {'x':210, 'y':320}, {'x':200, 'y':320}, {'x':190, 'y':300}]
    ppoint5 = xfl.make_ptr_flpoint(mypoint5)
    xfl.fl_polyf(ppoint5, 6, xfl.FL_BISQUE)

    mypoint6 = [{'x':240, 'y':280}, {'x':250, 'y':280}, {'x':260, 'y':300}, \
            {'x':250, 'y':320}, {'x':240, 'y':320}, {'x':230, 'y':300}]
    ppoint6 = xfl.make_ptr_flpoint(mypoint6)
    xfl.fl_polyl(ppoint6, 6, xfl.FL_BLANCHEDALMOND)

    mypoint7 = [{'x':300, 'y':280}, {'x':320, 'y':280}, {'x':320, 'y':300}, \
            {'x':340, 'y':310}, {'x':310, 'y':330}, {'x':310, 'y':350}, \
            {'x':300, 'y':340}, {'x':290, 'y':350}, {'x':310, 'y':300}]
    ppoint7 = xfl.make_ptr_flpoint(mypoint7)
    xfl.fl_polybound(ppoint7, 9, xfl.FL_BLUEVIOLET)

    return 0


def main(lsysargv, sysargv):

    xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)

    pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 600, 600)

    #xfl.fl_bk_color(xfl.FL_BLACK)

    pfree = xfl.fl_add_free(xfl.FL_INACTIVE_FREE, 50, 50, 300, 300, "myfree", \
        freehandler)

    xfl.fl_end_form()

    xfl.fl_show_form(pform, xfl.FL_PLACE_ASPECT, xfl.FL_TRANSIENT, "Free drawing")

    while xfl.fl_do_forms():
        pass                    # empty



if __name__ == '__main__':
    print("********* free_minimal.py *********")
    main(len(sys.argv), sys.argv)

