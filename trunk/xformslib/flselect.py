#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage select flobjects.
"""

#    Copyright (C) 2009, 2010  Luca Lazzaroni "LukenShiro"
#    e-mail: <lukenshiro@ngi.it>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, version 2.1 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU LGPL along with this
#    program. If not, see <http://www.gnu.org/licenses/>.
#
#    See CREDITS file to read acknowledgements and thanks to XForms,
#    ctypes and other developers.

# originally generated by 'h2xml+gccxml' and 'xml2py'
# then heavily reordered and reworked

# ############################################# #
# Interface to XForms shared flobject libraries #
# ############################################# #


import ctypes as cty
from xformslib import library
from xformslib import xfdata


#####################
# forms.h (select.h)
#####################

# Select flobject types

# fl_create_select function placeholder (internal)


def fl_add_select(selecttype, xpos, ypos, width, height, label):
    """fl_add_select(selecttype, xpos, ypos, width, height, label)
    -> ptr_flobject
    
    Adds a select (new generation choice) flobject to the form. It is a
    rather simple flobject that allows the user to pick alternatives from a
    linear list that pops up when he clicks on the flobject. It remembers the
    last selected item, which is also shown on top of the select flobject. It
    internally uses a popup.

    Parameters
    ----------
        selecttype : int
            type of select to be added. Values (from xfdata.py) 
            FL_NORMAL_SELECT, FL_MENU_SELECT, FL_DROPLIST_SELECT
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            text label of select

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject added

    Examples
    --------
        >>> selobj = fl_add_select(xfdata.FL_NORMAL_SELECT,
                120, 140, 250, 250, "MySelect")

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_add_select = library.cfuncproto(
        library.load_so_libforms(), "fl_add_select",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_select(int p1, FL_Coord p2, FL_Coord p3,
           FL_Coord p4, FL_Coord p5, const char * p6)""")
    library.check_if_initialized()
    library.checkfatal_allowed_value_in_list(selecttype, \
            xfdata.SELECTTYPE_list)
    i_selecttype = library.convert_to_intc(selecttype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_stringc(label)
    library.keep_elem_refs(selecttype, xpos, ypos, width, height, label, \
            i_selecttype, i_xpos, i_ypos, i_width, i_height, s_label)
    retval = _fl_add_select(i_selecttype, i_xpos, i_ypos, i_width, \
            i_height, s_label)
    return retval


def fl_clear_select(ptr_flobject):
    """fl_clear_select(ptr_flobject) -> result
    
    Removes all items from a select flobject. If you used
    fl_set_select_popup() to set a popup for the select flobject then
    that popup gets deleted automatically on calling fl_clear_select().
    The values automatically associated with items when calling
    fl_add_select_items() will start at 0 again.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject

    Returns
    -------
        result : int
            0 on success, or -1 (on failure)

    Examples
    --------
        >>> fl_clear_select(selobj)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_clear_select = library.cfuncproto(
        library.load_so_libforms(), "fl_clear_select",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_clear_select(FL_OBJECT * p1)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    _fl_clear_select(ptr_flobject)


def fl_add_select_items(ptr_flobject, entryitemstxt):
    """fl_add_select_items(ptr_flobject, entryitemstxt) -> ptr_flpopupentry

    Adds one or more items to a select flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject
        entryitemstxt : str
            text of the entry to be added and in-text special sequences with
            or without not separated additional arguments (if needed). Text
            may contain | to separate entries and newline characters which
            allows to create entries that span more than a single line. Only
            some special sequences are allowed: %x, %u, %f, %E, %L, %d, %h,
            %S, %s, %% (other combinations do not make sense here).
            *todo* to be verified!

    Returns
    -------
        ptr_flpopupentry : pointer to xfdata.FL_POPUP_ENTRY
            popup entry , or None (on failure)

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: HalfTested + NoDoc + Demo = NOT OK (sequence param.)
        See: Special sequences in entry text documentation.

    """
    _fl_add_select_items = library.cfuncproto(
        library.load_so_libforms(), "fl_add_select_items",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        xfdata.STRING],
        """FL_POPUP_ENTRY * fl_add_select_items(FL_OBJECT * p1,
           const char * p2, ...)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    s_entryitemstxt = library.convert_to_stringc(entryitemstxt)
    library.keep_elem_refs(ptr_flobject, entryitemstxt, s_entryitemstxt)
    retval = _fl_add_select_items(ptr_flobject, s_entryitemstxt)
    return retval
#      entryitems_txtlst : list_of_str_and_any_type
#        list representing the text of the entry to be added and in-text
#        special sequences with or without separate or not separated additional
#        arguments (if needed). Text may contain | to separate entries and
#        newline characters which allows to create entries that span more than
#        a single line. Only some special sequences are allowed: %x, %u, %f,
#        %E, %L, %d, %h, %S, %s, %% (other combinations do not make sense here).
#        Up to 20 additional separated arguments are supported in xforms-python
#        currently, only.
#   _fl_add_select_items = library.cfuncproto(
#        library.load_so_libforms(), "fl_add_select_items",
#        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
#        xfdata.STRING, cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p,
#        cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p,
#        cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p,
#        cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p, cty.c_void_p,
#        cty.c_void_p],
#        """FL_POPUP_ENTRY * fl_add_select_items(FL_OBJECT * p1,
#           const char * p2, ...)""")
#    library.check_if_initialized()
#    library.verify_flobjectptr_type(ptr_flobject)
#    # first str + 20 additional args max
#    tmpentryitems_txtlst, finalentryitems_txtlst = \
#        library.create_argslist_for_entrytxt(entryitems_txtlst, 21)
#    library.keep_elem_refs(ptr_flobject, entryitems_txtlst, \
#           tmpentryitems_txtlst, finalentryitems_txtlst)
#    retval = _fl_add_select_items(ptr_flobject, *finalentryitems_txtlst)
#    return retval


def fl_insert_select_items(ptr_flobject, ptr_flpopupentry, entryitemstxt):
    """fl_insert_select_items(ptr_flobject, ptr_flpopupentry, entryitemstxt)
    -> ptr_flpopupentry
    
    Inserts new items somewhere in the middle of a list of already
    existing items.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject
        ptr_flpopupentry : pointer to xfdata.FL_POPUP_ENTRY
            popup entry. If it is 'None' new items are inserted at the very
            start.
        entryitemstxt : str
            text of the entry to be added and in-text special sequences with
            or without not separated additional arguments (if needed). Text
            may contain | to separate entries and newline characters which
            allows to create entries that span more than a single line. Only
            some special sequences are allowed: %x, %u, %f, %E, %L, %d, %h,
            %S, %s (other combinations do not make sense here).

    Returns
    -------
        ptr_flpopupentry : pointer to xfdata.FL_POPUP_ENTRY
            popup entry, or None (on failure)

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: HalfTested + NoDoc + Demo = NOT OK (special sequence)
        See: Special sequences in entry text documentation.

    """
    _fl_insert_select_items = library.cfuncproto(
        library.load_so_libforms(), "fl_insert_select_items",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.FL_POPUP_ENTRY), xfdata.STRING],
        """FL_POPUP_ENTRY * fl_insert_select_items(FL_OBJECT * p1,
           FL_POPUP_ENTRY * p2, const char * p3, ...)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.verify_flpopupentryptr_type(ptr_flpopupentry)
    s_entryitemstxt = library.convert_to_stringc(entryitemstxt)
    library.keep_elem_refs(ptr_flobject, ptr_flpopupentry, entryitemstxt, \
            s_entryitemstxt)
    retval = _fl_insert_select_items(ptr_flobject, ptr_flpopupentry, \
            s_entryitemstxt)
    return retval


def fl_replace_select_item(ptr_flobject, ptr_flpopupentry, entryitemstxt):
    """fl_replace_select_item(ptr_flobject, ptr_flpopupentry, entryitemstxt)
    -> ptr_flpopupentry
    
    Replaces an existing item of a select flobject with another.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject
        ptr_flpopupentry : pointer to xfdata.FL_POPUP_ENTRY
            popup entry
        entryitemstxt : str
            text of the entry to be added and in-text special sequences with
            or without not separated additional arguments (if needed). Text
            may contain | to separate entries and newline characters which
            allows to create entries that span more than a single line. Only
            some special sequences are allowed: %x, %u, %f, %E, %L, %d, %h,
            %S, %s (other combinations do not make sense here).

    Returns
    -------
        ptr_flpopupentry : pointer to xfdata.FL_POPUP_ENTRY
            popup entry, or None (on failure)

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK
        See: Special sequences in entry text documentation.

    """
    _fl_replace_select_item = library.cfuncproto(
        library.load_so_libforms(), "fl_replace_select_item",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.FL_POPUP_ENTRY), xfdata.STRING],
        """FL_POPUP_ENTRY * fl_replace_select_item(FL_OBJECT * p1,
            FL_POPUP_ENTRY * p2, const char * p3, ...)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.verify_flpopupentryptr_type(ptr_flpopupentry)
    s_entryitemstxt = library.convert_to_stringc(entryitemstxt)
    library.keep_elem_refs(ptr_flobject, ptr_flpopupentry, entryitemstxt, \
            s_entryitemstxt)
    retval = _fl_replace_select_item(ptr_flobject, ptr_flpopupentry, \
            s_entryitemstxt)
    return retval


def fl_delete_select_item(ptr_flobject, ptr_flpopupentry):
    """fl_delete_select_item(ptr_flobject, ptr_flpopupentry) -> result
    
    Deletes an item of a select flobject. The values associated with items
    will not change due to removing an item.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject
        ptr_flpopupentry : pointer to xfdata.FL_POPUP_ENTRY
            popup entry

    Returns
    -------
        result : int
            0 on success, or -1 (on failure)

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_delete_select_item = library.cfuncproto(
        library.load_so_libforms(), "fl_delete_select_item",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.FL_POPUP_ENTRY)],
        """int fl_delete_select_item(FL_OBJECT * p1, FL_POPUP_ENTRY * p2)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject, ptr_flpopupentry)
    retval = _fl_delete_select_item(ptr_flobject, ptr_flpopupentry)
    return retval


def fl_set_select_items(ptr_flobject, ptr_flpopupitem):
    """fl_set_select_items(ptr_flobject, ptr_flpopupitem) -> numitems
    
    (Re)populates a select flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject
        ptr_flpopupitem : pointer to xfdata.FL_POPUP_ITEM
            popup item to be set. It can be prepared passing a dict (whose
            keys are corresponding to xfdata.FL_POPUP_ITEM's members) to
            xfstruct.make_flpopupitem function.

    Returns
    -------
        numitems : long
            number of items, or -1 (on failure)

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_select_items = library.cfuncproto(
        library.load_so_libforms(), "fl_set_select_items",
        cty.c_long, [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.FL_POPUP_ITEM)],
        """long int fl_set_select_items(FL_OBJECT * p1,
           FL_POPUP_ITEM * p2)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.verify_flpopupitemptr_type(ptr_flpopupitem)
    library.keep_elem_refs(ptr_flobject, ptr_flpopupitem)
    retval = _fl_set_select_items(ptr_flobject, ptr_flpopupitem)
    return retval


def fl_get_select_popup(ptr_flobject):
    """fl_get_select_popup(ptr_flobject) -> ptr_flpopup
    
    Finds out which item of a select flobject is currently selected.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject

    Returns
    -------
        ptr_flpopup : pointer to xfdata.FL_POPUP
            popup class instance

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_get_select_popup = library.cfuncproto(
        library.load_so_libforms(), "fl_get_select_popup",
        cty.POINTER(xfdata.FL_POPUP), [cty.POINTER(xfdata.FL_OBJECT)],
        """FL_POPUP * fl_get_select_popup(FL_OBJECT * p1)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_select_popup(ptr_flobject)
    return retval


def fl_set_select_popup(ptr_flobject, ptr_flpopup):
    """fl_set_select_popup(ptr_flobject, ptr_flpopup) -> result
    
    Creates a popup directly and then associates it with the select
    flobject. Supplied popup may not contain any entries other than
    those of type xfdata.FL_POPUP_NORMAL, and, of course, the popup
    cannot be a sub-popup of another popup).

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject
        ptr_flpopup : pointer to xfdata.FL_POPUP
            popup class instance

    Returns
    -------
        result : int
            1 on success, or -1 (on failure)

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_select_popup = library.cfuncproto(
        library.load_so_libforms(), "fl_set_select_popup",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.FL_POPUP)],
        """int fl_set_select_popup(FL_OBJECT * p1, FL_POPUP * p2)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.verify_flpopupptr_type(ptr_flpopup)
    library.keep_elem_refs(ptr_flobject, ptr_flpopup)
    retval = _fl_set_select_popup(ptr_flobject, ptr_flpopup)
    return retval


def fl_get_select_item(ptr_flobject):
    """fl_get_select_item(ptr_flobject) -> ptr_flpopupreturn
    
    Finds out currently selected item of a select flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject

    Returns
    -------
        ptr_flpopupreturn : pointer to xfdata.FL_POPUP_RETURN
            popup return

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_get_select_item = library.cfuncproto(
        library.load_so_libforms(), "fl_get_select_item",
        cty.POINTER(xfdata.FL_POPUP_RETURN), [cty.POINTER(xfdata.FL_OBJECT)],
        """FL_POPUP_RETURN * fl_get_select_item(FL_OBJECT * p1)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_select_item(ptr_flobject)
    return retval


def fl_set_select_item(ptr_flobject, ptr_flpopupentry):
    """fl_set_select_item(ptr_flobject, ptr_flpopupentry) -> ptr_flpopupreturn
    
    Defines a new item of a select flobject as currently selected.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject
        ptr_flpopupentry : pointer to xfdata.FL_POPUP_ENTRY
            popup entry class instance

    Returns
    -------
        ptr_flpopupreturn : pointer to xfdata.FL_POPUP_RETURN
            popup return

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: HalfTested + NoDoc + Demo = NOT OK (FL_POPUP_ENTRY not
        prepared)

    """
    _fl_set_select_item = library.cfuncproto(
        library.load_so_libforms(), "fl_set_select_item",
        cty.POINTER(xfdata.FL_POPUP_RETURN), [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.FL_POPUP_ENTRY)],
        """FL_POPUP_RETURN * fl_set_select_item(FL_OBJECT * p1,
           FL_POPUP_ENTRY * p2)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.verify_flpopupentryptr_type(ptr_flpopupentry)
    library.keep_elem_refs(ptr_flobject, ptr_flpopupentry)
    retval = _fl_set_select_item(ptr_flobject, ptr_flpopupentry)
    return retval


def fl_get_select_item_by_value(ptr_flobject, itemval):
    """fl_get_select_item_by_value(ptr_flobject, itemval) -> ptr_flpopupentry
    
    Finds the first item of select flobject with the value associated with
    the item.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject
        itemval : long
            value of the select item.

    Returns
    -------
        ptr_flpopupentry : pointer to xfdata.FL_POPUP_ENTRY
            popup entry class instance, or None (on failure)

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_select_item_by_value = library.cfuncproto(
        library.load_so_libforms(), "fl_get_select_item_by_value",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        cty.c_long],
        """FL_POPUP_ENTRY * fl_get_select_item_by_value(FL_OBJECT * p1,
           long int p2)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    l_itemval = library.convert_to_longc(itemval)
    library.keep_elem_refs(ptr_flobject, itemval, l_itemval)
    retval = _fl_get_select_item_by_value(ptr_flobject, l_itemval)
    return retval


def fl_get_select_item_by_label(ptr_flobject, label):
    """fl_get_select_item_by_label(ptr_flobject, label) -> ptr_flpopupentry
    
    Finds out an item of select flobject who has a certain label as
    displayed for the item in the popup.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject
        label : str
            label of the item.

    Returns
    -------
        ptr_flpopupentry : pointer to xfdata.FL_POPUP_ENTRY
            popup entry class instance

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_get_select_item_by_label = library.cfuncproto(
        library.load_so_libforms(), "fl_get_select_item_by_label",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        xfdata.STRING],
        """FL_POPUP_ENTRY * fl_get_select_item_by_label(FL_OBJECT * p1,
           const char * p2)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    s_label = library.convert_to_stringc(label)
    library.keep_elem_refs(ptr_flobject, label, s_label)
    retval = _fl_get_select_item_by_label(ptr_flobject, s_label)
    return retval


def fl_get_select_item_by_text(ptr_flobject, txtstr):
    """fl_get_select_item_by_text(ptr_flobject, txtstr) -> ptr_flpopupentry
    
    Finds out an item of select flobject who has supplied text
    (that might be the same as the label text in simple cases).

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject
        txtstr : str
            text of the item.

    Returns
    -------
        ptr_flpopupentry : pointer to xfdata.FL_POPUP_ENTRY
            popup entry class instance

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_select_item_by_text = library.cfuncproto(
        library.load_so_libforms(), "fl_get_select_item_by_text",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_OBJECT),
        xfdata.STRING],
        """FL_POPUP_ENTRY * fl_get_select_item_by_text(FL_OBJECT * p1,
           const char * p2)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    s_txtstr = library.convert_to_stringc(txtstr)
    library.keep_elem_refs(ptr_flobject, txtstr, s_txtstr)
    retval = _fl_get_select_item_by_text(ptr_flobject, s_txtstr)
    return retval


def fl_get_select_text_color(ptr_flobject):
    """fl_get_select_text_color(ptr_flobject) -> colr
    
    Finds out the color of the text of the currenty selected item
    on top of the flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject

    Returns
    -------
        colr : long_pos
            color

    Examples
    --------
        >>> txtcolr = fl_get_select_text_color(selobj)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_select_text_color = library.cfuncproto(
        library.load_so_libforms(), "fl_get_select_text_color",
        xfdata.FL_COLOR, [cty.POINTER(xfdata.FL_OBJECT)],
        """FL_COLOR fl_get_select_text_color(FL_OBJECT * p1)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_select_text_color(ptr_flobject)
    return retval


def fl_set_select_text_color(ptr_flobject, colr):
    """fl_set_select_text_color(ptr_flobject, colr) -> oldcolr
    
    Defines the color of the text of the currenty selected item on
    top of the flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject
        colr : long_pos
            color value

    Returns
    -------
        oldcolr : long_pos
            previous color

    Examples
    --------
        >>> oldcol = fl_set_select_text_color(selobj, xfdata.FL_BLUE)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_select_text_color = library.cfuncproto(
        library.load_so_libforms(), "fl_set_select_text_color",
        xfdata.FL_COLOR, [cty.POINTER(xfdata.FL_OBJECT), xfdata.FL_COLOR],
        """FL_COLOR fl_set_select_text_color(FL_OBJECT * p1, FL_COLOR p2)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.checknonfatal_allowed_value_in_list(colr, xfdata.COLOR_list)
    ul_colr = library.convert_to_FL_COLOR(colr)
    library.keep_elem_refs(ptr_flobject, colr, ul_colr)
    retval = _fl_set_select_text_color(ptr_flobject, ul_colr)
    return retval


def fl_get_select_text_font(ptr_flobject):
    """fl_get_select_text_font(ptr_flobject) -> result, style, size
    
    Finds out the font style and size used for the text of a select
    flobject.

    Parameters
    ----------
      ptr_flobject : pointer to xfdata.FL_OBJECT
        select flobject

    Returns
    -------
        result : int
            0 or -1 (on failure)
        style : int
            font style
        size : int
            font size

    Examples
    --------
        >>> rslt, style, size = fl_get_select_text_font(selobj)

    API_diversion
    -------------
        API changed from XForms, upstream is
        fl_get_select_text_font(ptr_flobject, p2, p3)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_select_text_font = library.cfuncproto(
        library.load_so_libforms(), "fl_get_select_text_font",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int),
        cty.POINTER(cty.c_int)],
        """int fl_get_select_text_font(FL_OBJECT * p1, int * p2, int * p3)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_style, ptr_style = library.make_intc_and_pointer()
    i_size, ptr_size = library.make_intc_and_pointer()
    library.keep_elem_refs(ptr_flobject, i_style, ptr_style, i_size, ptr_size)
    retval = _fl_get_select_text_font(ptr_flobject, ptr_style, ptr_size)
    return retval, i_style.value, i_size.value


def fl_set_select_text_font(ptr_flobject, style, size):
    """fl_set_select_text_font(ptr_flobject, style, size) -> result
    
    Defines the font style and size used for the text of a select
    flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject
        style : int
            text style. Values (from xfdata.py) FL_NORMAL_STYLE,
            FL_BOLD_STYLE, FL_ITALIC_STYLE, FL_BOLDITALIC_STYLE,
            FL_FIXED_STYLE, FL_FIXEDBOLD_STYLE, FL_FIXEDITALIC_STYLE,
            FL_FIXEDBOLDITALIC_STYLE, FL_TIMES_STYLE, FL_TIMESBOLD_STYLE,
            FL_TIMESITALIC_STYLE, FL_TIMESBOLDITALIC_STYLE, FL_MISC_STYLE,
            FL_MISCBOLD_STYLE, FL_MISCITALIC_STYLE, FL_SYMBOL_STYLE,
            FL_SHADOW_STYLE, FL_ENGRAVED_STYLE, FL_EMBOSSED_STYLE
        size : int
            text size. Values (from xfdata.py) FL_TINY_SIZE, FL_SMALL_SIZE,
            FL_NORMAL_SIZE, FL_MEDIUM_SIZE, FL_LARGE_SIZE, FL_HUGE_SIZE,
            FL_DEFAULT_SIZE

    Returns
    -------
        result : int
            0, or -1 (on failure)

    Examples
    --------
        >>> rslt = fl_set_select_text_font(selobj,
                xfdata.FL_TIMESBOLD_STYLE, xfdata.FL_LARGE_SIZE)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_select_text_font = library.cfuncproto(
        library.load_so_libforms(), "fl_set_select_text_font",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_int],
        """int fl_set_select_text_font(FL_OBJECT * p1, int p2, int p3)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.checkfatal_allowed_value_in_list(style, xfdata.TEXTSTYLE_list)
    library.checknonfatal_allowed_value_in_list(size, xfdata.FONTSIZE_list)
    i_style = library.convert_to_intc(style)
    i_size = library.convert_to_intc(size)
    library.keep_elem_refs(ptr_flobject, style, size, i_style, i_size)
    retval = _fl_set_select_text_font(ptr_flobject, i_style, i_size)
    return retval


def fl_get_select_text_align(ptr_flobject):
    """fl_get_select_text_align(ptr_flobject) -> align
    
    Finds out the alignment of the text with the currently selected
    item on top of the select flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject

    Returns
    -------
        align : int
            alignment of text

    Examples
    --------
        >>> algn = fl_get_select_text_align(selobj)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_select_text_align = library.cfuncproto(
        library.load_so_libforms(), "fl_get_select_text_align",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_select_text_align(FL_OBJECT * p1)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_select_text_align(ptr_flobject)
    return retval


def fl_set_select_text_align(ptr_flobject, align):
    """fl_set_select_text_align(ptr_flobject, align) -> oldalign
    
    Defines the alignment of the text with the currently selected item on
    top of the select flobject. The xfdata.FL_ALIGN_INSIDE flag should be
    set with align since the text always will be drawn withing the
    boundaries of the flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject
        align : int
            alignment of text. Values (from xfdata.py) FL_ALIGN_CENTER,
            FL_ALIGN_TOP, FL_ALIGN_BOTTOM, FL_ALIGN_LEFT, FL_ALIGN_RIGHT,
            FL_ALIGN_LEFT_TOP, FL_ALIGN_RIGHT_TOP, FL_ALIGN_LEFT_BOTTOM,
            FL_ALIGN_RIGHT_BOTTOM, FL_ALIGN_INSIDE, FL_ALIGN_VERT. Bitwise
            OR with FL_ALIGN_INSIDE is allowed.

    Returns
    -------
        oldalign : int
            old setting of alignment, or -1 (on errors)

    Examples
    --------
        >>> oldalgn = fl_set_select_text_align(selobj, xfdata.FL_ALIGN_TOP)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_select_text_align = library.cfuncproto(
        library.load_so_libforms(), "fl_set_select_text_align",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """int fl_set_select_text_align(FL_OBJECT * p1, int p2)""")
    library.check_if_initialized()
    library.checkfatal_allowed_value_in_list(align, xfdata.ALIGN_list)
    library.verify_flobjectptr_type(ptr_flobject)
    i_align = library.convert_to_intc(align)
    library.keep_elem_refs(ptr_flobject, align, i_align)
    retval = _fl_set_select_text_align(ptr_flobject, i_align)
    return retval


def fl_set_select_policy(ptr_flobject, policy):
    """fl_set_select_policy(ptr_flobject, policy) -> oldpol
    
    Defines a policy of a select flobject. By default, the popup of a
    select flobjects remains shown when the user releases the mouse
    somewhere outside the popup window (or on its title area). The
    alternative is to close the popup immediately when the user releases
    the mouse, independent of where it is.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            select flobject
        policy : int
            popup policy to be set. Values (from xfdata.py)
            FL_POPUP_NORMAL_SELECT, FL_POPUP_DRAG_SELECT

    Returns
    -------
        oldpol : int
            previous policy setting, or -1 (on error)

    Examples
    --------
        >>> fl_set_select_policy(selobj, xfdata.FL_POPUP_NORMAL_SELECT)

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_set_select_policy = library.cfuncproto(
        library.load_so_libforms(), "fl_set_select_policy",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """int fl_set_select_policy(FL_OBJECT * p1, int p2)""")
    library.check_if_initialized()
    library.checkfatal_allowed_value_in_list(policy, xfdata.POPUPPOLICY_list)
    library.verify_flobjectptr_type(ptr_flobject)
    i_policy = library.convert_to_intc(policy)
    library.keep_elem_refs(ptr_flobject, policy, i_policy)
    retval = _fl_set_select_policy(ptr_flobject, i_policy)
    return retval

