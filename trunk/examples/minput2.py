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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flinput import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *



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

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.ui = self.create_form_inputform()
        fl_register_raw_callback(self.ui.inputform, KeyPressMask, \
                                    self.peek_event)

        fl_show_form(self.ui.inputform, FL_PLACE_CENTER, \
                        FL_TRANSIENT, "Input")

        fl_do_forms()
        fl_finish()


    def peek_event(self, form, xev):

        if xev.contents.type == KeyPress:
            fl_set_object_label(self.ui.status, "keyboard input")
            fl_XFlush()          # necessary to show the label
            fl_msleep(50)
        return 0


    def input_callback(self, pobj, data):

        buf = "Input%ld returned" % data
        fl_set_object_label(self.ui.status, buf)
        fl_XFlush()
        fl_msleep(50)


    def howreturn_callback(self, pobj, data):
        fl_set_object_return(self.ui.input1, fl_get_button(pobj))
        fl_set_object_return(self.ui.input2, fl_get_button(pobj))


    def create_form_inputform(self):

        fdui = FD_inputform()

        fdui.inputform = fl_bgn_form(FL_NO_BOX, 475, 485)

        pobj = fl_add_box(FL_UP_BOX, 0, 0, 475, 485, "")
        fdui.input1 = fl_add_input(FL_MULTILINE_INPUT, 15, 275, 350, 180,
                                  "")
        fl_set_object_lalign(fdui.input1, FL_ALIGN_TOP)
        fl_set_object_callback(fdui.input1, self.input_callback, 1)

        fdui.howreturn = fl_add_checkbutton(FL_PUSH_BUTTON,
                                   375, 435, 80, 35, "always\nreturn")
        fl_set_object_color(fdui.howreturn, FL_COL1, FL_BLUE)
        fl_set_object_callback(fdui.howreturn, self.howreturn_callback, 0)

        fdui.status = fl_add_text(FL_NORMAL_TEXT, 20, 15, 270, 30, "")
        fl_set_object_boxtype(fdui.status, FL_FRAME_BOX)

        fl_add_button(FL_NORMAL_BUTTON, 375, 15, 80, 35, "Done")

        fdui.input2 = fl_add_input(FL_MULTILINE_INPUT, 15, 60, 349, 185,
                                  "")
        fl_set_object_lalign(fdui.input2, FL_ALIGN_TOP)
        fl_set_object_callback(fdui.input2, self.input_callback, 2)

        fl_end_form()

        return fdui




if __name__ == '__main__':
    Flminput2(len(sys.argv), sys.argv)

