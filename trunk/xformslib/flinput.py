#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage input flobjects.
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
from xformslib import flbasic


####################
# forms.h (input.h)
####################

# Routines

# fl_create_input function placeholder (internal)


def fl_add_input(inputtype, xpos, ypos, width, height, label):
    """fl_add_input(inputtype, xpos, ypos, width, height, label)
    -> ptr_flobject
    
    Adds an input flobject.

    Parameters
    ----------
        inputtype : int
            type of input to be added. Values (from xfdata.py)
            FL_NORMAL_INPUT, FL_FLOAT_INPUT, FL_INT_INPUT,
            FL_DATE_INPUT, FL_MULTILINE_INPUT, FL_HIDDEN_INPUT,
            FL_SECRET_INPUT
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            text label of input

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            flobject created

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Tested + Doc + Demo = OK

    """
    _fl_add_input = library.cfuncproto(
        library.load_so_libforms(), "fl_add_input",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_input(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.checkfatal_allowed_value_in_list(inputtype, xfdata.INPUTTYPE_list)
    i_inputtype = library.convert_to_intc(inputtype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_stringc(label)
    library.keep_elem_refs(inputtype, xpos, ypos, width, height, label, \
            i_inputtype, i_xpos, i_ypos, i_width, i_height, s_label)
    retval = _fl_add_input(i_inputtype, i_xpos, i_ypos, i_width, i_height, \
            s_label)
    return retval


def fl_set_input(ptr_flobject, text):
    """fl_set_input(ptr_flobject, text)
    
    Defines the particular input string, with no checks for validity.
    An empty string can be used to clear an input field.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject
        text : str
            input text

    Examples
    --------
        >>> fl_set_input(inpobj, "some text")

    Notes
    -----
        Status: Tested + Doc + Demo = OK

    """
    _fl_set_input = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.STRING],
        """void fl_set_input(FL_OBJECT * ob, const char * str)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    s_text = library.convert_to_stringc(text)
    library.keep_elem_refs(ptr_flobject, text, s_text)
    _fl_set_input(ptr_flobject, s_text)


# fl_set_input_return function placeholder (internal)


def fl_set_input_color(ptr_flobject, txtcolr, curscolr):
    """fl_set_input_color(ptr_flobject, txtcolr, curscolr)
    
    Defines text and cursor colors to be used in input flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject
        txtcolr : long_pos
            XForms colormap index as color for text
        curscolr : long_pos
            XForms colormap index as color for cursor

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_color = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input_color",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.FL_COLOR,
        xfdata.FL_COLOR],
        """void fl_set_input_color(FL_OBJECT * ob, FL_COLOR textcol,
           FL_COLOR curscol)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.checkfatal_allowed_value_in_list(txtcolr, xfdata.COLOR_list)
    library.checkfatal_allowed_value_in_list(curscolr, xfdata.COLOR_list)
    ul_txtcolr = library.convert_to_FL_COLOR(txtcolr)
    ul_curscolr = library.convert_to_FL_COLOR(curscolr)
    library.keep_elem_refs(ptr_flobject, txtcolr, curscolr, ul_txtcolr, \
            ul_curscolr)
    _fl_set_input_color(ptr_flobject, ul_txtcolr, ul_curscolr)


def fl_get_input_color(ptr_flobject):
    """fl_get_input_color(ptr_flobject) -> txtcolr, curscolr
    
    Finds out current color for text and cursor of an input flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject

    Returns
    -------
        txtcolr : long_pos
            XForms colormap index as color for text
        curscolr : long_pos
            XForms colormap index as color for cursor

    Examples
    --------
        >>> *todo*

    API_diversion
    ----------
        API changed from XForms, upstream is
        fl_get_input_color(ptr_flobject, textcolr, curscolr)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_input_color = library.cfuncproto(
        library.load_so_libforms(), "fl_get_input_color",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(xfdata.FL_COLOR),
        cty.POINTER(xfdata.FL_COLOR)],
        """void fl_get_input_color(FL_OBJECT * ob, FL_COLOR * textcol,
           FL_COLOR * curscol)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    ul_txtcolr, ptr_txtcolr = library.make_FL_COLOR_and_pointer()
    ul_curscolr, ptr_curscolr = library.make_FL_COLOR_and_pointer()
    library.keep_elem_refs(ptr_flobject, ul_txtcolr, ul_curscolr)
    _fl_get_input_color(ptr_flobject, ptr_txtcolr, ptr_curscolr)
    return ul_txtcolr.value, ul_curscolr.value


def fl_set_input_scroll(ptr_flobject, yesno):
    """fl_set_input_scroll(ptr_flobject, yesno)
    
    Turn on or off scrolling for an input field (for both multiline and
    single line input field).

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject
        yesno : int
            flag to enable/disable scrolling. Values 0 (disabled) or 1
            (enabled)

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_scroll = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input_scroll",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_input_scroll(FL_OBJECT * ob, int yes)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_yesno = library.convert_to_intc(yesno)
    library.keep_elem_refs(ptr_flobject, yesno, i_yesno)
    _fl_set_input_scroll(ptr_flobject, i_yesno)


def fl_set_input_cursorpos(ptr_flobject, xpos, ypos):
    """fl_set_input_cursorpos(ptr_flobject, xpos, ypos)
    
    Moves the cursor within the input field.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject
        xpos : int
            horizontal cursor position in characters
        ypos : int
            vertical cursor position in lines

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_input_cursorpos = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input_cursorpos",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_int],
        """void fl_set_input_cursorpos(FL_OBJECT * ob, int xpos, int ypos)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_xpos = library.convert_to_intc(xpos)
    i_ypos = library.convert_to_intc(ypos)
    library.keep_elem_refs(ptr_flobject, xpos, ypos, i_xpos, i_ypos)
    _fl_set_input_cursorpos(ptr_flobject, i_xpos, i_ypos)


def fl_set_input_selected(ptr_flobject, yesno):
    """fl_set_input_selected(ptr_flobject, yesno)
    
    Selects or deselects the current input. It places the cursor
    at the end of the string when selected.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject
        yesno : int
            flag to deselect/select input. Values 0 (deselected) or 1
            (selected)

    Examples
    --------
        >>> fl_set_input_selected(inpobj, 1)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_selected = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input_selected",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_input_selected(FL_OBJECT * ob, int yes)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_yesno = library.convert_to_intc(yesno)
    library.keep_elem_refs(ptr_flobject, yesno, i_yesno)
    _fl_set_input_selected(ptr_flobject, i_yesno)


def fl_set_input_selected_range(ptr_flobject, beginchar, endchar):
    """fl_set_input_selected_range(ptr_flobject, beginchar, endchar)
    
    Selects or deselects the current input of part of it. When begin is
    0 and end is the last character number, all input is selected. It
    places the cursor at the beginning of selected string.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject
        beginchar : int
            starting value in characters
        endchar : int
            ending value in characters

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_input_selected_range = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input_selected_range",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_int],
        """void fl_set_input_selected_range(FL_OBJECT * ob,
           int begin, int end)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_beginchar = library.convert_to_intc(beginchar)
    i_endchar = library.convert_to_intc(endchar)
    library.keep_elem_refs(ptr_flobject, beginchar, endchar, i_beginchar, \
            i_endchar)
    _fl_set_input_selected_range(ptr_flobject, i_beginchar, i_endchar)


def fl_get_input_selected_range(ptr_flobject):
    """fl_get_input_selected_range(ptr_flobject) -> selstr, beginchar, endchar
    
    Finds out the currently selected range, either selected by the
    application or by the user.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject

    Returns
    -------
        selstr : str
            selected string
        beginchar : int
            starting value of selection (in characters)
        endchar : int
            ending value of selection (in characters)

    Examples
    --------
        >>> selstr, vstart, vend = fl_get_input_selected_range(inpobj)

    API_diversion
    ----------
        API changed from XForms, upstream is
        fl_get_input_selected_range(ptr_flobject, begin, end)

    Notes
    -----
        Status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_get_input_selected_range = library.cfuncproto(
        library.load_so_libforms(), "fl_get_input_selected_range",
        xfdata.STRING, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int),
        cty.POINTER(cty.c_int)],
        """const char * fl_get_input_selected_range(FL_OBJECT * ob,
           int * begin, int * end)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_beginchar, ptr_beginchar = library.make_intc_and_pointer()
    i_endchar, ptr_endchar = library.make_intc_and_pointer()
    library.keep_elem_refs(ptr_flobject, i_beginchar, i_endchar, \
            ptr_beginchar, ptr_endchar)
    retval = _fl_get_input_selected_range(ptr_flobject, ptr_beginchar, \
            ptr_endchar)
    return retval, i_beginchar.value, i_endchar.value


def fl_set_input_maxchars(ptr_flobject, maxchars):
    """fl_set_input_maxchars(ptr_flobject, maxchars)
    
    Limits the number of characters per line for input fields of type
    xfdata.FL_NORMAL_INPUT. Note that input flobjects of type
    xfdata.FL_DATE_INPUT are limited to 10 characters per default and those
    of type xfdata.FL_SECRET_INPUT to 16.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject
        maxchars : int
            maximum characters to be set. If it is 0, limit is reset to
            infinite.

    Examples
    --------
        >>> fl_set_input_maxchars(inpobj, 20)

    Notes
    -----
        Status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_input_maxchars = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input_maxchars",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_input_maxchars(FL_OBJECT * ob, int maxchars)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_maxchars = library.convert_to_intc(maxchars)
    library.keep_elem_refs(ptr_flobject, maxchars, i_maxchars)
    _fl_set_input_maxchars(ptr_flobject, i_maxchars)


def fl_set_input_format(ptr_flobject, fmt, sep):
    """fl_set_input_format(ptr_flobject, fmt, sep)
    
    Defines the format used for an input flobject. Currently used only for
    xfdata.FL_DATE_INPUT flobjects.

    Parameters
    ----------
        fmt : int
            format for the input. Values (from xfdata.py) FL_INPUT_DDMM,
            FL_INPUT_MMDD
        sep : int or char
            printable single character used as separator

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_input_format = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input_format",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_int],
        """void fl_set_input_format(FL_OBJECT * ob, int fmt, int sep)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.checkfatal_allowed_value_in_list(fmt, xfdata.DATEFMT_list)
    i_fmt = library.convert_to_intc(fmt)
    if isinstance(sep, str):
        # workaround to let a character as int argument
        ordsep = ord(sep)
    else:
        ordsep = sep
    i_sep = library.convert_to_intc(ordsep)
    library.keep_elem_refs(ptr_flobject, fmt, sep, ordsep, i_fmt, i_sep)
    _fl_set_input_format(ptr_flobject, i_fmt, i_sep)


def fl_set_input_hscrollbar(ptr_flobject, pref):
    """fl_set_input_hscrollbar(ptr_flobject, pref)
    
    Defines horizontal scrollbar settings. By default, if an input field of
    type xfdata.FL_MULTILINE_INPUT contains more text than can be shown,
    scrollbars will appear with which the user can scroll the text around
    horizontally. Turning off scrollbars for an input field does not turn
    off scrolling, the user can still scroll the field using cursor and
    other keys.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject
        pref : int
            how is horizontal scrollbar shown. Values (from xfdata.py)
            FL_AUTO, FL_ON, FL_OFF

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_hscrollbar = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input_hscrollbar",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_input_hscrollbar(FL_OBJECT * ob, int pref)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.checkfatal_allowed_value_in_list(pref, xfdata.SCROLLBARVAL_list)
    i_pref = library.convert_to_intc(pref)
    library.keep_elem_refs(ptr_flobject, pref, i_pref)
    _fl_set_input_hscrollbar(ptr_flobject, i_pref)


def fl_set_input_vscrollbar(ptr_flobject, pref):
    """fl_set_input_vscrollbar(ptr_flobject, pref)
    
    Defines vertical scrollbar settings. By default, if an input field of
    type xfdata.FL_MULTILINE_INPUT contains more text than can be shown,
    scrollbars will appear with which the user can scroll the text around
    vertically. Turning off scrollbars for an input field does not turn off
    scrolling, the user can still scroll the field using cursor and other
    keys.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject
        pref : int
            how is vertical scrollbar shown. Values (from xfdata.py)
            FL_AUTO, FL_ON, FL_OFF

    Examples
    --------
        >>> fl_set_input_vscrollbar(inpobj, xfdata.FL_OFF)

    Notes
    -----
        Status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_input_vscrollbar = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input_vscrollbar",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_input_vscrollbar(FL_OBJECT * ob, int pref)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.checkfatal_allowed_value_in_list(pref, xfdata.SCROLLBARVAL_list)
    i_pref = library.convert_to_intc(pref)
    library.keep_elem_refs(ptr_flobject, pref, i_pref)
    _fl_set_input_vscrollbar(ptr_flobject, i_pref)


def fl_set_input_topline(ptr_flobject, linenum):
    """fl_set_input_topline(ptr_flobject, linenum)
    
    Scrolls vertically an input flobject (for input fields of type
    xfdata.FL_MULTILINE_INPUT only).

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject
        linenum : int
            the new top line id (starting from 1) in the input field.

    Examples
    --------
        >>> fl_set_input_topline(ptr_flobject, 3)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_topline = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input_topline",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_input_topline(FL_OBJECT * ob, int top)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_linenum = library.convert_to_intc(linenum)
    library.keep_elem_refs(ptr_flobject, linenum, i_linenum)
    _fl_set_input_topline(ptr_flobject, i_linenum)


def fl_set_input_scrollbarsize(ptr_flobject, height, width):
    """fl_set_input_scrollbarsize(ptr_flobject, height, width)
    
    Changes the size of the scrollbars. By default, the scrollbar size
    is dependent on the initial size of the input box.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject
        height : int
            horizontal height of scrollbar in pixels
        width : int
            vertical width of scrollbar in pixels

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_input_scrollbarsize = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input_scrollbarsize",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_int],
        """void fl_set_input_scrollbarsize(FL_OBJECT * ob, int hh, int vw)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_height = library.convert_to_intc(height)
    i_width = library.convert_to_intc(width)
    library.keep_elem_refs(ptr_flobject, height, width, i_height, i_width)
    _fl_set_input_scrollbarsize(ptr_flobject, i_height, i_width)


def fl_get_input_scrollbarsize(ptr_flobject):
    """fl_get_input_scrollbarsize(ptr_flobject) -> height, width
    
    Finds out the current settings for the horizontal scrollbar height
    and the vertical scrollbar width.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject

    Returns
    -------
        height : int
            horizontal height
        width : int
            vertical width

    API_diversion
    ----------
        API changed from XForms, upstream is
        fl_get_input_scrollbarsize(ptr_flobject, hh, vw)

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_get_input_scrollbarsize = library.cfuncproto(
        library.load_so_libforms(), "fl_get_input_scrollbarsize",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int),
        cty.POINTER(cty.c_int)],
        """void fl_get_input_scrollbarsize(FL_OBJECT * ob, int * hh,
           int * vw)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_height, ptr_height = library.make_intc_and_pointer()
    i_width, ptr_width = library.make_intc_and_pointer()
    library.keep_elem_refs(ptr_flobject, i_height, i_width)
    _fl_get_input_scrollbarsize(ptr_flobject, ptr_height, ptr_width)
    return i_height.value, i_width.value


def fl_set_input_xoffset(ptr_flobject, offset):
    """fl_set_input_xoffset(ptr_flobject, offset)
    
    Scrolls programmatically horizontally (to the left).

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject
        offset : int
            positive number of pixels to scroll to the left relative
            to the nominal position of the text lines.

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_xoffset = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input_xoffset",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_input_xoffset(FL_OBJECT * ob, int xoff)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_offset = library.convert_to_intc(offset)
    library.keep_elem_refs(ptr_flobject, offset, i_offset)
    _fl_set_input_xoffset(ptr_flobject, i_offset)


def fl_get_input_xoffset(ptr_flobject):
    """fl_get_input_xoffset(ptr_flobject) -> offset
    
    Finds out the current horizontal scrolling offset.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject

    Returns
    -------
        offset : int
            horizontal offset of input.

    Examples
    --------
        >>> hoffset = fl_get_input_xoffset(inpobj)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_input_xoffset = library.cfuncproto(
        library.load_so_libforms(), "fl_get_input_xoffset",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_input_xoffset(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_input_xoffset(ptr_flobject)
    return retval


def fl_set_input_fieldchar(ptr_flobject, fldchar):
    """fl_set_input_fieldchar(ptr_flobject, fldchar) -> oldchar
    
    Changes the character used to draw the text, for secret input field.
    By default text is drawn using spaces.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject
        fldchar : int or char
            character to use in secret input fields

    Returns
    -------
        oldchar : int
            old field character (ordinal form)

    Examples
    --------
        >>> oldchar = fl_set_input_fieldchar(inpobj, '*')

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_fieldchar = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input_fieldchar",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """int fl_set_input_fieldchar(FL_OBJECT * ob, int fchar)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    if isinstance(fldchar, str):
        # workaround to let a character as int argument
        ordfldc = ord(fldchar)
    else:
        ordfldc = fldchar
    i_fldchar = library.convert_to_intc(ordfldc)
    library.keep_elem_refs(ptr_flobject, fldchar, ordfldc, i_fldchar)
    retval = _fl_set_input_fieldchar(ptr_flobject, i_fldchar)
    return retval


def fl_get_input_topline(ptr_flobject):
    """fl_get_input_topline(ptr_flobject) -> linenum
    
    Finds out the current topline in the input field.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject

    Returns
    -------
        linenum. : int
            current topline

    Examples
    --------
        >>> fl_get_input_topline(ptr_flobject)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_input_topline = library.cfuncproto(
        library.load_so_libforms(), "fl_get_input_topline",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_input_topline(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_input_topline(ptr_flobject)
    return retval


def fl_get_input_screenlines(ptr_flobject):
    """fl_get_input_screenlines(ptr_flobject) -> numlines
    
    Finds out the number of lines that fit inside the input box.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject

    Returns
    -------
        numlines : int
            number of lines

    Examples
    --------
        >>> fl_get_input_screenlines(inpobj)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_input_screenlines = library.cfuncproto(
        library.load_so_libforms(), "fl_get_input_screenlines",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_input_screenlines(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_input_screenlines(ptr_flobject)
    return retval


def fl_get_input_cursorpos(ptr_flobject):
    """fl_get_input_cursorpos(ptr_flobject) -> result, xpos, ypos
    
    Finds out the cursor position measured in number of characters
    (including newline characters) in front of the cursor.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject

    Returns
    -------
        result : int
            num. or -1 (if the input field does not have input focus
            thus does not have a cursor)
        xpos : int
            horizontal position in characters
        ypos : int
            vertical position in characters

    Examples
    --------
        >>> rslt, x, y = fl_get_input_cursorpos(inpobj)

    API_diversion
    -------------
        API changed from XForms, upstream is
        fl_get_input_cursorpos(ptr_flobject, xpos, ypos)

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_get_input_cursorpos = library.cfuncproto(
        library.load_so_libforms(), "fl_get_input_cursorpos",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int),
        cty.POINTER(cty.c_int)],
        """int fl_get_input_cursorpos(FL_OBJECT * ob, int * x, int * y)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_xpos, ptr_xpos = library.make_intc_and_pointer()
    i_ypos, ptr_ypos = library.make_intc_and_pointer()
    library.keep_elem_refs(ptr_flobject, i_xpos, i_ypos, ptr_xpos, ptr_ypos)
    retval = _fl_get_input_cursorpos(ptr_flobject, ptr_xpos, ptr_ypos)
    return retval, i_xpos.value, i_ypos.value


def fl_set_input_cursor_visible(ptr_flobject, yesno):
    """fl_set_input_cursor_visible(ptr_flobject, yesno)
    
    Turns on or off the cursor of the input field.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject
        yesno : int
            flag to set/unset cursor visibility. Values 1 (visible)
            or 0 (not visible)

    Examples
    --------
        >>> fl_set_input_cursor_visible(inpobj, 1)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_cursor_visible = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input_cursor_visible",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_input_cursor_visible(FL_OBJECT * ob, int visible)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_yesno = library.convert_to_intc(yesno)
    library.keep_elem_refs(ptr_flobject, yesno, i_yesno)
    _fl_set_input_cursor_visible(ptr_flobject, i_yesno)


def fl_get_input_numberoflines(ptr_flobject):
    """fl_get_input_numberoflines(ptr_flobject) -> numlines
    
    Finds out the number of lines in the input field.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject

    Returns
    -------
        numlines : int
            number of lines in input

    Examples
    --------
        >>> fl_get_input_numberoflines(inpobj)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_input_numberoflines = library.cfuncproto(
        library.load_so_libforms(), "fl_get_input_numberoflines",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_input_numberoflines(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_input_numberoflines(ptr_flobject)
    return retval


def fl_get_input_format(ptr_flobject):
    """fl_get_input_format(ptr_flobject) -> fmt, sep
    
    Provides means for the validator to retrieve some information about
    user preference or other state dependent informations.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject

    Returns
    -------
        fmt : int
            format (from xfdata.py, e.g. FL_INPUT_DDMM ..)
        sep : int
            separator (in ordinal form)

    Examples
    --------
        >>> fmt, sep =  fl_get_input_format(inpobj)

    API_diversion
    -------------
        API changed from XForms, upstream is
        fl_get_input_format(ptr_flobject, fmt, sep)

    Notes
    -----
        Status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_get_input_format = library.cfuncproto(
        library.load_so_libforms(), "fl_get_input_format",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int),
        cty.POINTER(cty.c_int)],
        """void fl_get_input_format(FL_OBJECT * ob, int * fmt, int * sep)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_fmt, ptr_fmt = library.make_intc_and_pointer()
    i_sep, ptr_sep = library.make_intc_and_pointer()
    library.keep_elem_refs(ptr_flobject, i_fmt, i_sep, ptr_fmt, ptr_sep)
    _fl_get_input_format(ptr_flobject, ptr_fmt, ptr_sep)
    return i_fmt.value, i_sep.value


def fl_get_input(ptr_flobject):
    """fl_get_input(ptr_flobject) -> textins
    
    Finds out the text string in the field (when the user has changed it).

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject

    Returns
    -------
        textins : str
            user input string

    Examples
    --------
        >>> usertxt = fl_get_input(inpobj)

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_get_input = library.cfuncproto(
        library.load_so_libforms(), "fl_get_input",
        xfdata.STRING, [cty.POINTER(xfdata.FL_OBJECT)],
        """const char * fl_get_input(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_input(ptr_flobject)
    return retval


def fl_set_input_filter(ptr_flobject, pyfn_InputValidator):
    """fl_set_input_filter(ptr_flobject, pyfn_InputValidator) -> InputValidator
    
    Defines up a validator function, that is is called whenever a new
    (regular) character is entered.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject
        pyfn_InputValidator : python function, returned value
            name referring to function(ptr_flobject, oldstr, c, int) -> oldfilt
            function to set validator. oldstr is the string in the input
            field before the newly typed character c was added to form the
            new string cur. If the new character is not an acceptable
            character for the input field, the filter function should return
            xfdata.FL_INVALID otherwise xfdata.FL_VALID. If xfdata.FL_INVALID
            is returned, the new character is discarded and the input field
            remains unmodified. The function returns the old filter. While
            the built-in filters also sound the keyboard bell, this does not
            happen if a custom filter only returns FL_INVALID. To also sound
            the keyboard bell you can logically OR it with
            xfdata.FL_INVALID|FL_RINGBELL. This still leaves the possibility
            that the input is valid for every character entered, but the
            string is invalid for the field because it is incomplete. E.g.
            12.0e is valid for a float input field for every character typed,
            but the final string is not a valid floating point number. To
            guard again this, the filter function is also called just prior
            to returning the flobject with the argument c (for the newly
            entered character) set to zero. If the validator returns
            xfdata.FL_INVALID the flobject is not returned to the application
            program, but input focus can change to the next input field. If
            the return value xfdata.FL_INVALID|FL_RINGBELL, the keyboard
            bell is sounded and the flobject is not returned to the
            application program and the input focus remains in the flobject.

    Returns
    -------
        InputValidator : xfdata.FL_INPUTVALIDATOR
            old filter function for input

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    #FL_INPUTVALIDATOR = cty.CFUNCTYPE(cty.c_int, cty.POINTER( \
    #           xfdata.FL_OBJECT), xfdata.STRING, xfdata.STRING, cty.c_int)
    _fl_set_input_filter = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input_filter",
        xfdata.FL_INPUTVALIDATOR, [cty.POINTER(xfdata.FL_OBJECT),
        xfdata.FL_INPUTVALIDATOR],
        """FL_INPUTVALIDATOR fl_set_input_filter(FL_OBJECT * ob,
            FL_INPUTVALIDATOR validate)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.verify_function_type(pyfn_InputValidator)
    cfn_InputValidator = xfdata.FL_INPUTVALIDATOR(pyfn_InputValidator)
    library.keep_cfunc_refs(cfn_InputValidator, pyfn_InputValidator)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_set_input_filter(ptr_flobject, cfn_InputValidator)
    return retval


def fl_validate_input(ptr_flobject):
    """fl_validate_input(ptr_flobject) -> result
    
    Tests if the value in an input field is valid, according to the
    pre-defined validator function.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            input flobject

    Returns
    -------
        result : int
            xfdata.FL_VALID (if value is valid or if there is no
            validator function set for the input), otherwise FL_INVALID

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_validate_input = library.cfuncproto(
        library.load_so_libforms(), "fl_validate_input",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_validate_input(FL_OBJECT * obj)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_validate_input(ptr_flobject)
    return retval


fl_set_input_shortcut = flbasic.fl_set_object_shortcut


# edit keys

def fl_set_input_editkeymap(ptr_editkeymap):
    """fl_set_input_editkeymap(ptr_editkeymap)
    
    Changes the default edit keymaps. Edit keymap is global and affects all
    input field within the application. All cursor keys (<Left>, <Home> etc.)
    are reserved and their meanings hard-coded, thus can?t be used in the
    mapping. For example, if you try to set del_prev_char to <Home>, pressing
    the <Home> key will not delete the previous character. In filling the
    keymap structure, ASCII characters (i.e. characters with values below
    128, including the control characters with values below 32) should be
    specified by their ASCII codes (<Ctrl> C is 3 etc.), while all others by
    their Keysyms (XK_F1 etc.). Control and special character combinations
    can be obtained by adding xfdata.FL_CONTROL_MASK to the Keysym. To
    specify Meta add xfdata.FL_ALT_MASK to the key value.

    Parameters
    ----------
        ptr_editkeymap : pointer to xfdata.FL_EditKeymap
            class instance (filled or partially filled). If None, it
            restores the default keymap.

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_editkeymap = library.cfuncproto(
        library.load_so_libforms(), "fl_set_input_editkeymap",
        None, [cty.POINTER(xfdata.FL_EditKeymap)],
        """void fl_set_input_editkeymap(const char * keymap)""")
    library.check_if_initialized()
    if not ptr_editkeymap:         # it is None
        ptr_editkeymap = cty.cast(ptr_editkeymap, cty.c_void_p)
    else:
        library.verify_otherclassptr_type(ptr_editkeymap, cty.POINTER( \
            xfdata.FL_EditKeymap))
    library.keep_elem_refs(ptr_editkeymap)
    _fl_set_input_editkeymap(ptr_editkeymap)

