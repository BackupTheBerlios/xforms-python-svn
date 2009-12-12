#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  strsize.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



# Forms and Objects

class FD_form0(object):
    form0 = None
    vdata = None
    ldata = 0
    text = None

# callbacks for form form0

def exit_cb(ob, data):
    xf.fl_finish()
    sys.exit(0)


def input_cb(ob, data):
    s = xf.fl_get_input(ob)
    w = xf.fl_get_string_width(ob[0].lstyle, ob[0].lsize, \
                               s, len(s))
    h = xf.fl_get_string_height(ob[0].lstyle, ob[0].lsize, \
                                s, len(s), 0, 0)

    buf = "w=%d h=%d" % (w, h)
    xf.fl_set_object_label(fd_form0.text, buf)



def main(lsysargv, sysargv):
    global fd_form0

    xf.fl_initialize(lsysargv, sysargv, 0, 0, 0)
    fd_form0 = create_form_form0()

    # fill-in form initialization code

    # show the first form
    xf.fl_show_form(fd_form0.form0, xfc.FL_PLACE_CENTER, \
                    xfc.FL_FULLBORDER, "form0")

    xf.fl_do_forms()
    return 0



# Form definition file

def create_form_form0():

    fdui = FD_form0()

    fdui.form0 = xf.fl_bgn_form(xfc.FL_NO_BOX, 311, 181)

    xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 311, 181, "")

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 220, 130, \
                           80, 30, "Done")
    xf.fl_set_object_callback(obj, exit_cb, 0)

    obj = xf.fl_add_input(xfc.FL_NORMAL_INPUT, 20, 30, 280, 30, "")
    xf.fl_set_object_callback(obj, input_cb, 0)

    fdui.text = obj = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 60, 90, \
                                     130, 30, "Text")
    xf.fl_set_object_lalign(obj, xfc.FL_ALIGN_LEFT | \
                            xfc.FL_ALIGN_INSIDE)

    xf.fl_end_form()

    return fdui



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

