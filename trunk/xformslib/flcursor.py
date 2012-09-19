#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" xforms-python's functions to manage cursor flobjects.
"""

#    Copyright (C) 2009, 2010, 2011, 2012  Luca Lazzaroni "LukenShiro"
#    e-mail: <lukenshiro@ngi.it>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, version 2.1 of the License,
#    or (at your option) any later version.
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

# ########################################### #
# Interface to XForms shared-object libraries #
# ########################################### #


import ctypes as cty
from xformslib import library
from xformslib import xfdata


#############################
# forms.h (cursor.h)
# Cursor defs and prototypes
#############################


def fl_set_cursor(win, cursornum):
    """fl_set_cursor(win, cursornum)

    Defines cursor for window to a specific cursor number.

    Parameters
    ----------
        win : long_pos
            window
        cursornum : int
            cursor id (either the standard XC_* or Form-defined)

    Examples
    --------
        >>> fl_set_cursor(win0, xfdata.FL_CROSSHAIR_CURSOR)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_set_cursor = library.cfuncproto(
        library.load_so_libforms(), "fl_set_cursor",
        None, [xfdata.Window, cty.c_int],
        """void fl_set_cursor(Window win, int name)""")
    library.check_if_flinitialized()
    ul_win = library.convert_to_Window(win)
    i_cursornum = library.convert_to_intc(cursornum)
    library.keep_elem_refs(win, cursornum, ul_win, i_cursornum)
    _fl_set_cursor(ul_win, i_cursornum)


def fl_set_cursor_color(cursornum, fgcolr, bgcolr):
    """fl_set_cursor_color(cursornum, fgcolr, bgcolr)

    Defines foreground and background colors of a cursor.

    Parameters
    ----------
        cursornum : int
            cursor id
        fgcolr : long_pos
            foreground color to be set
        bgcolr : long_pos
            background color to be set

    Examples
    --------
        >>> fl_set_cursor_color(xfdata.FL_CROSSHAIR_CURSOR, xfdata.FL_WHITE,
                xfdata.FL_ORANGE)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_set_cursor_color = library.cfuncproto(
        library.load_so_libforms(), "fl_set_cursor_color",
        None, [cty.c_int, xfdata.FL_COLOR, xfdata.FL_COLOR],
        """void fl_set_cursor_color(int name, FL_COLOR fg, FL_COLOR bg)""")
    library.check_if_flinitialized()
    #library.checknonfatal_allowed_value_in_list(fgcolr, xfdata.COLOR_list)
    #library.checknonfatal_allowed_value_in_list(bgcolr, xfdata.COLOR_list)
    i_cursornum = library.convert_to_intc(cursornum)
    ul_fgcolr = library.convert_to_FL_COLOR(fgcolr)
    ul_bgcolr = library.convert_to_FL_COLOR(bgcolr)
    library.keep_elem_refs(cursornum, fgcolr, bgcolr, i_cursornum, \
            ul_fgcolr, ul_bgcolr)
    _fl_set_cursor_color(i_cursornum, ul_fgcolr, ul_bgcolr)


def fl_create_bitmap_cursor(source, maskstr, width, height, hotx, hoty):
    """fl_create_bitmap_cursor(source, maskstr, width, height, hotx, hoty)
    -> cursornum

    Creates a bitmap cursor, using cursors other than those defined by
    the standard cursor font.

    Parameters
    ----------
        source : str of ubytes
            bitmap to be used as cursor.
        maskstr : str of ubytes
            bitmap defining the shape of the cursor. The pixels set to 1
            define which source pixels are displayed. If it is empty ("") all
            bits in source are displayed.
        width : int
            width of cursor
        height : int
            height of cursor
        hotx : int
            horizontal hotspot of the cursor (relative to the source origin)
        hoty : int
            vertical hotspot of the cursor (relative to the source origin)

    Returns
    -------
        cursornum : int
            cursor id

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_create_bitmap_cursor = library.cfuncproto(
        library.load_so_libforms(), "fl_create_bitmap_cursor",
        cty.c_int, [xfdata.STRING, xfdata.STRING, cty.c_int, cty.c_int,
        cty.c_int, cty.c_int],
        """int fl_create_bitmap_cursor(const char * source,
           const char * mask, int w, int h, int hotx, int hoty)""")
    library.check_if_flinitialized()
    s_source = library.convert_to_stringc(source)
    if not maskstr:    # if it is empty
        s_maskstr = cty.cast(maskstr, cty.c_void_p)
    else:
        s_maskstr = library.convert_to_stringc(maskstr)
    i_width = library.convert_to_intc(width)
    i_height = library.convert_to_FL_Coord(height)
    i_hotx = library.convert_to_intc(hotx)
    i_hoty = library.convert_to_intc(hoty)
    library.keep_elem_refs(source, maskstr, width, height, hotx, hoty, \
            s_source, s_maskstr, i_width, i_height, i_hotx, i_hoty)
    retval = _fl_create_bitmap_cursor(s_source, s_maskstr, i_width, \
            i_height, i_hotx, i_hoty)
    return retval


def fl_create_animated_cursor(curseries, timeout):
    """fl_create_animated_cursor(curseries, timeout) -> cursornum

    Creates an animated series of cursors, that change after timeout
    is expired (several cursors are displayed one after another). Internally
    animated cursor works by utilizing the timeout callback, this means that
    if the application blocks (thus the main loop has no chance of servicing
    the timeouts), the animation will stop.

    Parameters
    ----------
        curseries : list of int
            sequence of cursor ids, either X standard cursors or cursor
            numbers returned by fl_create_bitmap_cursor(), terminated by -1.
        timeout : int
            time after which the cursor is changed, replacing by the next in
            sequence. An interval about 150 msec is a good value for typical
            uses.

    Returns
    -------
        cursornum : int
            cursor id

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_create_animated_cursor = library.cfuncproto(
        library.load_so_libforms(), "fl_create_animated_cursor",
        cty.c_int, [cty.POINTER(cty.c_int), cty.c_int],
        """int fl_create_animated_cursor(int * cur_names, int timeout)""")
    library.check_if_flinitialized()
    ptr_curseries = library.convert_to_ptr_intc(curseries)
    #print("pcurnums", pcurnums)
    i_timeout = library.convert_to_intc(timeout)
    library.keep_elem_refs(curseries, timeout, ptr_curseries, i_timeout)
    retval = _fl_create_animated_cursor(ptr_curseries, i_timeout)
    return retval


def fl_get_cursor_byname(cursornum):
    """fl_get_cursor_byname(cursornum) -> cursor

    Finds out cursor corresponding to its number (cursor id).

    Parameters
    ----------
        cursornum : int
            cursor id

    Returns
    -------
        cursor : long_pos
            cursor

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = OK

    """
    _fl_get_cursor_byname = library.cfuncproto(
        library.load_so_libforms(), "fl_get_cursor_byname",
        xfdata.Cursor, [cty.c_int],
        """Cursor fl_get_cursor_byname(int name)""")
    library.check_if_flinitialized()
    i_cursornum = library.convert_to_intc(cursornum)
    library.keep_elem_refs(cursornum, i_cursornum)
    retval = _fl_get_cursor_byname(i_cursornum)
    return retval


def fl_reset_cursor(win):
    """fl_reset_cursor(win)

    Resets used cursor, reverting to default one.

    Parameters
    ----------
        win : long_pos
            window

    Examples
    --------
        >> fl_reset_cursor(win0)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    fl_set_cursor(win, xfdata.FL_DEFAULT_CURSOR)

