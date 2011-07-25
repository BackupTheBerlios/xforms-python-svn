#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  xyplotactive.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#


import sys
import random
#sys.path.append("..")
import xformslib as xfl


# Forms and Objects
class FD_axyform(object):
    axypform = None
    vdata = None
    ldata = 0
    xyplot = None
    xmin = None
    xmax = None
    ymin = None
    ymax = None
    status = None


# callbacks for form axypform

def xyplot_cb(pobj, data):

    x, y, i = xfl.fl_get_xyplot(pobj)
    if i < 0:
        return

    buf = "X=%.3f  Y=%.3f" % (x, y)
    xfl.fl_set_object_label(xypui.status, buf)


def alwaysreturn_cb(pobj, data):
    if xfl.fl_get_button(pobj):
        returnval = xfl.FL_RETURN_CHANGED
    else:
        returnval = xfl.FL_RETURN_END_CHANGED
    xfl.fl_set_object_return(xypui.xyplot, returnval)


def interpolate_cb(pobj, data):
    if xfl.fl_get_button(pobj):
        value = 3
    else:
        value = 0
    xfl.fl_set_xyplot_interpolate(xypui.xyplot, 0, value, 0.2)


def inspect_cb(pobj, data):
    xfl.fl_set_xyplot_inspect(xypui.xyplot, xfl.fl_get_button(pobj))


def notic_cb(pobj, data):
    notic = xfl.fl_get_button(pobj)

    if notic:
        xfl.fl_set_xyplot_xtics(xypui.xyplot, -1, -1)
        xfl.fl_set_xyplot_ytics(xypui.xyplot, -1, -1)
    else:
        xfl.fl_set_xyplot_xtics(xypui.xyplot, 0, 0)
        xfl.fl_set_xyplot_ytics(xypui.xyplot, 0, 0)


def bounds_cb(pobj, data):
    # char buf[ 50 ]

    if not data:
        xmin = float(xfl.fl_get_input(xypui.xmin))
        xmax = float(xfl.fl_get_input(xypui.xmax))

        xfl.fl_set_xyplot_xbounds(xypui.xyplot, xmin, xmax)

        xmin, xmax = xfl.fl_get_xyplot_xbounds(xypui.xyplot)
        #sprintf( buf, "%g", xmin );
        buf = str(xmin)
        xfl.fl_set_input(xypui.xmin, buf)
        #sprintf( buf, "%g", xmax );
        buf = str(xmax)
        xfl.fl_set_input(xypui.xmax, buf)

    else:
        ymin = float(xfl.fl_get_input(xypui.ymin))
        ymax = float(xfl.fl_get_input(xypui.ymax))

        xfl.fl_set_xyplot_ybounds(xypui.xyplot, ymin, ymax)

        ymin, ymax = xfl.fl_get_xyplot_ybounds(xypui.xyplot)
        #sprintf( buf, "%g", ymin );
        buf = str(ymin)
        xfl.fl_set_input(xypui.ymin, buf)
        #sprintf( buf, "%g", ymax );
        buf = str(ymax)
        xfl.fl_set_input(xypui.ymax, buf)


def main(lsysargv, sysargv):
    global xypui

    x = [0.0] * 11
    y = [0.0] * 11

    xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
    xypui = create_form_axypform()

    # Fill-in form initialization code

    xfl.fl_set_xyplot_ybounds(xypui.xyplot, 0.0, 10.0)
    for i in range(0, 11):
        x[i] = y[i] = float(i)


    xfl.fl_add_xyplot_overlay(xypui.xyplot, 1, x, y, 11, xfl.FL_YELLOW)
    xfl.fl_set_xyplot_overlay_type(xypui.xyplot, 1, xfl.FL_LINEPOINTS_XYPLOT)
    xfl.fl_set_xyplot_interpolate(xypui.xyplot, 1, 2, 0.1);

    #srand( time( NULL ) );

    #for ( i = 0; i <= 10; i++ )
    #    y[ i ] +=  ( double ) rand( ) / RAND_MAX - 0.5;
    for i in range(0, 11):
        y[i] += float(random.random() / xfl.INT_MAX - 0.5)

    xfl.fl_set_xyplot_data(xypui.xyplot, x, y, 11, \
            "Active xyplot with overlay", "x-axis", "y-axis")
    xfl.fl_set_xyplot_linewidth(xypui.xyplot, 0, 2)
    xfl.fl_set_xyplot_xgrid(xypui.xyplot, xfl.FL_GRID_MINOR)

    # Show the first form

    xfl.fl_show_form(xypui.axypform, xfl.FL_PLACE_MOUSE | xfl.FL_FREE_SIZE,
            xfl.FL_FULLBORDER, "xyplotactive")

    xfl.fl_do_forms()

    return 0


def create_form_axypform():

    fdui = FD_axyform()

    fdui.axypform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 431, 301)

    xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 431, 301, "")

    fdui.xyplot = xfl.fl_add_xyplot(xfl.FL_ACTIVE_XYPLOT, 20, 50, \
            285, 235, "")
    xfl.fl_set_object_boxtype(fdui.xyplot, xfl.FL_DOWN_BOX)
    xfl.fl_set_object_color(fdui.xyplot, xfl.FL_BLACK, xfl.FL_GREEN)
    xfl.fl_set_object_lalign(fdui.xyplot, xfl.FL_ALIGN_BOTTOM | \
            xfl.FL_ALIGN_INSIDE)
    xfl.fl_set_object_callback(fdui.xyplot, xyplot_cb, 0)
    xfl.fl_set_object_gravity(fdui.xyplot, xfl.FL_NorthWest, xfl.FL_SouthEast)

    pobj = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 315, 40, 80, 25, \
            "AlwaysReturn")
    xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_BLUE)
    xfl.fl_set_object_callback(pobj, alwaysreturn_cb, 0)
    xfl.fl_set_object_gravity(pobj, xfl.FL_NorthEast, xfl.FL_NorthEast)

    pobj = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 315, 65, 80, 25, \
            "Interpolate")
    xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_BLUE)
    xfl.fl_set_object_callback(pobj, interpolate_cb, 0)
    xfl.fl_set_object_gravity(pobj, xfl.FL_NorthEast, xfl.FL_NorthEast)

    pobj = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 315, 90, 85, 25, \
            "InspectOnly")
    xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_BLUE)
    xfl.fl_set_object_callback(pobj, inspect_cb, 0)
    xfl.fl_set_object_gravity(pobj, xfl.FL_NorthEast, xfl.FL_NorthEast)

    pobj = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 315, 120, 85, 25, \
            "NoTics")
    xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_BLUE)
    xfl.fl_set_object_callback(pobj, notic_cb, 0)
    xfl.fl_set_object_gravity(pobj, xfl.FL_NorthEast, xfl.FL_NorthEast)

    fdui.xmin = xfl.fl_add_input(xfl.FL_FLOAT_INPUT, 315, 150, 50, 20,
            " x_min")
    xfl.fl_set_input(fdui.xmin, "0.0")
    xfl.fl_set_object_lalign(fdui.xmin, xfl.FL_ALIGN_RIGHT)
    xfl.fl_set_object_callback(fdui.xmin, bounds_cb, 0)
    xfl.fl_set_object_gravity(fdui.xmin, xfl.FL_NorthEast, xfl.FL_NorthEast)

    fdui.xmax = xfl.fl_add_input(xfl.FL_FLOAT_INPUT, 315, 170, 50, 20,
            " x_max")
    xfl.fl_set_input(fdui.xmax, "10.0")
    xfl.fl_set_object_lalign(fdui.xmax, xfl.FL_ALIGN_RIGHT)
    xfl.fl_set_object_callback(fdui.xmax, bounds_cb, 0)
    xfl.fl_set_object_gravity(fdui.xmax, xfl.FL_NorthEast, xfl.FL_NorthEast)

    fdui.ymin = xfl.fl_add_input(xfl.FL_FLOAT_INPUT, 315, 200, 50, 20,
             " y_min")
    xfl.fl_set_input(fdui.ymin, "0.0")
    xfl.fl_set_object_lalign(fdui.ymin, xfl.FL_ALIGN_RIGHT)
    xfl.fl_set_object_callback(fdui.ymin, bounds_cb, 1)
    xfl.fl_set_object_gravity(fdui.ymin, xfl.FL_NorthEast, xfl.FL_NorthEast)

    fdui.ymax = xfl.fl_add_input(xfl.FL_FLOAT_INPUT, 315, 220, 50, 20,
             " y_max")
    xfl.fl_set_input(fdui.ymax, "10.0")
    xfl.fl_set_object_lalign(fdui.ymax, xfl.FL_ALIGN_RIGHT)
    xfl.fl_set_object_callback(fdui.ymax, bounds_cb, 1)
    xfl.fl_set_object_gravity(fdui.ymax, xfl.FL_NorthEast, xfl.FL_NorthEast)

    fdui.status = xfl.fl_add_box(xfl.FL_BORDER_BOX, 20, 15, 285, 25, "")
    xfl.fl_set_object_boxtype(fdui.status, xfl.FL_DOWN_BOX)
    xfl.fl_set_object_gravity(fdui.status, xfl.FL_NorthWest, xfl.FL_NorthEast)
    xfl.fl_set_object_lalign(fdui.status, xfl.FL_ALIGN_CENTER | \
            xfl.FL_ALIGN_INSIDE)

    pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 325, 250, 90, 30, "Done")
    xfl.fl_set_object_gravity(pobj, xfl.FL_SouthEast, xfl.FL_SouthEast)

    xfl.fl_end_form()

    return fdui



if __name__ == '__main__':
    print("********* xyplotactive.py *********")
    main(len(sys.argv), sys.argv)

