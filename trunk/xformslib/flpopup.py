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





####################
# forms.h (popupfn.h)
####################

def fl_popup_add(win, title):
    """ fl_popup_add(win, title) -> pPopup

        @param win: window
        @param title: text of title shown at the top of the popup
                      in a framed box

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_add = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_add",
        cty.POINTER(xfdata.FL_POPUP), [xfdata.Window, xfdata.STRING],
        """FL_POPUP * fl_popup_add(Window p1, const char * p2)""")
    library.check_if_initialized()
    ulwin = library.convert_to_Window(win)
    stitle = library.convert_to_string(title)
    library.keep_elem_refs(win, title, ulwin, stitle)
    retval = _fl_popup_add(ulwin, stitle)
    return retval


def fl_popup_add_entries(pPopup, entrytxt):
    """ fl_popup_add_entries(pPopup, entrytxt) -> pPopupEntry

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_add_entries = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_add_entries",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_POPUP), xfdata.STRING],
        """FL_POPUP_ENTRY * fl_popup_add_entries(FL_POPUP * p1,
           const char * p2)""")
    library.check_if_initialized()
    sentrytxt = library.convert_to_string(entrytxt)
    library.keep_elem_refs(pPopup, entrytxt, sentrytxt)
    retval = _fl_popup_add_entries(pPopup, sentrytxt)
    return retval


def fl_popup_insert_entries(pPopup, pPopupEntry, entrytxt):
    """ fl_popup_insert_entries(pPopup, pPopupEntry, entrytxt) -> pPopupEntry

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_popup_insert_entries = library.cfuncproto(
            library.load_so_libforms(), "fl_popup_insert_entries",
            cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_POPUP),
            cty.POINTER(xfdata.FL_POPUP_ENTRY), xfdata.STRING],
            """FL_POPUP_ENTRY * fl_popup_insert_entries(FL_POPUP * p1,
               FL_POPUP_ENTRY * p2, const char * p3)""")
    library.check_if_initialized()
    sentrytxt = library.convert_to_string(entrytxt)
    library.keep_elem_refs(pPopup, pPopupEntry, entrytxt, sentrytxt)
    retval = _fl_popup_insert_entries(pPopup, pPopupEntry, sentrytxt)
    return retval


def fl_popup_create(win, text, pPopupItem):
    """ fl_popup_create(win, text, pPopupItem) -> pPopup

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_popup_create = library.cfuncproto(
            library.load_so_libforms(), "fl_popup_create",
                cty.POINTER(xfdata.FL_POPUP), [xfdata.Window, xfdata.STRING,
                cty.POINTER(xfdata.FL_POPUP_ITEM)],
            """FL_POPUP * fl_popup_create(Window p1, const char * p2,
               FL_POPUP_ITEM * p3)""")
    library.check_if_initialized()
    ulwin = library.convert_to_Window(win)
    stext = library.convert_to_string(text)
    library.keep_elem_refs(win, text, pPopupItem, ulwin, stext)
    retval = _fl_popup_create(ulwin, stext, pPopupItem)
    return retval


def fl_popup_add_items(pPopup, pPopupItem):
    """ fl_popup_add_items(pPopup, pPopupItem) -> pPopupEntry

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_popup_add_items = library.cfuncproto(
            library.load_so_libforms(), "fl_popup_add_items",
                cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_POPUP),
                cty.POINTER(xfdata.FL_POPUP_ITEM)],
            """FL_POPUP_ENTRY * fl_popup_add_items(FL_POPUP * p1,
               FL_POPUP_ITEM * p2)
""")
    library.check_if_initialized()
    library.keep_elem_refs(pPopup, pPopupItem)
    retval = _fl_popup_add_items(pPopup, pPopupItem)
    return retval


def fl_popup_insert_items(pPopup, pPopupEntry, pPopupItem):
    """ fl_popup_insert_items(pPopup, pPopupEntry, pPopupItem) -> pPopupEntry

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_insert_items = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_insert_items",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_POPUP),
        cty.POINTER(xfdata.FL_POPUP_ENTRY), cty.POINTER(xfdata.FL_POPUP_ITEM)],
        """FL_POPUP_ENTRY * fl_popup_insert_items(FL_POPUP * p1,
           FL_POPUP_ENTRY * p2, FL_POPUP_ITEM * p3)""")
    library.check_if_initialized()
    library.keep_elem_refs(pPopup, pPopupEntry, pPopupItem)
    retval = _fl_popup_insert_items(pPopup, pPopupEntry, pPopupItem)
    return retval


def fl_popup_delete(pPopup):
    """ fl_popup_delete(pPopup) -> num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_delete = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_delete",
        cty.c_int, [cty.POINTER(xfdata.FL_POPUP)],
        """int fl_popup_delete(FL_POPUP * p1)""")
    library.check_if_initialized()
    library.keep_elem_refs(pPopup)
    retval = _fl_popup_delete(pPopup)
    return retval


def fl_popup_entry_delete(pPopupEntry):
    """ fl_popup_entry_delete(pPopupEntry) -> num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_delete = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_delete",
        cty.c_int, [cty.POINTER(xfdata.FL_POPUP_ENTRY)],
        """int fl_popup_entry_delete(FL_POPUP_ENTRY * p1)""")
    library.check_if_initialized()
    library.keep_elem_refs(pPopupEntry)
    retval = _fl_popup_entry_delete(pPopupEntry)
    return retval


def fl_popup_do(pPopup):
    """ fl_popup_do(pPopup) -> pPopupReturn

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_do = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_do",
        cty.POINTER(xfdata.FL_POPUP_RETURN), [cty.POINTER(xfdata.FL_POPUP)],
        """FL_POPUP_RETURN * fl_popup_do(FL_POPUP * p1)""")
    library.check_if_initialized()
    library.keep_elem_refs(pPopup)
    retval = _fl_popup_do(pPopup)
    return retval


def fl_popup_set_position(pPopup, x, y):
    """ fl_popup_set_position(pPopup, x, y)

        Sets position where the popup is supposed to appear (if never called
        the popup appears at the mouse position)

        @param pPopup: pointer to Popup
        @param x: horizontal position (upper-left corner)
        @param y: vertical position (upper-left corner)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_set_position = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_set_position",
        None, [cty.POINTER(xfdata.FL_POPUP), cty.c_int, cty.c_int],
        """void fl_popup_set_position(FL_POPUP * p1, int p2, int p3)""")
    library.check_if_initialized()
    ix = library.convert_to_int(x)
    iy = library.convert_to_int(y)
    library.keep_elem_refs(pPopup, x, y, ix, iy)
    _fl_popup_set_position(pPopup, ix, iy)


def fl_popup_get_policy(pPopup):
    """ fl_popup_get_policy(pPopup) -> num.

        @param pPopup: pointer to Popup

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_get_policy = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_get_policy",
        cty.c_int, [cty.POINTER(xfdata.FL_POPUP)],
        """int fl_popup_get_policy(FL_POPUP * p1)""")
    library.check_if_initialized()
    library.keep_elem_refs(pPopup)
    retval = _fl_popup_get_policy(pPopup)
    return retval


def fl_popup_set_policy(pPopup, policy):
    """ fl_popup_set_policy(pPopup, policy) -> num.

        Sets policy of handling the popup (i.e. does it get closed when the
        user releases the mouse button outside an active entry or not?)

        @param pPopup: pointer to Popup
        @param policy: policy to be set

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_set_policy = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_set_policy",
        cty.c_int, [cty.POINTER(xfdata.FL_POPUP), cty.c_int],
        """int fl_popup_set_policy(FL_POPUP * p1, int p2)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(policy, xfdata.POPUPPOLICY_list)
    ipolicy = library.convert_to_int(policy)
    library.keep_elem_refs(pPopup, policy, ipolicy)
    retval = _fl_popup_set_policy(pPopup, ipolicy)
    return retval


# already defined in xfdata

def fl_popup_set_callback(pPopup, py_PopupCb):
    """ fl_popup_set_callback(pPopup, py_PopupCb) -> popup callback func.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    #FL_POPUP_CB = cty.CFUNCTYPE(cty.c_int, cty.POINTER(xfdata.FL_POPUP_RETURN))
    _fl_popup_set_callback = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_set_callback",
        xfdata.FL_POPUP_CB, [cty.POINTER(xfdata.FL_POPUP), xfdata.FL_POPUP_CB],
        """FL_POPUP_CB fl_popup_set_callback(FL_POPUP * p1,
           FL_POPUP_CB p2)""")
    library.check_if_initialized()
    c_PopupCb = xfdata.FL_POPUP_CB(py_PopupCb)
    library.keep_cfunc_refs(c_PopupCb, py_PopupCb)
    library.keep_elem_refs(pPopup)
    retval = _fl_popup_set_callback(pPopup, c_PopupCb)
    return retval


def fl_popup_get_title_font(pPopup):
    """ fl_popup_get_title_font(pPopup) -> style, size

        @attention: API change from XForms - upstream was
                    fl_popup_get_title_font(pPopup, style, size)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_get_title_font = library.cfuncproto(
            library.load_so_libforms(), "fl_popup_get_title_font",
            None, [cty.POINTER(xfdata.FL_POPUP), cty.POINTER(cty.c_int),
            cty.POINTER(cty.c_int)],
            """void fl_popup_get_title_font(FL_POPUP * p1, int * p2,
               int * p3)""")
    library.check_if_initialized()
    style, pstyle = library.make_int_and_pointer()
    size, psize = library.make_int_and_pointer()
    library.keep_elem_refs(pPopup, style, size, pstyle, psize)
    _fl_popup_get_title_font(pPopup, pstyle, psize)
    return style.value, size.value


def fl_popup_set_title_font(pPopup, style, size):
    """ fl_popup_set_title_font(pPopup, style, size)

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_popup_set_title_font = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_set_title_font",
        None, [cty.POINTER(xfdata.FL_POPUP), cty.c_int, cty.c_int],
        """void fl_popup_set_title_font(FL_POPUP * p1, int p2, int p3)""")
    library.check_if_initialized()
    istyle = library.convert_to_int(style)
    isize = library.convert_to_int(size)
    library.keep_elem_refs(pPopup, style, size, istyle, isize)
    _fl_popup_set_title_font(pPopup, istyle, isize)


def fl_popup_entry_get_font(pPopup):
    """ fl_popup_entry_get_font(pPopup) -> style, size

        @attention: API change from XForms - upstream was
                    fl_popup_entry_get_font(pPopup, style, size)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_get_font = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_get_font",
        None, [cty.POINTER(xfdata.FL_POPUP), cty.POINTER(cty.c_int),
        cty.POINTER(cty.c_int)],
        """void fl_popup_entry_get_font(FL_POPUP * p1, int * p2, int * p3)""")
    library.check_if_initialized()
    style, pstyle = library.make_int_and_pointer()
    size, psize = library.make_int_and_pointer()
    library.keep_elem_refs(pPopup, style, size, pstyle, psize)
    _fl_popup_entry_get_font(pPopup, pstyle, psize)
    return style.value, size.value


def fl_popup_entry_set_font(pPopup, style, size):
    """ fl_popup_entry_set_font(pPopup, style, size)

        Sets the font of a popup entry.

        @param pPopup: pointer to Popup
        @param style: style of the popup entry
        @param size: size of the popup entry

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_popup_entry_set_font = library.cfuncproto(
            library.load_so_libforms(), "fl_popup_entry_set_font",
            None, [cty.POINTER(xfdata.FL_POPUP), cty.c_int, cty.c_int],
            """void fl_popup_entry_set_font(FL_POPUP * p1, int p2, int p3)
""")
    library.check_if_initialized()
    istyle = library.convert_to_int(style)
    isize = library.convert_to_int(size)
    library.keep_elem_refs(pPopup, style, size, istyle, isize)
    _fl_popup_entry_set_font(pPopup, istyle, isize)


def fl_popup_get_bw(pPopup):
    """ fl_popup_get_bw(pPopup) -> borderwidth

        Returns the border width of a popupfn.

        @param pPopup: pointer to popup

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_popup_get_bw = library.cfuncproto(
            library.load_so_libforms(), "fl_popup_get_bw",
            cty.c_int, [cty.POINTER(xfdata.FL_POPUP)],
            """int fl_popup_get_bw(FL_POPUP * p1)
""")
    library.check_if_initialized()
    library.keep_elem_refs(pPopup)
    retval = _fl_popup_get_bw(pPopup)
    return retval


def fl_popup_set_bw(pPopup, bw):
    """ fl_popup_set_bw(pPopup, bw) -> num.

        Sets the border width of a popupfn.

        @param pPopup: pointer to popup
        @param bw: border width value to be set

        @status: Tested + NoDoc + Demo = OK
    """

    _fl_popup_set_bw = library.cfuncproto(
            library.load_so_libforms(), "fl_popup_set_bw",
            cty.c_int, [cty.POINTER(xfdata.FL_POPUP), cty.c_int],
            """int fl_popup_set_bw(FL_POPUP * p1, int p2)
""")
    library.check_if_initialized()
    ibw = library.convert_to_int(bw)
    library.keep_elem_refs(pPopup, bw, ibw)
    retval = _fl_popup_set_bw(pPopup, ibw)
    return retval


def fl_popup_get_color(pPopup, colrpos):
    """ fl_popup_get_color(pPopup, colrpos) -> color

        @type colrpos: [num./int] from xfdata module FL_POPUP_BACKGROUND_COLOR,
                       FL_POPUP_HIGHLIGHT_COLOR, FL_POPUP_TITLE_COLOR,
                       FL_POPUP_TEXT_COLOR, FL_POPUP_HIGHLIGHT_TEXT_COLOR,
                       FL_POPUP_DISABLED_TEXT_COLOR, FL_POPUP_RADIO_COLOR

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_get_color = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_get_color",
        xfdata.FL_COLOR, [cty.POINTER(xfdata.FL_POPUP), cty.c_int],
        """FL_COLOR fl_popup_get_color(FL_POPUP * p1, int p2)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(colrpos, xfdata.POPUPCOLOR_list)
    icolrpos = library.convert_to_int(colrpos)
    library.keep_elem_refs(pPopup, colrpos, icolrpos)
    retval = _fl_popup_get_color(pPopup, icolrpos)
    return retval


def fl_popup_set_color(pPopup, colrpos, colr):
    """ fl_popup_set_color(pPopup, colrpos, colr) -> color

        @param colrpos: popup color type
        @type colrpos: [num./int] from xfdata module FL_POPUP_BACKGROUND_COLOR,
                       FL_POPUP_HIGHLIGHT_COLOR, FL_POPUP_TITLE_COLOR,
                       FL_POPUP_TEXT_COLOR, FL_POPUP_HIGHLIGHT_TEXT_COLOR,
                       FL_POPUP_DISABLED_TEXT_COLOR, FL_POPUP_RADIO_COLOR
        @param colr: color value to be set

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_set_color = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_set_color",
        xfdata.FL_COLOR, [cty.POINTER(xfdata.FL_POPUP), cty.c_int, xfdata.FL_COLOR],
        """FL_COLOR fl_popup_set_color(FL_POPUP * p1, int p2, FL_COLOR p3)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(colrpos, xfdata.POPUPCOLOR_list)
    library.check_admitted_listvalues(colrpos, xfdata.COLOR_list)
    icolrpos = library.convert_to_int(colrpos)
    ulcolr = library.convert_to_FL_COLOR(colr)
    library.keep_elem_refs(pPopup, colrpos, colr, icolrpos, ulcolr)
    retval = _fl_popup_set_color(pPopup, icolrpos, ulcolr)
    return retval


def fl_popup_set_cursor(pPopup, cursnum):
    """ fl_popup_set_cursor(pPopup, cursnum)

        Changes the cursor displayed when a popup is shown.

        @param pPopup: pointer to FL_POPUP
        @param cursnum: id of a symbolic cursor shapes' names

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_set_cursor = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_set_cursor",
        None, [cty.POINTER(xfdata.FL_POPUP), cty.c_int],
        """void fl_popup_set_cursor(FL_POPUP * p1, int p2)""")
    icursnum = library.convert_to_int(cursnum)
    library.keep_elem_refs(pPopup, cursnum, icursnum)
    _fl_popup_set_cursor(pPopup, icursnum)


def fl_popup_get_title(pPopup):
    """ fl_popup_get_title(pPopup) -> title string

        Returns the title of a popupfn.

        @param pPopup: pointer to popup

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_get_title = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_get_title",
        xfdata.STRING, [cty.POINTER(xfdata.FL_POPUP)],
        """const char * fl_popup_get_title(FL_POPUP * p1)""")
    library.check_if_initialized()
    library.keep_elem_refs(pPopup)
    retval = _fl_popup_get_title(pPopup)
    return retval


def fl_popup_set_title(pPopup, title):
    """ fl_popup_set_title(pPopup, title) -> popup

        Sets the title of a popupfn.

        @param pPopup: pointer to popup
        @param title: title of the popup

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_set_title = library.cfuncproto(
            library.load_so_libforms(), "fl_popup_set_title",
            cty.POINTER(xfdata.FL_POPUP), [cty.POINTER(xfdata.FL_POPUP), xfdata.STRING],
            """FL_POPUP * fl_popup_set_title(FL_POPUP * p1, const char * p2)""")
    library.check_if_initialized()
    stitle = library.convert_to_string(title)
    library.keep_elem_refs(pPopup, title, stitle)
    retval = _fl_popup_set_title(pPopup, stitle)
    return retval


def fl_popup_entry_set_callback(pPopupEntry, py_PopupCb):
    """ fl_popup_entry_set_callback(pPopupEntry, py_PopupCb) -> popup_callback

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_popup_entry_set_callback = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_set_callback",
        xfdata.FL_POPUP_CB, [cty.POINTER(xfdata.FL_POPUP_ENTRY),
        xfdata.FL_POPUP_CB],
        """FL_POPUP_CB fl_popup_entry_set_callback(FL_POPUP_ENTRY * p1,
           FL_POPUP_CB p2)""")
    library.check_if_initialized()
    c_PopupCb = xfdata.FL_POPUP_CB(py_PopupCb)
    library.keep_cfunc_refs(c_PopupCb, py_PopupCb)
    library.keep_elem_refs(pPopupEntry)
    retval = _fl_popup_entry_set_callback(pPopupEntry, c_PopupCb)
    return retval


def fl_popup_entry_set_enter_callback(pPopupEntry, py_PopupCb):
    """ fl_popup_entry_set_enter_callback(pPopupEntry, py_PopupCb) -> popup_callback

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_set_enter_callback = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_set_enter_callback",
        xfdata.FL_POPUP_CB, [cty.POINTER(xfdata.FL_POPUP_ENTRY),
        xfdata.FL_POPUP_CB],
        """FL_POPUP_CB fl_popup_entry_set_enter_callback(
           FL_POPUP_ENTRY * p1, FL_POPUP_CB p2)""")
    library.check_if_initialized()
    c_PopupCb = xfdata.FL_POPUP_CB(py_PopupCb)
    library.keep_cfunc_refs(c_PopupCb, py_PopupCb)
    library.keep_elem_refs(pPopupEntry)
    retval = _fl_popup_entry_set_enter_callback(pPopupEntry, c_PopupCb)
    return retval


def fl_popup_entry_set_leave_callback(pPopupEntry, py_PopupCb):
    """ fl_popup_entry_set_leave_callback(pPopupEntry, py_PopupCb) -> popup_callback

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_set_leave_callback = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_set_leave_callback",
        xfdata.FL_POPUP_CB, [cty.POINTER(xfdata.FL_POPUP_ENTRY),
        xfdata.FL_POPUP_CB],
        """FL_POPUP_CB fl_popup_entry_set_leave_callback(
           FL_POPUP_ENTRY * p1, FL_POPUP_CB p2)""")
    library.check_if_initialized()
    c_PopupCb = xfdata.FL_POPUP_CB(py_PopupCb)
    library.keep_cfunc_refs(c_PopupCb, py_PopupCb)
    library.keep_elem_refs(pPopupEntry)
    retval = _fl_popup_entry_set_leave_callback(pPopupEntry, c_PopupCb)
    return retval


def fl_popup_entry_get_state(pPopupEntry):
    """ fl_popup_entry_get_state(pPopupEntry) -> state num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_get_state = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_get_state",
        cty.c_uint, [cty.POINTER(xfdata.FL_POPUP_ENTRY)],
        """unsigned int fl_popup_entry_get_state(FL_POPUP_ENTRY * p1)""")
    library.check_if_initialized()
    library.keep_elem_refs(pPopupEntry)
    retval = _fl_popup_entry_get_state(pPopupEntry)
    return retval


def fl_popup_entry_set_state(pPopupEntry, state):
    """ fl_popup_entry_set_state(pPopupEntry, state) -> state num.

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_popup_entry_set_state = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_set_state",
        cty.c_uint, [cty.POINTER(xfdata.FL_POPUP_ENTRY), cty.c_uint],
        """unsigned int fl_popup_entry_set_state(FL_POPUP_ENTRY * p1,
           unsigned int p2)""")
    library.check_if_initialized()
    uistate = library.convert_to_uint(state)
    library.keep_elem_refs(pPopupEntry, state, uistate)
    retval = _fl_popup_entry_set_state(pPopupEntry, uistate)
    return retval


def fl_popup_entry_clear_state(pPopupEntry, state):
    """ fl_popup_entry_clear_state(pPopupEntry, state) -> state num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_clear_state = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_clear_state",
        cty.c_uint, [cty.POINTER(xfdata.FL_POPUP_ENTRY), cty.c_uint],
        """unsigned int fl_popup_entry_clear_state(FL_POPUP_ENTRY * p1,
           unsigned int p2)""")
    library.check_if_initialized()
    uistate = library.convert_to_uint(state)
    library.keep_elem_refs(pPopupEntry, state, uistate)
    retval = _fl_popup_entry_clear_state(pPopupEntry, uistate)
    return retval


def fl_popup_entry_raise_state(pPopupEntry, state):
    """ fl_popup_entry_raise_state(pPopupEntry, state) -> state num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_raise_state = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_raise_state",
        cty.c_uint, [cty.POINTER(xfdata.FL_POPUP_ENTRY), cty.c_uint],
        """unsigned int fl_popup_entry_raise_state(FL_POPUP_ENTRY * p1,
           unsigned int p2)""")
    library.check_if_initialized()
    uistate = library.convert_to_uint(state)
    library.keep_elem_refs(pPopupEntry, state, uistate)
    retval = _fl_popup_entry_raise_state(pPopupEntry, uistate)
    return retval


def fl_popup_entry_toggle_state(pPopupEntry, state):
    """ fl_popup_entry_toggle_state(pPopupEntry, state) -> num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_toggle_state = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_toggle_state",
        cty.c_uint, [cty.POINTER(xfdata.FL_POPUP_ENTRY), cty.c_uint],
        """unsigned int fl_popup_entry_toggle_state(FL_POPUP_ENTRY * p1,
           unsigned int p2)""")
    library.check_if_initialized()
    uistate = library.convert_to_uint(state)
    library.keep_elem_refs(pPopupEntry, state, uistate)
    retval = _fl_popup_entry_toggle_state(pPopupEntry, uistate)
    return retval


def fl_popup_entry_set_text(pPopupEntry, text):
    """ fl_popup_entry_set_text(p1, txtstr) -> num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_set_text = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_set_text",
        cty.c_int, [cty.POINTER(xfdata.FL_POPUP_ENTRY), xfdata.STRING],
        """int fl_popup_entry_set_text(FL_POPUP_ENTRY * p1,
           const char * p2)""")
    library.check_if_initialized()
    stext = library.convert_to_string(text)
    library.keep_elem_refs(pPopupEntry, text, stext)
    retval = _fl_popup_entry_set_text(pPopupEntry, stext)
    return retval


def fl_popup_entry_set_shortcut(pPopupEntry, textsc):
    """ fl_popup_entry_set_shortcut(pPopupEntry, textsc)

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_popup_entry_set_shortcut = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_set_shortcut",
        None, [cty.POINTER(xfdata.FL_POPUP_ENTRY), xfdata.STRING],
        """void fl_popup_entry_set_shortcut(FL_POPUP_ENTRY * p1,
           const char * p2)""")
    library.check_if_initialized()
    stextsc = library.convert_to_string(textsc)
    library.keep_elem_refs(pPopupEntry, textsc, stextsc)
    _fl_popup_entry_set_shortcut(pPopupEntry, stextsc)


def fl_popup_entry_set_value(pPopupEntry, val):
    """ fl_popup_entry_set_value(pPopupEntry, p2) -> num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_set_value = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_set_value",
        cty.c_long, [cty.POINTER(xfdata.FL_POPUP_ENTRY), cty.c_long],
        """long int fl_popup_entry_set_value(FL_POPUP_ENTRY * p1,
           long int p2)""")
    library.check_if_initialized()
    lval = library.convert_to_long(val)
    library.keep_elem_refs(pPopupEntry, val, lval)
    retval = _fl_popup_entry_set_value(pPopupEntry, lval)
    return retval


def fl_popup_entry_set_user_data(pPopupEntry, vdata):
    """ fl_popup_entry_set_user_data(pPopupEntry, vdata) -> ??

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_set_user_data = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_set_user_data",
        cty.c_void_p, [cty.POINTER(xfdata.FL_POPUP_ENTRY), cty.c_void_p],
        """void * fl_popup_entry_set_user_data(FL_POPUP_ENTRY * p1,
           void * p2)""")
    library.check_if_initialized()
    pvdata = cty.cast(vdata, cty.c_void_p)
    library.keep_elem_refs(pPopupEntry, vdata, pvdata)
    retval = _fl_popup_entry_set_user_data(pPopupEntry, pvdata)
    return retval


def fl_popup_entry_get_by_position(pPopup, numpos):
    """ fl_popup_entry_get_by_position(pPopup, numpos) -> pPopupEntry

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_get_by_position = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_get_by_position",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_POPUP), cty.c_int],
        """FL_POPUP_ENTRY * fl_popup_entry_get_by_position(FL_POPUP * p1,
           int p2)""")
    library.check_if_initialized()
    inumpos = library.convert_to_int(numpos)
    library.keep_elem_refs(pPopup, numpos, inumpos)
    retval = _fl_popup_entry_get_by_position(pPopup, inumpos)
    return retval


def fl_popup_entry_get_by_value(pPopup, val):
    """ fl_popup_entry_get_by_value(pPopup, val) -> pPopupEntry

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_get_by_value = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_get_by_value",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_POPUP), cty.c_long],
        """FL_POPUP_ENTRY * fl_popup_entry_get_by_value(FL_POPUP * p1,
           long int p2)""")
    library.check_if_initialized()
    lval = library.convert_to_long(val)
    library.keep_elem_refs(pPopup, val, lval)
    retval = _fl_popup_entry_get_by_value(pPopup, lval)
    return retval


def fl_popup_entry_get_by_user_data(pPopup, vdata):
    """ fl_popup_entry_get_by_user_data(pPopup, vdata) -> pPopupEntry

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_get_by_user_data = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_get_by_user_data",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_POPUP), cty.c_void_p],
        """FL_POPUP_ENTRY * fl_popup_entry_get_by_user_data(FL_POPUP * p1,
           void * p2)""")
    library.check_if_initialized()
    pvdata = cty.cast(vdata, cty.c_void_p)
    library.keep_elem_refs(pPopup, vdata, pvdata)
    retval = _fl_popup_entry_get_by_user_data(pPopup, pvdata)
    return retval


def fl_popup_entry_get_by_text(pPopup, text):
    """ fl_popup_entry_get_by_text(pPopup, text) -> pPopupEntry

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_get_by_text = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_get_by_text",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_POPUP),
        xfdata.STRING],
        """FL_POPUP_ENTRY * fl_popup_entry_get_by_text(FL_POPUP * p1,
           const char * p2)""")
    library.check_if_initialized()
    stext = library.convert_to_string(text)
    library.keep_elem_refs(pPopup, text, stext)
    retval = _fl_popup_entry_get_by_text(pPopup, stext)
    return retval


def fl_popup_entry_get_by_label(pPopup, label):
    """ fl_popup_entry_get_by_label(pPopup, label) -> pPopupEntry

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_get_by_label = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_get_by_label",
        cty.POINTER(xfdata.FL_POPUP_ENTRY), [cty.POINTER(xfdata.FL_POPUP),
        xfdata.STRING],
        """FL_POPUP_ENTRY * fl_popup_entry_get_by_label(FL_POPUP * p1,
           const char * p2)""")
    library.check_if_initialized()
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(pPopup, label, slabel)
    retval = _fl_popup_entry_get_by_label(pPopup, slabel)
    return retval


def fl_popup_entry_get_group(pPopupEntry):
    """ fl_popup_entry_get_group(pPopupEntry) -> num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_get_group = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_get_group",
        cty.c_int, [cty.POINTER(xfdata.FL_POPUP_ENTRY)],
        """int fl_popup_entry_get_group(FL_POPUP_ENTRY * p1)""")
    library.check_if_initialized()
    library.keep_elem_refs(pPopupEntry)
    retval = _fl_popup_entry_get_group(pPopupEntry)
    return retval


def fl_popup_entry_set_group(pPopupEntry, num):
    """ fl_popup_entry_set_group(pPopupEntry, num) -> num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_set_group = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_set_group",
        cty.c_int, [cty.POINTER(xfdata.FL_POPUP_ENTRY), cty.c_int],
        """int fl_popup_entry_set_group(FL_POPUP_ENTRY * p1, int p2)""")
    library.check_if_initialized()
    inum = library.convert_to_int(num)
    library.keep_elem_refs(pPopupEntry, num, inum)
    retval = _fl_popup_entry_set_group(pPopupEntry, inum)
    return retval


def fl_popup_entry_get_subpopup(pPopupEntry):
    """ fl_popup_entry_get_subpopup(pPopupEntry) -> pPopup

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_get_subpopup = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_get_subpopup",
        cty.POINTER(xfdata.FL_POPUP), [cty.POINTER(xfdata.FL_POPUP_ENTRY)],
        """FL_POPUP * fl_popup_entry_get_subpopup(FL_POPUP_ENTRY * p1)""")
    library.check_if_initialized()
    library.keep_elem_refs(pPopupEntry)
    retval = _fl_popup_entry_get_subpopup(pPopupEntry)
    return retval


def fl_popup_entry_set_subpopup(pPopupEntry, pPopup):
    """ fl_popup_entry_set_subpopup(pPopupEntry, pPopup) -> pPopup

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_entry_set_subpopup = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_entry_set_subpopup",
        cty.POINTER(xfdata.FL_POPUP), [cty.POINTER(xfdata.FL_POPUP_ENTRY),
        cty.POINTER(xfdata.FL_POPUP)],
        """FL_POPUP * fl_popup_entry_set_subpopup(FL_POPUP_ENTRY * p1,
           FL_POPUP * p2)""")
    library.check_if_initialized()
    library.keep_elem_refs(pPopupEntry, pPopup)
    retval = _fl_popup_entry_set_subpopup(pPopupEntry, pPopup)
    return retval


def fl_popup_get_size(pPopup):
    """ fl_popup_get_size(pPopup) -> size num., width, height

        @attention: API change from XForms - upstream was
                    fl_popup_get_size(pPopup, w, h)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_get_size = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_get_size",
        cty.c_int, [cty.POINTER(xfdata.FL_POPUP), cty.POINTER(cty.c_uint),
        cty.POINTER(cty.c_uint)],
        """int fl_popup_get_size(FL_POPUP * p1, unsigned int * p2,
           unsigned int * p3)""")
    library.check_if_initialized()
    w, pw = library.make_uint_and_pointer()
    h, ph = library.make_uint_and_pointer()
    library.keep_elem_refs(pPopup, w, h, pw, ph)
    retval = _fl_popup_get_size(pPopup, pw, ph)
    return retval, w.value, h.value


def fl_popup_get_min_width(pPopup):
    """ fl_popup_get_min_width(pPopup) -> width num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_get_min_width = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_get_min_width",
        cty.c_int, [cty.POINTER(xfdata.FL_POPUP)],
        """int fl_popup_get_min_width(FL_POPUP * p1)""")
    library.check_if_initialized()
    library.keep_elem_refs(pPopup)
    retval = _fl_popup_get_min_width(pPopup)
    return retval


def fl_popup_set_min_width(pPopup, minwidth):
    """ fl_popup_set_min_width(pPopup, minwidth) -> width num.

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_popup_set_min_width = library.cfuncproto(
        library.load_so_libforms(), "fl_popup_set_min_width",
        cty.c_int, [cty.POINTER(xfdata.FL_POPUP), cty.c_int],
        """int fl_popup_set_min_width(FL_POPUP * p1, int p2)""")
    library.check_if_initialized()
    iminwidth = library.convert_to_int(minwidth)
    library.keep_elem_refs(pPopup, minwidth, iminwidth)
    retval = _fl_popup_set_min_width(pPopup, iminwidth)
    return retval


