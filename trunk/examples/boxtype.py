#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  boxtype.c XForms demo, with some adaptations.
#
#  boxtype.c was written by M. Overmars and T.C. Zhao (1997),
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo show the different boxtypes. Note that some
# boxtypes are not appropriate for some objects
#

import sys
#sys.path.append("..")
import xformslib as xfl


border = xfl.FL_TRANSIENT

#define VN( a ) { a, #a }

gmode = [ {'val':xfl.StaticGray, 'name':"StaticGray"}, \
        {'val':xfl.GrayScale, 'name':"GrayScale"}, \
	{'val':xfl.StaticColor, 'name':"StaticColor"}, \
	{'val':xfl.PseudoColor, 'name':"PseudoColor"}, \
	{'val':xfl.TrueColor, 'name':"TrueColor"}, \
	{'val':xfl.DirectColor, 'name':"DirectColor"} ]


btypes = [ {'val':xfl.FL_NO_BOX, 'name':"No box"}, \
        {'val':xfl.FL_UP_BOX, 'name':"Up box"}, \
        {'val':xfl.FL_DOWN_BOX, 'name':"Down box"}, \
        {'val':xfl.FL_BORDER_BOX, 'name':"Border box"}, \
        {'val':xfl.FL_SHADOW_BOX, 'name':"Shadow box"}, \
        {'val':xfl.FL_FLAT_BOX, 'name':"Flat box"}, \
        {'val':xfl.FL_FRAME_BOX, 'name':"Frame box"}, \
        {'val':xfl.FL_EMBOSSED_BOX, 'name':"Embossed box"}, \
        {'val':xfl.FL_ROUNDED_BOX, 'name':"Rounded box"}, \
        {'val':xfl.FL_RFLAT_BOX, 'name':"Rflat box"}, \
        {'val':xfl.FL_RSHADOW_BOX, 'name':"Rshadow box"}, \
        {'val':xfl.FL_OVAL_BOX, 'name':"Oval box"}, \
        {'val':xfl.FL_ROUNDED3D_UPBOX, 'name':"Rounded 3D up box"}, \
        {'val':xfl.FL_ROUNDED3D_DOWNBOX, 'name':"Rounded 3D down box"}, \
        {'val':xfl.FL_OVAL3D_UPBOX, 'name':"Oval 3D up box"}, \
        {'val':xfl.FL_OVAL3D_DOWNBOX, 'name':"Oval 3D down box"},\
        {'val':-1, 'name':""} ]

#include "srs.xbm"


tobj = [None] * 18

browserlines = [" ", "@C1@c@l@bObjects Demo", " ", \
        "This demo shows you most", "objects that currently", \
        "exist in the Forms Library.", " ", \
        "You can change the boxtype", "of the different objects", \
        "using the buttons at the", "top of the form. Note that", \
        "some combinations might not", "look too good. Also realize", \
        "that for all object classes", "many different types are", \
        "available with different", "behaviour.", " ", \
        "With this demo you can also",   "see the effect of the drawing", \
        "mode on the appearance of the", "objects."]



class Flboxtype(object):
    # Main Routine
    def __init__(self, lsysargv, sysargv):
        self.pform = self.pexitob = self.pbtypeob = self.pmodeob = None

        c = xfl.FL_BLACK
        #	char **p;
        #	VN_struct *vn;
        #	VN_struct *g = gmode,
        #		      *gs = g + sizeof gmode / sizeof *gmode;

        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)

        self.create_form()

        sorceress_width, sorceress_height, sorceress_bits = \
                xfl.import_xbmdata_from_file("srs.xbm")
        xfl.fl_set_bitmap_data(tobj[2], sorceress_width, sorceress_height, \
                sorceress_bits)

        xfl.fl_add_chart_value(tobj[3], 15, "Item 1", c)
        c += 1
        xfl.fl_add_chart_value(tobj[3], 5, "Item 2", c)
        c += 1
        xfl.fl_add_chart_value(tobj[3], -10, "Item 3", c)
        c += 1
        xfl.fl_add_chart_value(tobj[3], 25, "Item 4", c)
        c += 1

        xfl.fl_add_nmenu_items(tobj[14], \
                "Item 1|Item 2|Item 3|Item 4|item 5")

        xfl.fl_add_select_items(tobj[15], "Item 1")
        xfl.fl_add_select_items(tobj[15], "Item 2")
        xfl.fl_add_select_items(tobj[15], "Item 3")
        xfl.fl_add_select_items(tobj[15], "Item 4")
        xfl.fl_add_select_items(tobj[15], "Item 5")

        xfl.fl_set_timer(tobj[16], 1000.0)

        # for ( p = browserlines; *p; p++ )
        for p in browserlines:
            xfl.fl_add_browser_line(tobj[17], p)

        #	for ( vn = btypes; vn->val >= 0; vn++ )
        for vn in btypes:
            xfl.fl_add_select_items(self.pbtypeob, vn['name'])

        #	for ( i = 1; g < gs; g++, i++ )
        for g in range(0, len(gmode)):
            pitem = xfl.fl_add_select_items(self.pmodeob, gmode[g]['name'])

            if not xfl.fl_mode_capable(gmode[g]['val'], 0):
                xfl.fl_popup_entry_set_state(pitem, xfl.FL_POPUP_DISABLED)

        # xfl.fl_vmode not working??
        xfl.fl_set_select_item(self.pmodeob, xfl.fl_get_select_item_by_value( \
                self.pmodeob, xfl.fl_get_vclass()))         # 5 xfl.fl_get_vclass()))  #xfl.fl_vmode.value))

        xfl.fl_set_select_item(self.pbtypeob, \
                xfl.fl_get_select_item_by_value(self.pbtypeob, 1))
        self.boxtype_cb(self.pbtypeob, 0)

        xfl.fl_show_form(self.pform, xfl.FL_PLACE_MOUSE, border, "Box types")

        while True:
            if xfl.fl_is_same_object(xfl.fl_do_forms(), self.pexitob):
                break

        xfl.fl_finish()



    def boxtype_cb(self, pobj, arg):

        req_bt = (xfl.fl_get_select_item(pobj)).contents.val
        lastbt = -1

        if lastbt != req_bt:
            xfl.fl_freeze_form(self.pform)
            xfl.fl_redraw_form(self.pform)
            #for ( i = 0; i < sizeof tobj / sizeof *tobj; i++ )
            for i in range(0, len(tobj)):
                xfl.fl_set_object_boxtype(tobj[i], btypes[req_bt]['val'])
                if self.pform.contents.frozen:
                    # workaround to avoid error on unfreezing
                    xfl.fl_unfreeze_form(self.pform)
                lastbt = req_bt


    def mode_cb(self, pobj, arg):
        lval = -1
        modeval = (xfl.fl_get_select_item(pobj)).contents.val

        if modeval == lval:
            return

        xfl.fl_hide_form(self.pform)
        #print gmode[val]['val']
        xfl.fl_set_graphics_mode(gmode[modeval]['val'], 0)
        xfl.fl_show_form(self.pform, xfl.FL_PLACE_GEOMETRY, border, \
                "Box types")

        lval = modeval


    # Creation Routines
    def create_form(self):

        self.pform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 720, 520)

        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 720, 520, "")
        xfl.fl_set_object_color(pobj, xfl.FL_BLUE, xfl.FL_COL1)

        pobj = xfl.fl_add_box(xfl.FL_DOWN_BOX, 10, 90, 700, 420, "")
        xfl.fl_set_object_color(pobj, xfl.FL_COL1, xfl.FL_COL1)

        pobj = xfl.fl_add_box(xfl.FL_DOWN_BOX, 10, 10, 700, 70, "")
        xfl.fl_set_object_color(pobj, xfl.FL_SLATEBLUE, xfl.FL_COL1)

        tobj[0] = xfl.fl_add_box(xfl.FL_UP_BOX, 30, 110, 110, 110, "Box")

        tobj[1] = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 30, 240, 110, 30, \
                "Text")

        tobj[2] = xfl.fl_add_bitmap(xfl.FL_NORMAL_BITMAP, 40, 280, 90, 80, \
                "Bitmap")
        xfl.fl_set_object_lcol(tobj[2], xfl.FL_BLUE)

        tobj[3] = xfl.fl_add_chart(xfl.FL_BAR_CHART, 160, 110, 160, 110, \
                "Chart")

        tobj[4] = xfl.fl_add_clock(xfl.FL_ANALOG_CLOCK, 40, 390, 90, 90, \
                "Clock")
        xfl.fl_set_object_dblbuffer(tobj[4], 1)

        tobj[5] = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 340, 110, 120, 30, \
                "Button")

        tobj[6] = xfl.fl_add_lightbutton(xfl.FL_PUSH_BUTTON, 340, 150, \
                120, 30, "Lightbutton")

        tobj[7] = xfl.fl_add_roundbutton(xfl.FL_PUSH_BUTTON, 340, 190, \
                120, 30, "Roundbutton")

        tobj[8] = xfl.fl_add_slider(xfl.FL_VERT_SLIDER, 160, 250, 40, 230, \
                "Slider")

        tobj[9] = xfl.fl_add_valslider(xfl.FL_VERT_SLIDER, 220, 250, 40, 230, \
                "Valslider")

        tobj[10] = xfl.fl_add_dial(xfl.FL_LINE_DIAL, 280, 250, 100, 100, \
                "Dial")

        tobj[11] = xfl.fl_add_positioner(xfl.FL_NORMAL_POSITIONER, 280, 380, \
                150, 100, "Positioner")

        tobj[12] = xfl.fl_add_counter(xfl.FL_NORMAL_COUNTER, 480, 110, \
                210, 30, "Counter")

        tobj[13] = xfl.fl_add_input(xfl.FL_NORMAL_INPUT, 520, 170, 170, 30, \
                "Input")

        tobj[14] = xfl.fl_add_nmenu(xfl.FL_NORMAL_NMENU, 400, 240, 100, 30, \
                "Menu")

        tobj[15] = xfl.fl_add_select(xfl.FL_NORMAL_SELECT, 580, 250, 110, 30, \
                "Select")

        tobj[16] = xfl.fl_add_timer(xfl.FL_VALUE_TIMER, 580, 210, 110, 30, \
                "Timer")
        xfl.fl_set_object_dblbuffer(tobj[16], 1)

        tobj[17] = xfl.fl_add_browser(xfl.FL_NORMAL_BROWSER, 450, 300, \
                240, 180, "Browser")

        self.pexitob = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 590, 30, \
                100, 30, "Exit")

        self.pbtypeob = xfl.fl_add_select(xfl.FL_NORMAL_SELECT, 110, 30, \
                130, 30, "Boxtype")
        xfl.fl_set_object_callback(self.pbtypeob, self.boxtype_cb, 0)
        xfl.fl_popup_set_title(xfl.fl_get_select_popup(self.pbtypeob), \
                "Boxtype")

        self.pmodeob = xfl.fl_add_select(xfl.FL_NORMAL_SELECT, 370, 30, \
                130, 30, "Graphics mode")
        xfl.fl_set_object_callback(self.pmodeob, self.mode_cb, 0)
        xfl.fl_popup_set_title(xfl.fl_get_select_popup(self.pmodeob), \
                "Graphics mode")

        xfl.fl_end_form ()



if __name__ == '__main__':
    print("********* boxtype.py *********")
    Flboxtype(len(sys.argv), sys.argv)

