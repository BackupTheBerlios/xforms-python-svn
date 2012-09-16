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
import xformslib as xfl


# Forms and Objects
class FD_input(object):
    input_ = None
    vdata = None
    cdata = ""
    ldata = 0
    norminput = None
    intinput = None
    floatinput = None
    dateinput = None
    secretinput = None
    multiinput = None
    report = None


class Flinputall(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.fd_input = self.create_form_input()
        # fill-in form initialization code
        xfl.fl_set_object_dblbuffer(self.fd_input.report, 1)
        xfl.fl_set_object_return(self.fd_input.norminput, \
                xfl.FL_RETURN_ALWAYS)
        xfl.fl_set_object_return(self.fd_input.intinput, \
                xfl.FL_RETURN_ALWAYS)
        xfl.fl_set_object_return(self.fd_input.floatinput, \
                xfl.FL_RETURN_ALWAYS)
        xfl.fl_set_object_return(self.fd_input.dateinput, \
                xfl.FL_RETURN_ALWAYS)
        xfl.fl_set_object_return(self.fd_input.secretinput, \
                xfl.FL_RETURN_ALWAYS)
        xfl.fl_set_object_return(self.fd_input.multiinput, \
                xfl.FL_RETURN_ALWAYS)
        # show the first form
        xfl.fl_show_form(self.fd_input.input_, xfl.FL_PLACE_CENTERFREE, \
                xfl.FL_FULLBORDER, "input")
        while xfl.fl_do_forms():
            pass    # empty

    # callbacks for form input

    def done_cb(self, pobj, data):
        xfl.fl_finish()
        sys.exit(0)


    def input_cb(self, pobj, data):
        unused, cx, cy = xfl.fl_get_input_cursorpos(pobj)
        buf = "x = %d, y = %d" % (cx, cy)
        xfl.fl_set_object_label(self.fd_input.report, buf)


    def hide_show_cb(self, pobj, data):
        if xfl.fl_object_is_visible(self.fd_input.multiinput):
            xfl.fl_hide_object(self.fd_input.multiinput)
        else:
            xfl.fl_show_object(self.fd_input.multiinput)


    # Form definition file
    def create_form_input(self):
        fdui = FD_input()
        fdui.input_ = xfl.fl_bgn_form(xfl.FL_NO_BOX, 441, 441)
        pobj = xfl.fl_add_box( xfl.FL_UP_BOX, 0, 0, 441, 441, "")
        fdui.norminput = xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 40, 40, \
                340, 30, "Normal Input")
        xfl.fl_set_object_lalign(fdui.norminput, xfl.FL_ALIGN_LEFT_TOP)
        xfl.fl_set_object_callback(fdui.norminput, self.input_cb, 0)
        xfl.fl_set_object_return(fdui.norminput, xfl.FL_RETURN_END_CHANGED)
        fdui.intinput = xfl.fl_add_input(xfl.FL_INT_INPUT, 40, 100, 160, \
                30, "Integer Input")
        xfl.fl_set_object_lalign(fdui.intinput, xfl.FL_ALIGN_LEFT_TOP)
        xfl.fl_set_object_return(fdui.intinput, xfl.FL_RETURN_END_CHANGED)
        fdui.floatinput = xfl.fl_add_input(xfl.FL_FLOAT_INPUT, 230, 100, \
                160, 30, "Float Input")
        xfl.fl_set_object_lalign(fdui.floatinput, xfl.FL_ALIGN_LEFT_TOP)
        xfl.fl_set_object_return(fdui.floatinput, xfl.FL_RETURN_END_CHANGED)
        fdui.dateinput = xfl.fl_add_input(xfl.FL_DATE_INPUT, 40, 150, \
                160, 30, "Date Input")
        xfl.fl_set_object_lalign(fdui.dateinput, xfl.FL_ALIGN_LEFT_TOP)
        xfl.fl_set_object_return(fdui.dateinput, xfl.FL_RETURN_END_CHANGED)
        fdui.secretinput = xfl.fl_add_input(xfl.FL_SECRET_INPUT, 230, 150, \
                160, 30, "Secret Input")
        xfl.fl_set_object_lalign(fdui.secretinput, xfl.FL_ALIGN_LEFT_TOP)
        xfl.fl_set_object_return(fdui.secretinput, xfl.FL_RETURN_END_CHANGED)
        fdui.multiinput = xfl.fl_add_input(xfl.FL_MULTILINE_INPUT, 40, 210, \
                360, 180, "Multi-line input")
        xfl.fl_set_object_lalign(fdui.multiinput, xfl.FL_ALIGN_LEFT_TOP)
        xfl.fl_set_object_callback(fdui.multiinput, self.input_cb, 0)
        xfl.fl_set_object_return(fdui.multiinput, xfl.FL_RETURN_ALWAYS)
        fdui.report = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 30, 400, 210, 30, \
                "")
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 330, 400, 70, 30, \
                "Done")
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_callback(pobj, self.done_cb, 0)
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 250, 400, 80, 30, \
                "Hide/Show")
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_callback(pobj, self.hide_show_cb, 0)
        xfl.fl_end_form()
        return fdui


if __name__ == '__main__':
    print("********* inputall.py *********")
    Flinputall(len(sys.argv), sys.argv)
