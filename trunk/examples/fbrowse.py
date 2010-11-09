#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  fbrowse.c XForms demo, with some adaptations.
#
#  fbrowse.c was written by T.C. Zhao and M. Overmars
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo shows the use of a browser and a file selector.
# Good browser/scrollbar test
#

import sys
import xformslib as xfl



class FLfbrowse(object):

    def __init__(self, lsysarg, sysargv):

        xfl.fl_initialize(lsysarg, sysargv, "FormDemo", 0, 0)
        fdnew = self.create_form()

        xfl.fl_clear_browser(self.pbr)
        xfl.fl_add_browser_line(self.pbr, "LOAD A FILE.")
        xfl.fl_set_browser_fontstyle(self.pbr, xfl.FL_FIXED_STYLE)

        xfl.fl_show_form(fdnew, xfl.FL_PLACE_FREE, xfl.FL_FULLBORDER, \
                "Browser")

        poret = xfl.fl_do_forms()

        if poret.contents.label:
            prndata = poret.contents.label
        else:
            prndata = ""
        print "%p %d %s\n" % poret.contents, poret.contents.objclass, prndata

        xfl.fl_hide_form(fdnew)
        xfl.fl_free_form(fdnew)

        xfl.fl_finish()


    def load_file(self, pobj, arg):
        fname = xfl.fl_show_file_selector("File To Load", "", "*", "")
        if fname:
            if not xfl.fl_load_browser(self.pbr, fname):
                xfl.fl_add_browser_line(self.pbr,"NO SUCH FILE!")


    def set_size(self, pobj, arg):
        xfl.fl_set_browser_fontsize(self.pbr, arg)


    def exit_program(self, pobj, data):
        xfl.fl_finish()
        sys.exit(0)


    def hide_show(self, pobj, data):
        if xfl.fl_object_is_visible(self.pbr):
            xfl.fl_hide_object(self.pbr)
        else:
            xfl.fl_show_object(self.pbr)


    def create_form(self):

        x = 20
        dx = 80
        dy = 28

        pform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 590, 610)
        pobj1 = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 590, 610, "")

        self.pbr = xfl.fl_add_browser(xfl.FL_NORMAL_BROWSER, 20, 20, \
                550, 530, "")
        xfl.fl_set_object_boxtype(self.pbr, xfl.FL_EMBOSSED_BOX)

        pobj1 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, x, 565, dx-5, dy, \
                "Load")
        xfl.fl_set_object_callback(pobj1, self.load_file, 0)
        x += dx

        pobj2 = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, x, 565, \
                dx, dy, "Tiny")
        xfl.fl_set_object_callback(pobj2, self.set_size, xfl.FL_TINY_SIZE)
        x += dx

        pobj3 = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, x , 565, \
                dx, dy, "Small")
        xfl.fl_set_object_callback(pobj3, self.set_size, xfl.FL_SMALL_SIZE)
        xfl.fl_set_button(pobj3, xfl.FL_SMALL_SIZE == xfl.FL_BROWSER_FONTSIZE)
        x += dx

        pobj4 = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, x , 565, \
                dx, dy, "Normal")
        xfl.fl_set_object_callback(pobj4, self.set_size, xfl.FL_NORMAL_SIZE)
        xfl.fl_set_button(pobj4, xfl.FL_NORMAL_SIZE == xfl.FL_BROWSER_FONTSIZE)
        x += dx

        pobj5 = xfl.fl_add_lightbutton(xfl.FL_RADIO_BUTTON, x , 565, \
                dx, dy, "Large")
        xfl.fl_set_object_callback(pobj5, self.set_size, xfl.FL_LARGE_SIZE)
        x += dx

        pobj6 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, x, 565, \
                dx, dy, "Hide/Show")
        xfl.fl_set_object_callback(pobj6, self.hide_show, 0)
        x += dx

        pobj7 = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, x, 565, dx, dy, "Exit")       #60->dx
        xfl.fl_set_object_callback(pobj7, self.exit_program, 0)

        xfl.fl_end_form()

        xfl.fl_adjust_form_size(pform)

        return pform



if __name__ == '__main__':
    FLfbrowse(len(sys.argv), sys.argv)
