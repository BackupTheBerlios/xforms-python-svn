#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  sliderall.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the different types of sliders
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc




def create_form_form():
    global pform, pexitobj

    pform = xf.fl_bgn_form(xfc.FL_NO_BOX, 780, 320)

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 780, 320, "")
    xf.fl_set_object_color(pobj, xfc.FL_PALEGREEN, xfc.FL_COL1)

    pobj = xf.fl_add_box(xfc.FL_SHADOW_BOX, 20, 30, 360, 270, \
                        "SLIDER")
    xf.fl_set_object_color(pobj, xfc.FL_SLATEBLUE, 47)
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_TOP)
    xf.fl_set_object_lstyle(pobj, xfc.FL_BOLD_STYLE)

    pobj = xf.fl_add_box(xfc.FL_SHADOW_BOX, 390, 30, 370, 270, \
                        "VALSLIDER")
    xf.fl_set_object_color(pobj, xfc.FL_SLATEBLUE, xfc.FL_COL1)
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_TOP)
    xf.fl_set_object_lstyle(pobj, xfc.FL_BOLD_STYLE)

    pobj = xf.fl_add_slider(xfc.FL_VERT_SLIDER, 30, 50, 40, 220, \
                           "vert")
    xf.fl_set_object_color(pobj, xfc.FL_INDIANRED, xfc.FL_PALEGREEN)

    pobj = xf.fl_add_slider(xfc.FL_VERT_FILL_SLIDER, 80, 50, 40, 220, \
                           "vert_fill")
    xf.fl_set_object_color(pobj, xfc.FL_INDIANRED, xfc.FL_PALEGREEN)

    pobj = xf.fl_add_slider(xfc.FL_HOR_SLIDER, 180, 50, 195, 40, "hor")
    xf.fl_set_object_color(pobj, xfc.FL_INDIANRED, xfc.FL_PALEGREEN)

    pobj = xf.fl_add_slider(xfc.FL_HOR_FILL_SLIDER, 180, 110, 190, 40, \
                           "hor_fill")
    xf.fl_set_object_color(pobj, xfc.FL_INDIANRED, xfc.FL_PALEGREEN)

    pobj = xf.fl_add_valslider(xfc.FL_VERT_NICE_SLIDER, 610, 50, 30, 220, \
                              "vert_nice")
    xf.fl_set_object_boxtype(pobj, xfc.FL_FLAT_BOX)
    xf.fl_set_object_color(pobj, xfc.FL_SLATEBLUE, xfc.FL_INDIANRED)

    pobj = xf.fl_add_valslider(xfc.FL_VERT_FILL_SLIDER, 660, 50, 40, 220, \
                              "vert_fill")
    xf.fl_set_object_color(pobj, xfc.FL_INDIANRED, xfc.FL_PALEGREEN)

    pobj = xf.fl_add_valslider(xfc.FL_HOR_SLIDER, 400, 50, 190, 40, \
                              "hor")
    xf.fl_set_object_color(pobj, xfc.FL_INDIANRED, xfc.FL_PALEGREEN)

    pobj = xf.fl_add_valslider(xfc.FL_HOR_FILL_SLIDER, 400, 110, 190, 40, \
                              "hor_fill")
    xf.fl_set_object_color(pobj, xfc.FL_INDIANRED, xfc.FL_PALEGREEN)

    xf.fl_add_valslider(xfc.FL_HOR_BROWSER_SLIDER, 400, 220, 190, 25, \
                        "hor_browser")

    pexitobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 450, 260, 100, 30, \
                               "Exit")
    xf.fl_set_object_color(pexitobj, xfc.FL_INDIANRED, xfc.FL_RED)

    pobj = xf.fl_add_slider(xfc.FL_VERT_NICE_SLIDER, 130, 50, 30, 220, \
                           "vert_nice")
    xf.fl_set_object_boxtype(pobj, xfc.FL_FLAT_BOX)
    xf.fl_set_object_color(pobj, xfc.FL_SLATEBLUE, xfc.FL_INDIANRED)

    pobj = xf.fl_add_slider(xfc.FL_HOR_NICE_SLIDER, 180, 170, 190, 30, \
                           "hor_nice")
    xf.fl_set_object_boxtype(pobj, xfc.FL_FLAT_BOX)
    xf.fl_set_object_color(pobj, xfc.FL_SLATEBLUE, xfc.FL_INDIANRED)

    xf.fl_add_slider(xfc.FL_HOR_BROWSER_SLIDER, 180, 220, 190, 25, \
                     "hor_browser")

    pobj = xf.fl_add_valslider(xfc.FL_HOR_NICE_SLIDER, 400, 170, 190, 30, \
                              "hor_nice")
    xf.fl_set_object_boxtype(pobj, xfc.FL_FLAT_BOX)
    xf.fl_set_object_color(pobj, xfc.FL_SLATEBLUE, xfc.FL_INDIANRED)

    pobj = xf.fl_add_valslider(xfc.FL_VERT_SLIDER, 710, 50, 40, 220, \
                              "vert")
    xf.fl_set_object_color(pobj, xfc.FL_INDIANRED, xfc.FL_PALEGREEN)

    xf.fl_end_form()



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    create_form_form()

    xf.fl_show_form(pform, xfc.FL_PLACE_CENTER | xfc.FL_FREE_SIZE, \
                    xfc.FL_FULLBORDER, "All Sliders")

    while True:
        pobj = xf.fl_do_forms()
        if xf.fl_is_same_object(pobj, pexitobj):
            break

    xf.fl_hide_form(pform)

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

