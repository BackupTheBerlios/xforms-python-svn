#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  related XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
#  demo showing the effect of different border widths
#

# Forms and Objects

import sys

from xformslib import library as xf
from xformslib import xfconst as xfc


# callbacks for form bwform

def done_callback(obj, data):
    xf.fl_finish()
    sys.exit(0)


def bw_callback(obj, data):
    bws = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
    r = xf.fl_get_select_item(obj)
    if not r:
        print "error: NULL pointer"
        sys.exit(1)
    else:
        indx = r[0].val
        bw = bws[indx]
        xf.fl_set_object_bw(bwgroup, bw)
        xf.fl_set_object_bw(doneobj, bw)
        xf.fl_popup_set_bw(r[0].popup, bw)



def main(lsysargv, sysargv):

    global bwgroup, doneobj

    # application default. Can be overriden by the command line options

    xf.fl_set_border_width(1)

    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

    bwform = xf.fl_bgn_form(xfc.FL_NO_BOX, 380, 340)

    bwgroup = xf.fl_bgn_group()

    xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 380, 340, "")

    xf.fl_add_frame(xfc.FL_EMBOSSED_FRAME, 220, 60, 135, 145, "")

    xf.fl_add_frame(xfc.FL_ENGRAVED_FRAME, 15, 60, 185, 145, "")

    xf.fl_add_slider(xfc.FL_HOR_SLIDER, 25, 70, 160, 20, "")

    xf.fl_add_valslider(xfc.FL_HOR_BROWSER_SLIDER, 25, 105, 160, 20, "")

    obj = xf.fl_add_scrollbar(xfc.FL_HOR_THIN_SCROLLBAR, 25, 140, 160, 20, "")
    xf.fl_set_scrollbar_size(obj, 0.2)

    xf.fl_add_counter(xfc.FL_NORMAL_COUNTER, 25, 175, 160, 20, "")

    pmobj = xf.fl_add_pixmapbutton(xfc.FL_NORMAL_BUTTON, 305, 145, \
                                             40, 35, "")

    xf.fl_add_positioner(xfc.FL_NORMAL_POSITIONER, 30, 225, 100, 80, "")

    xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 230, 65, 100, 28, "Button")

    xf.fl_add_lightbutton(xfc.FL_PUSH_BUTTON, 230, 98, 100, 28, "LightButton")

    xf.fl_add_roundbutton(xfc.FL_PUSH_BUTTON, 230, 128, 80, 32, "Button")

    obj = xf.fl_add_round3dbutton(xfc.FL_PUSH_BUTTON, 230, 152, 80, 32, \
                                  "Button")
    xf.fl_set_object_color(obj, xfc.FL_COL1, xfc.FL_BLUE)

    xf.fl_add_checkbutton(xfc.FL_PUSH_BUTTON, 230, 175, 80, 32, "Button")

    xf.fl_add_input(xfc.FL_NORMAL_INPUT, 195, 240, 160, 28, "Input")

    bw_select = xf.fl_add_select(xfc.FL_MENU_SELECT, 105, \
                                 20, 100, 28, "Border Width")
    xf.fl_set_object_callback(bw_select, bw_callback, 0)

    xf.fl_end_group()

    doneobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 270, 290, \
                                            75, 30, "Done" )
    xf.fl_set_object_callback(doneobj, done_callback, 0)

    xf.fl_end_form()

    # end create_form_bwform

    # form initialization code

    xf.fl_set_pixmapbutton_file(pmobj, "crab.xpm")

    xf.fl_add_select_items(bw_select, \
             "-5 Pixel|-4 Pixel|-3 Pixel|-2 Pixel|-1 Pixel|" \
             " 1 Pixel| 2 Pixel| 3 Pixel| 4 Pixel| 5 Pixel")

    bw = xf.fl_get_border_width()
    if (bw < -5 or bw == 0 or bw > 5):
        xf.fl_set_border_width(bw = -2)

    txt = "%2d Pixel" % bw
    pupretn = xf.fl_get_select_item_by_label(bw_select, txt)
    xf.fl_set_select_item(bw_select, pupretn)

    # show the form

    xf.fl_show_form(bwform, xfc.FL_PLACE_CENTER, xfc.FL_TRANSIENT, \
                    "bwform")

    while xf.fl_do_forms():
        pass                # empty


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

