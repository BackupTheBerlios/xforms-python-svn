#!/usr/bin/env python

#  This file is part of xforms-python, and it is a variant of
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
import xformslib as xfl




def main(lsysargv, sysargv):

    xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
    pform = create_form_form()

    xfl.fl_show_form(pform, xfl.FL_PLACE_CENTER, xfl.FL_FULLBORDER, \
            "IconTest")
    xfl.fl_do_forms()
    return 0


def create_form_form():

    pform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 151, 111)

    pobj = xfl.fl_add_pixmapbutton(xfl.FL_NORMAL_BUTTON, 0, 0, 151, 111, \
            "Iconify Me\nvia Window Manager")
    xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_BOTTOM | xfl.FL_ALIGN_INSIDE)
    xfl.fl_set_object_lstyle(pobj, xfl.FL_BOLD_STYLE)
    xfl.fl_set_pixmapbutton_file(pobj, "crab.xpm")

    xfl.fl_end_form()

    return pform



if __name__ == '__main__':
    print("********* iconify_var.py *********")
    main(len(sys.argv), sys.argv)
