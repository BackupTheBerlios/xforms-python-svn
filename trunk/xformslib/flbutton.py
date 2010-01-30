#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

"""
    xforms-python - Python wrapper for XForms (X11) GUI C toolkit library
    using ctypes

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
from xformslib import library
from xformslib import xfdata
from xformslib import flbasic
from xformslib import flbitmap




#############################################################
# forms.h (button.h)
# All Buttons: regular button, light button and round button
#############################################################

# Routines

# fl_create_button function placeholder (internal)
# fl_create_roundbutton function placeholder (internal)
# fl_create_round3dbutton function placeholder (internal)
# fl_create_lightbutton function placeholder (internal)
# fl_create_checkbutton function placeholder (internal)
# fl_create_bitmapbutton function placeholder (internal)
# fl_create_pixmapbutton function placeholder (internal)
# fl_create_scrollbutton function placeholder (internal)
# fl_create_labelbutton function placeholder (internal)


def fl_add_roundbutton(buttontype, x, y, w, h, label):
    """Adds a roundbutton object.

    @param buttontype: type of button object to be added. Values (from
        xfdata module) FL_NORMAL_BUTTON, FL_PUSH_BUTTON, FL_RADIO_BUTTON,
        FL_HIDDEN_BUTTON, FL_TOUCH_BUTTON, FL_INOUT_BUTTON, FL_RETURN_BUTTON,
        FL_HIDDEN_RET_BUTTON, FL_MENU_BUTTON, FL_TOGGLE_BUTTON
    @type buttontype: int
    @param x: horizontal position (upper-left corner)
    @type x: int
    @param y: vertical position (upper-left corner)
    @type y: int
    @param w: width in coord units
    @type w: int
    @param h: height in coord units
    @type h: int
    @param label: text label of button
    @type label: str

    @returns: button object created (pFlObject)
    @rtype: pointer to xfdata.FL_OBJECT

    @example: btnobj = fl_add_roundbutton(xfdata.FL_TOGGLE_BUTTON, 145,
        199, 120, 30, "MyButton")

    @status: Tested + Doc + Demo = OK

    """
    _fl_add_roundbutton = library.cfuncproto(
        library.load_so_libforms(), "fl_add_roundbutton",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_roundbutton(int type, FL_Coord x,
           FL_Coord y, FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(buttontype, xfdata.BUTTONTYPE_list)
    ibuttontype = library.convert_to_int(buttontype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(buttontype, x, y, w, h, label, ibuttontype, ix, \
                           iy, iw, ih, slabel)
    retval = _fl_add_roundbutton(ibuttontype, ix, iy, iw, ih, slabel)
    return retval


def fl_add_round3dbutton(buttontype, x, y, w, h, label):
    """Adds a 3D roundbutton object.

    @param buttontype: type of button object to be added. Values (from xfdata
        module) FL_NORMAL_BUTTON, FL_PUSH_BUTTON, FL_RADIO_BUTTON,
        FL_HIDDEN_BUTTON, FL_TOUCH_BUTTON, FL_INOUT_BUTTON, FL_RETURN_BUTTON,
        FL_HIDDEN_RET_BUTTON, FL_MENU_BUTTON, FL_TOGGLE_BUTTON
    @type buttontype: int
    @param x: horizontal position (upper-left corner)
    @type x: int
    @param y: vertical position (upper-left corner)
    @type y: int
    @param w: width in coord units
    @type w: int
    @param h: height in coord units
    @type h: int
    @param label: text label of button
    @type label: str

    @returns: button object created (pFlObject)
    @rtype: pointer to xfdata.FL_OBJECT

    @example: btnobj = fl_add_round3dbutton(xfdata.FL_TOGGLE_BUTTON, 145,
        199, 120, 30, "MyButton")

    @status: Tested + Doc + Demo = OK

    """
    _fl_add_round3dbutton = library.cfuncproto(
        library.load_so_libforms(), "fl_add_round3dbutton",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_round3dbutton(int type, FL_Coord x,
           FL_Coord y, FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(buttontype, xfdata.BUTTONTYPE_list)
    ibuttontype = library.convert_to_int(buttontype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(buttontype, x, y, w, h, label, ibuttontype, ix, \
                           iy, iw, ih, slabel)
    retval = _fl_add_round3dbutton(ibuttontype, ix, iy, iw, ih, slabel)
    return retval


def fl_add_lightbutton(buttontype, x, y, w, h, label):
    """Adds a lightbutton object (with an on/off light switch).

    @param buttontype: type of button to be added. Values (from xfdata module)
        FL_NORMAL_BUTTON, FL_PUSH_BUTTON, FL_RADIO_BUTTON,
        FL_HIDDEN_BUTTON, FL_TOUCH_BUTTON, FL_INOUT_BUTTON, FL_RETURN_BUTTON,
        FL_HIDDEN_RET_BUTTON, FL_MENU_BUTTON, FL_TOGGLE_BUTTON
    @type buttontype: int
    @param x: horizontal position (upper-left corner)
    @type x: int
    @param y: vertical position (upper-left corner)
    @type y: int
    @param w: width in coord units
    @type w: int
    @param h: height in coord units
    @type h: int
    @param label: text label of button
    @type label: str

    @returns: button object created (pFlObject)
    @rtype: pointer to xfdata.FL_OBJECT

    @example: btnobj = fl_add_lightbutton(xfdata.FL_TOGGLE_BUTTON, 145,
        199, 120, 30, "MyButton")

    @status: Tested + Doc + Demo = OK

    """
    _fl_add_lightbutton = library.cfuncproto(
        library.load_so_libforms(), "fl_add_lightbutton",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_lightbutton(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(buttontype, xfdata.BUTTONTYPE_list)
    ibuttontype = library.convert_to_int(buttontype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(buttontype, x, y, w, h, label, ibuttontype, ix, \
                           iy, iw, ih, slabel)
    retval = _fl_add_lightbutton(ibuttontype, ix, iy, iw, ih, slabel)
    return retval


def fl_add_checkbutton(buttontype, x, y, w, h, label):
    """Adds a checkbutton object.

    @param buttontype: type of button object to be added. Values (from xfdata
        module) FL_NORMAL_BUTTON, FL_PUSH_BUTTON, FL_RADIO_BUTTON,
        FL_HIDDEN_BUTTON, FL_TOUCH_BUTTON, FL_INOUT_BUTTON, FL_RETURN_BUTTON,
        FL_HIDDEN_RET_BUTTON, FL_MENU_BUTTON, FL_TOGGLE_BUTTON
    @type buttontype: int
    @param x: horizontal position (upper-left corner)
    @type x: int
    @param y: vertical position (upper-left corner)
    @type y: int
    @param w: width in coord units
    @type w: int
    @param h: height in coord units
    @type h: int
    @param label: text label of button
    @type label: str

    @returns: button object created (pFlObject)
    @rtype: pointer to xfdata.FL_OBJECT

    @example: btnobj = fl_add_checkbutton(xfdata.FL_TOGGLE_BUTTON, 145,
        199, 120, 30, "MyButton")

    @status: Tested + Doc + Demo = OK

    """
    _fl_add_checkbutton = library.cfuncproto(
        library.load_so_libforms(), "fl_add_checkbutton",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_checkbutton(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(buttontype, xfdata.BUTTONTYPE_list)
    ibuttontype = library.convert_to_int(buttontype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(buttontype, x, y, w, h, label, ibuttontype, ix, \
                           iy, iw, ih, slabel)
    retval = _fl_add_checkbutton(ibuttontype, ix, iy, iw, ih, slabel)
    return retval


def fl_add_button(buttontype, x, y, w, h, label):
    """Adds a button object to the current form.

    @param buttontype: type of button to be added. Values (from xfdata
        module) FL_NORMAL_BUTTON, FL_PUSH_BUTTON, FL_RADIO_BUTTON,
        FL_HIDDEN_BUTTON, FL_TOUCH_BUTTON, FL_INOUT_BUTTON, FL_RETURN_BUTTON,
        FL_HIDDEN_RET_BUTTON, FL_MENU_BUTTON, FL_TOGGLE_BUTTON
    @type buttontype: int
    @param x: horizontal position (upper-left corner)
    @type x: int
    @param y: vertical position (upper-left corner)
    @type y: int
    @param w: width in coord units
    @type w: int
    @param h: height in coord units
    @type h: int
    @param label: text label of button
    @type label: str

    @returns: button object created (pFlObject)
    @rtype: pointer to xfdata.FL_OBJECT

    @example: btnobj = fl_add_button(xfdata.FL_TOGGLE_BUTTON, 145,
        199, 120, 30, "MyButton")

    @status: Tested + Doc + Demo = OK

    """
    _fl_add_button = library.cfuncproto(
        library.load_so_libforms(), "fl_add_button",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_button(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(buttontype, xfdata.BUTTONTYPE_list)
    ibuttontype = library.convert_to_int(buttontype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(buttontype, x, y, w, h, label, ibuttontype, ix, \
                           iy, iw, ih, slabel)
    retval = _fl_add_button(ibuttontype, ix, iy, iw, ih, slabel)
    return retval


def fl_add_bitmapbutton(buttontype, x, y, w, h, label):
    """Adds a bitmapbutton object.

    @param buttontype: type of button to be added. Values (from xfdata
        module) FL_NORMAL_BUTTON, FL_PUSH_BUTTON, FL_RADIO_BUTTON,
        FL_HIDDEN_BUTTON, FL_TOUCH_BUTTON, FL_INOUT_BUTTON, FL_RETURN_BUTTON,
        FL_HIDDEN_RET_BUTTON, FL_MENU_BUTTON, FL_TOGGLE_BUTTON
    @type buttontype: int
    @param x: horizontal position (upper-left corner)
    @type x: int
    @param y: vertical position (upper-left corner)
    @type y: int
    @param w: width in coord units
    @type w: int
    @param h: height in coord units
    @type h: int
    @param label: text label of button
    @type label: str

    @returns: button object created (pFlObject)
    @rtype: pointer to xfdata.FL_OBJECT

    @example: btnobj = fl_add_bitmapbutton(xfdata.FL_TOGGLE_BUTTON, 145,
        199, 120, 30, "MyButton")

    @status: Tested + Doc + Demo = OK

    """
    _fl_add_bitmapbutton = library.cfuncproto(
        library.load_so_libforms(), "fl_add_bitmapbutton",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord, \
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_bitmapbutton(int type, FL_Coord x,
           FL_Coord y, FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(buttontype, xfdata.BUTTONTYPE_list)
    ibuttontype = library.convert_to_int(buttontype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(buttontype, x, y, w, h, label, ibuttontype, ix, \
                           iy, iw, ih, slabel)
    retval = _fl_add_bitmapbutton(ibuttontype, ix, iy, iw, ih, slabel)
    return retval


def fl_add_scrollbutton(buttontype, x, y, w, h, label):
    """Adds a scrollbutton object.

    @param buttontype: type of button to be added. Values (from xfdata
        module) FL_NORMAL_BUTTON, FL_PUSH_BUTTON, FL_RADIO_BUTTON,
        FL_HIDDEN_BUTTON, FL_TOUCH_BUTTON, FL_INOUT_BUTTON, FL_RETURN_BUTTON,
        FL_HIDDEN_RET_BUTTON, FL_MENU_BUTTON, FL_TOGGLE_BUTTON
    @type buttontype: int
    @param x: horizontal position (upper-left corner)
    @type x: int
    @param y: vertical position (upper-left corner)
    @type y: int
    @param w: width in coord units
    @type w: int
    @param h: height in coord units
    @type h: int
    @param label: text label of button
    @type label: str

    @returns: button object created (pFlObject)
    @rtype: pointer to xfdata.FL_OBJECT

    @example: btnobj = fl_add_scrollbutton(xfdata.FL_TOGGLE_BUTTON, 145,
        199, 120, 30, "MyButton")

    @status: Tested + Doc + NoDemo = OK

    """
    _fl_add_scrollbutton = library.cfuncproto(
        library.load_so_libforms(), "fl_add_scrollbutton",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord, \
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_scrollbutton(int type, FL_Coord x,
           FL_Coord y, FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(buttontype, xfdata.BUTTONTYPE_list)
    ibuttontype = library.convert_to_int(buttontype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(buttontype, x, y, w, h, label, ibuttontype, ix, iy, iw,
                   ih, slabel)
    retval = _fl_add_scrollbutton(ibuttontype, ix, iy, iw, ih, slabel)
    return retval


def fl_add_labelbutton(buttontype, x, y, w, h, label):
    """Adds a labelbutton object.

    @param buttontype: type of button to be added. Values (from xfdata module)
        FL_NORMAL_BUTTON, FL_PUSH_BUTTON, FL_RADIO_BUTTON, FL_HIDDEN_BUTTON,
        FL_TOUCH_BUTTON, FL_INOUT_BUTTON, FL_RETURN_BUTTON,
        FL_HIDDEN_RET_BUTTON, FL_MENU_BUTTON, FL_TOGGLE_BUTTON
    @type buttontype: int
    @param x: horizontal position (upper-left corner)
    @type x: int
    @param y: vertical position (upper-left corner)
    @type y: int
    @param w: width in coord units
    @type w: int
    @param h: height in coord units
    @type h: int
    @param label: text label of button
    @type label: str

    @returns: button object created (pFlObject)
    @rtype: pointer to xfdata.FL_OBJECT

    @example: btnobj = fl_add_labelbutton(xfdata.FL_TOGGLE_BUTTON, 145,
        199, 120, 30, "MyButton")

    @status: Tested + Doc + NoDemo = OK

    """
    _fl_add_labelbutton = library.cfuncproto(
        library.load_so_libforms(), "fl_add_labelbutton",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord, \
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_labelbutton(int type, FL_Coord x,
           FL_Coord y, FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(buttontype, xfdata.BUTTONTYPE_list)
    ibuttontype = library.convert_to_int(buttontype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(buttontype, x, y, w, h, label, ibuttontype, ix, \
                           iy, iw, ih, slabel)
    retval = _fl_add_labelbutton(ibuttontype, ix, iy, iw, ih, slabel)
    return retval


def fl_set_bitmapbutton_data(pFlObject, w, h, bits):
    """
    fl_set_bitmapbutton_data(pFlObject, w, h, bits)

    @param pFlObject: object
    @type pFlObject: pointer to xfdata.FL_OBJECT
    @param w: width in coord units
    @type w: int
    @param h: height in coord units
    @type h: int
    @param bits: bitmap data
    @type bits: str of ubytes

    @status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_bitmapbutton_data = library.cfuncproto(
        library.load_so_libforms(), "fl_set_bitmapbutton_data",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_int,
        cty.POINTER(cty.c_ubyte)],
        """void fl_set_bitmapbutton_data(FL_OBJECT * ob, int w, int h,
           unsigned char * bits)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    iw = library.convert_to_int(w)
    ih = library.convert_to_int(h)
    pbits = cty.cast(bits, cty.POINTER(cty.c_ubyte))
    library.keep_elem_refs(pFlObject, w, h, bits, iw, ih, pbits)
    _fl_set_bitmapbutton_data(pFlObject, iw, ih, pbits)


def fl_add_pixmapbutton(buttontype, x, y, w, h, label):
    """Adds a pixmapbutton object.

    @param buttontype: type of button to be added. Values (from xfdata
        module) i.e. FL_NORMAL_BUTTON, FL_PUSH_BUTTON, FL_RADIO_BUTTON,
        FL_HIDDEN_BUTTON, FL_TOUCH_BUTTON, FL_INOUT_BUTTON,
        FL_RETURN_BUTTON, FL_HIDDEN_RET_BUTTON, FL_MENU_BUTTON,
        FL_TOGGLE_BUTTON
    @type buttontype: int
    @param x: horizontal position (upper-left corner)
    @type x: int
    @param y: vertical position (upper-left corner)
    @type y: int
    @param w: width in coord units
    @type w: int
    @param h: height in coord units
    @type h: int
    @param label: text label of button
    @type label: str

    @returns: button object created (pFlObject)
    @rtype: pointer to xfdata.FL_OBJECT

    @example: btnobj = fl_add_roundbutton(xfdata.FL_TOGGLE_BUTTON, 145,
        199, 120, 30, "MyButton")

    @status: Tested + Doc + Demo = OK

    """
    _fl_add_pixmapbutton = library.cfuncproto(
        library.load_so_libforms(), "fl_add_pixmapbutton",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord, \
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_pixmapbutton(int type, FL_Coord x,
           FL_Coord y, FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(buttontype, xfdata.BUTTONTYPE_list)
    ibuttontype = library.convert_to_int(buttontype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(buttontype, x, y, w, h, label, ibuttontype, ix, \
                           iy, iw, ih, slabel)
    retval = _fl_add_pixmapbutton(ibuttontype, ix, iy, iw, ih, slabel)
    return retval


def fl_set_pixmapbutton_focus_outline(pFlObject, yes):
    """
    fl_set_pixmapbutton_focus_outline(pFlObject, yes)

    @param pFlObject: button object
    @type pFlObject: pointer to xfdata.FL_OBJECT
    @param yes: ?
    @type yes: int

    @status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_pixmapbutton_focus_outline = library.cfuncproto(
        library.load_so_libforms(), "fl_set_pixmapbutton_focus_outline",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_pixmapbutton_focus_outline(FL_OBJECT * ob, int yes)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    iyes = library.convert_to_int(yes)
    library.keep_elem_refs(pFlObject, yes, iyes)
    _fl_set_pixmapbutton_focus_outline(pFlObject, iyes)


fl_set_pixmapbutton_data = flbitmap.fl_set_pixmap_data
fl_set_pixmapbutton_show_focus = fl_set_pixmapbutton_focus_outline



def fl_set_pixmapbutton_focus_data(pFlObject, bits):
    """
    fl_set_pixmapbutton_focus_data(pFlObject, bits)

    @param pFlObject: button object
    @type pFlObject: pointer to xfdata.FL_OBJECT
    @param bits: pixmap data
    @type bits: str

    @status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_pixmapbutton_focus_data = library.cfuncproto(
        library.load_so_libforms(), "fl_set_pixmapbutton_focus_data",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(xfdata.STRING)],
        """void fl_set_pixmapbutton_focus_data(FL_OBJECT * ob,
           char * * bits)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    pbits = cty.cast(bits, cty.POINTER(xfdata.STRING))
    library.keep_elem_refs(pFlObject, bits, pbits)
    _fl_set_pixmapbutton_focus_data(pFlObject, pbits)


def fl_set_pixmapbutton_focus_file(pFlObject, fname):
    """
    fl_set_pixmapbutton_focus_file(pFlObject, fname)

    @param pFlObject: button object
    @type pFlObject: pointer to xfdata.FL_OBJECT
    @param fname: filename
    @type fname: str

    @status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_pixmapbutton_focus_file = library.cfuncproto(
        library.load_so_libforms(), "fl_set_pixmapbutton_focus_file",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.STRING],
        """void fl_set_pixmapbutton_focus_file(FL_OBJECT * ob,
           const char * fname)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    sfname = library.convert_to_string(fname)
    library.keep_elem_refs(pFlObject, fname, sfname)
    _fl_set_pixmapbutton_focus_file(pFlObject, sfname)


def fl_set_pixmapbutton_focus_pixmap(pFlObject, pix, mask):
    """
    fl_set_pixmapbutton_focus_pixmap(pFlObject, pix, mask)

    @param pFlObject: pointer to object
    @type pFlObject: pointer to xfdata.FL_OBJECT
    @param pix: pixmap id
    @type pix: long_pos
    @param mask: pixmap id
    @type mask: long_pos

    @status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_pixmapbutton_focus_pixmap = library.cfuncproto(
        library.load_so_libforms(), "fl_set_pixmapbutton_focus_pixmap",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.Pixmap, xfdata.Pixmap],
        """void fl_set_pixmapbutton_focus_pixmap(FL_OBJECT * ob,
           Pixmap id, Pixmap mask)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    ulpix = library.convert_to_ulong(pix)
    ulmask = library.convert_to_ulong(mask)
    library.keep_elem_refs(pFlObject, pix, mask, ulpix, ulmask)
    _fl_set_pixmapbutton_focus_pixmap(pFlObject, ulpix, ulmask)


def fl_get_button(pFlObject):
    """Returns the state value of the button.

    @param pFlObject: button object
    @type pFlObject: pointer to xfdata.FL_OBJECT

    @returns: num.
    @rtype: int

    @example: btnstate = fl_get_button(btnobj)

    @status: Tested + Doc + Demo = OK

    """
    _fl_get_button = library.cfuncproto(
        library.load_so_libforms(), "fl_get_button",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_button(FL_OBJECT * ob)""")
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_button(pFlObject)
    return retval


def fl_set_button(pFlObject, yn):
    """Sets the button state (not pushed/pushed).

    @param pFlObject: button object
    @type pFlObject: pointer to xfdata.FL_OBJECT
    @param yn: state of button to be set. Values 0 (if not pushed) or
        1 (if pushed)
    @type yn: int

    @example: fl_set_button(btnobj, 1)

    @status: Tested + Doc + Demo = OK

    """
    _fl_set_button = library.cfuncproto(
        library.load_so_libforms(), "fl_set_button",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_button(FL_OBJECT * ob, int pushed)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    iyn = library.convert_to_int(yn)
    library.keep_elem_refs(pFlObject, yn, iyn)
    _fl_set_button(pFlObject, yn)


def fl_get_button_numb(pFlObject):
    """Returns the number of the last used mouse button. fl_mouse_button()
    function will also return the mouse number.

    @param pFlObject: button object
    @type pFlObject: pointer to xfdata.FL_OBJECT

    @returns: num.
    @rtype: int

    @example: lastused = fl_get_button_numb(pobj)

    @status: Tested + Doc + NoDemo = OK

    """
    _fl_get_button_numb = library.cfuncproto(
        library.load_so_libforms(), "fl_get_button_numb",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_button_numb(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_button_numb(pFlObject)
    return retval


fl_set_button_shortcut = flbasic.fl_set_object_shortcut


def fl_create_generic_button(btnclass, buttontype, x, y, w, h, label):
    """Creates a generic button object.

    @param btnclass: value of a new button class
    @type btnclass: int
    @param buttontype: type of button to be created. Values (from xfdata
        module) FL_NORMAL_BUTTON, FL_PUSH_BUTTON, FL_RADIO_BUTTON,
        FL_HIDDEN_BUTTON, FL_TOUCH_BUTTON, FL_INOUT_BUTTON, FL_RETURN_BUTTON,
        FL_HIDDEN_RET_BUTTON, FL_MENU_BUTTON, FL_TOGGLE_BUTTON
    @type buttontype: int
    @param x: horizontal position (upper-left corner)
    @type x: int
    @param y: vertical position (upper-left corner)
    @type y: int
    @param w: width in coord units
    @type w: int
    @param h: height in coord units
    @type h: int
    @param label: text label of button
    @type label: str

    @returns: button object created (pFlObject)
    @rtype: pointer to xfdata.FL_OBJECT

    @example: newbtnobj = fl_add_roundbutton(1001, xfdata.FL_TOGGLE_BUTTON, 145,
        199, 120, 30, "MyButton")

    @status: Tested + Doc + NoDemo = OK

    """
    _fl_create_generic_button = library.cfuncproto(
        library.load_so_libforms(), "fl_create_generic_button",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_create_generic_button(int objclass, int type,
           FL_Coord x, FL_Coord y, FL_Coord w, FL_Coord h,
           const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(buttontype, xfdata.BUTTONTYPE_list)
    ibtnclass = library.convert_to_int(btnclass)
    ibuttontype = library.convert_to_int(buttontype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(btnclass, buttontype, x, y, w, h, label, ibtnclass,
                   ibuttontype, ix, iy, iw, ih, slabel)
    retval = _fl_create_generic_button(ibtnclass, ibuttontype, ix, iy,
                                       iw, ih, slabel)
    return retval


def fl_add_button_class(btnclass, py_DrawButton, py_CleanupButton):
    """Associates a button class with a drawing function.

    @param btnclass: value of a new button class
    @type btnclass: int
    @param py_DrawButton: python function to draw button, no return
    @type py_DrawButton: __ funcname (pFlObject) __
    @param py_CleanupButton: python function to cleanup button, no return
    @type py_CleanupButton: __ funcname (pButtonSpec) __

    @example: def drawbtn(pobj):
    @example: |->| ...
    @example: def cleanbtn(buttonspec):
    @example: |->|
    @example: fl_add_button_class(1001, drawbtn, cleanbtn)

    @status: Tested + Doc + NoDemo = OK

    """
    #FL_DrawButton = cty.CFUNCTYPE(None, cty.POINTER(xfdata.FL_OBJECT))
    #FL_CleanupButton = cty.CFUNCTYPE(None, cty.POINTER(xfdata.FL_BUTTON_SPEC))
    _fl_add_button_class = library.cfuncproto(
        library.load_so_libforms(), "fl_add_button_class",
        None, [cty.c_int, xfdata.FL_DrawButton, xfdata.FL_CleanupButton],
        """void fl_add_button_class(int bclass, FL_DrawButton drawit,
           FL_CleanupButton cleanup)""")
    library.check_if_initialized()
    ibtnclass = library.convert_to_int(btnclass)
    c_DrawButton = xfdata.FL_DrawButton(py_DrawButton)
    c_CleanupButton = xfdata.FL_CleanupButton(py_CleanupButton)
    library.keep_cfunc_refs(c_DrawButton, py_DrawButton, c_CleanupButton,
                            py_CleanupButton)
    library.keep_elem_refs(btnclass, ibtnclass)
    _fl_add_button_class(ibtnclass, c_DrawButton, c_CleanupButton)


def fl_set_button_mouse_buttons(pFlObject, buttons):
    """Sets up to which mouse buttons the button object will react.

    @param pFlObject: button object
    @type pFlObject: pointer to xfdata.FL_OBJECT
    @param buttons: value of mouse buttons to be set (bitwise OR of
         the numbers 1 for the left mouse button, 2 for the middle,
         4 for the right mouse button, 8 for moving the scroll wheel
         up "button" and 16 for scrolling down "button".)
    @type buttons: int_pos

    @example: fl_set_button_mouse_buttons(pobj, 8|16)

    @status: Tested + Doc + NoDemo = OK

    """
    _fl_set_button_mouse_buttons = library.cfuncproto(
        library.load_so_libforms(), "fl_set_button_mouse_buttons",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_uint],
        """void fl_set_button_mouse_buttons(FL_OBJECT * ob,
           unsigned int buttons)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    ibuttons = library.convert_to_int(buttons)
    library.keep_elem_refs(pFlObject, buttons, ibuttons)
    _fl_set_button_mouse_buttons(pFlObject, ibuttons)


def fl_get_button_mouse_buttons(pFlObject):
    """Returns a value indicating which mouse buttons the button object will
    react to (bitwise OR of the numbers 1 for the left mouse button, 2 for
    the middle, 4 for the right mouse button, 8 for moving the scroll wheel
    up "button" and 16 for scrolling down "button".)

    @param pFlObject: pointer to button object
    @type pFlObject: pointer to xfdata.FL_OBJECT

    @returns: buttons value
    @rtype: int_pos

    @example: moubtn = fl_get_button_mouse_buttons(pobj)

    @attention: API change from XForms - upstream was
        fl_get_button_mouse_buttons(pFlObject, buttons)

    @status: Tested + Doc + NoDemo = OK

    """
    _fl_get_button_mouse_buttons = library.cfuncproto(
        library.load_so_libforms(), "fl_get_button_mouse_buttons",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_uint)],
        """void fl_get_button_mouse_buttons(FL_OBJECT * ob,
           unsigned int * buttons)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    buttons, pbuttons = library.make_uint_and_pointer()
    library.keep_elem_refs(pFlObject, buttons, pbuttons)
    _fl_get_button_mouse_buttons(pFlObject, pbuttons)
    return buttons.value

