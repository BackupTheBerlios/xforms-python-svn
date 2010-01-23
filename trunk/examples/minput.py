#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  minput XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
#


import sys
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flinput import *
from xformslib.flbutton import *
from xformslib.xfdata import *




def input_cb(pobj, data):
    notused, x, y = fl_get_input_cursorpos(pobj)
    print "INPUT - x=%d y=%d\n" % x, y


def input2_cb(pobj, data):
    notused, x, y = fl_get_input_cursorpos(pobj)
    print "INPUT2 - y=%d x=%d\n" % y, x


def main(lsysargv, sysargv):

    fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    pform = fl_bgn_form(FL_UP_BOX, 400, 450)

    pobj1 = fl_add_input(FL_MULTILINE_INPUT, 30, 270, 340, 150, "")
    fl_set_object_callback(pobj1, input2_cb, 0)

    pobj2 = fl_add_input(FL_MULTILINE_INPUT, 30, 90, 340, 150, "")
    fl_set_object_lsize(pobj2, FL_NORMAL_SIZE)
    fl_set_object_callback(pobj2, input_cb, 0)

    pbut = fl_add_button(FL_NORMAL_BUTTON, 160, 30, 80, 30, "Exit")

    fl_end_form()

    fl_show_form(pform, FL_PLACE_CENTERFREE, FL_FULLBORDER, \
                    "MultiLineInput")

    while True:
        pobj = fl_do_forms()
        if fl_is_same_object(pobj, pbut):
            break

    fl_finish()

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

