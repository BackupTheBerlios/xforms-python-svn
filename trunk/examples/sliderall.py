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
import xformslib as xfl



class Flsliderall(object):
    def __init__(self, lsysargv, sysargv):

        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.create_form_form()

        xfl.fl_show_form(self.pform, xfl.FL_PLACE_CENTER | xfl.FL_FREE_SIZE, \
                xfl.FL_FULLBORDER, "All Sliders")

        while True:
            pobj = xfl.fl_do_forms()
            if xfl.fl_is_same_object(pobj, self.pexitobj):
                break

        xfl.fl_hide_form(self.pform)
        xfl.fl_finish()


    def create_form_form(self):

        self.pform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 780, 320)

        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 780, 320, "")
        xfl.fl_set_object_color(pobj, xfl.FL_PALEGREEN, xfl.FL_COL1)
        pobj = xfl.fl_add_box(xfl.FL_SHADOW_BOX, 20, 30, 360, 270, \
                "SLIDER")
        xfl.fl_set_object_color(pobj, xfl.FL_SLATEBLUE, 47)
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_TOP)
        xfl.fl_set_object_lstyle(pobj, xfl.FL_BOLD_STYLE)
        pobj = xfl.fl_add_box(xfl.FL_SHADOW_BOX, 390, 30, 370, 270, \
                "VALSLIDER")
        xfl.fl_set_object_color(pobj, xfl.FL_SLATEBLUE, xfl.FL_COL1)
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_TOP)
        xfl.fl_set_object_lstyle(pobj, xfl.FL_BOLD_STYLE)
        pobj = xfl.fl_add_slider(xfl.FL_VERT_SLIDER, 30, 50, 40, 220, \
                "vert")
        xfl.fl_set_object_color(pobj, xfl.FL_INDIANRED, xfl.FL_PALEGREEN)
        pobj = xfl.fl_add_slider(xfl.FL_VERT_FILL_SLIDER, 80, 50, 40, 220, \
                "vert_fill")
        xfl.fl_set_object_color(pobj, xfl.FL_INDIANRED, xfl.FL_PALEGREEN)
        pobj = xfl.fl_add_slider(xfl.FL_HOR_SLIDER, 180, 50, 195, 40, "hor")
        xfl.fl_set_object_color(pobj, xfl.FL_INDIANRED, xfl.FL_PALEGREEN)
        pobj = xfl.fl_add_slider(xfl.FL_HOR_FILL_SLIDER, 180, 110, 190, 40, \
                "hor_fill")
        xfl.fl_set_object_color(pobj, xfl.FL_INDIANRED, xfl.FL_PALEGREEN)
        pobj = xfl.fl_add_valslider(xfl.FL_VERT_NICE_SLIDER, 610, 50, \
                30, 220, "vert_nice")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_FLAT_BOX)
        xfl.fl_set_object_color(pobj, xfl.FL_SLATEBLUE, xfl.FL_INDIANRED)
        pobj = xfl.fl_add_valslider(xfl.FL_VERT_FILL_SLIDER, 660, 50, \
                40, 220, "vert_fill")
        xfl.fl_set_object_color(pobj, xfl.FL_INDIANRED, xfl.FL_PALEGREEN)
        pobj = xfl.fl_add_valslider(xfl.FL_HOR_SLIDER, 400, 50, 190, 40, \
                "hor")
        xfl.fl_set_object_color(pobj, xfl.FL_INDIANRED, xfl.FL_PALEGREEN)
        pobj = xfl.fl_add_valslider(xfl.FL_HOR_FILL_SLIDER, 400, 110, \
                190, 40, "hor_fill")
        xfl.fl_set_object_color(pobj, xfl.FL_INDIANRED, xfl.FL_PALEGREEN)
        xfl.fl_add_valslider(xfl.FL_HOR_BROWSER_SLIDER, 400, 220, 190, 25, \
                "hor_browser")
        self.pexitobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 450, 260, \
                100, 30, "Exit")
        xfl.fl_set_object_color(self.pexitobj, xfl.FL_INDIANRED, xfl.FL_RED)
        pobj = xfl.fl_add_slider(xfl.FL_VERT_NICE_SLIDER, 130, 50, 30, 220, \
                "vert_nice")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_FLAT_BOX)
        xfl.fl_set_object_color(pobj, xfl.FL_SLATEBLUE, xfl.FL_INDIANRED)
        pobj = xfl.fl_add_slider(xfl.FL_HOR_NICE_SLIDER, 180, 170, 190, 30, \
                "hor_nice")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_FLAT_BOX)
        xfl.fl_set_object_color(pobj, xfl.FL_SLATEBLUE, xfl.FL_INDIANRED)
        xfl.fl_add_slider(xfl.FL_HOR_BROWSER_SLIDER, 180, 220, 190, 25, \
                "hor_browser")
        pobj = xfl.fl_add_valslider(xfl.FL_HOR_NICE_SLIDER, 400, 170, \
                190, 30, "hor_nice")
        xfl.fl_set_object_boxtype(pobj, xfl.FL_FLAT_BOX)
        xfl.fl_set_object_color(pobj, xfl.FL_SLATEBLUE, xfl.FL_INDIANRED)
        pobj = xfl.fl_add_valslider(xfl.FL_VERT_SLIDER, 710, 50, 40, 220, \
                "vert")
        xfl.fl_set_object_color(pobj, xfl.FL_INDIANRED, xfl.FL_PALEGREEN)

        xfl.fl_end_form()



if __name__ == '__main__':
    Flsliderall(len(sys.argv), sys.argv)
