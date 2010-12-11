#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  strsize.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#

import sys
#sys.path.append("..")
import xformslib as xfl



# Forms and Objects
class FD_form0(object):
    form0 = None
    vdata = None
    ldata = 0
    text = None


class Flstrsize(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        # fill-in form initialization code
        self.fd_form0 = self.create_form_form0()
        # show the first form
        xfl.fl_show_form(self.fd_form0.form0, xfl.FL_PLACE_CENTER, \
                xfl.FL_FULLBORDER, "form0")
        xfl.fl_do_forms()


    # callbacks for form form0
    def exit_cb(self, pobj, data):
        xfl.fl_finish()
        sys.exit(0)


    def input_cb(self, pobj, data):
        s = xfl.fl_get_input(pobj)
        w = xfl.fl_get_string_width(xfl.fl_get_object_lstyle(pobj), \
                xfl.fl_get_object_lsize(pobj), s, len(s))
        h, asc, desc = xfl.fl_get_string_height( \
                xfl.fl_get_object_lstyle(pobj), \
                xfl.fl_get_object_lsize(pobj), s, len(s))
        buf = "w=%d h=%d" % (w, h)
        xfl.fl_set_object_label(self.fd_form0.text, buf)


    # Form definition
    def create_form_form0(self):

        fdui = FD_form0()
        fdui.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 311, 181)

        xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 311, 181, "")
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 220, 130, \
                80, 30, "Done")
        xfl.fl_set_object_callback(pobj, self.exit_cb, 0)
        pobj = xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 20, 30, 280, 30, "")
        xfl.fl_set_object_callback(pobj, self.input_cb, 0)
        fdui.text = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 60, 90, \
                130, 30, "Text")
        xfl.fl_set_object_lalign(fdui.text, xfl.FL_ALIGN_LEFT | \
                xfl.FL_ALIGN_INSIDE)
        xfl.fl_end_form()
        return fdui



if __name__ == '__main__':
    print ("********* strsize.py *********")
    Flstrsize(len(sys.argv), sys.argv)

