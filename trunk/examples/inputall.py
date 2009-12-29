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
from xformslib import library as xf
from xformslib import xfdata as xfc



# Forms and Objects

class FD_input(object):
    input_ = None
    vdata = None
    cdata = ""
    ldata = 0
    norminput = None
    multiinput = None
    report = None


# callbacks for form input

def done_cb(pobj, data):
    xf.fl_finish()
    sys.exit(0)


def input_cb(pobj, data):
    unused, cx, cy = xf.fl_get_input_cursorpos(pobj)
    buf = "x=%d y=%d" % (cx.value, cy.value)
    xf.fl_set_object_label(fd_input.report, buf)


def hide_show_cb(pobj, data):
    if fd_input.multiinput.contents.visible:
        xf.fl_hide_object(fd_input.multiinput)
    else:
        xf.fl_show_object(fd_input.multiinput)



def main(lsysargv, sysargv):
    global fd_input

    xf.fl_initialize(lsysargv, sysargv, 0, 0, 0)
    fd_input = create_form_input()

    # fill-in form initialization code

    xf.fl_set_object_dblbuffer(fd_input.report, 1)
    xf.fl_set_object_return(fd_input.multiinput, xfc.FL_RETURN_ALWAYS)
    xf.fl_set_object_return(fd_input.norminput, xfc.FL_RETURN_ALWAYS)

    # show the first form

    xf.fl_show_form(fd_input.input_, xfc.FL_PLACE_CENTERFREE, \
                    xfc.FL_FULLBORDER, "input")

    while xf.fl_do_forms():
        pass    # empty

    return 0



# Form definition file

def create_form_input():

    fdui = FD_input()

    fdui.input_ = xf.fl_bgn_form( xfc.FL_NO_BOX, 441, 441)

    pobj = xf.fl_add_box( xfc.FL_UP_BOX, 0, 0, 441, 441, "")

    fdui.norminput = xf.fl_add_input(xfc.FL_NORMAL_INPUT, 40, 40, \
                                     340, 30, "Normal Input")
    xf.fl_set_object_lalign(fdui.norminput, xfc.FL_ALIGN_LEFT_TOP)
    xf.fl_set_object_callback(fdui.norminput, input_cb, 0)
    xf.fl_set_object_return(fdui.norminput, xfc.FL_RETURN_END_CHANGED)

    pobj = xf.fl_add_input(xfc.FL_INT_INPUT, 40, 100, 160, 30, \
                          "Integer Input")
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_LEFT_TOP)
    xf.fl_set_object_return(pobj, xfc.FL_RETURN_END_CHANGED)

    pobj = xf.fl_add_input(xfc.FL_FLOAT_INPUT, 230, 100, 160, 30, \
                          "Float Input")
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_LEFT_TOP)
    xf.fl_set_object_return(pobj, xfc.FL_RETURN_END_CHANGED)

    pobj = xf.fl_add_input(xfc.FL_DATE_INPUT, 40, 150, 160, 30, \
                          "Date Input")
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_LEFT_TOP)
    xf.fl_set_object_return(pobj, xfc.FL_RETURN_END_CHANGED)

    pobj = xf.fl_add_input(xfc.FL_SECRET_INPUT, 230, 150, 160, 30, \
                          "Secret Input")
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_LEFT_TOP)
    xf.fl_set_object_return(pobj, xfc.FL_RETURN_END_CHANGED)

    fdui.multiinput = xf.fl_add_input(xfc.FL_MULTILINE_INPUT, 40, 210, \
                                      360, 180, "Multi-line input")
    xf.fl_set_object_lalign(fdui.multiinput, xfc.FL_ALIGN_LEFT_TOP)
    xf.fl_set_object_callback(fdui.multiinput, input_cb, 0)
    xf.fl_set_object_return(fdui.multiinput, xfc.FL_RETURN_ALWAYS)

    fdui.report = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 30, 400, 210, 30, \
                                 "")

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 330, 400, 70, 30, "Done")
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_callback(pobj, done_cb, 0)

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 250, 400, 70, 30, "Hide/Show")
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_CENTER)
    xf.fl_set_object_callback(pobj, hide_show_cb, 0)

    xf.fl_end_form()

    return fdui



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

