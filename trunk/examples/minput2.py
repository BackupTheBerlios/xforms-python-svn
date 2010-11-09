#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  minput2.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Input return setting and raw callback. Terrible hack.
#

import sys
#sys.path.append("..")
import xformslib as xfl



# Forms and Objects
class FD_inputform(object):
    inputform = None
    vdata = None
    ldata = 0
    input1 = None
    howreturn = None
    status = None
    input2 = None


class Flminput2(object):

    def __init__(self, lsysargv, sysargv):

        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.ui = self.create_form_inputform()
        xfl.fl_register_raw_callback(self.ui.inputform, xfl.KeyPressMask, \
                self.peek_event)
        xfl.fl_show_form(self.ui.inputform, xfl.FL_PLACE_CENTER, \
                xfl.FL_TRANSIENT, "Input")
        xfl.fl_do_forms()
        xfl.fl_finish()


    def peek_event(self, form, xev):
        if xev.contents.type == xfl.KeyPress:
            xfl.fl_set_object_label(self.ui.status, "keyboard input")
            xfl.fl_XFlush()          # necessary to show the label
            xfl.fl_msleep(50)
        return 0


    def input_callback(self, pobj, data):
        buf = "Input%ld returned" % data
        xfl.fl_set_object_label(self.ui.status, buf)
        xfl.fl_XFlush()
        xfl.fl_msleep(50)


    def howreturn_callback(self, pobj, data):
        xfl.fl_set_object_return(self.ui.input1, xfl.fl_get_button(pobj))
        xfl.fl_set_object_return(self.ui.input2, xfl.fl_get_button(pobj))


    def create_form_inputform(self):

        fdui = FD_inputform()

        fdui.inputform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 475, 485)

        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 475, 485, "")
        fdui.input1 = xfl.fl_add_input(xfl.FL_MULTILINE_INPUT, 15, 275, \
                350, 180, "")
        xfl.fl_set_object_lalign(fdui.input1, xfl.FL_ALIGN_TOP)
        xfl.fl_set_object_callback(fdui.input1, self.input_callback, 1)
        fdui.howreturn = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON,
                                   375, 435, 80, 35, "always\nreturn")
        xfl.fl_set_object_color(fdui.howreturn, xfl.FL_COL1, xfl.FL_BLUE)
        xfl.fl_set_object_callback(fdui.howreturn, self.howreturn_callback, 0)
        fdui.status = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 20, 15, 270, 30, "")
        xfl.fl_set_object_boxtype(fdui.status, xfl.FL_FRAME_BOX)
        xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 375, 15, 80, 35, "Done")
        fdui.input2 = xfl.fl_add_input(xfl.FL_MULTILINE_INPUT, 15, 60, \
                349, 185, "")
        xfl.fl_set_object_lalign(fdui.input2, xfl.FL_ALIGN_TOP)
        xfl.fl_set_object_callback(fdui.input2, self.input_callback, 2)

        xfl.fl_end_form()

        return fdui



if __name__ == '__main__':
    Flminput2(len(sys.argv), sys.argv)
