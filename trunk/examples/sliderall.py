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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flslider import *
from xformslib.flmisc import *
from xformslib.xfdata import *




class Flsliderall(object):
    def __init__(self, lsysargv, sysargv):

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.create_form_form()

        fl_show_form(self.pform, FL_PLACE_CENTER | FL_FREE_SIZE, \
                        FL_FULLBORDER, "All Sliders")

        while True:
            pobj = fl_do_forms()
            if fl_is_same_object(pobj, self.pexitobj):
                break

        fl_hide_form(self.pform)
        fl_finish()


    def create_form_form(self):

        self.pform = fl_bgn_form(FL_NO_BOX, 780, 320)

        pobj = fl_add_box(FL_UP_BOX, 0, 0, 780, 320, "")
        fl_set_object_color(pobj, FL_PALEGREEN, FL_COL1)

        pobj = fl_add_box(FL_SHADOW_BOX, 20, 30, 360, 270, \
                            "SLIDER")
        fl_set_object_color(pobj, FL_SLATEBLUE, 47)
        fl_set_object_lalign(pobj, FL_ALIGN_TOP)
        fl_set_object_lstyle(pobj, FL_BOLD_STYLE)

        pobj = fl_add_box(FL_SHADOW_BOX, 390, 30, 370, 270, \
                            "VALSLIDER")
        fl_set_object_color(pobj, FL_SLATEBLUE, FL_COL1)
        fl_set_object_lalign(pobj, FL_ALIGN_TOP)
        fl_set_object_lstyle(pobj, FL_BOLD_STYLE)

        pobj = fl_add_slider(FL_VERT_SLIDER, 30, 50, 40, 220, \
                               "vert")
        fl_set_object_color(pobj, FL_INDIANRED, FL_PALEGREEN)

        pobj = fl_add_slider(FL_VERT_FILL_SLIDER, 80, 50, 40, 220, \
                               "vert_fill")
        fl_set_object_color(pobj, FL_INDIANRED, FL_PALEGREEN)

        pobj = fl_add_slider(FL_HOR_SLIDER, 180, 50, 195, 40, "hor")
        fl_set_object_color(pobj, FL_INDIANRED, FL_PALEGREEN)

        pobj = fl_add_slider(FL_HOR_FILL_SLIDER, 180, 110, 190, 40, \
                               "hor_fill")
        fl_set_object_color(pobj, FL_INDIANRED, FL_PALEGREEN)

        pobj = fl_add_valslider(FL_VERT_NICE_SLIDER, 610, 50, 30, 220, \
                                  "vert_nice")
        fl_set_object_boxtype(pobj, FL_FLAT_BOX)
        fl_set_object_color(pobj, FL_SLATEBLUE, FL_INDIANRED)

        pobj = fl_add_valslider(FL_VERT_FILL_SLIDER, 660, 50, 40, 220, \
                                  "vert_fill")
        fl_set_object_color(pobj, FL_INDIANRED, FL_PALEGREEN)

        pobj = fl_add_valslider(FL_HOR_SLIDER, 400, 50, 190, 40, \
                                  "hor")
        fl_set_object_color(pobj, FL_INDIANRED, FL_PALEGREEN)

        pobj = fl_add_valslider(FL_HOR_FILL_SLIDER, 400, 110, 190, 40, \
                                  "hor_fill")
        fl_set_object_color(pobj, FL_INDIANRED, FL_PALEGREEN)

        fl_add_valslider(FL_HOR_BROWSER_SLIDER, 400, 220, 190, 25, \
                            "hor_browser")

        self.pexitobj = fl_add_button(FL_NORMAL_BUTTON, 450, 260, 100, 30, \
                                   "Exit")
        fl_set_object_color(self.pexitobj, FL_INDIANRED, FL_RED)

        pobj = fl_add_slider(FL_VERT_NICE_SLIDER, 130, 50, 30, 220, \
                               "vert_nice")
        fl_set_object_boxtype(pobj, FL_FLAT_BOX)
        fl_set_object_color(pobj, FL_SLATEBLUE, FL_INDIANRED)

        pobj = fl_add_slider(FL_HOR_NICE_SLIDER, 180, 170, 190, 30, \
                               "hor_nice")
        fl_set_object_boxtype(pobj, FL_FLAT_BOX)
        fl_set_object_color(pobj, FL_SLATEBLUE, FL_INDIANRED)

        fl_add_slider(FL_HOR_BROWSER_SLIDER, 180, 220, 190, 25, \
                         "hor_browser")

        pobj = fl_add_valslider(FL_HOR_NICE_SLIDER, 400, 170, 190, 30, \
                                  "hor_nice")
        fl_set_object_boxtype(pobj, FL_FLAT_BOX)
        fl_set_object_color(pobj, FL_SLATEBLUE, FL_INDIANRED)

        pobj = fl_add_valslider(FL_VERT_SLIDER, 710, 50, 40, 220, \
                                  "vert")
        fl_set_object_color(pobj, FL_INDIANRED, FL_PALEGREEN)

        fl_end_form()




if __name__ == '__main__':
    Flsliderall(len(sys.argv), sys.argv)

