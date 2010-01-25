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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flslider import *
from xformslib.flscrollbar import *
from xformslib.flcounter import *
from xformslib.flbutton import *
from xformslib.flpositioner import *
from xformslib.flinput import *
from xformslib.flbitmap import *
from xformslib.flpopup import *
from xformslib.flmisc import *
from xformslib.flselect import *
from xformslib.xfdata import *




class BorderWidth(object):
    def __init__(self, lsysargv, sysargv):
        # application default. Can be overriden by the command line options
        fl_set_border_width(1)
        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.pbwform = fl_bgn_form(FL_NO_BOX, 380, 340)
        self.pbwgroup = fl_bgn_group()
        fl_add_box(FL_UP_BOX, 0, 0, 380, 340, "")
        fl_add_frame(FL_EMBOSSED_FRAME, 220, 60, 135, 145, "")
        fl_add_frame(FL_ENGRAVED_FRAME, 15, 60, 185, 145, "")
        fl_add_slider(FL_HOR_SLIDER, 25, 70, 160, 20, "")
        fl_add_valslider(FL_HOR_BROWSER_SLIDER, 25, 105, 160, 20, "")
        self.pobj = fl_add_scrollbar(FL_HOR_THIN_SCROLLBAR, 25, 140, 160, 20, "")
        fl_set_scrollbar_size(self.pobj, 0.2)
        fl_add_counter(FL_NORMAL_COUNTER, 25, 175, 160, 20, "")
        self.ppmobj = fl_add_pixmapbutton(FL_NORMAL_BUTTON, 305, 145, \
                                          40, 35, "")
        fl_add_positioner(FL_NORMAL_POSITIONER, 30, 225, 100, 80, "")
        fl_add_button(FL_NORMAL_BUTTON, 230, 65, 100, 28, "Button")
        fl_add_lightbutton(FL_PUSH_BUTTON, 230, 98, 100, 28, "LightButton")
        fl_add_roundbutton(FL_PUSH_BUTTON, 230, 128, 80, 32, "Button")
        self.pobj = fl_add_round3dbutton(FL_PUSH_BUTTON, 230, 152, 80, 32, \
                                  "Button")
        fl_set_object_color(self.pobj, FL_COL1, FL_BLUE)
        fl_add_checkbutton(FL_PUSH_BUTTON, 230, 175, 80, 32, "Button")
        fl_add_input(FL_NORMAL_INPUT, 195, 240, 160, 28, "Input")
        self.pbwselect = fl_add_select(FL_MENU_SELECT, 105, \
                                  20, 100, 28, "Border Width")
        fl_set_object_callback(self.pbwselect, self.bw_callback, 0)
        fl_end_group()
        self.pdoneobj = fl_add_button(FL_NORMAL_BUTTON, 270, 290, \
                                            75, 30, "Done")
        fl_set_object_callback(self.pdoneobj, self.done_callback, 0)
        fl_end_form()
        # end create_form_bwform

        # form initialization code
        fl_set_pixmapbutton_file(self.ppmobj, "crab.xpm")
        fl_add_select_items(self.pbwselect, \
             "-5 Pixel|-4 Pixel|-3 Pixel|-2 Pixel|-1 Pixel|" \
             " 1 Pixel| 2 Pixel| 3 Pixel| 4 Pixel| 5 Pixel")
        pbw = fl_get_border_width()
        if (pbw < -5 or pbw == 0 or pbw > 5):
            pbw = -2
            fl_set_border_width(pbw)

        txt = "%2d Pixel" % pbw
        ppupretn = fl_get_select_item_by_label(self.pbwselect, txt)
        fl_set_select_item(self.pbwselect, ppupretn)

        # show the form
        fl_show_form(self.pbwform, FL_PLACE_CENTER, FL_TRANSIENT, \
                            "bwform")

        while fl_do_forms():
            pass                # empty


    def done_callback(self, pobj, data):
        # callbacks for form bwform
        fl_finish()
        sys.exit(0)


    def bw_callback(self, pobj, data):
        bws = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        pr = fl_get_select_item(pobj)
        indx = pr.contents.val
        bw = bws[indx]
        fl_set_object_bw(self.pbwgroup, bw)
        fl_set_object_bw(self.pdoneobj, bw)
        fl_popup_set_bw(pr.contents.popup, bw)





if __name__ == '__main__':
    BorderWidth(len(sys.argv), sys.argv)

