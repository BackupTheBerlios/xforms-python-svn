#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage nmenu objects.

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


#####################
# forms.h (nmenu.h)
#####################

# Nmenu object types

# fl_create_nmenu function placeholder (internal)


def fl_add_nmenu(nmenutype, x, y, w, h, label):
    """Adds a new generation menu (nmenu) object. It heavily depends on
    popups.

    --

    :Parameters:
      `nmenutype` : type of nmenu to be. Values (from xfdata.py)
        FL_NORMAL_NMENU, FL_NORMAL_TOUCH_NMENU, FL_BUTTON_NMENU,
        FL_BUTTON_TOUCH_NMENU
      `x` : int
        horizontal position (upper-left corner)
      `y` : int
        vertical position (upper-left corner)
      `w` : int
        width in coord units
      `h` : int
        height in coord units
      `label` : str
        text label of nmenu object

    :return: nmenu object added (pFlObject)
    :rtype: pointer to xfdata.FL_OBJECT

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_add_nmenu = libr.cfuncproto(
        libr.load_so_libforms(), "fl_add_nmenu",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_nmenu(int p1, FL_Coord p2, FL_Coord p3,
           FL_Coord p4, FL_Coord p5, const char * p6)""")
    libr.check_if_initialized()
    libr.checkfatal_allowed_value_in_list(nmenutype, xfdata.NMENUTYPE_list)
    inmenutype = libr.convert_to_int(nmenutype)
    ix = libr.convert_to_FL_Coord(x)
    iy = libr.convert_to_FL_Coord(y)
    iw = libr.convert_to_FL_Coord(w)
    ih = libr.convert_to_FL_Coord(h)
    slabel = libr.convert_to_string(label)
    libr.keep_elem_refs(nmenutype, x, y, w, h, label, inmenutype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_nmenu(inmenutype, ix, iy, iw, ih, slabel)
    return retval


def fl_clear_nmenu(pFlObject):
    """Removes all items from a nmenu object at once.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object

    :return: num.
    :rtype: int

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_clear_nmenu = libr.cfuncproto(
        libr.load_so_libforms(), "fl_clear_nmenu",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_clear_nmenu(FL_OBJECT * p1)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_clear_nmenu(pFlObject)
    return retval


def fl_add_nmenu_items(pFlObject, entryitems_txtlst):
    """Adds items to an existing nmenu object.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object
      `entryitems_txtlst` : list_of_str_and_any_type
        list representing the text of the entry to be added and in-text
        special sequences with or without separate or not separated additional
        arguments (if needed). Text may contain `|` to separate entries and
        newline characters which allows to create entries that span more than
        a single line. Special sequences who are allowed are: %x, %u, %f, %E,
        %L, %m, %T or %t, %R or %r, %l, %d, %h, %S, %s. Up to 20 additional
        separated arguments are supported in xforms-python currently, only.

    :return: popup entry
    :rtype: pointer to xfdata.FL_POPUP_ENTRY

    :see: `Special sequences in entry text` documentation.

    :note: e.g. *todo*

    :status: HalfTested + NoDoc + Demo = NOT OK (sequence param.)

    """
    _fl_add_nmenu_items = libr.cfuncproto(
        libr.load_so_libforms(), "fl_add_nmenu_items",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        xfdata.STRING, cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p,
        cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p,
        cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p,
        cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p,
        cty.c_void_p],
        """FL_POPUP_ENTRY * fl_add_nmenu_items(FL_OBJECT * p1,
           const char * p2, ...)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    # first str + 20 additional args max
    tmpentryitems_txtlst, finalentryitems_txtlst = \
        libr.create_argslist_for_entrytxt(entryitems_txtlst, 21)
    libr.keep_elem_refs(pFlObject, entryitems_txtlst, tmpentryitems_txtlst, \
                        finalentryitems_txtlst)
    retval = _fl_add_nmenu_items(pFlObject, *finalentryitems_txtlst)
    return retval


def fl_insert_nmenu_items(pFlObject, pPopupEntry, entryitems_txtlst):
    """Inserts additional items in nmenu object.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object
      `pPopupEntry` : pointer to xfdata.FL_POPUP_ENTRY
        existing popup entry, after which the new items are to be inserted.
        If it's 'None', it inserts items at the very start.
      `entryitems_txtlst` : list_of_str_and_any_type
        list representing the text of the entry to be added and in-text
        special sequences with or without separate or not separated additional
        arguments (if needed). Text may contain `|` to separate entries and
        newline characters which allows to create entries that span more than
        a single line. Special sequences who are allowed are: %x, %u, %f, %E,
        %L, %m, %T or %t, %R or %r, %l, %d, %h, %S, %s. Up to 20 additional
        separated arguments are supported in xforms-python currently, only.

    :return: popup entry
    :rtype: pointer to xfdata.FL_POPUP_ENTRY

    :see: `Special sequences in entry text` documentation.

    :note: e.g. *todo*

    :status: HalfTested + NoDoc + Demo = NOT OK (special sequences)

    """
    _fl_insert_nmenu_items = libr.cfuncproto(
        libr.load_so_libforms(), "fl_insert_nmenu_items",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.FL_POPUP_ENTRY), xfdata.STRING, cty.c_void_p,
        cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p,
        cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p,
        cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p,
        cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p],
        """FL_POPUP_ENTRY * fl_insert_nmenu_items(FL_OBJECT * p1,
           FL_POPUP_ENTRY * p2, const char * p3, ...)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    # first str + 20 additional args max
    tmpentryitems_txtlst, finalentryitems_txtlst = \
        libr.create_argslist_for_entrytxt(entryitems_txtlst, 21)
    libr.keep_elem_refs(pFlObject, pPopupEntry, entryitems_txtlst, \
                        tmpentryitems_txtlst, finalentryitems_txtlst)
    retval = _fl_insert_nmenu_items(pFlObject, pPopupEntry, \
                                    *finalentryitems_txtlst)
    return retval


def fl_replace_nmenu_item(pFlObject, pPopupEntry, entryitems_txtlst):
    """Replaces an existing item of a nmenu object with another.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object
      `pPopupEntry` : pointer to xfdata.FL_POPUP_ENTRY
        old popup entry to be replaced
      `entryitems_txtlst` : list_of_str_and_any_type
        list representing the text of the entry to be added and in-text
        special sequences with or without separate or not separated additional
        arguments (if needed). Text may contain `|` to separate entries and
        newline characters which allows to create entries that span more than
        a single line. Special sequences who are allowed are: %x, %u, %f, %E,
        %L, %m, %T or %t, %R or %r, %l, %d, %h, %S, %s. Up to 20 additional
        separated arguments are supported in xforms-python currently, only.

    :return: popup entry
    :rtype: pointer to xfdata.FL_POPUP_ENTRY

    :see: `Special sequences in entry text` documentation.

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_replace_nmenu_item = libr.cfuncproto(
        libr.load_so_libforms(), "fl_replace_nmenu_item",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.FL_POPUP_ENTRY), xfdata.STRING, cty.c_void_p,
        cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p,
        cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p,
        cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p,
        cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p],
        """FL_POPUP_ENTRY * fl_replace_nmenu_item(FL_OBJECT * p1,
           FL_POPUP_ENTRY * p2, const char * p3, ...)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.verify_flpopupentryptr_type(pPopupEntry)
    # first str + 20 additional args max
    tmpentryitems_txtlst, finalentryitems_txtlst = \
        libr.create_argslist_for_entrytxt(entryitems_txtlst, 21)
    libr.keep_elem_refs(pFlObject, pPopupEntry, entryitems_txtlst, \
                        tmpentryitems_txtlst, finalentryitems_txtlst)
    retval = _fl_replace_nmenu_item(pFlObject, pPopupEntry, \
                                    *finalentryitems_txtlst)
    return retval


def fl_delete_nmenu_item(pFlObject, pPopupEntry):
    """Deletes an item from a nmenu object.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object
      `pPopupEntry` : pointer to xfdata.FL_POPUP_ENTRY
        existing popup entry to delete

    :return: num.
    :rtype: int

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_delete_nmenu_item = libr.cfuncproto(
        libr.load_so_libforms(), "fl_delete_nmenu_item",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.FL_POPUP_ENTRY)],
        """int fl_delete_nmenu_item(FL_OBJECT * p1, FL_POPUP_ENTRY * p2)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.verify_flpopupentryptr_type(pPopupEntry)
    libr.keep_elem_refs(pFlObject, pPopupEntry)
    retval = _fl_delete_nmenu_item(pFlObject, pPopupEntry)
    return retval


def fl_set_nmenu_items(pFlObject, pPopupItem):
    """Sets a popup nmenu item.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object
      `pPopupItem` : pointer to xfdata.FL_POPUP_ITEM
        popup item to be set

    :return: first nmenu item, or None (on failure)
    :rtype: pointer to xfdata.FL_POPUP_ENTRY

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_nmenu_items = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_nmenu_items",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.FL_POPUP_ITEM)],
        """FL_POPUP_ENTRY * fl_set_nmenu_items(FL_OBJECT * p1,
           FL_POPUP_ITEM * p2)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.verify_flpopupitemptr_type(pPopupItem)
    libr.keep_elem_refs(pFlObject, pPopupItem)
    retval = _fl_set_nmenu_items(pFlObject, pPopupItem)
    return retval


def fl_add_nmenu_items2(pFlObject, pPopupItem):
    """Adds items to a nmenu object (alternative).

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object
      `pPopupItem` : pointer to xfdata.FL_POPUP_ITEM
        popup item to be set. It needs to be prepared beforehand with
        libr.create_pPopupItem_from_list(..) function for single or multiple
        lists, or with libr.create_pPopupItem_from_dict(..) for a single dict.

    :return: first nmenu item, or None (on failure)
    :rtype: pointer to xfdata.FL_POPUP_ENTRY

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_add_nmenu_items2 = libr.cfuncproto(
        libr.load_so_libforms(), "fl_add_nmenu_items2",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.FL_POPUP_ITEM)],
        """FL_POPUP_ENTRY * fl_add_nmenu_items2(FL_OBJECT * obj,
           FL_POPUP_ITEM * p2)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.verify_flpopupitemptr_type(pPopupItem)
    libr.keep_elem_refs(pFlObject, pPopupItem)
    retval = _fl_add_nmenu_items2(pFlObject, pPopupItem)
    return retval


def fl_insert_nmenu_items2(pFlObject, pPopupEntry, pPopupItem):
    """Inserts items in a nmenu object (alternative).

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object
      `pPopupEntry` : pointer to xfdata.FL_POPUP_ENTRY
        existing popup entry, after which the new items are to be inserted.
        If it is 'None', it inserts items at the very start.
      `pPopupItem` : pointer to xfdata.FL_POPUP_ITEM
        popup item to be set. It needs to be prepared beforehand with
        libr.create_pPopupItem_from_list(..) function for single or multiple
        lists, or with libr.create_pPopupItem_from_dict(..) for a single dict.

    :return: first nmenu item, or None (on failure)
    :rtype: pointer to xfdata.FL_POPUP_ENTRY

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_insert_nmenu_items2 = libr.cfuncproto(
        libr.load_so_libforms(), "fl_insert_nmenu_items2",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.FL_POPUP_ENTRY), cty.POINTER(xfdata.FL_POPUP_ITEM)],
        """FL_POPUP_ENTRY * fl_insert_nmenu_items2(FL_OBJECT * obj,
           FL_POPUP_ITEM * p2, FL_POPUP_ITEM * p3)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    if not pPopupEntry:         # it's None
        pPopupEntry_alt = cty.cast(pPopupEntry, cty.POINTER(cty.c_void_p))
    else:                       # real FL_POPUP_ENTRY pointer
        pPopupEntry_alt = pPopupEntry
        libr.verify_flpopupentryptr_type(pPopupEntry_alt)
    libr.verify_flpopupitemptr_type(pPopupItem)
    libr.keep_elem_refs(pFlObject, pPopupEntry, pPopupEntry_alt, pPopupItem)
    retval = _fl_insert_nmenu_items2(pFlObject, pPopupEntry_alt, pPopupItem)
    return retval


def fl_replace_nmenu_items2(pFlObject, pPopupEntry, pPopupItem):
    """Replaces an item of a nmenu object (alternative).

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object
      `pPopupEntry` : pointer to xfdata.FL_POPUP_ENTRY
        old popup entry to be replaced
      `pPopupItem` : pointer to xfdata.FL_POPUP_ITEM
        new popup item. It needs to be prepared beforehand with
        libr.create_pPopupItem_from_list(..) function for single or multiple
        lists, or with libr.create_pPopupItem_from_dict(..) for a single dict.

    :return: first nmenu item, or None (on failure)
    :rtype: pointer to xfdata.FL_POPUP_ENTRY

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_replace_nmenu_items2 = libr.cfuncproto(
        libr.load_so_libforms(), "fl_replace_nmenu_items2",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.FL_POPUP_ENTRY), cty.POINTER(xfdata.FL_POPUP_ITEM)],
        """FL_POPUP_ENTRY * fl_replace_nmenu_items2(FL_OBJECT * obj,
           FL_POPUP_ENTRY * p2, FL_POPUP_ITEM * p3)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.verify_flpopupentryptr_type(pPopupEntry)
    libr.verify_flpopupitemptr_type(pPopupItem)
    libr.keep_elem_refs(pFlObject, pPopupEntry, pPopupItem)
    retval = _fl_replace_nmenu_items2(pFlObject, pPopupEntry, pPopupItem)
    return retval


def fl_get_nmenu_popup(pFlObject):
    """Determines which popup is associated with the nmenu object.

    --

    :Parameters:
     `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object

    :return: popup class instance (pPopup)
    :rtype: pointer to xfdata.FL_POPUP

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_nmenu_popup = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_nmenu_popup",
        cty.POINTER(xfdata.FL_POPUP), [cty.POINTER(xfdata.FL_OBJECT)],
        """FL_POPUP * fl_get_nmenu_popup(FL_OBJECT * p1)""")
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_nmenu_popup(pFlObject)
    return retval


def fl_set_nmenu_popup(pFlObject, pPopup):
    """Sets an existing popup as the nmenu's popup. The popup you associate
    with the nmenu object in this way can't be a sub-popup.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object
      `pPopup` : pointer to xfdata.FL_POPUP
        popup class instance

    :return: popup class instance
    :rtype: pointer to xfdata.FL_POPUP

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_nmenu_popup = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_nmenu_popup",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.FL_POPUP)],
        """int fl_set_nmenu_popup(FL_OBJECT * p1, FL_POPUP * p2)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.verify_flpopupptr_type(pPopup)
    libr.keep_elem_refs(pFlObject, pPopup)
    retval = _fl_set_nmenu_popup(pFlObject, pPopup)
    return retval


def fl_get_nmenu_item(pFlObject):
    """Finds out which item of a nmenu object was selected.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object

    :return: popup return class instance (pPopupReturn)), or None (if no
        selection was made the last time the nmenu object was used)
    :rtype: pointer to xfdata.FL_POPUP_RETURN

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_get_nmenu_item = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_nmenu_item",
        cty.POINTER(xfdata.FL_POPUP_RETURN), [cty.POINTER(xfdata.FL_OBJECT)],
        """FL_POPUP_RETURN * fl_get_nmenu_item(FL_OBJECT * p1)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_nmenu_item(pFlObject)
    return retval


def fl_get_nmenu_item_by_value(pFlObject, value):
    """Searches through the list of all items (including items in sub-popups)
    and returns the first one with the val associated with the item

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object
      `value` : long
        value corresponding to an item to be searched.

    :return: first item associated, or None (if none is found)
    :rtype: pointer to xfdata.FL_POPUP_ENTRY

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_get_nmenu_item_by_value = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_nmenu_item_by_value",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        cty.c_long],
        """FL_POPUP_ENTRY * fl_get_nmenu_item_by_value(FL_OBJECT * p1,
           long int p2)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    lvalue = libr.convert_to_long(value)
    libr.keep_elem_refs(pFlObject, value, lvalue)
    retval = _fl_get_nmenu_item_by_value(pFlObject, lvalue)
    return retval


def fl_get_nmenu_item_by_label(pFlObject, label):
    """Searches for a certain label as displayed for the item in the nmenu's
    popup.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object
      `label` : str
        text associated with an item.

    :return: first item associated, or None (if none is found)
    :rtype: pointer to xfdata.FL_POPUP_ENTRY

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_nmenu_item_by_label = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_nmenu_item_by_label",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        xfdata.STRING],
        """FL_POPUP_ENTRY * fl_get_nmenu_item_by_label(FL_OBJECT * p1,
           const char * p2)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    slabel = libr.convert_to_string(label)
    libr.keep_elem_refs(pFlObject, label, slabel)
    retval = _fl_get_nmenu_item_by_label(pFlObject, slabel)
    return retval


def fl_get_nmenu_item_by_text(pFlObject, text):
    """Searches for the text the item in nmenu object was created by (that
    might be the same as the label text in simple cases).

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object
      `text` : str
        text associated with an item.

    :return: first item associated, or None (if none is found)
    :rtype: pointer to xfdata.FL_POPUP_ENTRY

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_nmenu_item_by_text = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_nmenu_item_by_text",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        xfdata.STRING],
        """FL_POPUP_ENTRY * fl_get_nmenu_item_by_text(FL_OBJECT * p1,
           const char * p2)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    stext = libr.convert_to_string(text)
    libr.keep_elem_refs(pFlObject, text, stext)
    retval = _fl_get_nmenu_item_by_text(pFlObject, stext)
    return retval


def fl_set_nmenu_policy(pFlObject, policy):
    """Changes nmenu policy about closing, so that the popup also gets closed
    (without a selection) when the mouse button is clicked or released on a
    non-selectable item (giving the impression of a "pull-down" menu). By
    default, the popup is closed when an item is selected or (without a
    selection) when the user clicks somehwere outside of the popups area.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object
      `policy` : int
        under which conditions the nmenu's popup gets closed. Values (from
        xfdata.py) FL_POPUP_NORMAL_SELECT (default) or FL_POPUP_DRAG_SELECT

    :return: old policy settings, or -1 (on failure)
    :rtype: int

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_nmenu_policy = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_nmenu_policy",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """int fl_set_nmenu_policy(FL_OBJECT * p1, int p2)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.checkfatal_allowed_value_in_list(policy, xfdata.POPUPPOLICY_list)
    ipolicy = libr.convert_to_int(policy)
    libr.keep_elem_refs(pFlObject, policy, ipolicy)
    retval = _fl_set_nmenu_policy(pFlObject, ipolicy)
    return retval


def fl_set_nmenu_hl_text_color(pFlObject, colr):
    """Sets the color of label when it is in "active" state (i.e. while the
    popup is shown). In "inactive" state this is set by fl_set_object_lcol().
    By default, this color is xfdata.FL_BLACK for nmenus that are shown as a
    button while being "active", while for normal nmenus it?s the same color
    that is used items in the popup when the mouse is hovering over them.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        nmenu object
      `colr` : long_pos
        color to be set

    :return:  old color, or xfdata.FL_MAX_COLORS (on failure)
    :rtype: long_pos

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_nmenu_hl_text_color = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_nmenu_hl_text_color",
        xfdata.FL_COLOR, [cty.POINTER(xfdata.FL_OBJECT), xfdata.FL_COLOR],
        """FL_COLOR fl_set_nmenu_hl_text_color(FL_OBJECT * p1,
           FL_COLOR p2)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.checknonfatal_allowed_value_in_list(colr, xfdata.COLOR_list)
    ulcolr = libr.convert_to_FL_COLOR(colr)
    libr.keep_elem_refs(pFlObject, colr, ulcolr)
    retval = _fl_set_nmenu_hl_text_color(pFlObject, ulcolr)
    return retval
