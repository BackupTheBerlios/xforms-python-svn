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

    *****************************************************************


    @newfield example: Example, Example
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



#############################
# forms.h (cursor.h)
# Cursor defs and prototypes
#############################


def fl_set_cursor(win, cursnum):
    """Set cursor for window to provided cursor number name. Name
    is either the standard XC_ or Form defined.

    @param win: window
    @type win: long_pos
    @param cursnum: cursor number
    @type cursnum: int

    @status: Tested + NoDoc + Demo = OK
    """
    _fl_set_cursor = library.cfuncproto(
        library.load_so_libforms(), "fl_set_cursor",
        None, [xfdata.Window, cty.c_int],
        """void fl_set_cursor(Window win, int name)""")
    library.check_if_initialized()
    ulwin = library.convert_to_Window(win)
    icursnum = library.convert_to_int(cursnum)
    library.keep_elem_refs(win, cursnum, ulwin, icursnum)
    _fl_set_cursor(ulwin, icursnum)


def fl_set_cursor_color(cursnum, fgcolr, bgcolr):
    """Sets foreground and background colors for cursor.

    @param cursnum: cursor number
    @type cursnum: int
    @param fgcolr: foreground color to be set
    @type fgcolr: long_pos
    @param bgcolr: background color to be set
    @type bgcolr: long_pos

    @status: Tested + NoDoc + Demo = OK
    """
    _fl_set_cursor_color = library.cfuncproto(
        library.load_so_libforms(), "fl_set_cursor_color",
        None, [cty.c_int, xfdata.FL_COLOR, xfdata.FL_COLOR],
        """void fl_set_cursor_color(int name, FL_COLOR fg, FL_COLOR bg)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(fgcolr, xfdata.COLOR_list)
    library.check_admitted_listvalues(bgcolr, xfdata.COLOR_list)
    icursnum = library.convert_to_int(cursnum)
    ulfgcolr = library.convert_to_FL_COLOR(fgcolr)
    ulbgcolr = library.convert_to_FL_COLOR(bgcolr)
    library.keep_elem_refs(cursnum, fgcolr, bgcolr, icursnum, ulfgcolr, ulbgcolr)
    _fl_set_cursor_color(icursnum, ulfgcolr, ulbgcolr)


def fl_create_bitmap_cursor(source, maskstr, w, h, hotx, hoty):
    """ fl_create_bitmap_cursor(source, maskstr, w, h, hotx, hoty) -> num.

    @status: HalfTested + NoDoc + Demo = NOT OK (bitmap after animated problematic)
    """
    _fl_create_bitmap_cursor = library.cfuncproto(
        library.load_so_libforms(), "fl_create_bitmap_cursor",
        cty.c_int, [xfdata.STRING, xfdata.STRING, cty.c_int, cty.c_int, cty.c_int,
        cty.c_int],
        """int fl_create_bitmap_cursor(const char * source,
           const char * mask, int w, int h, int hotx, int hoty)""")
    library.check_if_initialized()
    ssource = library.convert_to_string(source)
    smaskstr = library.convert_to_string(maskstr)
    iw = library.convert_to_int(w)
    ih = library.convert_to_FL_Coord(h)
    ihotx = library.convert_to_int(hotx)
    ihoty = library.convert_to_int(hoty)
    library.keep_elem_refs(source, maskstr, w, h, hotx, hoty, ssource, smaskstr,
                   iw, ih, ihotx, ihoty)
    retval = _fl_create_bitmap_cursor(ssource, smaskstr, iw, ih, ihotx, ihoty)
    return retval


def fl_create_animated_cursor(curnums, timeout):
    """ fl_create_animated_cursor(curnums, timeout) -> num.

    @status: HalfTested + NoDoc + Demo = NOT OK (curnums data problematic)
    """
    _fl_create_animated_cursor = library.cfuncproto(
        library.load_so_libforms(), "fl_create_animated_cursor",
        cty.c_int, [cty.POINTER(cty.c_int), cty.c_int],
        """int fl_create_animated_cursor(int * cur_names, int timeout)""")
    library.check_if_initialized()
    pcurnums = cty.cast(curnums, cty.POINTER(cty.c_int))
    #print "pcurnums", pcurnums
    itimeout = library.convert_to_int(timeout)
    library.keep_elem_refs(curnums, timeout, pcurnums, itimeout)
    retval = _fl_create_animated_cursor(pcurnums, itimeout)
    return retval


def fl_get_cursor_byname(cursnum):
    """Returns cursor corresponding to number.

    @param cursnum: cursor number
    @type cursnum: int

    @returns: cursor
    @rtype: long_pos

    @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_cursor_byname = library.cfuncproto(
        library.load_so_libforms(), "fl_get_cursor_byname",
        xfdata.Cursor, [cty.c_int],
        """Cursor fl_get_cursor_byname(int name)""")
    library.check_if_initialized()
    icursnum = library.convert_to_int(cursnum)
    library.keep_elem_refs(cursnum, icursnum)
    retval = _fl_get_cursor_byname(icursnum)
    return retval


def fl_reset_cursor(win):
    """ Reset used cursor, reverting to default one.

    @param win: window

    @example: fl_reset_cursor(win0)

    @status: Tested + NoDoc + Demo = OK
    """
    fl_set_cursor(win, xfdata.FL_DEFAULT_CURSOR)

