#!/usr/bin/env python3

#  This file is part of xforms-python, and it has been ported from
#  xyplotover.c XForms demo, with some adaptations.
#
#  xyplotover.c was written by M. Overmars and T.C. Zhao.
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Demo showing the use of xyplot overlay, plot key and
# PostScript output.
#

import sys
import math
#sys.path.append("..")
import xformslib as xfl


# Forms and Objects
class FD_fff(object):
    fff = None
    vdata = None
    ldata = 0
    xyplot = None


def main(lsysargv, sysargv):

    xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)

    fd_fff = create_form_fff()

    # fill-in form initialization code

    init_xyplot(fd_fff)

    # show the first form

    xfl.fl_show_form(fd_fff.fff, xfl.FL_PLACE_MOUSE | xfl.FL_FREE_SIZE, \
            xfl.FL_TRANSIENT, "XYPlot Overlay")

    xfl.fl_do_forms()

    if xfl.fl_object_ps_dump(fd_fff.xyplot, "test.ps") >= 0:
        print("PostScript output test.ps written\n")

    return 0


def init_xyplot(fd_fff):

    xx = [0.0] * 20     #float xx[ 20 ],
    yy = [0.0] * 20     #yy[ 20 ];

    #for ( i = 0; i <= 10; i++ )
    for i in range(0, 10+1):
        xx[i] = float(i)
        yy[i] = math.exp( - (xx[i] - 5) * (xx[i] - 5) / 8)

    xfl.fl_set_xyplot_data(fd_fff.xyplot, xx, yy, 8, "Plot Title", \
            "X-Axis", "Y|Axis")
    xfl.fl_set_xyplot_ybounds(fd_fff.xyplot, 0, 1.1)
    xfl.fl_set_xyplot_xbounds(fd_fff.xyplot, 0, 10)
    xfl.fl_add_xyplot_overlay(fd_fff.xyplot, 1, xx, yy, 11, xfl.FL_YELLOW)
    xfl.fl_set_xyplot_overlay_type(fd_fff.xyplot, 1, xfl.FL_LINEPOINTS_XYPLOT)
    xfl.fl_set_xyplot_interpolate(fd_fff.xyplot, 1, 2, 0.1)

    xfl.fl_add_xyplot_text(fd_fff.xyplot, 0.5, 1.0, "Gaussian\nDistribution", \
            xfl.FL_ALIGN_RIGHT, xfl.FL_WHITE)

    xfl.fl_set_xyplot_key(fd_fff.xyplot, 0, "Original")
    xfl.fl_set_xyplot_key(fd_fff.xyplot, 1, "Overlay")
    xfl.fl_set_xyplot_key_position(fd_fff.xyplot, 9.8, 1.08, \
            xfl.FL_ALIGN_LEFT_BOTTOM)


def create_form_fff():

    fdui = FD_fff()

    fdui.fff = xfl.fl_bgn_form( xfl.FL_NO_BOX, 370, 310)

    xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 370, 310, "")

    fdui.xyplot = xfl.fl_add_xyplot(xfl.FL_IMPULSE_XYPLOT, 10, 20, 350, 260, \
            "An XYPlot with overlay")
    xfl.fl_set_object_lalign(fdui.xyplot, \
            xfl.fl_to_inside_lalign(xfl.FL_ALIGN_BOTTOM))

    xfl.fl_set_object_lsize(fdui.xyplot, xfl.FL_NORMAL_SIZE)
    xfl.fl_set_object_boxtype(fdui.xyplot, xfl.FL_DOWN_BOX)
    xfl.fl_set_object_color(fdui.xyplot, xfl.FL_BLACK, xfl.FL_GREEN)

    pobj = xfl.fl_add_button(xfl.FL_HIDDEN_BUTTON, 10, 10, 350, 290, "")
    xfl.fl_set_button_shortcut(pobj, "qQ", 0)

    xfl.fl_end_form()

    return fdui



if __name__ == '__main__':
    print("********* xyplotover.py *********")
    main(len(sys.argv), sys.argv)

