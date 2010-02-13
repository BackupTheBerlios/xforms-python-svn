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
from xformslib import flbasic as flba
from xformslib import flxbasic as flxb
from xformslib import flslider as flsd
from xformslib import flscrollbar as flsb
from xformslib import flcounter as flct
from xformslib import flbutton as flbt
from xformslib import flpositioner as flpt
from xformslib import flinput as flin
from xformslib import flbitmap as flbm
from xformslib import flpopup as flpp
from xformslib import flmisc as flms
from xformslib import flselect as flse
from xformslib import xfdata as xfc




class BorderWidth(object):
    def __init__(self, lsysargv, sysargv):
        # application default. Can be overriden by the command line options
        flba.fl_set_border_width(1)
        flxb.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)
        self.pbwform = flba.fl_bgn_form(xfc.FL_NO_BOX, 380, 340)
        self.pbwgroup = flba.fl_bgn_group()
        flms.fl_add_box(xfc.FL_UP_BOX, 0, 0, 380, 340, "")
        flms.fl_add_frame(xfc.FL_EMBOSSED_FRAME, 220, 60, 135, 145, "")
        flms.fl_add_frame(xfc.FL_ENGRAVED_FRAME, 15, 60, 185, 145, "")
        flsd.fl_add_slider(xfc.FL_HOR_SLIDER, 25, 70, 160, 20, "")
        flsd.fl_add_valslider(xfc.FL_HOR_BROWSER_SLIDER, 25, 105, 160, 20, "")
        self.pobj = flsb.fl_add_scrollbar(xfc.FL_HOR_THIN_SCROLLBAR, 25, 140, 160, 20, "")
        flsb.fl_set_scrollbar_size(self.pobj, 0.2)
        flct.fl_add_counter(xfc.FL_NORMAL_COUNTER, 25, 175, 160, 20, "")
        self.ppmobj = flbt.fl_add_pixmapbutton(xfc.FL_NORMAL_BUTTON, 305, 145, \
                                              40, 35, "")
        flpt.fl_add_positioner(xfc.FL_NORMAL_POSITIONER, 30, 225, 100, 80, "")
        flbt.fl_add_button(xfc.FL_NORMAL_BUTTON, 230, 65, 100, 28, "Button")
        flbt.fl_add_lightbutton(xfc.FL_PUSH_BUTTON, 230, 98, 100, 28, "LightButton")
        flbt.fl_add_roundbutton(xfc.FL_PUSH_BUTTON, 230, 128, 80, 32, "Button")
        self.pobj = flbt.fl_add_round3dbutton(xfc.FL_PUSH_BUTTON, 230, 152, 80, 32, \
                                  "Button")
        flba.fl_set_object_color(self.pobj, xfc.FL_COL1, xfc.FL_BLUE)
        flbt.fl_add_checkbutton(xfc.FL_PUSH_BUTTON, 230, 175, 80, 32, "Button")
        flin.fl_add_input(xfc.FL_NORMAL_INPUT, 195, 240, 160, 28, "Input")
        self.pbwselect = flse.fl_add_select(xfc.FL_MENU_SELECT, 105, \
                                          20, 100, 28, "Border Width")
        flba.fl_set_object_callback(self.pbwselect, self.bw_callback, 0)
        flba.fl_end_group()
        self.pdoneobj = flbt.fl_add_button(xfc.FL_NORMAL_BUTTON, 270, 290, \
                                            75, 30, "Done")
        flba.fl_set_object_callback(self.pdoneobj, self.done_callback, 0)
        flba.fl_end_form()
        # end create_form_bwform

        # form initialization code
        flbm.fl_set_pixmapbutton_file(self.ppmobj, "crab.xpm")
        flse.fl_add_select_items(self.pbwselect, \
             "-5 Pixel|-4 Pixel|-3 Pixel|-2 Pixel|-1 Pixel|" \
             " 1 Pixel| 2 Pixel| 3 Pixel| 4 Pixel| 5 Pixel")
        pbw = flba.fl_get_border_width()
        if (pbw < -5 or pbw == 0 or pbw > 5):
            pbw = -2
            flba.fl_set_border_width(pbw)

        txt = "%2d Pixel" % pbw
        ppupretn = flse.fl_get_select_item_by_label(self.pbwselect, txt)
        flse.fl_set_select_item(self.pbwselect, ppupretn)

        # show the form
        flba.fl_show_form(self.pbwform, xfc.FL_PLACE_CENTER, xfc.FL_TRANSIENT, \
                            "bwform")

        while flba.fl_do_forms():
            pass                # empty


    def done_callback(self, pobj, data):
        # callbacks for form bwform
        flxb.fl_finish()
        sys.exit(0)


    def bw_callback(self, pobj, data):
        bws = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        pr = flse.fl_get_select_item(pobj)
        indx = pr.contents.val
        bw = bws[indx]
        flba.fl_set_object_bw(self.pbwgroup, bw)
        flba.fl_set_object_bw(self.pdoneobj, bw)
        flpp.fl_popup_set_bw(pr.contents.popup, bw)





if __name__ == '__main__':
    BorderWidth(len(sys.argv), sys.argv)

