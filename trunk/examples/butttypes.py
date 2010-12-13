#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  butttypes.c XForms demo, with some adaptations.
#
#  butttypes.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# All button types
#

import sys
import xformslib as xfl



class Flbuttontypes(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.create_form_form0()
        # fill-in form initialization code
        # show the first form
        xfl.fl_show_form(self.form0, xfl.FL_PLACE_CENTER, \
                xfl.FL_FULLBORDER, "form0")
        xfl.fl_do_forms()


    def create_form_form0(self):

        self.form0 = xfl.fl_bgn_form(xfl.FL_NO_BOX, 360, 330)

        pobj0 = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 360, 330, "")

        pobj1 = xfl.fl_add_button(xfl.FL_HIDDEN_BUTTON, 0, 0, \
                360, 330, "")
        xfl.fl_set_object_lalign(pobj1, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_callback(pobj1, self.button_cb, 0)

        pobj2 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 18, 15, \
                107, 30, "Normal")
        xfl.fl_set_object_lalign(pobj2, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(pobj2, xfl.FL_BOLD_STYLE)
        xfl.fl_set_object_callback(pobj2, self.button_cb, 1)

        pobj3 = xfl.fl_add_button(xfl.FL_PUSH_BUTTON, 18, 53, \
                107, 30, "Push")
        xfl.fl_set_object_lalign(pobj3, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(pobj3, xfl.FL_BOLD_STYLE)
        xfl.fl_set_object_callback(pobj3, self.button_cb, 2)

        pobj4 = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 18, 91, \
                107, 30, "Radio 1")
        xfl.fl_set_object_lalign(pobj4, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(pobj4, xfl.FL_BOLD_STYLE)
        xfl.fl_set_object_callback(pobj4, self.button_cb, 3)
        xfl.fl_set_button(pobj4, 1)

        pobj5 = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 18, 129, \
                107, 30, "Radio 2")
        xfl.fl_set_object_lalign(pobj5, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(pobj5, xfl.FL_BOLD_STYLE)
        xfl.fl_set_object_callback(pobj5, self.button_cb, 4)

        pobj6 = xfl.fl_add_button(xfl.FL_TOUCH_BUTTON, 18, 167, \
                107, 30, "Touch")
        xfl.fl_set_object_lalign(pobj6, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(pobj6, xfl.FL_BOLD_STYLE)
        xfl.fl_set_object_callback(pobj6, self.button_cb, 5)
        xfl.fl_set_object_return(pobj6, xfl.FL_RETURN_CHANGED)

        pobj7 = xfl.fl_add_button(xfl.FL_INOUT_BUTTON, 18, 205, \
                107, 30, "InOut")
        xfl.fl_set_object_lalign(pobj7, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(pobj7, xfl.FL_BOLD_STYLE)
        xfl.fl_set_object_callback(pobj7, self.button_cb, 6)

        pobj8 = xfl.fl_add_button(xfl.FL_MENU_BUTTON, 18, 243, \
                107, 30, "Menu")
        xfl.fl_set_object_lalign(pobj8, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(pobj8, xfl.FL_BOLD_STYLE)
        xfl.fl_set_object_callback(pobj8, self.button_cb, 7)

        pobj9 = xfl.fl_add_button(xfl.FL_RETURN_BUTTON, 18, 281, \
                107, 30, "Return")
        xfl.fl_set_object_lalign(pobj9, xfl.FL_ALIGN_CENTER)
        xfl.fl_set_object_lstyle(pobj9, xfl.FL_BOLD_STYLE)
        xfl.fl_set_object_callback(pobj9, self.button_cb, 8)

        self.br = xfl.fl_add_browser(xfl.FL_NORMAL_BROWSER, 135, 15, \
                210, 296, "")
        xfl.fl_set_object_color(self.br, xfl.FL_COL1, xfl.FL_YELLOW)
        xfl.fl_set_object_callback(self.br, self.button_cb, 9)

        xfl.fl_end_form()


    # callbacks for form form0
    def button_cb(self, pobj, data):
        buf = ""
        if (xfl.fl_get_object_type(pobj) == xfl.FL_HIDDEN_BUTTON):
            if xfl.fl_show_question("Want to Quit ?", 1) == 1:
                xfl.fl_finish()
                sys.exit(0)
        else:
            #sprintf( buf, "%s callback called: %d", ob->label, xfl.fl_get_button( ob ))
            buf = "%s callback called: %d" % (xfl.fl_get_object_label(pobj), \
                    xfl.fl_get_button(pobj))
            xfl.fl_addto_browser(self.br, buf)



if __name__ == '__main__':
    print("********* butttypes.py *********")
    appl = Flbuttontypes(len(sys.argv), sys.argv)

