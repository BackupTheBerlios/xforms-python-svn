#!/usr/bin/env python3

#  This file is part of xforms-python, and it has been ported from
#  strange_button.c XForms demo, with some adaptations.
#
#  strange_button.c is written by Jens Thoms Toerring <jt@toerring.de>
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#

import sys
#sys.path.append("..")
import xformslib as xfl


# Forms and Objects
class FD_x(object):
    vdata = None
    cdata = None
    ldata = 0
    c = None


class Flstrangebutton(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, "Button", None, 0)
        self.fd_x = self.create_form_x()
        xfl.fl_show_form(self.fd_x.x, xfl.FL_PLACE_CENTERFREE, \
                xfl.FL_FULLBORDER, "strange button")
        xfl.fl_do_forms()
        if xfl.fl_form_is_visible(self.fd_x.x):
            xfl.fl_hide_form(self.fd_x.x)
        xfl.fl_finish()
        sys.exit(0)


    def ccb(self, pobj, data):
        button = xfl.fl_mouse_button()
        idx = xfl.fl_get_label_char_at_mouse(pobj)
        label = xfl.fl_get_object_label(pobj)

        if idx == -1:
            return

        digit = label[idx]      # it's an int
        if button == xfl.FL_LEFT_MOUSE or button == xfl.FL_SCROLLUP_MOUSE:
            if digit == "9":
                digit = "0"
            else:
                digit = chr(ord(digit) + 1)
        elif button == xfl.FL_RIGHT_MOUSE or button == xfl.FL_SCROLLDOWN_MOUSE:
            if digit == "0":
                digit = "9"
            else:
                digit = chr(ord(digit) - 1)

        newstrng = list(label)
        newstrng[idx] = digit
        strng = "".join(newstrng)
        xfl.fl_set_object_label(pobj, strng)


    def create_form_x(self):

        fdui = FD_x()
        fdui.x = xfl.fl_bgn_form(xfl.FL_FLAT_BOX, 170, 176)
        pobj = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 20, 10, 150, 50, \
                "Click on the digits...\n(left or right button)")
        xfl.fl_set_object_lsize(pobj, xfl.FL_NORMAL_SIZE)

        fdui.c = xfl.fl_add_button(xfl.FL_TOUCH_BUTTON, 40, 65, 90, 40, "012345")
        xfl.fl_set_object_boxtype(fdui.c, xfl.FL_EMBOSSED_BOX );
        xfl.fl_set_object_color(fdui.c, xfl.FL_YELLOW, xfl.FL_YELLOW );
        xfl.fl_set_object_lstyle(fdui.c, \
                xfl.FL_FIXED_STYLE | xfl.FL_EMBOSSED_STYLE)
        xfl.fl_set_object_lsize(fdui.c, xfl.FL_LARGE_SIZE );
        xfl.fl_set_object_callback(fdui.c, self.ccb, 0)
        xfl.fl_set_button_mouse_buttons(fdui.c, 1 | 4 | 8 | 16)
        xfl.fl_set_object_helper(fdui.c, \
                "May not look like a button but it's one...\n" \
                "(Also try the scroll wheel if you have.)" )

        pobj = xfl.fl_add_button(xfl.FL_RETURN_BUTTON, 50, 130, 70, 30, "Exit" );
        xfl.fl_set_button_mouse_buttons(pobj, 1)

        xfl.fl_end_form()
        xfl.fl_adjust_form_size(fdui.x)
        return fdui


if __name__ == '__main__':
    print("********* strange_button.py *********")
    Flstrangebutton(len(sys.argv), sys.argv)
