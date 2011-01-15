#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  borderwidth.c XForms demo, with some adaptations.
#
#  borderwidth.c was written by T.C. Zhao and M. Overmars (1997)
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
#  demo showing the effect of different border widths
#

import sys
import xformslib as xfl


class BorderWidth(object):
    def __init__(self, lsysargv, sysargv):
        # application default. Can be overriden by the command line options
        xfl.fl_set_border_width(1)
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        self.pbwform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 380, 340)
        self.pbwgroup = xfl.fl_bgn_group()
        xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 380, 340, "")
        xfl.fl_add_frame(xfl.FL_EMBOSSED_FRAME, 220, 60, 135, 145, "")
        xfl.fl_add_frame(xfl.FL_ENGRAVED_FRAME, 15, 60, 185, 145, "")
        xfl.fl_add_slider(xfl.FL_HOR_SLIDER, 25, 70, 160, 20, "")
        xfl.fl_add_valslider(xfl.FL_HOR_BROWSER_SLIDER, 25, 105, \
                160, 20, "")
        self.pobj = xfl.fl_add_scrollbar(xfl.FL_HOR_THIN_SCROLLBAR,
                25, 140, 160, 20, "")
        xfl.fl_set_scrollbar_size(self.pobj, 0.2)
        xfl.fl_add_counter(xfl.FL_NORMAL_COUNTER, 25, 175, \
                160, 20, "")
        self.ppmobj = xfl.fl_add_pixmapbutton(xfl.FL_NORMAL_BUTTON, \
                305, 145, 40, 35, "")
        xfl.fl_add_positioner(xfl.FL_NORMAL_POSITIONER, 30, 225, \
                100, 80, "")
        xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 230, 65, 100, 28, \
                "Button")
        xfl.fl_add_lightbutton(xfl.FL_PUSH_BUTTON, 230, 98, 100, 28, \
                "LightButton")
        xfl.fl_add_roundbutton(xfl.FL_PUSH_BUTTON, 230, 128, \
                80, 32, "Button")
        self.pobj = xfl.fl_add_round3dbutton(xfl.FL_PUSH_BUTTON, \
                230, 152, 80, 32, "Button")
        xfl.fl_set_object_color(self.pobj, xfl.FL_COL1, xfl.FL_BLUE)
        xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 230, 175, \
                80, 32, "Button")
        xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 195, 240, 160, 28, \
                "Input")
        self.pbwselect = xfl.fl_add_select(xfl.FL_MENU_SELECT, 105, \
                20, 100, 28, "Border Width")
        xfl.fl_set_object_callback(self.pbwselect, self.bw_callback, 0)
        xfl.fl_end_group()
        self.pdoneobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 270, 290, \
                75, 30, "Done")
        xfl.fl_set_object_callback(self.pdoneobj, self.done_callback, 0)
        xfl.fl_end_form()
        # end create_form_bwform

        # form initialization code
        xfl.fl_set_pixmapbutton_file(self.ppmobj, "crab.xpm")
        xfl.fl_add_select_items(self.pbwselect, \
                "-5 Pixel|-4 Pixel|-3 Pixel|-2 Pixel|-1 Pixel|" \
                " 1 Pixel| 2 Pixel| 3 Pixel| 4 Pixel| 5 Pixel")
        pbw = xfl.fl_get_border_width()
        if (pbw < -5 or pbw == 0 or pbw > 5):
            pbw = -2
            xfl.fl_set_border_width(pbw)

        txt = "%2d Pixel" % pbw
        ppupentr = xfl.fl_get_select_item_by_label(self.pbwselect, txt)
        xfl.fl_set_select_item(self.pbwselect, ppupentr)

        # show the form
        xfl.fl_show_form(self.pbwform, xfl.FL_PLACE_CENTER, \
                xfl.FL_TRANSIENT, "bwform")

        while xfl.fl_do_forms():
            pass                # empty


    # callbacks for form bwform

    def done_callback(self, pobj, data):
        xfl.fl_finish()
        sys.exit(0)


    def bw_callback(self, pobj, data):
        bws = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        pr = xfl.fl_get_select_item(pobj)
        indx = pr.contents.val
        bw = bws[indx]
        xfl.fl_set_object_bw(self.pbwgroup, bw)
        xfl.fl_set_object_bw(self.pdoneobj, bw)
        xfl.fl_popup_set_bw(pr.contents.popup, bw)



if __name__ == '__main__':
    print("********* borderwidth.py *********")
    appl = BorderWidth(len(sys.argv), sys.argv)

