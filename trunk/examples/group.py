#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  group.c XForms demo, with some adaptations and no deprecate functions.
#
#  group.c was written by M. Overmars and T.C. Zhao.
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# Demo showing the use of groups
#

import sys
#sys.path.append("..")
import xformslib as xfl



# Forms and Objects

NGROUP = 4

class FD_objsform(object):
    objsform = None
    vdata = None
    cdata = ""
    ldata = 0
    bitbutton = None
    pixbutton = None
    bit = None
    pix = None
    chart = None
    quit = None
    menu = None
    choice = None
    browser = None
    xyplot = None
    button = [None] * 5
    group = [None] * 5


# callbacks for form objsform

def show_group(pobj, data):
    for i in range(0, NGROUP+1):
        if i == data:
            xfl.fl_show_object(fd_objsform.group[i])
        else:
            xfl.fl_hide_object(fd_objsform.group[i])


def init_gui(fd):

    x = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    y = [5.5, 4.0, 4.5, 3.8, 4.0, 5.0]
    label = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat"]

    xfl.fl_add_nmenu_items(fd.menu, "One\tF1|Two\tF2|Three\tF3|Four\tF4")

    xfl.fl_add_select_items(fd.choice, "Option1|Option2|Option3")

    crab = xfl.import_xpmdata_from_file("crab45.xpm")          # "porsche.xpm"
    xfl.fl_set_pixmapbutton_data(fd.pixbutton, crab)
    xfl.fl_set_pixmap_data(fd.pix, crab)
    bm1_width, bm1_height, bm1_bits = xfl.import_xbmdata_from_file("bm1.xbm")
    xfl.fl_set_bitmapbutton_data(fd.bitbutton, bm1_width, bm1_height, \
            bm1_bits)
    nomail_width, nomail_height, nomail_bits = \
            xfl.import_xbmdata_from_file("nomail.xbm")
    xfl.fl_set_bitmap_data(fd.bit, nomail_width, nomail_height, nomail_bits)

    xfl.fl_set_browser_fontsize(fd.browser, xfl.FL_NORMAL_SIZE)
    xfl.fl_addto_browser(fd.browser, "browser line 1\nbrowser line 2")
    xfl.fl_addto_browser(fd.browser, "browser line 3\nbrowser line 4")
    xfl.fl_addto_browser(fd.browser, "browser line 5\nbrowser line 6")
    xfl.fl_addto_browser(fd.browser, "browser line 7\nbrowser line 8")
    xfl.fl_addto_browser(fd.browser, "browser line 9\nbrowser line 10")
    xfl.fl_addto_browser(fd.browser, "browser line 11\nbrowser line 12")
    xfl.fl_addto_browser(fd.browser, "browser line 13\nbrowser line 14")
    xfl.fl_addto_browser(fd.browser, "browser line 15\nbrowser line 16")
    xfl.fl_addto_browser(fd.browser, "browser line 17\nbrowser line 18")

    for i in range(0, len(y)):
        xfl.fl_add_chart_value(fd.chart, y[i], label[i], i + 1)

    xfl.fl_set_xyplot_data(fd.xyplot, x, y, 6, "", "","")
    xfl.fl_add_xyplot_overlay(fd.xyplot, 1, x, y, 6, xfl.FL_RED)
    xfl.fl_add_xyplot_text(fd.xyplot, 2.5, 5.2, "Weekly Summary", \
            xfl.FL_ALIGN_CENTER, xfl.FL_BLUE)
    xfl.fl_add_xyplot_text(fd.xyplot, 3, 3.85, "@-22->", xfl.FL_ALIGN_TOP, \
            xfl.FL_RED)

    xfl.fl_set_xyplot_overlay_type(fd.xyplot, 1, xfl.FL_NORMAL_XYPLOT)
    xfl.fl_set_xyplot_alphaxtics(fd.xyplot, "Mon|Tue|Wed|Thu|Fri|Sat", "")
    xfl.fl_set_xyplot_ytics(fd.xyplot, -1, -1)
    xfl.fl_set_xyplot_linewidth(fd.xyplot, 0, 3)


def main(lsysargv, sysargv):
    global fd_objsform

    xfl.fl_initialize(lsysargv, sysargv, "", None, 0)
    fd_objsform = create_form_objsform()
    init_gui(fd_objsform)

    # fill-in form initialization code
    xfl.fl_set_button(fd_objsform.button[0], 1)
    show_group(0, 0)

    # show the first form
    xfl.fl_show_form(fd_objsform.objsform, xfl.FL_PLACE_CENTER, \
            xfl.FL_FULLBORDER, "objsform")

    while True:
        if xfl.fl_is_same_object(xfl.fl_do_forms(), fd_objsform.quit):
            break


    xfl.fl_finish()
    return 0


# Form definition file generated with fdesign.
def create_form_objsform():
    fdui = FD_objsform()

    fdui.objsform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 456, 361)

    xfl.fl_add_box(xfl.FL_FLAT_BOX, 0, 0, 456, 361, "")
    xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 455, 360, "")
    xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 456, 70, "")

    fdui.button[0] = xfl.fl_add_button(xfl.FL_RADIO_BUTTON, 15, 20, 75, 30, \
             "Static")
    xfl.fl_set_object_lsize(fdui.button[0], xfl.FL_NORMAL_SIZE)
    xfl.fl_set_object_lstyle(fdui.button[0], xfl.FL_TIMESBOLD_STYLE)
    xfl.fl_set_object_callback(fdui.button[0], show_group, 0)

    fdui.button[1] = xfl.fl_add_button( xfl.FL_RADIO_BUTTON, 90, 20, 75, 30, \
            "Button")
    xfl.fl_set_object_lsize(fdui.button[1], xfl.FL_NORMAL_SIZE)
    xfl.fl_set_object_lstyle(fdui.button[1], xfl.FL_TIMESBOLD_STYLE)
    xfl.fl_set_object_callback(fdui.button[1], show_group, 1)

    fdui.button[2] = xfl.fl_add_button( xfl.FL_RADIO_BUTTON, 165, 20, 70, 30, \
            "Valuator")
    xfl.fl_set_object_lsize(fdui.button[2], xfl.FL_NORMAL_SIZE)
    xfl.fl_set_object_lstyle(fdui.button[2], xfl.FL_TIMESBOLD_STYLE)
    xfl.fl_set_object_callback(fdui.button[2], show_group, 2)

    fdui.button[3] = xfl.fl_add_button( xfl.FL_RADIO_BUTTON, 235, 20, 70, 30, \
            "Input")
    xfl.fl_set_object_lsize(fdui.button[3], xfl.FL_NORMAL_SIZE)
    xfl.fl_set_object_lstyle(fdui.button[3], xfl.FL_TIMESBOLD_STYLE)
    xfl.fl_set_object_callback(fdui.button[3], show_group, 3)

    fdui.button[4] = xfl.fl_add_button( xfl.FL_RADIO_BUTTON, 305, 20, 70, 30, \
            "Other")
    xfl.fl_set_object_lsize(fdui.button[4], xfl.FL_NORMAL_SIZE)
    xfl.fl_set_object_lstyle(fdui.button[4], xfl.FL_TIMESBOLD_STYLE)
    xfl.fl_set_object_callback(fdui.button[4], show_group, 4)

    xfl.fl_add_box(xfl.FL_UP_BOX, 0, 70, 456, 291, "")

    xfl.fl_add_box(xfl.FL_DOWN_BOX, 9, 90, 435, 260, "")

    fdui.group[2] = xfl.fl_bgn_group()

    pobj = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 260, 140, 80, 30, "Text")
    xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_LEFT | xfl.FL_ALIGN_INSIDE)

    xfl.fl_add_slider(xfl.FL_HOR_BROWSER_SLIDER, 60, 120, 170, 25, "")

    pobj = xfl.fl_add_slider(xfl.FL_HOR_FILL_SLIDER, 60, 160, 170, 30, "")
    xfl.fl_set_slider_value(pobj, 0.54)

    pobj = xfl.fl_add_slider(xfl.FL_VERT_SLIDER, 390, 110, 30, 170, "")
    xfl.fl_set_slider_value(pobj, 0.48)

    xfl.fl_add_valslider(xfl.FL_VERT_SLIDER, 350, 110, 30, 170, "")

    pobj = xfl.fl_add_dial(xfl.FL_FILL_DIAL, 50, 220, 90, 70, "")
    xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_BLUE)

    xfl.fl_add_positioner(xfl.FL_NORMAL_POSITIONER, 150, 210, 120, 100, "")

    xfl.fl_add_counter(xfl.FL_NORMAL_COUNTER, 300, 300, 130, 30, "")

    xfl.fl_end_group()

    fdui.group[1] = xfl.fl_bgn_group()

    fdui.bitbutton = xfl.fl_add_bitmapbutton(xfl.FL_NORMAL_BUTTON, 60, 250, \
            50, 40, "")

    fdui.pixbutton = xfl.fl_add_pixmapbutton(xfl.FL_NORMAL_BUTTON, 85, 120, \
            80, 80, "")

    xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 290, 270, 90, 35, "Button")

    pobj = xfl.fl_add_round3dbutton(xfl.FL_PUSH_BUTTON, 260, 95, 60, 40, \
            "Round3DButton")
    xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_MAGENTA)

    xfl.fl_add_roundbutton(xfl.FL_PUSH_BUTTON, 220, 140, 60, 40, \
            "RoundButton")

    pobj = xfl.fl_add_checkbutton(xfl.FL_PUSH_BUTTON, 190, 230, 50, 40, \
            "CheckButton")
    xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_BLUE)

    xfl.fl_add_lightbutton(xfl.FL_PUSH_BUTTON, 290, 200, 100, 30, \
            "LightButton")

    pobj = xfl.fl_add_button(xfl.FL_PUSH_BUTTON, 120, 290, 100, 35, \
            "Button")
    xfl.fl_set_object_boxtype(pobj, xfl.FL_ROUNDED3D_UPBOX)

    xfl.fl_end_group()

    fdui.group[0] = xfl.fl_bgn_group()

    pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 40, 120, 70, 70, "A Box")
    xfl.fl_set_object_lsize(pobj, xfl.FL_NORMAL_SIZE)
    xfl.fl_set_object_lstyle(pobj, xfl.FL_TIMESBOLD_STYLE)

    fdui.bit = xfl.fl_add_bitmap(xfl.FL_NORMAL_BITMAP, 30, 220, 80, 70, \
            "bitmap")

    xfl.fl_add_clock(xfl.FL_ANALOG_CLOCK, 330, 240, 90, 80, "")

    pobj = xfl.fl_add_frame(xfl.FL_ENGRAVED_FRAME, 130, 120, 80, 70, \
            "A Frame")
    xfl.fl_set_object_lsize(pobj, xfl.FL_NORMAL_SIZE)
    xfl.fl_set_object_lstyle(pobj, xfl.FL_TIMESBOLD_STYLE)

    fdui.pix = xfl.fl_add_pixmap(xfl.FL_NORMAL_PIXMAP, 340, 110, 90, 70, \
            "pixmap")

    fdui.chart = xfl.fl_add_chart(xfl.FL_PIE_CHART, 160, 210, 130, 110, \
            "chart")

    pobj = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 240, 130, 100, 30, \
            "Text stuff\nand more stuff")
    xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_CENTER | xfl.FL_ALIGN_INSIDE)

    xfl.fl_end_group()

    fdui.group[3] = xfl.fl_bgn_group()

    xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 140, 120, 150, 30, "Input")

    xfl.fl_add_input(xfl.FL_MULTILINE_INPUT, 60, 170, 320, 130, "")

    xfl.fl_end_group()

    fdui.quit = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 385, 20, 60, 30, \
            "Quit")

    fdui.group[4] = xfl.fl_bgn_group()

    fdui.menu = xfl.fl_add_nmenu(xfl.FL_NORMAL_NMENU, 190, 110, 40, 19, \
            "Menu")
    xfl.fl_set_object_boxtype(fdui.menu, xfl.FL_FLAT_BOX)

    fdui.choice = xfl.fl_add_select(xfl.FL_NORMAL_SELECT, 290, 110, 120, 30, \
            "")

    fdui.browser = xfl.fl_add_browser(xfl.FL_NORMAL_BROWSER, 30, 140, \
            140, 150, "")

    fdui.xyplot = xfl.fl_add_xyplot( xfl.FL_IMPULSE_XYPLOT, 190, 150, \
            240, 180, "")
    xfl.fl_set_object_lsize(fdui.xyplot, xfl.FL_DEFAULT_SIZE)

    xfl.fl_end_group()

    xfl.fl_end_form()

    return fdui



if __name__ == '__main__':
    print("********* group.py *********")
    main(len(sys.argv), sys.argv)

