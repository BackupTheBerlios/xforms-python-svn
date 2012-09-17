#!/usr/bin/env python3

#  This file is part of xforms-python, and it has been ported from
#  new_popup.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#

import sys
import xformslib as xfl


class FlPopup(object):
    def __init__(self, lsysargv, sysargv):
        self.pm = None
        xfl.fl_initialize(lsysargv, sysargv, "FormDemo", None, 0)
        pform = xfl.fl_bgn_form(xfl.FL_UP_BOX, 260, 210)
        xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 260, 210, "")
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 150, 150, \
                90, 35, "Done")
        xfl.fl_set_object_callback(pobj, self.done_cb, 0)
        pobj = xfl.fl_add_button(xfl.FL_MENU_BUTTON, 30, 90, 100, 30, "Popup")
        xfl.fl_set_button_shortcut(pobj, "Pp#p", 1)
        xfl.fl_set_object_callback(pobj, self.do_pup, 0)
        xfl.fl_end_form()
        # initialize
        xfl.fl_show_form(pform, xfl.FL_PLACE_MOUSE, xfl.FL_TRANSIENT, \
                "New Popup Demo")
        xfl.fl_do_forms()
        sys.exit(0)


    def done_cb(self, pobj, data):      # data unused
        xfl.fl_finish()
        sys.exit(0)


    def style_cb(self, ppopupretn):
        pudata = xfl.fls_convert_ptrvoid_to_ptrlongc( \
                ppopupretn.contents.user_data)
        udataval = pudata.contents.value
        print("Userdata: %d" % udataval)
        pmyentry1 = ppopupretn.contents.popup.contents.entries
        for idx in range(0, 3):
            try:
                print(pmyentry1, pmyentry1[idx].text)
                xfl.fl_popup_entry_clear_state(pmyentry1[idx], \
                        xfl.FL_POPUP_CHECKED)
            except:
                break
        #xfl.fl_popup_entry_raise_state(ppopupretn.contents.entry, \
        #        xfl.FL_POPUP_CHECKED)
        style, size = xfl.fl_popup_entry_get_font(self.pm)
        mod = style & (xfl.FL_SHADOW_STYLE | \
                xfl.FL_ENGRAVED_STYLE | xfl.FL_EMBOSSED_STYLE)
        print("style", style, "mod", mod, "pr->val", \
                ppopupretn.contents.val, "pr->val|mod", \
                ppopupretn.contents.val | mod)
        xfl.fl_popup_entry_set_font(self.pm, ppopupretn.contents.val | mod, \
                size)
        return xfl.FL_IGNORE


    def size_cb(self, ppopupretn):
        pudata = xfl.fls_convert_ptrvoid_to_ptrlongc( \
                ppopupretn.contents.user_data)
        udataval = pudata.contents.value
        print("Userdata: %d" % udataval)
        pmyentry2 = ppopupretn.contents.popup.contents.entries
        for idx in range(0, 5):
            try:
                xfl.fl_popup_entry_clear_state(pmyentry2[idx], \
                        xfl.FL_POPUP_CHECKED)
            except:
                break
        #xfl.fl_popup_entry_raise_state(ppopupretn.contents.entry, \
        #        xfl.FL_POPUP_CHECKED)
        style, unused = xfl.fl_popup_entry_get_font(self.pm)
        xfl.fl_popup_entry_set_font(self.pm, style, ppopupretn.contents.val)
        style, unused = xfl.fl_popup_get_title_font(self.pm)
        xfl.fl_popup_set_title_font(self.pm, style, ppopupretn.contents.val)
        return xfl.FL_IGNORE


    def mod_cb(self, ppopupretn):
        pudata = xfl.fls_convert_ptrvoid_to_ptrlongc( \
                ppopupretn.contents.user_data)
        udataval = pudata.contents.value
        print("Userdata: %d" % udataval)
        pmyentry3 = ppopupretn.contents.popup.contents.entries
        for idx in range(0, 4):
            try:
                xfl.fl_popup_entry_clear_state(pmyentry3[idx], \
                        xfl.FL_POPUP_CHECKED)
            except:
                break
        #xfl.fl_popup_entry_raise_state(ppopupretn.contents.entry, \
        #        xfl.FL_POPUP_CHECKED)
        style, size = xfl.fl_popup_entry_get_font(self.pm)
        print("style, size", style, size)
        if ppopupretn.contents.val != 0:
            style &= ~ (xfl.FL_SHADOW_STYLE | xfl.FL_ENGRAVED_STYLE | \
                    xfl.FL_EMBOSSED_STYLE)
            xfl.fl_popup_entry_set_font(self.pm, style | \
                    ppopupretn.contents.val, size)
        else:
            xfl.fl_popup_entry_set_font(self.pm, ppopupretn.contents.val, \
                    size)
        return xfl.FL_IGNORE


    def pol_cb(self, ppopupretn):
        #xfl.FL_POPUP_ENTRY *e;
        #for ( e = r->popup->entries; e != NULL; e = e->next )
        #    if ( e != r->entry )
        #        xfl.fl_popup_entry_clear_state( e, xfl.FL_POPUP_CHECKED );
        pudata = xfl.fls_convert_ptrvoid_to_ptrlongc( \
                ppopupretn.contents.user_data)
        udataval = pudata.contents.value
        print("Userdata: %d" % udataval)
        pmyentry4 = ppopupretn.contents.popup.contents.entries
        for idx in range(0, 2):
            try:
                xfl.fl_popup_entry_clear_state(pmyentry4[idx], \
                        xfl.FL_POPUP_CHECKED)
            except:
                break
        #xfl.fl_popup_entry_raise_state(ppopupretn.contents.entry, \
        #        xfl.FL_POPUP_CHECKED)
        xfl.fl_popup_set_policy(self.pm, ppopupretn.contents.val)
        return xfl.FL_IGNORE


    def do_pup(self, pobj, q):      # q unused
        if self.pm is None:
            owin = xfl.FL_ObjWin(pobj)
            self.pm = xfl.fl_popup_add(owin, "Popup")
            self.psm1 = xfl.fl_popup_add(owin, "STYLES")
            self.psm2 = xfl.fl_popup_add(owin, "SIZES")
            self.psm3 = xfl.fl_popup_add(owin, "MODS")
            self.psm4 = xfl.fl_popup_add(owin, "POLICIES")
            self.ppopnor = xfl.fl_popup_add_entries(self.psm4, \
                    "FL_POPUP_NORMAL_SELECT%T%x%f", \
                    x=xfl.FL_POPUP_NORMAL_SELECT, f=self.pol_cb)
            xfl.fl_popup_entry_set_user_data(self.ppopnor, 15)
            self.ppopdra = xfl.fl_popup_add_entries(self.psm4, \
                    "FL_POPUP_DRAG_SELECT%t%x%f",
                    x=xfl.FL_POPUP_DRAG_SELECT, f=self.pol_cb)
            xfl.fl_popup_entry_set_user_data(self.ppopdra, 16)

            self.pmodnon = xfl.fl_popup_add_entries(self.psm3, \
                    "None%x%f%R", x=xfl.FL_NORMAL_STYLE, f=self.mod_cb, Rr=1)            #%R
            xfl.fl_popup_entry_set_user_data(self.pmodnon, 11)
            self.pmodsha = xfl.fl_popup_add_entries(self.psm3, \
                    "FL_SHADOW_STYLE%x%f%r", x=xfl.FL_SHADOW_STYLE, \
                    f=self.mod_cb, Rr=1)
            xfl.fl_popup_entry_set_user_data(self.pmodsha, 12)
            self.pmodeng = xfl.fl_popup_add_entries(self.psm3, \
                    "FL_ENGRAVED_STYLE%x%f%r", x=xfl.FL_ENGRAVED_STYLE, \
                    f=self.mod_cb, Rr=1)
            xfl.fl_popup_entry_set_user_data(self.pmodeng, 14)
            self.pmodemb = xfl.fl_popup_add_entries(self.psm3, \
                    "FL_EMBOSSED_STYLE%x%f%r", x=xfl.FL_EMBOSSED_STYLE, \
                    f=self.mod_cb, Rr=1)
            xfl.fl_popup_entry_set_user_data(self.pmodemb, 15)

            self.pstynor = xfl.fl_popup_add_entries(self.psm1, \
                    "FL_NORMAL_STYLE%SN%x%f%R%s", x=xfl.FL_NORMAL_STYLE, \
                    f=self.style_cb, Rr=1, s="nN^N")            #%R
            xfl.fl_popup_entry_set_user_data(self.pstynor, 1)
            self.pstybol = xfl.fl_popup_add_entries(self.psm1, \
                    "FL_BOLD_STYLE%SB%x%f%r%s", x=xfl.FL_BOLD_STYLE, \
                    f=self.style_cb, Rr=1, s="bB^B")
            xfl.fl_popup_entry_set_user_data(self.pstybol, 2)
            self.pstyita = xfl.fl_popup_add_entries(self.psm1, \
                    "FL_ITALIC_STYLE%SI%x%f%r%s", x=xfl.FL_ITALIC_STYLE, \
                    f=self.style_cb, Rr=1, s="iI^I")
            xfl.fl_popup_entry_set_user_data(self.pstyita, 3)
            self.pstybolita = xfl.fl_popup_add_entries(self.psm1, \
                    "FL_BOLDITALIC_STYLE%SO%x%f%r%s", \
                    x=xfl.FL_BOLDITALIC_STYLE, f=self.style_cb, \
                    Rr=1, s="oO^O")
            xfl.fl_popup_entry_set_user_data(self.pstybolita, 4)
            xfl.fl_popup_add_entries(self.psm1, \
                    "%l|Font modifier%SCtrl-M%m%s", m=self.psm3, s="^m")
            self.psiztin = xfl.fl_popup_add_entries(self.psm2, \
                    "FL_TINY_SIZE%x%f%r", x=xfl.FL_TINY_SIZE, \
                    f=self.size_cb, Rr=1)
            xfl.fl_popup_entry_set_user_data(self.psiztin, 5)
            self.psizsma = xfl.fl_popup_add_entries(self.psm2, \
                    "FL_SMALL_SIZE%x%f%r", x=xfl.FL_SMALL_SIZE, \
                    f=self.size_cb, Rr=1)
            xfl.fl_popup_entry_set_user_data(self.psizsma, 6)
            self.psiznor = xfl.fl_popup_add_entries(self.psm2, \
                    "FL_NORMAL_SIZE%x%f%R", x=xfl.FL_NORMAL_SIZE, \
                    f=self.size_cb, Rr=1)            #%R
            xfl.fl_popup_entry_set_user_data(self.psiznor, 7)
            self.psizmed = xfl.fl_popup_add_entries(self.psm2, \
                    "FL_MEDIUM_SIZE%x%f%r", x=xfl.FL_MEDIUM_SIZE, \
                    f=self.size_cb, Rr=1)
            xfl.fl_popup_entry_set_user_data(self.psizmed, 8)
            self.psizlar = xfl.fl_popup_add_entries(self.psm2, \
                    "FL_LARGE_SIZE%x%f%r", x=xfl.FL_LARGE_SIZE, \
                    f=self.size_cb, Rr=1)
            xfl.fl_popup_entry_set_user_data(self.psizlar, 9)
            self.psizhug = xfl.fl_popup_add_entries(self.psm2, \
                    "FL_HUGE_SIZE%x%f%r", x=xfl.FL_HUGE_SIZE, \
                    f=self.size_cb, Rr=1)
            xfl.fl_popup_entry_set_user_data(self.psizhug, 10)
            xfl.fl_popup_add_entries(self.pm, "Font style%m", m=self.psm1)
            xfl.fl_popup_add_entries(self.pm, "Font size%m", m=self.psm2)
            xfl.fl_popup_add_entries(self.pm, "Policy%m", m=self.psm4)
            xfl.fl_popup_set_min_width(self.pm, 100)
        if xfl.fl_get_button_numb(pobj) >= xfl.FL_SHORTCUT:
            xfl.fl_popup_set_position(self.pm, \
                    pobj.contents.form.contents.x + pobj.contents.x, \
                    pobj.contents.form.contents.y + pobj.contents.y + \
                    pobj.contents.h)
        xfl.fl_popup_do(self.pm)


if __name__ == '__main__':
    print("********* new_popup.py *********")
    FlPopup(len(sys.argv), sys.argv)
