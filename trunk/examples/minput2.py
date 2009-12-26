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
from xformslib import library as xf
from xformslib import xfdata as xfc



# Forms and Objects

class FD_inputform(object):
    inputform = None
    vdata = None
    ldata = 0
    input1 = None
    howreturn = None
    status = None
    input2 = None


#FD_inputform *ui;


def peek_event(form, xev):

    #if ( ( ( XEvent * )xev )->type == KeyPress )
    if xev[0].type == xfc.KeyPress:
        xf.fl_set_object_label(ui.status, "keyboard input")
        # XFlush( fl_get_display( ) );   /* necessary to show the label */
        xf.fl_msleep(50)

    return 0



def main(lsysargv, sysargv):
    global ui

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
    ui = create_form_inputform()
    xf.fl_register_raw_callback(ui.inputform, xfc.KeyPressMask, peek_event)

    xf.fl_show_form(ui.inputform, xfc.FL_PLACE_CENTER, xfc.FL_TRANSIENT, \
                    "Input")

    xf.fl_do_forms()
    xf.fl_finish()

    return 0



def input_callback(ob, data):

     buf = "Input%ld returned" % data
     xf.fl_set_object_label(ui.status, buf)
     #XFlush( xf.fl_get_display( ))
     xf.fl_msleep(50)



def howreturn_callback(ob, data):
    xf.fl_set_input_return(ui.input1, xf.fl_get_button(ob))
    xf.fl_set_input_return(ui.input2, xf.fl_get_button(ob))



def create_form_inputform():

    fdui = FD_inputform()

    fdui.inputform = xf.fl_bgn_form(xfc.FL_NO_BOX, 475, 485)

    obj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 475, 485, "")
    fdui.input1 = xf.fl_add_input(xfc.FL_MULTILINE_INPUT, 15, 275, 350, 180,
                                  "")
    xf.fl_set_object_lalign(fdui.input1, xfc.FL_ALIGN_TOP)
    xf.fl_set_object_callback(fdui.input1, input_callback, 1)

    fdui.howreturn = xf.fl_add_checkbutton(xfc.FL_PUSH_BUTTON,
                                           375, 435, 80, 35, "always\nreturn")
    xf.fl_set_object_color(fdui.howreturn, xfc.FL_COL1, xfc.FL_BLUE)
    xf.fl_set_object_callback(fdui.howreturn, howreturn_callback, 0)

    fdui.status = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 20, 15, 270, 30, "")
    xf.fl_set_object_boxtype(fdui.status, xfc.FL_FRAME_BOX)

    xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 375, 15, 80, 35, "Done")

    fdui.input2 = xf.fl_add_input(xfc.FL_MULTILINE_INPUT, 15, 60, 349, 185,
                                  "")
    xf.fl_set_object_lalign(fdui.input2, xfc.FL_ALIGN_TOP)
    xf.fl_set_object_callback(fdui.input2, input_callback, 2)

    xf.fl_end_form()

    return fdui




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

