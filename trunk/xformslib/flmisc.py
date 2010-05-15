#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage miscellaneous objects.

    Copyright (C) 2009, 2010  Luca Lazzaroni "LukenShiro"
    e-mail: <lukenshiro@ngi.it>

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


# originally generated by 'h2xml+gccxml' and 'xml2py'
# then heavily reordered and reworked

# ############################################# #
# Interface to XForms shared object libraries   #
# ############################################# #

import ctypes as cty
from xformslib import library as libr
from xformslib import xfdata


##################
# forms.h (box.h)
##################

# fl_create_box function placeholder (internal)


def fl_add_box(boxtype, x, y, w, h, label):
    """Adds a box object.

    --

    :Parameters:
      `boxtype` : int
        type of the box to be added. Values (from xfdata.py) FL_NO_BOX,
        FL_UP_BOX, FL_DOWN_BOX, FL_BORDER_BOX, FL_SHADOW_BOX, FL_FRAME_BOX,
        FL_ROUNDED_BOX, FL_EMBOSSED_BOX, FL_FLAT_BOX, FL_RFLAT_BOX,
        FL_RSHADOW_BOX, FL_OVAL_BOX, FL_ROUNDED3D_UPBOX, FL_ROUNDED3D_DOWNBOX,
        FL_OVAL3D_UPBOX, FL_OVAL3D_DOWNBOX, FL_OVAL3D_FRAMEBOX,
        FL_OVAL3D_EMBOSSEDBOX
      `x` : int
        horizontal position (upper-left corner)
      `y` : int
        vertical position (upper-left corner)
      `w` : int
        width in coord units
      `h` : int
        height in coord units
      `label` : str
        text label of box

    :return: box object added (pFlObject)
    :rtype: pointer to xfdata.FL_OBJECT

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_add_box = libr.cfuncproto(
        libr.load_so_libforms(), "fl_add_box",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_box(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    libr.check_if_initialized()
    libr.check_admitted_value_in_list(boxtype, xfdata.BOXTYPE_list)
    iboxtype = libr.convert_to_int(boxtype)
    ix = libr.convert_to_FL_Coord(x)
    iy = libr.convert_to_FL_Coord(y)
    iw = libr.convert_to_FL_Coord(w)
    ih = libr.convert_to_FL_Coord(h)
    slabel = libr.convert_to_string(label)
    libr.keep_elem_refs(boxtype, x, y, w, h, label, iboxtype, ix, iy, iw,
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


def fl_stuff_clipboard(pFlObject, clipbdtype, data, size, \
                       py_LoseSelectionCb):
    """Stores data in clipboard?

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        clipboard object
      `clipbdtype` : long
        type of clipboard (not used)
      `data` : *todo*
        *todo*
      `size` : long
        *todo*
      `py_LoseSelectionCb` : python function callback, returning value
        name referring to function(pFlObject, longnum) -> num.

    :return: num.
    :rtype: int

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    #FL_LOSE_SELECTION_CB = cty.CFUNCTYPE(cty.c_int, cty.POINTER( \
    #                       xfdata.FL_OBJECT), cty.c_long)
    _fl_stuff_clipboard = libr.cfuncproto(
        libr.load_so_libforms(), "fl_stuff_clipboard",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_long, cty.c_void_p,
        cty.c_long, xfdata.FL_LOSE_SELECTION_CB],
        """int fl_stuff_clipboard(FL_OBJECT * ob, long int type,
           const char * data, long int size,
           FL_LOSE_SELECTION_CB lose_callback)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    lclipbdtype = libr.convert_to_long(clipbdtype)
    pdata = cty.cast(data, cty.c_void_p)
    lsize = libr.convert_to_long(size)
    libr.verify_function_type(py_LoseSelectionCb)
    c_LoseSelectionCb = xfdata.FL_LOSE_SELECTION_CB(py_LoseSelectionCb)
    libr.keep_cfunc_refs(c_LoseSelectionCb, py_LoseSelectionCb)
    libr.keep_elem_refs(pFlObject, clipbdtype, data, size, lclipbdtype,
                        pdata, lsize)
    retval = _fl_stuff_clipboard(pFlObject, lclipbdtype, pdata, lsize,
                                 c_LoseSelectionCb)
    return retval


def fl_request_clipboard(pFlObject, clipbdtype, py_SelectionCb):
    """Retrieves data from clipboard?

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        clipboard object
      `clipbdtype` : long
        type of clipboard (not used)
      `py_SelectionCb` : python function callback, returning value
        name referring to function(pFlObject, longnum, vdata, longnum)
        -> num.

    :return: 0, or -1 (if it's on different window?)
    :rtype: int

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    #FL_SELECTION_CB = cty.CFUNCTYPE(cty.c_int, cty.POINTER(xfdata.FL_OBJECT),
    #                                cty.c_long, cty.c_void_p, cty.c_long)
    _fl_request_clipboard = libr.cfuncproto(
        libr.load_so_libforms(), "fl_request_clipboard",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_long,
        xfdata.FL_SELECTION_CB],
        """int fl_request_clipboard(FL_OBJECT * ob, long int type,
           FL_SELECTION_CB got_it_callback)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    lclipbdtype = libr.convert_to_long(clipbdtype)
    libr.verify_function_type(py_SelectionCb)
    c_SelectionCb = xfdata.FL_SELECTION_CB(py_SelectionCb)
    libr.keep_cfunc_refs(c_SelectionCb, py_SelectionCb)
    libr.keep_elem_refs(pFlObject, clipbdtype, lclipbdtype)
    retval = _fl_request_clipboard(pFlObject, lclipbdtype, c_SelectionCb)
    return retval




###################
# forms.h (flps.h)
###################

# postscript stuff


def flps_init():
    """Customizes the output by changing the PostScript output control
    parameters.

    --

    :return: class instance
    :rtype: pointer to xfdata.FLPS_CONTROL

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _flps_init = libr.cfuncproto(
        libr.load_so_libflimage(), "flps_init",
        cty.POINTER(xfdata.FLPS_CONTROL), [],
        """FLPS_CONTROL * flps_init()""")
    libr.check_if_initialized()
    retval = _flps_init()
    return retval


def fl_object_ps_dump(pFlObject, fname):
    """Obtains hardcopies of some objects in a what-you-see-is-what-you-get
    (WYSIWYG) way, especially those that are dynamic and of vector-graphics
    in nature. It outputs the specified object in PostScript. The object must
    be visible at the time of the function call. The hardcopy should mostly
    be WYSIWYG and centered on the printed page. The orientation is determined
    such that a balanced margin results, i.e., if the width of the object is
    larger than the height, landscape mode will be used. Further, if the
    object is too big to fit on the printed page, a scale factor will be
    applied so the object fits. The box underneath the object is by default
    not drawn and in the default black&white mode, all curves are drawn in
    black.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        object. Only the xfdata.FL_XYPLOT object is supported.
      `fname` : str
        name of output file. If NULL, a fselector will be shown to ask the
        user for a file name.

    :return: non-negative num., or negative num. (on failure)
    :rtype: int

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_object_ps_dump = libr.cfuncproto(
        libr.load_so_libflimage(), "fl_object_ps_dump",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), xfdata.STRING],
        """int fl_object_ps_dump(FL_OBJECT * ob, const char * fname)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    sfname = libr.convert_to_string(fname)
    libr.keep_elem_refs(pFlObject, fname, sfname)
    retval = _fl_object_ps_dump(pFlObject, sfname)
    return retval


####################
# forms.h (frame.h)
####################

# fl_create_frame function placeholder (internal)


def fl_add_frame(frametype, x, y, w, h, label):
    """Adds a frame object.

    --

    :Parameters:
      `frametype` : int
        type of frame to be added. Values (from xfdata.py) FL_NO_FRAME,
        FL_UP_FRAME, FL_DOWN_FRAME, FL_BORDER_FRAME, FL_SHADOW_FRAME,
        FL_ENGRAVED_FRAME, FL_ROUNDED_FRAME, FL_EMBOSSED_FRAME, FL_OVAL_FRAME
      `x` : int
        horizontal position (upper-left corner)
      `y` : int
        vertical position (upper-left corner)
      `w` : int
        width in coord units
      `h` : int
        height in coord units
      `label` : str
        text label of frame

    :return: frame object added (pFlObject)
    :rtype: pointer to xfdata.FL_OBJECT

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_add_frame = libr.cfuncproto(
        libr.load_so_libforms(), "fl_add_frame",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_frame(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    libr.check_if_initialized()
    libr.check_admitted_value_in_list(frametype, xfdata.FRAMETYPE_list)
    iframetype = libr.convert_to_int(frametype)
    ix = libr.convert_to_FL_Coord(x)
    iy = libr.convert_to_FL_Coord(y)
    iw = libr.convert_to_FL_Coord(w)
    ih = libr.convert_to_FL_Coord(h)
    slabel = libr.convert_to_string(label)
    libr.keep_elem_refs(frametype, x, y, w, h, label, iframetype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_frame(iframetype, ix, iy, iw, ih, slabel)
    return retval


# labeld frame

# fl_create_labelframe function placeholder (internal)


def fl_add_labelframe(frametype, x, y, w, h, label):
    """Adds a labelframe object.

    --

    :Parameters:
      `frametype` : int
        type of labelframe to be added. Values (from xfdata.py) FL_NO_FRAME,
        FL_UP_FRAME, FL_DOWN_FRAME, FL_BORDER_FRAME, FL_SHADOW_FRAME,
        FL_ENGRAVED_FRAME, FL_ROUNDED_FRAME, FL_EMBOSSED_FRAME, FL_OVAL_FRAME
      `x` : int
        horizontal position (upper-left corner)
      `y` : int
        vertical position (upper-left corner)
      `w` : int
        width in coord units
      `h` : int
        height in coord units
      `label` : str
        text label of labelframe

    :return: labelframe object added (pFlObject)
    :rtype: pointer to xfdata.FL_OBJECT

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_add_labelframe = libr.cfuncproto(
        libr.load_so_libforms(), "fl_add_labelframe",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_labelframe(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    libr.check_if_initialized()
    libr.check_admitted_value_in_list(frametype, xfdata.FRAMETYPE_list)
    iframetype = libr.convert_to_int(frametype)
    ix = libr.convert_to_FL_Coord(x)
    iy = libr.convert_to_FL_Coord(y)
    iw = libr.convert_to_FL_Coord(w)
    ih = libr.convert_to_FL_Coord(h)
    slabel = libr.convert_to_string(label)
    libr.keep_elem_refs(frametype, x, y, w, h, label, iframetype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_labelframe(iframetype, ix, iy, iw, ih, slabel)
    return retval



#####################
# forms.h (free.h)
# Object Class: Free
#####################

# fl_create_free function placeholder (internal)


def fl_add_free(freetype, x, y, w, h, label, py_HandlePtr):
    """Adds a free object.

    --

    :Parameters:
      `freetype` : int
        type of free to be added. Value (from xfdata.py) FL_NORMAL_FREE,
        FL_INACTIVE_FREE, FL_INPUT_FREE, FL_CONTINUOUS_FREE, FL_ALL_FREE,
        FL_SLEEPING_FREE
      `x` : int
        horizontal position (upper-left corner)
      `y` : int
        vertical position (upper-left corner)
      `w` : int
        width in coord units
      `h` : int
        height in coord units
      `label` : str
        text label of free
      `py_HandlePtr` : python function to handle free object, returning value
        name referring to function(int, pFlObject, int, coord, coord, int,
        voidp) -> num.

    :return: free object added (pFlObject)
    :rtype: pointer to xfdata.FL_OBJECT

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    #FL_HANDLEPTR = cty.CFUNCTYPE(cty.c_int, cty.POINTER(FL_OBJECT), \
    #   cty.c_int, FL_Coord, FL_Coord, cty.c_int, cty.c_void_p)
    _fl_add_free = libr.cfuncproto(
        libr.load_so_libforms(), "fl_add_free",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING,
        xfdata.FL_HANDLEPTR],
        """FL_OBJECT * fl_add_free(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label, FL_HANDLEPTR handle)""")
    libr.check_if_initialized()
    libr.check_admitted_value_in_list(freetype, xfdata.FREETYPE_list)
    ifreetype = libr.convert_to_int(freetype)
    ix = libr.convert_to_FL_Coord(x)
    iy = libr.convert_to_FL_Coord(y)
    iw = libr.convert_to_FL_Coord(w)
    ih = libr.convert_to_FL_Coord(h)
    slabel = libr.convert_to_string(label)
    libr.verify_function_type(py_HandlePtr)
    c_HandlePtr = xfdata.FL_HANDLEPTR(py_HandlePtr)
    libr.keep_cfunc_refs(c_HandlePtr, py_HandlePtr)
    libr.keep_elem_refs(freetype, x, y, w, h, label, ifreetype, ix, iy, iw,
                        ih, slabel)
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
    """Adds a text object.

    --

    :Parameters:
      `texttype` : int
        type of text to be added. Values FL_NORMAL_TEXT
      `x` : int
        horizontal position (upper-left corner)
      `y` : int
        vertical position (upper-left corner)
      `w` : int
        width in coord units
      `h` : int
        height in coord units
      `label` : str
        text label of text

    :return: text object added
    :rtype: pointer to xfdata.FL_OBJECT

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_add_text = libr.cfuncproto(
        libr.load_so_libforms(), "fl_add_text",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_text(int type, FL_Coord x, FL_Coord y,
            FL_Coord w, FL_Coord h, const char * label)""")
    libr.check_if_initialized()
    libr.check_admitted_value_in_list(texttype, xfdata.TEXTTYPE_list)
    itexttype = libr.convert_to_int(texttype)
    ix = libr.convert_to_FL_Coord(x)
    iy = libr.convert_to_FL_Coord(y)
    iw = libr.convert_to_FL_Coord(w)
    ih = libr.convert_to_FL_Coord(h)
    slabel = libr.convert_to_string(label)
    libr.keep_elem_refs(texttype, x, y, w, h, label, itexttype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_text(itexttype, ix, iy, iw, ih, slabel)
    return retval


###############################
# forms.h (xpopup.h)
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
    """*todo*

    --

    :return: graphics context id
    :rtype: xfdata.GC

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_gc_ = libr.cfuncproto(
        libr.load_so_libforms(), "fl_gc_",
        xfdata.GC, [],
        """GC fl_gc_()""")
    libr.check_if_initialized()
    retval = _fl_gc_()
    return retval

#fl_gc = fl_gc_()       # commented to prevent a SegmentationFault --LK
fl_gc = fl_gc_


def fl_textgc_():
    """*todo*

    --

    :return: graphics context id
    :rtype: xfdata.GC

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_textgc_ = libr.cfuncproto(
        libr.load_so_libforms(), "fl_textgc_",
        xfdata.GC, [],
        """GC fl_textgc_()""")
    libr.check_if_initialized()
    retval = _fl_textgc_()
    return retval

#fl_textgc = fl_textgc_()       # commented to prevent a SegmentationFault --LK
fl_textgc = fl_textgc_


def fl_fheight_():
    """*todo*

    --

    :return: num.
    :rtype: int

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_fheight_ = libr.cfuncproto(
        libr.load_so_libforms(), "fl_fheight_",
        cty.c_int, [],
        """int fl_fheight_()""")
    libr.check_if_initialized()
    retval = _fl_fheight_()
    return retval


#fl_fheight = fl_fheight_()     # commented to prevent a SegmentationFault --LK
fl_fheight = fl_fheight_


def fl_fdesc_():
    """*todo*

    --


    :return: num.
    :rtype: int

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_fdesc_ = libr.cfuncproto(
        libr.load_so_libforms(), "fl_fdesc_",
        cty.c_int, [],
        """int fl_fdesc_()""")
    libr.check_if_initialized()
    retval = _fl_fdesc_()
    return retval

#fl_fdesc = fl_fdesc_()   # commented to prevent a SegmentationFault --LK
fl_fdesc = fl_fdesc_


def fl_cur_win_():
    """*todo*

    --

    :return: window id
    :rtype: long_pos

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_cur_win_ = libr.cfuncproto(
        libr.load_so_libforms(), "fl_cur_win_",
        xfdata.Window, [],
        """Window fl_cur_win_()""")
    libr.check_if_initialized()
    retval = _fl_cur_win_()
    return retval

#fl_cur_win = fl_cur_win_()  # commented to prevent a SegmentationFault--LK
fl_cur_win = fl_cur_win_


def fl_cur_fs_():
    """*todo*

    --

    :return: font structure class instance
    :rtype: pointer to xfdata.XFontStruct

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_cur_fs_ = libr.cfuncproto(
        libr.load_so_libforms(), "fl_cur_fs_",
        cty.POINTER(xfdata.XFontStruct), [],
        """XFontStruct * fl_cur_fs_()""")
    libr.check_if_initialized()
    retval = _fl_cur_fs_()
    return retval


#fl_cur_fs = fl_cur_fs_()  # commented to prevent a SegmentationFault --LK
fl_cur_fs = fl_cur_fs_


def fl_display_():
    """*todo*

    --

    :return: current display? (pDisplay)
    :rtype: pointer to xfdata.Display

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_display_ = libr.cfuncproto(
        libr.load_so_libforms(), "fl_display_",
        cty.POINTER(xfdata.Display), [],
        """Display * fl_display_()""")
    libr.check_if_initialized()
    retval = _fl_display_()
    return retval



# flps_apply_gamma(p1) function placeholder (internal)
# flps_arc(fill, x, y, r, t1, t2, colr)function placeholder (internal)
# flps_circ(fill, x, y, r, colr) function placeholder (internal)
# flps_color(colr) function placeholder (internal)
# flps_draw_box(style, x, y, w, h, colr, bwIn) function placeholder (internal)
# flps_draw_checkbox(boxtype, x, y, w, h, colr, bw)
#  function placeholder (internal)
# flps_draw_frame(style, x, y, w, h, colr, bw) function placeholder (internal)
# flps_draw_symbol(label, x, y, w, h, colr) function placeholder (internal)
# flps_draw_tbox(style, x, y, w, h, colr, bw) function placeholder (internal)
# flps_draw_text(align, x, y, w, h, colr, style, size, text)
#  function placeholder (internal)
# flps_draw_text_beside(align, x, y, w, h, colr, style, size, text)
#  function placeholder (internal)
# flps_emit_header(title, npages, xi, yi, xf, yf)
#  function placeholder (internal)
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
# flps_pieslice(fill, x, y, w, h, t1, t2, colr)
# function placeholder (internal)
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
