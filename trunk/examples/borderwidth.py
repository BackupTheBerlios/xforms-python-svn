#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  borderwidth.c XForms demo, with some adaptations.
#
#  borderwidth.c was written by T.C. Zhao and M. Overmars  (1997)
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
#  demo showing the effect of different border widths
#

import sys
from xformslib import flbasic, flxbasic, flselect, flmisc, \
    flslider, flscrollbar, flcounter, flbutton, flpositioner, \
    flinput, flbitmap, flpopup, xfdata



class BorderWidth(object):
    def __init__(self, lsysargv, sysargv):
        # application default. Can be overriden by the command line options
        flbasic.fl_set_border_width(1)
        flxbasic.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.pbwform = flbasic.fl_bgn_form(xfdata.FL_NO_BOX, 380, 340)
        self.pbwgroup = flbasic.fl_bgn_group()
        flmisc.fl_add_box(xfdata.FL_UP_BOX, 0, 0, 380, 340, "")
        flmisc.fl_add_frame(xfdata.FL_EMBOSSED_FRAME, 220, 60, 135, 145, "")
        flmisc.fl_add_frame(xfdata.FL_ENGRAVED_FRAME, 15, 60, 185, 145, "")
        flslider.fl_add_slider(xfdata.FL_HOR_SLIDER, 25, 70, 160, 20, "")
        flslider.fl_add_valslider(xfdata.FL_HOR_BROWSER_SLIDER, 25, 105, 160, 20, "")
        self.pobj = flscrollbar.fl_add_scrollbar(xfdata.FL_HOR_THIN_SCROLLBAR, 25, 140, 160, 20, "")
        flscrollbar.fl_set_scrollbar_size(self.pobj, 0.2)
        flcounter.fl_add_counter(xfdata.FL_NORMAL_COUNTER, 25, 175, 160, 20, "")
        self.ppmobj = flbutton.fl_add_pixmapbutton(xfdata.FL_NORMAL_BUTTON, 305, 145, \
                                          40, 35, "")
        positionerfn.fl_add_positioner(xfdata.FL_NORMAL_POSITIONER, 30, 225, 100, 80, "")
        flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 230, 65, 100, 28, "Button")
        flbutton.fl_add_lightbutton(xfdata.FL_PUSH_BUTTON, 230, 98, 100, 28, "LightButton")
        flbutton.fl_add_roundbutton(xfdata.FL_PUSH_BUTTON, 230, 128, 80, 32, "Button")
        self.pobj = flbutton.fl_add_round3dbutton(xfdata.FL_PUSH_BUTTON, 230, 152, 80, 32, \
                                  "Button")
        flbasic.fl_set_object_color(self.pobj, xfdata.FL_COL1, xfdata.FL_BLUE)
        flbutton.fl_add_checkbutton(xfdata.FL_PUSH_BUTTON, 230, 175, 80, 32, "Button")
        inputfn.fl_add_input(xfdata.FL_NORMAL_INPUT, 195, 240, 160, 28, "Input")
        self.pbwselect = flselect.fl_add_select(xfdata.FL_MENU_SELECT, 105, \
                                  20, 100, 28, "Border Width")
        flbasic.fl_set_object_callback(self.pbwselect, self.bw_callback, 0)
        flbasic.fl_end_group()
        self.pdoneobj = flbutton.fl_add_button(xfdata.FL_NORMAL_BUTTON, 270, 290, \
                                            75, 30, "Done")
        flbasic.fl_set_object_callback(self.pdoneobj, self.done_callback, 0)
        flbasic.fl_end_form()
        # end create_form_bwform

        # form initialization code
        flbitmap.fl_set_pixmapbutton_file(self.ppmobj, "crab.xpm")
        flselect.fl_add_select_items(self.pbwselect, \
             "-5 Pixel|-4 Pixel|-3 Pixel|-2 Pixel|-1 Pixel|" \
             " 1 Pixel| 2 Pixel| 3 Pixel| 4 Pixel| 5 Pixel")
        pbw = flbasic.fl_get_border_width()
        if (pbw < -5 or pbw == 0 or pbw > 5):
            pbw = -2
            flbasic.fl_set_border_width(pbw)

        txt = "%2d Pixel" % pbw
        ppupretn = flselect.fl_get_select_item_by_label(self.pbwselect, txt)
        flselect.fl_set_select_item(self.pbwselect, ppupretn)

        # show the form
        flbasic.fl_show_form(self.pbwform, xfdata.FL_PLACE_CENTER, xfdata.FL_TRANSIENT, \
                            "bwform")

        while flbasic.fl_do_forms():
            pass                # empty


    def done_callback(self, pobj, data):
        # callbacks for form bwform
        flxbasic.fl_finish()
        sys.exit(0)


    def bw_callback(self, pobj, data):
        bws = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        pr = flselect.fl_get_select_item(pobj)
        indx = pr.contents.val
        bw = bws[indx]
        flbasic.fl_set_object_bw(self.pbwgroup, bw)
        flbasic.fl_set_object_bw(self.pdoneobj, bw)
        popupfn.fl_popup_set_bw(pr.contents.popup, bw)





if __name__ == '__main__':
    appl = BorderWidth(len(sys.argv), sys.argv)

