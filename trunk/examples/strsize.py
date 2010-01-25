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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flmisc import *
from xformslib.flbutton import *
from xformslib.flinput import *
from xformslib.xfdata import *



# Forms and Objects

class FD_form0(object):
    form0 = None
    vdata = None
    ldata = 0
    text = None



class Flstrsize(object):
    def __init__(self, lsysargv, sysargv):

        fl_initialize(lsysargv, sysargv, 0, 0, 0)

        # fill-in form initialization code
        self.fd_form0 = self.create_form_form0()

        # show the first form
        fl_show_form(self.fd_form0.form0, FL_PLACE_CENTER, \
                     FL_FULLBORDER, "form0")

        fl_do_forms()


    # callbacks for form form0

    def exit_cb(self, pobj, data):
        fl_finish()
        sys.exit(0)


    def input_cb(self, pobj, data):
        s = fl_get_input(pobj)
        w = fl_get_string_width(fl_get_object_lstyle(pobj), \
                                fl_get_object_lsize(pobj), s, len(s))
        h, asc, desc = fl_get_string_height(fl_get_object_lstyle(pobj), \
                             fl_get_object_lsize(pobj), s, len(s))

        buf = "w=%d h=%d" % (w, h)
        fl_set_object_label(self.fd_form0.text, buf)


    # Form definition
    def create_form_form0(self):

        fdui = FD_form0()
        fdui.form0 = fl_bgn_form(FL_NO_BOX, 311, 181)
        fl_add_box(FL_UP_BOX, 0, 0, 311, 181, "")
        pobj = fl_add_button(FL_NORMAL_BUTTON, 220, 130, \
                             80, 30, "Done")
        fl_set_object_callback(pobj, self.exit_cb, 0)
        pobj = fl_add_input(FL_NORMAL_INPUT, 20, 30, 280, 30, "")
        fl_set_object_callback(pobj, self.input_cb, 0)
        fdui.text = fl_add_text(FL_NORMAL_TEXT, 60, 90, \
                                130, 30, "Text")
        fl_set_object_lalign(fdui.text, FL_ALIGN_LEFT | \
                             FL_ALIGN_INSIDE)
        fl_end_form()
        return fdui




if __name__ == '__main__':
    Flstrsize(len(sys.argv), sys.argv)

