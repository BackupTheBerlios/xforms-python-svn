#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

"""
    xforms-python - Python wrapper for XForms (X11) GUI C toolkit library
    using ctypes

    Copyright (C) 2009, 2010  Luca Lazzaroni "LukenShiro"
        <lukenshiro@ngi.it>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as
    published by the Free Software Foundation, version 2.1 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU LGPL along with this
    program. If not, see <http://www.gnu.org/licenses/>.

    See CREDITS file to read acknowledgements and thanks to XForms,
    ctypes and other developers.
"""


__docformat__ = "epytext en"    # to be used with epydoc doc


# originally generated by 'h2xml+gccxml' and 'xml2py'
# then heavily reordered and reworked

# ############################################# #
# Interface to XForms shared object libraries   #
# ############################################# #

import ctypes as cty
from xformslib import library
from xformslib import xfdata



##################
# forms.h (box.h)
##################

# fl_create_box function placeholder (internal)


def fl_add_box(boxtype, x, y, w, h, label):
    """ fl_add_box(boxtype, x, y, w, h, label) -> pFlObject

        Adds a box object.

        @param boxtype: type of the box to be added (<int>)
        @type boxtype: (from xfdata module) FL_NO_BOX, FL_UP_BOX, FL_DOWN_BOX,
                       FL_BORDER_BOX, FL_SHADOW_BOX, FL_FRAME_BOX,
                       FL_ROUNDED_BOX, FL_EMBOSSED_BOX, FL_FLAT_BOX,
                       FL_RFLAT_BOX, FL_RSHADOW_BOX, FL_OVAL_BOX,
                       FL_ROUNDED3D_UPBOX, FL_ROUNDED3D_DOWNBOX,
                       FL_OVAL3D_UPBOX, FL_OVAL3D_DOWNBOX, FL_OVAL3D_FRAMEBOX,
                       FL_OVAL3D_EMBOSSEDBOX
        @param x: horizontal position (upper-left corner)
        @param y: vertical position (upper-left corner)
        @param w: width in coord units
        @param h: height in coord units
        @param label: text label of box

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_add_box = library.cfuncproto(
        library.load_so_libforms(), "fl_add_box",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_box(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(boxtype, xfdata.BOXTYPE_list)
    iboxtype = library.convert_to_int(boxtype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(boxtype, x, y, w, h, label, iboxtype, ix, iy, iw,
                   ih, slabel)
    retval = _fl_add_box(iboxtype, ix, iy, iw, ih, slabel)
    return retval


#####################
# forms.h (choice.h)
#####################

# fl_create_choice function placeholder (internal and deprecated)
# fl_add_choice function placeholder (deprecated)
# fl_clear_choice function placeholder (deprecated)
# fl_addto_choice function placeholder (deprecated)
# fl_replace_choice function placeholder (deprecated)
# fl_delete_choice function placeholder (deprecated)
# fl_set_choice function placeholder (deprecated)
# fl_set_choice_text function placeholder (deprecated)
# fl_get_choice function placeholder (deprecated)
# fl_get_choice_item_text function placeholder (deprecated)
# fl_get_choice_maxitems function placeholder (deprecated)
# fl_get_choice_text function placeholder (deprecated)
# fl_set_choice_fontsize function placeholder (deprecated)
# fl_set_choice_fontstyle function placeholder (deprecated)
# fl_set_choice_align function placeholder (deprecated)
# fl_get_choice_item_mode function placeholder (deprecated)
# fl_set_choice_item_mode function placeholder (deprecated)
# fl_set_choice_item_shortcut function placeholder (deprecated)
# fl_set_choice_item_entries function placeholder (deprecated)
# fl_set_choice_notitle function placeholder (deprecated)



#################################
# forms.h (clipbd.h)
# prototypes for clipboard stuff
#################################


def fl_stuff_clipboard(pFlObject, clipbdtype, data, size, py_LoseSelectionCb):
    """ fl_stuff_clipboard(pFlObject, clipbdtype, data, size, py_LoseSelectionCb) -> num.

    @param pFlObject: pointer to clipboard object
    @type pFlObject: pointer to xfdata.FL_OBJECT
    @param clipbdtype: type of clipboard (not used)
    @type clipbdtype: num./long
    @param py_LoseSelectionCb: python function callback, returning value
    @type py_LoseSelectionCb: func(pFlObject, longnum) -> num.

    @status: Untested + NoDoc + NoDemo = NOT OK
    """
    #FL_LOSE_SELECTION_CB = cty.CFUNCTYPE(cty.c_int, cty.POINTER(xfdata.FL_OBJECT),
    #                                     cty.c_long)
    _fl_stuff_clipboard = library.cfuncproto(
            library.load_so_libforms(), "fl_stuff_clipboard",
            cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_long, cty.c_void_p,
            cty.c_long, xfdata.FL_LOSE_SELECTION_CB],
            """int fl_stuff_clipboard(FL_OBJECT * ob, long int type,
               const char * data, long int size,
               FL_LOSE_SELECTION_CB lose_callback)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    lclipbdtype = library.convert_to_long(clipbdtype)
    pdata = cty.cast(data, cty.c_void_p)
    lsize = library.convert_to_long(size)
    c_LoseSelectionCb = xfdata.FL_LOSE_SELECTION_CB(py_LoseSelectionCb)
    library.keep_cfunc_refs(c_LoseSelectionCb, py_LoseSelectionCb)
    library.keep_elem_refs(pFlObject, clipbdtype, data, size, lclipbdtype, pdata, lsize)
    retval = _fl_stuff_clipboard(pFlObject, lclipbdtype, pdata, lsize,
                                 c_LoseSelectionCb)
    return retval


def fl_request_clipboard(pFlObject, clipbdtype, py_SelectionCb):
    """ fl_request_clipboard(pFlObject, clipbdtype, py_SelectionCb) -> num.

    @param pFlObject: pointer to clipboard object
    @type pFlObject: pointer to xfdata.FL_OBJECT
    @param clipbdtype: type of clipboard (not used)
    @param py_SelectionCb: python function callback, returning value
    @type py_SelectionCb: func(pFlObject, longnum, ptr_void,
                              longnum) -> num.

    @status: Untested + NoDoc + NoDemo = NOT OK
    """
    #FL_SELECTION_CB = cty.CFUNCTYPE(cty.c_int, cty.POINTER(xfdata.FL_OBJECT),
    #                                cty.c_long, cty.c_void_p, cty.c_long)
    _fl_request_clipboard = library.cfuncproto(
        library.load_so_libforms(), "fl_request_clipboard",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_long,
        xfdata.FL_SELECTION_CB],
        """int fl_request_clipboard(FL_OBJECT * ob, long int type,
           FL_SELECTION_CB got_it_callback)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    lclipbdtype = library.convert_to_long(clipbdtype)
    c_SelectionCb = xfdata.FL_SELECTION_CB(py_SelectionCb)
    library.keep_cfunc_refs(c_SelectionCb, py_SelectionCb)
    library.keep_elem_refs(pFlObject, clipbdtype, lclipbdtype)
    retval = _fl_request_clipboard(pFlObject, lclipbdtype, c_SelectionCb)
    return retval





###################
# forms.h (flps.h)
###################

# postscript stuff


def flps_init():
    """
    flps_init() -> flps_control class

    @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _flps_init = library.cfuncproto(
        library.load_so_libflimage(), "flps_init",
        cty.POINTER(xfdata.FLPS_CONTROL), [],
        """FLPS_CONTROL * flps_init()""")
    library.check_if_initialized()
    retval = _flps_init()
    return retval


def fl_object_ps_dump(pFlObject, fname):
    """fl_object_ps_dump(pFlObject, fname) -> num.

    @param pFlObject: pointer to object
    @type pFlObject: pointer to xfdata.FL_OBJECT

    @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_object_ps_dump = library.cfuncproto(
        library.load_so_libflimage(), "fl_object_ps_dump",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), xfdata.STRING],
        """int fl_object_ps_dump(FL_OBJECT * ob, const char * fname)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    sfname = library.convert_to_string(fname)
    library.keep_elem_refs(pFlObject, fname, sfname)
    retval = _fl_object_ps_dump(pFlObject, sfname)
    return retval


####################
# forms.h (frame.h)
####################

# fl_create_frame function placeholder (internal)


def fl_add_frame(frametype, x, y, w, h, label):
    """
        fl_add_frame(frametype, x, y, w, h, label) -> pFlObject

        Adds a frame object.

        @param frametype: type of frame to be added
        @param frametype: [num./int] from xfdata module FL_NO_FRAME,
                          FL_UP_FRAME, FL_DOWN_FRAME, FL_BORDER_FRAME,
                          FL_SHADOW_FRAME, FL_ENGRAVED_FRAME, FL_ROUNDED_FRAME,
                          FL_EMBOSSED_FRAME, FL_OVAL_FRAME
        @param x: horizontal position (upper-left corner)
        @param x: vertical position (upper-left corner)
        @param w: width in coord units
        @param h: height in coord units
        @param label: text label of frame

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_add_frame = library.cfuncproto(
        library.load_so_libforms(), "fl_add_frame",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_frame(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(frametype, xfdata.FRAMETYPE_list)
    iframetype = library.convert_to_int(frametype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(frametype, x, y, w, h, label, iframetype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_frame(iframetype, ix, iy, iw, ih, slabel)
    return retval


# labeld frame

# fl_create_labelframe function placeholder (internal)


def fl_add_labelframe(frametype, x, y, w, h, label):
    """
        fl_add_labelframe(frametype, x, y, w, h, label) -> pFlObject

        Adds a labelframe object.

        @param frametype: type of labelframe to be added
        @param frametype: [num./int] from xfdata module FL_NO_FRAME,
                          FL_UP_FRAME, FL_DOWN_FRAME, FL_BORDER_FRAME,
                          FL_SHADOW_FRAME, FL_ENGRAVED_FRAME, FL_ROUNDED_FRAME,
                          FL_EMBOSSED_FRAME, FL_OVAL_FRAME
        @param x: horizontal position (upper-left corner)
        @param x: vertical position (upper-left corner)
        @param w: width in coord units
        @param h: height in coord units
        @param label: text label of labelframe

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_add_labelframe = library.cfuncproto(
        library.load_so_libforms(), "fl_add_labelframe",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_labelframe(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(frametype, xfdata.FRAMETYPE_list)
    iframetype = library.convert_to_int(frametype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(frametype, x, y, w, h, label, iframetype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_labelframe(iframetype, ix, iy, iw, ih, slabel)
    return retval



#####################
# forms.h (free.h)
# Object Class: Free
#####################

# fl_create_free function placeholder (internal)


def fl_add_free(freetype, x, y, w, h, label, py_HandlePtr):
    """
        fl_add_free(freetype, x, y, w, h, label, py_HandlePtr) -> pFlObject

        Adds a free object.

        @param freetype: type of free to be added
        @type freetype: [num./int] from xfdata module FL_NORMAL_FREE,
                        FL_INACTIVE_FREE, FL_INPUT_FREE, FL_CONTINUOUS_FREE,
                        FL_ALL_FREE, FL_SLEEPING_FREE
        @param x: horizontal position (upper-left corner)
        @param x: vertical position (upper-left corner)
        @param w: width in coord units
        @param h: height in coord units
        @param label: text label of free

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_add_free = library.cfuncproto(
        library.load_so_libforms(), "fl_add_free",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING,
        xfdata.FL_HANDLEPTR],
        """FL_OBJECT * fl_add_free(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label, FL_HANDLEPTR handle)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(freetype, xfdata.FREETYPE_list)
    ifreetype = library.convert_to_int(freetype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    c_HandlePtr = xfdata.FL_HANDLEPTR(py_HandlePtr)
    library.keep_cfunc_refs(c_HandlePtr, py_HandlePtr)
    library.keep_elem_refs(freetype, x, y, w, h, label, ifreetype, ix, iy, iw, ih,
                   slabel)
    retval = _fl_add_free(ifreetype, ix, iy, iw, ih, slabel, c_HandlePtr)
    return retval



#####################
# forms.h (menu.h)
# Object Class: Menu
#####################

# fl_create_menu function placeholder (internal and deprecated)
# fl_add_menu function placeholder (deprecated)
# fl_clear_menu function placeholder (deprecated)
# fl_set_menu function placeholder (deprecated)
# fl_addto_menu function placeholder (deprecated)
# fl_replace_menu function placeholder (deprecated)
# fl_delete_menu function placeholder (deprecated)
# fl_set_menu_item_callback function placeholder (deprecated)
# fl_set_menu_item_shortcut function placeholder (deprecated)
# fl_set_menu_item_mode function placeholder (deprecated)
# fl_show_menu_symbol function placeholder (deprecated)
# fl_set_menu_popup function placeholder (deprecated)
# fl_get_menu_popup function placeholder (deprecated)
# fl_get_menu function placeholder (deprecated)
# fl_get_menu_item_text function placeholder (deprecated)
# fl_get_menu_maxitems function placeholder (deprecated)
# fl_get_menu_item_mode function placeholder (deprecated)
# fl_get_menu_text function placeholder (deprecated)
# fl_set_menu_entries function placeholder (deprecated)
# fl_set_menu_notitle function placeholder (deprecated)
# fl_set_menu_item_id function placeholder (deprecated)


###################
# forms.h (text.h)
###################

# fl_create_text function placeholder (internal)


def fl_add_text(texttype, x, y, w, h, label):
    """
        fl_add_text(texttype, x, y, w, h, label) -> pFlObject

        Adds a text object.

        @param texttype: type of text to be added. Values FL_NORMAL_TEXT
        @type texttype: int
        @param x: horizontal position (upper-left corner)
        @param x: vertical position (upper-left corner)
        @param w: width in coord units
        @param h: height in coord units
        @param label: text label of text

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_add_text = library.cfuncproto(
        library.load_so_libforms(), "fl_add_text",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_text(int type, FL_Coord x, FL_Coord y,
            FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(texttype, xfdata.TEXTTYPE_list)
    itexttype = library.convert_to_int(texttype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(texttype, x, y, w, h, label, itexttype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_text(itexttype, ix, iy, iw, ih, slabel)
    return retval


###############################
# forms.h (xpopupfn.h)
# Prototypes for xpop-up menus
###############################

# fl_setpup_entries function placeholder (deprecated)
# fl_newpup function placeholder (deprecated)
# fl_defpup function placeholder (deprecated)
# fl_addtopup function placeholder (deprecated)
# fl_setpup_mode function placeholder (deprecated)
# fl_freepup function placeholder (deprecated)
# fl_dopup function placeholder (deprecated)
# fl_setpup_default_cursor function placeholder (deprecated)
# fl_setpup_default_color function placeholder (deprecated)
# fl_setpup_default_pup_checked_color function placeholder (deprecated)
# fl_setpup_default_fontsize function placeholder (deprecated)
# fl_setpup_default_fontstyle function placeholder (deprecated)
#fl_setpup_fontsize placeholder (deprecated)
#fl_setpup_fontstyle placeholder (deprecated)
#fl_setpup_color placeholder (deprecated)
#fl_setpup_default_checkcolor placeholder (deprecated)
#fl_setpup_checkcolor placeholder (deprecated)
# fl_setpup_default_bw function placeholder (deprecated)
# fl_setpup_shortcut function placeholder (deprecated)
# fl_setpup_position function placeholder (deprecated)
# fl_setpup_selection function placeholder (deprecated)
# fl_setpup_shadow function placeholder (deprecated)
# fl_setpup_softedge function placeholder (deprecated)
# fl_setpup_bw function placeholder (deprecated)
# fl_setpup_title function placeholder (deprecated)
#FL_PUP_ENTERCB placeholder (deprecated)
# fl_setpup_entercb function placeholder (deprecated)
#FL_PUP_LEAVECB placeholder (deprecated)
# fl_setpup_leavecb function placeholder (deprecated)
# fl_setpup_pad function placeholder (deprecated)
# fl_setpup_cursor function placeholder (deprecated)
# fl_setpup_maxpup function placeholder (deprecated)
# fl_getpup_mode function placeholder (deprecated)
# fl_getpup_text function placeholder (deprecated)
# fl_showpup function placeholder (deprecated)
# fl_hidepup function placeholder (deprecated)
# fl_getpup_items function placeholder (deprecated)
# fl_current_pup function placeholder (deprecated)
# fl_setpup_itemcb function placeholder (deprecated)
# fl_setpup_menucb function placeholder (deprecated)
# fl_setpup_submenu function placeholder (deprecated)
# fl_setpup placeholder


# the following (fl_fheight) etc. were never documented and were
# removed from V0.89, but apparently this broke some applications that
# were using them. Put them back in 10/22/00

def fl_gc_():
    """
    fl_gc_() -> gc

    @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_gc_ = library.cfuncproto(
        library.load_so_libforms(), "fl_gc_",
        xfdata.GC, [],
        """GC fl_gc_()""")
    library.check_if_initialized()
    retval = _fl_gc_()
    return retval

#fl_gc = fl_gc_()       # commented to prevent a SegmentationFault --LK
fl_gc = fl_gc_


def fl_textgc_():
    """
    fl_textgc_() -> gc

    @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_textgc_ = library.cfuncproto(
        library.load_so_libforms(), "fl_textgc_",
        xfdata.GC, [],
        """GC fl_textgc_()""")
    library.check_if_initialized()
    retval = _fl_textgc_()
    return retval

#fl_textgc = fl_textgc_()       # commented to prevent a SegmentationFault --LK
fl_textgc = fl_textgc_


def fl_fheight_():
    """
    fl_fheight_() -> num.

    @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_fheight_ = library.cfuncproto(
        library.load_so_libforms(), "fl_fheight_",
        cty.c_int, [],
        """int fl_fheight_()""")
    library.check_if_initialized()
    retval = _fl_fheight_()
    return retval


#fl_fheight = fl_fheight_()     # commented to prevent a SegmentationFault --LK
fl_fheight = fl_fheight_


def fl_fdesc_():
    """
    fl_fdesc_() -> num.

    @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_fdesc_ = library.cfuncproto(
        library.load_so_libforms(), "fl_fdesc_",
        cty.c_int, [],
        """int fl_fdesc_()""")
    library.check_if_initialized()
    retval = _fl_fdesc_()
    return retval

#fl_fdesc = fl_fdesc_()         # commented to prevent a SegmentationFault --LK
fl_fdesc = fl_fdesc_


def fl_cur_win_():
    """
    fl_cur_win_() -> window

    @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_cur_win_ = library.cfuncproto(
        library.load_so_libforms(), "fl_cur_win_",
        xfdata.Window, [],
        """Window fl_cur_win_()""")
    library.check_if_initialized()
    retval = _fl_cur_win_()
    return retval

#fl_cur_win = fl_cur_win_()     # commented to prevent a SegmentationFault--LK
fl_cur_win = fl_cur_win_


def fl_cur_fs_():
    """
    fl_cur_fs_() -> XFontStruct class

    @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_cur_fs_ = library.cfuncproto(
        library.load_so_libforms(), "fl_cur_fs_",
        cty.POINTER(xfdata.XFontStruct), [],
        """XFontStruct * fl_cur_fs_()""")
    library.check_if_initialized()
    retval = _fl_cur_fs_()
    return retval


#fl_cur_fs = fl_cur_fs_()       # commented to prevent a SegmentationFault --LK
fl_cur_fs = fl_cur_fs_


def fl_display_():
    """
    fl_display_() -> pDisplay

    @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_display_ = library.cfuncproto(
        library.load_so_libforms(), "fl_display_",
        cty.POINTER(xfdata.Display), [],
        """Display * fl_display_()""")
    library.check_if_initialized()
    retval = _fl_display_()
    return retval



# flps_apply_gamma(p1) function placeholder (internal)
# flps_arc(fill, x, y, r, t1, t2, colr)function placeholder (internal)
# flps_circ(fill, x, y, r, colr) function placeholder (internal)
# flps_color(colr) function placeholder (internal)
# flps_draw_box(style, x, y, w, h, colr, bwIn) function placeholder (internal)
# flps_draw_checkbox(boxtype, x, y, w, h, colr, bw) function placeholder (internal)
# flps_draw_frame(style, x, y, w, h, colr, bw) function placeholder (internal)
# flps_draw_symbol(label, x, y, w, h, colr) function placeholder (internal)
# flps_draw_tbox(style, x, y, w, h, colr, bw) function placeholder (internal)
# flps_draw_text(align, x, y, w, h, colr, style, size, text) function placeholder (internal)
# flps_draw_text_beside(align, x, y, w, h, colr, style, size, text) function placeholder (internal)
# flps_emit_header(title, npages, xi, yi, xf, yf) function placeholder (internal)
# flps_emit_prolog() function placeholder (internal)
# flps_get_gray255(colr) function placeholder (internal)
# flps_get_linestyle() function placeholder (internal)
# flps_get_linewidth() function placeholder (internal)
# flps_get_namedcolor(colrname) function placeholder (internal)
# flps_invalidate_color_cache() function placeholder (internal)
# flps_invalidate_font_cache() function placeholder (internal)
# flps_invalidate_linewidth_cache() function placeholder (internal)
# flps_invalidate_symbol_cache() function placeholder (internal)
# flps_line(xi, yi, xf, yf, colr) function placeholder (internal)
# flps_lines(Point, numpt, colr) function placeholder (internal)
# flps_linestyle(linestyle) function placeholder (internal)
# flps_linewidth(linewidth) function placeholder (internal)
# flps_log(text) function placeholder (internal)
# flps_output(fmt) function placeholder (internal)
# flps_oval(fill, x, y, w, h, colr) function placeholder (internal)
# flps_pieslice(fill, x, y, w, h, t1, t2, colr) function placeholder (internal)
# flps_poly(fill, Point, numpt, colr) function placeholder (internal)
# flps_rectangle(fill, x, y, w, h, colr) function placeholder (internal)
# flps_reset_cache() function placeholder (internal)
# flps_reset_linewidth() function placeholder (internal)
# flps_restore_flps() function placeholder (internal)
# flps_rgbcolor(r, g, b) function placeholder (internal)
# flps_roundrectangle(fill, x, y, w, h, colr) function placeholder (internal)
# flps_set_clipping(x, y, w, h) function placeholder (internal)
# flps_set_font(style, size) function placeholder (internal)
# flps_unset_clipping() function placeholder (internal)

