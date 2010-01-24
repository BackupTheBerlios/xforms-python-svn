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




#####################
# forms.h (select.h)
#####################

# Select object types

# fl_create_select function placeholder (internal)


def fl_add_select(selecttype, x, y, w, h, label):
    """
        fl_add_select(selecttype, x, y, w, h, label) -> pFlObject

        Adds a select object.

        @param selecttype: type of select to be added
        @param x: horizontal position (upper-left corner)
        @param x: vertical position (upper-left corner)
        @param w: width in coord units
        @param h: height in coord units
        @param label: text label of select

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_add_select = library.cfuncproto(
        library.load_so_libforms(), "fl_add_select",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_select(int p1, FL_Coord p2, FL_Coord p3,
           FL_Coord p4, FL_Coord p5, const char * p6)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(selecttype, xfdata.SELECTTYPE_list)
    iselecttype = library.convert_to_int(selecttype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(selecttype, x, y, w, h, label, iselecttype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_select(iselecttype, ix, iy, iw, ih, slabel)
    return retval


def fl_clear_select(pFlObject):
    """
        fl_clear_select(pFlObject)

        @param pFlObject: pointer to select object

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_clear_select = library.cfuncproto(
            library.load_so_libforms(), "fl_clear_select",
            cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
            """int fl_clear_select(FL_OBJECT * p1)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    _fl_clear_select(pFlObject)


def fl_add_select_items(pFlObject, itemstr):
    """
        fl_add_select_items(pFlObject, itemstr) -> pPopupEntry

        @status: HalfTested + NoDoc + Demo = NOT OK (sequence param.)
    """

    _fl_add_select_items = library.cfuncproto(
            library.load_so_libforms(), "fl_add_select_items",
            cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
            xfdata.STRING],
            """FL_POPUP_ENTRY * fl_add_select_items(FL_OBJECT * p1,
               const char * p2)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    sitemstr = library.convert_to_string(itemstr)
    library.keep_elem_refs(pFlObject, itemstr, sitemstr)
    retval = _fl_add_select_items(pFlObject, sitemstr)
    return retval


def fl_insert_select_items(pFlObject, pPopupEntry, itemstr):
    """
        fl_insert_select_items(pFlObject, pPopupEntry, itemstr) -> pPopupEntry

        @param itemstr: text of the item (among special sequences only %S is
           supported

        @status: HalfTested + NoDoc + Demo = NOT OK (special sequence)
    """

    _fl_insert_select_items = library.cfuncproto(
            library.load_so_libforms(), "fl_insert_select_items",
            cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
            cty.POINTER(xfdata.FL_POPUP_ENTRY), xfdata.STRING],
            """FL_POPUP_ENTRY * fl_insert_select_items(FL_OBJECT * p1,
               FL_POPUP_ENTRY * p2, const char * p3)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    sitemstr = library.convert_to_string(itemstr)
    library.keep_elem_refs(pFlObject, pPopupEntry, itemstr, sitemstr)
    retval = _fl_insert_select_items(pFlObject, pPopupEntry, sitemstr)
    return retval


def fl_replace_select_item(pFlObject, pPopupEntry, itemstr):
    """
        fl_replace_select_item(pFlObject, pPopupEntry, itemstr) -> pPopupEntry

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_replace_select_item = library.cfuncproto(
            library.load_so_libforms(), "fl_replace_select_item",
            cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
            cty.POINTER(xfdata.FL_POPUP_ENTRY), xfdata.STRING],
            """FL_POPUP_ENTRY * fl_replace_select_item(FL_OBJECT * p1,
               FL_POPUP_ENTRY * p2, const char * p3)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    sitemstr = library.convert_to_string(itemstr)
    library.keep_elem_refs(pFlObject, pPopupEntry, itemstr, sitemstr)
    retval = _fl_replace_select_item(pFlObject, pPopupEntry, sitemstr)
    return retval


def fl_delete_select_item(pFlObject, pPopupEntry):
    """
        fl_delete_select_item(pFlObject, pPopupEntry) -> num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_delete_select_item = library.cfuncproto(
            library.load_so_libforms(), "fl_delete_select_item",
            cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(xfdata.FL_POPUP_ENTRY)],
            """int fl_delete_select_item(FL_OBJECT * p1, FL_POPUP_ENTRY * p2)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject, pPopupEntry)
    retval = _fl_delete_select_item(pFlObject, pPopupEntry)
    return retval


def fl_set_select_items(pFlObject, pPopupItem):
    """
        fl_set_select_items(pFlObject, pPopupItem) -> num.

        (Re)populates a select object xfdata.

        @param pFlObject: pointer to select object
        @param pPopupItem: pointer to FL_POPUP_ITEM class instance (array of it)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_set_select_items = library.cfuncproto(
        library.load_so_libforms(), "fl_set_select_items",
        cty.c_long, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(xfdata.FL_POPUP_ITEM)],
        """long int fl_set_select_items(FL_OBJECT * p1,
           FL_POPUP_ITEM * p2)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject, pPopupItem)
    retval = _fl_set_select_items(pFlObject, pPopupItem)
    return retval


def fl_get_select_popup(pFlObject):
    """
        fl_get_select_popup(pFlObject) -> pPopup

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_get_select_popup = library.cfuncproto(
        library.load_so_libforms(), "fl_get_select_popup",
        cty.POINTER(xfdata.FL_POPUP), [cty.POINTER(xfdata.FL_OBJECT)],
        """FL_POPUP * fl_get_select_popup(FL_OBJECT * p1)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_select_popup(pFlObject)
    return retval


def fl_set_select_popup(pFlObject, pPopup):
    """
        fl_set_select_popup(pFlObject, pPopup) -> num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_set_select_popup = library.cfuncproto(
        library.load_so_libforms(), "fl_set_select_popup",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(xfdata.FL_POPUP)],
        """int fl_set_select_popup(FL_OBJECT * p1, FL_POPUP * p2)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject, pPopup)
    retval = _fl_set_select_popup(pFlObject, pPopup)
    return retval


def fl_get_select_item(pFlObject):
    """
        fl_get_select_item(pFlObject) -> pPopupReturn

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_get_select_item = library.cfuncproto(
        library.load_so_libforms(), "fl_get_select_item",
        cty.POINTER(xfdata.FL_POPUP_RETURN), [cty.POINTER(xfdata.FL_OBJECT)],
        """FL_POPUP_RETURN * fl_get_select_item(FL_OBJECT * p1)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_select_item(pFlObject)
    return retval


def fl_set_select_item(pFlObject, pPopupEntry):
    """
        fl_set_select_item(pFlObject, pPopupEntry) -> pPopupReturn

        Set a new item as currently selected.

        @param pFlObject: pointer to select object
        @param pPopupEntry: pointer to FL_POPUP_ENTRY class instance

        @status: HalfTested + NoDoc + Demo = NOT OK (FL_POPUP_ENTRY not prepared)
    """
    _fl_set_select_item = library.cfuncproto(
        library.load_so_libforms(), "fl_set_select_item",
        cty.POINTER(xfdata.FL_POPUP_RETURN), [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.FL_POPUP_ENTRY)],
        """FL_POPUP_RETURN * fl_set_select_item(FL_OBJECT * p1,
           FL_POPUP_ENTRY * p2)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject, pPopupEntry)
    retval = _fl_set_select_item(pFlObject, pPopupEntry)
    return retval


def fl_get_select_item_by_value(pFlObject, value):
    """
        fl_get_select_item_by_value(pFlObject, value) -> pPopupEntry

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_select_item_by_value = library.cfuncproto(
        library.load_so_libforms(), "fl_get_select_item_by_value",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        cty.c_long],
        """FL_POPUP_ENTRY * fl_get_select_item_by_value(FL_OBJECT * p1,
           long int p2)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    lvalue = library.convert_to_long(value)
    library.keep_elem_refs(pFlObject, value, lvalue)
    retval = _fl_get_select_item_by_value(pFlObject, lvalue)
    return retval


def fl_get_select_item_by_label(pFlObject, label):
    """
        fl_get_select_item_by_label(pFlObject, label) -> pPopupEntry

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_get_select_item_by_label = library.cfuncproto(
        library.load_so_libforms(), "fl_get_select_item_by_label",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        xfdata.STRING],
        """FL_POPUP_ENTRY * fl_get_select_item_by_label(FL_OBJECT * p1,
           const char * p2)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(pFlObject, label, slabel)
    retval = _fl_get_select_item_by_label(pFlObject, slabel)
    return retval


def fl_get_select_item_by_text(pFlObject, txtstr):
    """
        fl_get_select_item_by_text(pFlObject, txtstr) -> pPopupEntry

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_select_item_by_text = library.cfuncproto(
        library.load_so_libforms(), "fl_get_select_item_by_text",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        xfdata.STRING],
        """FL_POPUP_ENTRY * fl_get_select_item_by_text(FL_OBJECT * p1,
           const char * p2)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    stxtstr = library.convert_to_string(txtstr)
    library.keep_elem_refs(pFlObject, txtstr, stxtstr)
    retval = _fl_get_select_item_by_text(pFlObject, stxtstr)
    return retval


def fl_get_select_text_color(pFlObject):
    """
        fl_get_select_text_color(pFlObject) -> color

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_select_text_color = library.cfuncproto(
        library.load_so_libforms(), "fl_get_select_text_color",
        xfdata.FL_COLOR, [cty.POINTER(xfdata.FL_OBJECT)],
        """FL_COLOR fl_get_select_text_color(FL_OBJECT * p1)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_select_text_color(pFlObject)
    return retval


def fl_set_select_text_color(pFlObject, colr):
    """
        fl_set_select_text_color(pFlObject, colr) -> color

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_set_select_text_color = library.cfuncproto(
        library.load_so_libforms(), "fl_set_select_text_color",
        xfdata.FL_COLOR, [cty.POINTER(xfdata.FL_OBJECT), xfdata.FL_COLOR],
        """FL_COLOR fl_set_select_text_color(FL_OBJECT * p1, FL_COLOR p2)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.check_admitted_listvalues(colr, xfdata.COLOR_list)
    ulcolr = library.convert_to_FL_COLOR(colr)
    library.keep_elem_refs(pFlObject, colr, ulcolr)
    retval = _fl_set_select_text_color(pFlObject, ulcolr)
    return retval


def fl_get_select_text_font(pFlObject):
    """
        fl_get_select_text_font(pFlObject) -> num, num1, num2

        @attention: API change from XForms - upstream was
           fl_get_select_text_font(pFlObject, p2, p3)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_get_select_text_font = library.cfuncproto(
            library.load_so_libforms(), "fl_get_select_text_font",
            cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int),
            cty.POINTER(cty.c_int)],
            """int fl_get_select_text_font(FL_OBJECT * p1, int * p2, int * p3)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    num1, pnum1 = library.make_int_and_pointer()
    num2, pnum2 = library.make_int_and_pointer()
    library.keep_elem_refs(pFlObject, num1, num2, pnum1, pnum2)
    retval = _fl_get_select_text_font(pFlObject, pnum2, pnum2)
    return retval, num1.value, num2.value


def fl_set_select_text_font(pFlObject, p2, p3):
    """
        fl_set_select_text_font(pFlObject, p2, p3) -> font num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_set_select_text_font = library.cfuncproto(
            library.load_so_libforms(), "fl_set_select_text_font",
            cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_int],
            """int fl_set_select_text_font(FL_OBJECT * p1, int p2, int p3)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    ip2 = library.convert_to_int(p2)
    ip3 = library.convert_to_int(p3)
    library.keep_elem_refs(pFlObject, p2, p3, ip2, ip3)
    retval = _fl_set_select_text_font(pFlObject, ip2, ip3)
    return retval


def fl_get_select_text_align(pFlObject):
    """
        fl_get_select_text_align(pFlObject) -> num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_get_select_text_align = library.cfuncproto(
            library.load_so_libforms(), "fl_get_select_text_align",
            cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
            """int fl_get_select_text_align(FL_OBJECT * p1)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_select_text_align(pFlObject)
    return retval


def fl_set_select_text_align(pFlObject, p2):
    """
        fl_set_select_text_align(pFlObject, p2) -> num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_set_select_text_align = library.cfuncproto(
            library.load_so_libforms(), "fl_set_select_text_align",
            cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
            """int fl_set_select_text_align(FL_OBJECT * p1, int p2)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    ip2 = library.convert_to_int(p2)
    library.keep_elem_refs(pFlObject, p2, ip2)
    retval = _fl_set_select_text_align(pFlObject, ip2)
    return retval


def fl_set_select_policy(pFlObject, num):
    """
        fl_set_select_policy(pFlObject, num) -> num.

        @status: Tested + NoDoc + Demo = OK
    """

    _fl_set_select_policy = library.cfuncproto(
            library.load_so_libforms(), "fl_set_select_policy",
            cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
            """int fl_set_select_policy(FL_OBJECT * p1, int p2)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    inum = library.convert_to_int(num)
    library.keep_elem_refs(pFlObject, num, inum)
    retval = _fl_set_select_policy(pFlObject, inum)
    return retval


