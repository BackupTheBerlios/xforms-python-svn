#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  iconify.c XForms demo, with some adaptations.
#
#  iconify.c was written by M. Overmars and T.C. Zhao
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Test iconification
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flbitmap import *
from xformslib.xfdata import *



# from "crab.xpm" file
    # width height ncolors chars_per_pixel / pixels data
crab = \
    "28 28 6 2 " \
    ".  c None 	 m white 	 s s_SkyBlue " \
    "x  c orange 	 m black 	 s s_orange " \
    "*  c #ff72c2 	 m black 	 s s_#ff72c2 " \
    "+  c SteelBlue 	 m white 	 s s_SteelBlue " \
    "G  c black 	 m black 	 s s_black " \
    "a  c LightGrey 	 m white 	 s s_LightGrey " \
    ". . . . . . * * * * . . . . . . . . . * * * * . . . . . " \
    ". . . . + * x x * . . . . . . . . . . + * x x * . . . . " \
    ". . . + * x x * . . . . . . . . . . . . + * x x * . . . " \
    ". . + * x * . . . * . . . . . . . . . * . . + * x * . . " \
    ". . + * x * . . + * . . . . . . . . + * . . + * x * . . " \
    ". . + * x * . + * * . . . . . . . . + * * . + * x * . . " \
    ". . + * x * + * * . . . . . . . . . . + * * + * x * . . " \
    ". . + * x * * * . . . . . . . . . . . . + * * x x * . . " \
    ". . . + * x * . . + * . . . . . . + * . . + * x * . . . " \
    ". . . + * x . . + * . + * * . * * . + * . . + x * . . . " \
    ". . . . + x . . + * . + * * . * * . + * . . + x . . . . " \
    ". . . . + x . . . + * + * * * * * + * . . . + x . . . . " \
    ". . . . + * x . . + * * * * * * * * * . . + x * . . . . " \
    ". . . . . + * x * * * * x x x x x * * * * x * . . . . . " \
    ". . . . + + + * * x x x x x x x x x x x x * . . . . . . " \
    ". . + + * x x x x x x x x x x x x x x x x x x * x . . . " \
    ". + * x x a + * * x x x x x x x x x x x * * a G * x * . " \
    "+ * x . . . + * * x x x x x x x x x x x * * G . . . x * " \
    ". . . . . . + * * x x x x x x x x x x x * * . . . . . . " \
    ". . . . . + * * x x x x x x x x x x x x x * * . . . . . " \
    ". . . + * x x x * x x x x x x x x x x x * x x x * . . . " \
    ". . + * x a a + * * x x x x x x x x x * * a a a x * . . " \
    ". + * x G G G + * * x x x x x x x x x * * a G G G x * . " \
    ". + * G . . . + * x * x x x x x x x * x * a G . . . * . " \
    ". . . . . . + * x a * * * x x x * * * a x * G . . . . . " \
    ". . . . . + * x a G a a * * * * * a a G a x * G . . . . " \
    ". . . . . + x a G . G G a a a a a G G . G G x a G . . . " \
    ". . . . . + x a G . . . G G G G G . . . . . x a G . . . "


def main(lsysargv, sysargv):

    fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    pform = create_form_form()

    # unused because of segfault down there
    #pix, w, h, mask, hx, hy = fl_read_pixmapfile(fl_root, "crab.xpm", 0)
    #fl_set_form_icon(pform, pix, mask)

    fl_show_form(pform, FL_PLACE_CENTER, FL_FULLBORDER, "IconTest")
    fl_do_forms()
    return 0


def create_form_form():

    pform = fl_bgn_form(FL_NO_BOX, 151, 111)

    pobj = fl_add_pixmapbutton(FL_NORMAL_BUTTON, 0, 0, 151, 111,
                               "Iconify Me\nvia Window Manager")
    fl_set_object_lalign(pobj, FL_ALIGN_BOTTOM | FL_ALIGN_INSIDE)
    fl_set_object_lstyle(pobj, FL_BOLD_STYLE)
    fl_set_pixmapbutton_file(pobj, "crab.xpm")
    #fl_set_pixmap_data(pobj, crab) not used as it gives a SegmentationFault :-/

    fl_end_form()

    return pform



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

