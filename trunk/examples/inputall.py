#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  inputall.c XForms demo, with some adaptations.
#
#  inputall.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Show all the input field types
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flinput import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *



# Forms and Objects

class FD_input(object):
    input_ = None
    vdata = None
    cdata = ""
    ldata = 0
    norminput = None
    multiinput = None
    report = None


class Flinputall(object):
    def __init__(self, lsysargv, sysargv):

        fl_initialize(lsysargv, sysargv, 0, 0, 0)
        self.fd_input = self.create_form_input()

        # fill-in form initialization code
        fl_set_object_dblbuffer(self.fd_input.report, 1)
        fl_set_object_return(self.fd_input.multiinput, FL_RETURN_ALWAYS)
        fl_set_object_return(self.fd_input.norminput, FL_RETURN_ALWAYS)

        # show the first form
        fl_show_form(self.fd_input.input_, FL_PLACE_CENTERFREE, \
                     FL_FULLBORDER, "input")

        while fl_do_forms():
            pass    # empty

        return 0


    # callbacks for form input

    def done_cb(self, pobj, data):
        fl_finish()
        sys.exit(0)


    def input_cb(self, pobj, data):
        unused, cx, cy = fl_get_input_cursorpos(pobj)
        buf = "x=%d y=%d" % (cx, cy)
        fl_set_object_label(self.fd_input.report, buf)


    def hide_show_cb(self, pobj, data):
        if fl_object_is_visible(self.fd_input.multiinput):
            fl_hide_object(self.fd_input.multiinput)
        else:
            fl_show_object(self.fd_input.multiinput)


    # Form definition file
    def create_form_input(self):

        fdui = FD_input()

        fdui.input_ = fl_bgn_form(FL_NO_BOX, 441, 441)

        pobj = fl_add_box( FL_UP_BOX, 0, 0, 441, 441, "")

        fdui.norminput = fl_add_input(FL_NORMAL_INPUT, 40, 40, \
                                      340, 30, "Normal Input")
        fl_set_object_lalign(fdui.norminput, FL_ALIGN_LEFT_TOP)
        fl_set_object_callback(fdui.norminput, self.input_cb, 0)
        fl_set_object_return(fdui.norminput, FL_RETURN_END_CHANGED)

        pobj = fl_add_input(FL_INT_INPUT, 40, 100, 160, 30, \
                            "Integer Input")
        fl_set_object_lalign(pobj, FL_ALIGN_LEFT_TOP)
        fl_set_object_return(pobj, FL_RETURN_END_CHANGED)

        pobj = fl_add_input(FL_FLOAT_INPUT, 230, 100, 160, 30, \
                            "Float Input")
        fl_set_object_lalign(pobj, FL_ALIGN_LEFT_TOP)
        fl_set_object_return(pobj, FL_RETURN_END_CHANGED)

        pobj = fl_add_input(FL_DATE_INPUT, 40, 150, 160, 30, \
                            "Date Input")
        fl_set_object_lalign(pobj, FL_ALIGN_LEFT_TOP)
        fl_set_object_return(pobj, FL_RETURN_END_CHANGED)

        pobj = fl_add_input(FL_SECRET_INPUT, 230, 150, 160, 30, \
                            "Secret Input")
        fl_set_object_lalign(pobj, FL_ALIGN_LEFT_TOP)
        fl_set_object_return(pobj, FL_RETURN_END_CHANGED)

        fdui.multiinput = fl_add_input(FL_MULTILINE_INPUT, 40, 210, \
                                       360, 180, "Multi-line input")
        fl_set_object_lalign(fdui.multiinput, FL_ALIGN_LEFT_TOP)
        fl_set_object_callback(fdui.multiinput, self.input_cb, 0)
        fl_set_object_return(fdui.multiinput, FL_RETURN_ALWAYS)

        fdui.report = fl_add_text(FL_NORMAL_TEXT, 30, 400, 210, 30, "")

        pobj = fl_add_button(FL_NORMAL_BUTTON, 330, 400, 70, 30, "Done")
        fl_set_object_lalign(pobj, FL_ALIGN_CENTER)
        fl_set_object_callback(pobj, self.done_cb, 0)

        pobj = fl_add_button(FL_NORMAL_BUTTON, 250, 400, 70, 30, \
                             "Hide/Show")
        fl_set_object_lalign(pobj, FL_ALIGN_CENTER)
        fl_set_object_callback(pobj, self.hide_show_cb, 0)

        fl_end_form()

        return fdui



if __name__ == '__main__':
    Flinputall(len(sys.argv), sys.argv)

