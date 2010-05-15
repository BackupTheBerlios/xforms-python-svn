#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage input objects.

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
from xformslib import flbasic



####################
# forms.h (input.h)
####################

# Routines

# fl_create_input function placeholder (internal)


def fl_add_input(inputtype, x, y, w, h, label):
    """Adds an input object.

    --

    :Parameters:
      `inputtype` : int
        type of input to be added. Values (from xfdata.py) FL_NORMAL_INPUT,
        FL_FLOAT_INPUT, FL_INT_INPUT, FL_DATE_INPUT, FL_MULTILINE_INPUT,
        FL_HIDDEN_INPUT, FL_SECRET_INPUT
      `x` : int
        horizontal position (upper-left corner)
      `y` : int
        vertical position (upper-left corner)
      `w` : int
        width in coord units
      `h` : int
        height in coord units
      `label` : str
        text label of input

    :return: object created (pFlObject)
    :rtype: pointer to xfdata.FL_OBJECT

    :note: e.g. *todo*

    :status: Tested + Doc + Demo = OK

    """
    _fl_add_input = libr.cfuncproto(
        libr.load_so_libforms(), "fl_add_input",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_input(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    libr.check_if_initialized()
    libr.check_admitted_value_in_list(inputtype, xfdata.INPUTTYPE_list)
    iinputtype = libr.convert_to_int(inputtype)
    ix = libr.convert_to_FL_Coord(x)
    iy = libr.convert_to_FL_Coord(y)
    iw = libr.convert_to_FL_Coord(w)
    ih = libr.convert_to_FL_Coord(h)
    slabel = libr.convert_to_string(label)
    libr.keep_elem_refs(inputtype, x, y, w, h, label, iinputtype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_input(iinputtype, ix, iy, iw, ih, slabel)
    return retval


def fl_set_input(pFlObject, text):
    """Sets the particular input string, with no checks for validity. An
    empty string can be used to clear an input field.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object
      `text` : str
        input text

    :note: e.g. *todo*

    :status: Tested + Doc + Demo = OK

    """
    _fl_set_input = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.STRING],
        """void fl_set_input(FL_OBJECT * ob, const char * str)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    stext = libr.convert_to_string(text)
    libr.keep_elem_refs(pFlObject, text, stext)
    _fl_set_input(pFlObject, stext)


# fl_set_input_return function placeholder (internal)


def fl_set_input_color(pFlObject, txtcolr, curscolr):
    """Sets text and cursor colors to be used in input object.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object
      `txtcolr` : long_pos
        color value for text
      `curscolr` : long_pos
        color value for cursor

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_color = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input_color",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.FL_COLOR,
        xfdata.FL_COLOR],
        """void fl_set_input_color(FL_OBJECT * ob, FL_COLOR textcol,
           FL_COLOR curscol)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.check_admitted_value_in_list(txtcolr, xfdata.COLOR_list)
    libr.check_admitted_value_in_list(curscolr, xfdata.COLOR_list)
    ultxtcolr = libr.convert_to_FL_COLOR(txtcolr)
    ulcurscolr = libr.convert_to_FL_COLOR(curscolr)
    libr.keep_elem_refs(pFlObject, txtcolr, curscolr, ultxtcolr, ulcurscolr)
    _fl_set_input_color(pFlObject, ultxtcolr, ulcurscolr)


def fl_get_input_color(pFlObject):
    """Obtains current color for text and cursor of an input object.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object

    :return: color value for text, color value for cursor
    :rtype: long_pos, long_pos

    :note: e.g. *todo*

    :attention: API change from XForms - upstream was
        fl_get_input_color(pFlObject, textcolr, curscolr)

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_input_color = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_input_color",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(xfdata.FL_COLOR),
        cty.POINTER(xfdata.FL_COLOR)],
        """void fl_get_input_color(FL_OBJECT * ob, FL_COLOR * textcol,
           FL_COLOR * curscol)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    txtcolr, ptxtcolr = libr.make_FL_COLOR_and_pointer()
    curscolr, pcurscolr = libr.make_FL_COLOR_and_pointer()
    libr.keep_elem_refs(pFlObject, txtcolr, curscolr)
    _fl_get_input_color(pFlObject, ptxtcolr, pcurscolr)
    return txtcolr.value, curscolr.value


def fl_set_input_scroll(pFlObject, yesno):
    """Turn on/off scrolling for an input field (for both multiline and single
    line input field).

    --

    :Parameters:

      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object
      `yesno` : int
        flag to enable/disable scrolling. Values 0 (disabled) or 1 (enabled)

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_scroll = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input_scroll",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_input_scroll(FL_OBJECT * ob, int yes)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    iyesno = libr.convert_to_int(yesno)
    libr.keep_elem_refs(pFlObject, yesno, iyesno)
    _fl_set_input_scroll(pFlObject, iyesno)


def fl_set_input_cursorpos(pFlObject, xpos, ypos):
    """Moves the cursor within the input field.

    --

    :Parameters:

      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object
      `xpos` : int
        horizontal cursor position in characters
      `ypos` : int
        vertical cursor position in lines

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_input_cursorpos = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input_cursorpos",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_int],
        """void fl_set_input_cursorpos(FL_OBJECT * ob, int xpos, int ypos)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    ixpos = libr.convert_to_int(xpos)
    iypos = libr.convert_to_int(ypos)
    libr.keep_elem_refs(pFlObject, xpos, ypos, ixpos, iypos)
    _fl_set_input_cursorpos(pFlObject, ixpos, iypos)


def fl_set_input_selected(pFlObject, yesno):
    """Selects or deselects the current input. It places the cursor at
    the end of the string when selected.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object
      `yesno` : int
        flag to deselect/select input. Values 0 (deselected) or 1 (selected)

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_selected = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input_selected",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_input_selected(FL_OBJECT * ob, int yes)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    iyesno = libr.convert_to_int(yesno)
    libr.keep_elem_refs(pFlObject, yesno, iyesno)
    _fl_set_input_selected(pFlObject, iyesno)


def fl_set_input_selected_range(pFlObject, begin, end):
    """Selects or deselects the current input of part of it. When begin is
    0 and end is the last character number, all input is selected. It places
    the cursor at the beginning of selected string.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object
      `begin` : int
        starting value in characters
      `end` : int
        ending value in characters

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_input_selected_range = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input_selected_range",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_int],
        """void fl_set_input_selected_range(FL_OBJECT * ob,
           int begin, int end)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    ibegin = libr.convert_to_int(begin)
    iend = libr.convert_to_int(end)
    libr.keep_elem_refs(pFlObject, begin, end, ibegin, iend)
    _fl_set_input_selected_range(pFlObject, ibegin, iend)


def fl_get_input_selected_range(pFlObject):
    """Obtains the currently selected range, either selected by the
    application or by the user.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object

    :return: selected string, starting value, ending value of selection
        in characters
    :rtype: str, int, int

    :note: e.g. *todo*

    :attention: API change from XForms - upstream was
        fl_get_input_selected_range(pFlObject, begin, end)

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_get_input_selected_range = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_input_selected_range",
        xfdata.STRING, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int),
        cty.POINTER(cty.c_int)],
        """const char * fl_get_input_selected_range(FL_OBJECT * ob,
           int * begin, int * end)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    begin, pbegin = libr.make_int_and_pointer()
    end, pend = libr.make_int_and_pointer()
    libr.keep_elem_refs(pFlObject, begin, end, pbegin, pend)
    retval = _fl_get_input_selected_range(pFlObject, pbegin, pend)
    return retval, begin.value, end.value


def fl_set_input_maxchars(pFlObject, maxchars):
    """Limits the number of characters per line for input fields of type
    xfdata.FL_NORMAL_INPUT. Note that input objects of type
    xfdata.FL_DATE_INPUT are limited to 10 characters per default and those
    of type xfdata.FL_SECRET_INPUT to 16.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object
      `maxchars` : int
        maximum characters to be set. If it's 0, limit is reset to infinite.

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_input_maxchars = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input_maxchars",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_input_maxchars(FL_OBJECT * ob, int maxchars)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    imaxchars = libr.convert_to_int(maxchars)
    libr.keep_elem_refs(pFlObject, maxchars, imaxchars)
    _fl_set_input_maxchars(pFlObject, imaxchars)


def fl_set_input_format(pFlObject, fmt, sep):
    """Sets the format used for an input object. Currently used only for
    xfdata.FL_DATE_INPUT objects.

    --

    :Parameters:
      `fmt` : int
        format for the input. Values (from xfdata.py) FL_INPUT_DDMM,
        FL_INPUT_MMDD
      `sep` : int or char
        printable single character used as separator

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_input_format = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input_format",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_int],
        """void fl_set_input_format(FL_OBJECT * ob, int fmt, int sep)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.check_admitted_value_in_list(fmt, xfdata.DATEFMT_list)
    if isinstance(sep, str):
        # workaround to let a character as int argument
        ordsep = ord(sep)
    else:
        ordsep = sep
    ifmt = libr.convert_to_int(fmt)
    isep = libr.convert_to_int(ordsep)
    libr.keep_elem_refs(pFlObject, fmt, sep, ordsep, ifmt, isep)
    _fl_set_input_format(pFlObject, ifmt, isep)


def fl_set_input_hscrollbar(pFlObject, pref):
    """Sets horizontal scrollbar settings. By default, if an input field of
    type xfdata.FL_MULTILINE_INPUT contains more text than can be shown,
    scrollbars will appear with which the user can scroll the text around
    horizontally. Turning off scrollbars for an input field does not turn off
    scrolling, the user can still scroll the field using cursor and other keys.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object
      `pref` : int
        how is horizontal scrollbar shown. Values (from xfdata.py) FL_AUTO,
        FL_ON, FL_OFF

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_hscrollbar = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input_hscrollbar",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_input_hscrollbar(FL_OBJECT * ob, int pref)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.check_admitted_value_in_list(pref, xfdata.SCROLLBARVAL_list)
    ipref = libr.convert_to_int(pref)
    libr.keep_elem_refs(pFlObject, pref, ipref)
    _fl_set_input_hscrollbar(pFlObject, ipref)


def fl_set_input_vscrollbar(pFlObject, pref):
    """Sets vertical scrollbar settings. By default, if an input field of type
    xfdata.FL_MULTILINE_INPUT contains more text than can be shown, scrollbars
    will appear with which the user can scroll the text around vertically.
    Turning off scrollbars for an input field does not turn off scrolling, the
    user can still scroll the field using cursor and other keys.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object
      `pref` : int
        how is vertical scrollbar shown. Values (from xfdata.py) FL_AUTO,
        FL_ON, FL_OFF

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_input_vscrollbar = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input_vscrollbar",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_input_vscrollbar(FL_OBJECT * ob, int pref)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.check_admitted_value_in_list(pref, xfdata.SCROLLBARVAL_list)
    ipref = libr.convert_to_int(pref)
    libr.keep_elem_refs(pFlObject, pref, ipref)
    _fl_set_input_vscrollbar(pFlObject, ipref)


def fl_set_input_topline(pFlObject, linenum):
    """Scrolls vertically an input object (for input fields of type
    xfdata.FL_MULTILINE_INPUT only).

    --

    :Parameters:

      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object
      `linenum` : int
        the new top line (starting from 1) in the input field.

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_topline = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input_topline",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_input_topline(FL_OBJECT * ob, int top)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    ilinenum = libr.convert_to_int(linenum)
    libr.keep_elem_refs(pFlObject, linenum, ilinenum)
    _fl_set_input_topline(pFlObject, ilinenum)


def fl_set_input_scrollbarsize(pFlObject, hh, vw):
    """Changes the size of the scrollbars. By default, the scrollbar size is
    dependent on the initial size of the input box.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object
      `hh` : int
        horizontal height of scrollbar in pixels
      `vw` : int
        vertical width of scrollbar in pixels

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_input_scrollbarsize = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input_scrollbarsize",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_int],
        """void fl_set_input_scrollbarsize(FL_OBJECT * ob, int hh, int vw)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    ihh = libr.convert_to_int(hh)
    ivw = libr.convert_to_int(vw)
    libr.keep_elem_refs(pFlObject, hh, vw, ihh, ivw)
    _fl_set_input_scrollbarsize(pFlObject, ihh, ivw)


def fl_get_input_scrollbarsize(pFlObject):
    """Obtains the current settings for the horizontal scrollbar height and
    the vertical scrollbar width.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object

    :return: horizontal height (hh), vertical width (vw)
    :rtype: int, int

    :attention: API change from XForms - upstream was
        fl_get_input_scrollbarsize(pFlObject, hh, vw)

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_get_input_scrollbarsize = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_input_scrollbarsize",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int),
        cty.POINTER(cty.c_int)],
        """void fl_get_input_scrollbarsize(FL_OBJECT * ob, int * hh,
           int * vw)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    hh, phh = libr.make_int_and_pointer()
    vw, pvw = libr.make_int_and_pointer()
    libr.keep_elem_refs(pFlObject, hh, vw)
    _fl_get_input_scrollbarsize(pFlObject, phh, pvw)
    return hh.value, vw.value


def fl_set_input_xoffset(pFlObject, offset):
    """Scroll programmatically horizontally (to the left).

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object
      `offset` : int
        positive number of pixels to scroll to the left relative to the
        nominal position of the text lines.

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_xoffset = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input_xoffset",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_input_xoffset(FL_OBJECT * ob, int xoff)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    ioffset = libr.convert_to_int(offset)
    libr.keep_elem_refs(pFlObject, offset, ioffset)
    _fl_set_input_xoffset(pFlObject, ioffset)


def fl_get_input_xoffset(pFlObject):
    """Obtains the current horizontal scrolling offset.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object

    :return: horizontal offset of input.
    :rtype: int

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_input_xoffset = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_input_xoffset",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_input_xoffset(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_input_xoffset(pFlObject)
    return retval


def fl_set_input_fieldchar(pFlObject, fldchar):
    """Changes the character used to draw the text, for secret input field. By
    default text is drawn using spaces.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object
      `fldchar` : int or char
        character to use in secret input fields

    :return: old field character (ordinal form)
    :rtype: int

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_fieldchar = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input_fieldchar",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """int fl_set_input_fieldchar(FL_OBJECT * ob, int fchar)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    if isinstance(fldchar, str):
        # workaround to let a character as int argument
        ordfldc = ord(fldchar)
    else:
        ordfldc = fldchar
    ifldchar = libr.convert_to_int(ordfldc)
    libr.keep_elem_refs(pFlObject, fldchar, ordfldc, ifldchar)
    retval = _fl_set_input_fieldchar(pFlObject, ifldchar)
    return retval


def fl_get_input_topline(pFlObject):
    """Obtains the current topline in the input field.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object

    :return: num.
    :rtype: int

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_input_topline = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_input_topline",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_input_topline(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_input_topline(pFlObject)
    return retval


def fl_get_input_screenlines(pFlObject):
    """Obtains the number of lines that fit inside the input box.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object

    :return: num.
    :rtype: int

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_input_screenlines = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_input_screenlines",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_input_screenlines(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_input_screenlines(pFlObject)
    return retval


def fl_get_input_cursorpos(pFlObject):
    """Obtains the cursor position measured in number of characters (including
    newline characters) in front of the cursor.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object

    :return: num. or -1 (if the input field does not have input focus thus
        does not have a cursor), horizontal position (x), vertical position
        (y)
    :rtype: int, int, int

    :note: e.g. *todo*

    :attention: API change from XForms - upstream was
        fl_get_input_cursorpos(pFlObject, x, y)

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_get_input_cursorpos = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_input_cursorpos",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int),
        cty.POINTER(cty.c_int)],
        """int fl_get_input_cursorpos(FL_OBJECT * ob, int * x, int * y)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    x, px = libr.make_int_and_pointer()
    y, py = libr.make_int_and_pointer()
    libr.keep_elem_refs(pFlObject, x, y)
    retval = _fl_get_input_cursorpos(pFlObject, px, py)
    return retval, x.value, y.value


def fl_set_input_cursor_visible(pFlObject, yesno):
    """Turns on/off the cursor of the input field.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object
      `yesno` : int
        flag to set/unset cursor visibility. Values 1 (visible) or 0 (not
        visible)

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_cursor_visible = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input_cursor_visible",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_input_cursor_visible(FL_OBJECT * ob, int visible)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    iyesno = libr.convert_to_int(yesno)
    libr.keep_elem_refs(pFlObject, yesno, iyesno)
    _fl_set_input_cursor_visible(pFlObject, iyesno)


def fl_get_input_numberoflines(pFlObject):
    """Obtains the number of lines in the input field.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object

    :return: number of lines in input
    :rtype: int

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_input_numberoflines = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_input_numberoflines",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_input_numberoflines(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_input_numberoflines(pFlObject)
    return retval


def fl_get_input_format(pFlObject):
    """Provides means for the validator to retrieve some information about
    user preference or other state dependent informations.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object

    :return: format, separator (in ordinal form)
    :rtype: int, int

    :note: e.g. *todo*

    :attention: API change from XForms - upstream was
        fl_get_input_format(pFlObject, fmt, sep)

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_get_input_format = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_input_format",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int),
        cty.POINTER(cty.c_int)],
        """void fl_get_input_format(FL_OBJECT * ob, int * fmt, int * sep)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    fmt, pfmt = libr.make_int_and_pointer()
    sep, psep = libr.make_int_and_pointer()
    libr.keep_elem_refs(pFlObject, fmt, sep, pfmt, psep)
    _fl_get_input_format(pFlObject, pfmt, psep)
    return fmt.value, sep.value


def fl_get_input(pFlObject):
    """Obtains the text string in the field (when the user has changed it).

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object

    :return: user input string
    :rtype: str

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_get_input = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_input",
        xfdata.STRING, [cty.POINTER(xfdata.FL_OBJECT)],
        """const char * fl_get_input(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_input(pFlObject)
    return retval


def fl_set_input_filter(pFlObject, py_InputValidator):
    """Sets up a validator function, that is is called whenever a new
    (regular) character is entered.
    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object
      `py_InputValidator` : python function to set a validator, returned value
        name referring to function(pFlObject, oldstr, c, int) -> oldfilt
        oldstr is the string in the input field before the newly typed
        character c was added to form the new string cur. If the new character
        is not an acceptable character for the input field, the filter
        function should return xfdata.FL_INVALID otherwise xfdata.FL_VALID.
        If xfdata.FL_INVALID is returned, the new character is discarded and
        the input field remains unmodified. The function returns the old
        filter. While the built-in filters also sound the keyboard bell, this
        doesn?t happen if a custom filter only returns FL_INVALID. To also
        sound the keyboard bell you can logically OR it with xfdata.FL_INVALID
        | xfdata.FL_RINGBELL. This still leaves the possibility that the
        input is valid for every character entered, but the string is invalid
        for the field because it is incomplete. E.g. 12.0e is valid for a
        float input field for every character typed, but the final string is
        not a valid floating point number. To guard again this, the filter
        function is also called just prior to returning the object with the
        argument c (for the newly entered character) set to zero. If the
        validator returns xfdata.FL_INVALID the object is not returned to the
        application program, but input focus can change to the next input
        field. If the return value xfdata.FL_INVALID | xfdata.FL_RINGBELL,
        the keyboard bell is sounded and the object is not returned to the
        application program and the input focus remains in the object.

    :return: old filter function for input
    :rtype: xfdata.FL_INPUTVALIDATOR

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    #FL_INPUTVALIDATOR = cty.CFUNCTYPE(cty.c_int, cty.POINTER( \
    #           xfdata.FL_OBJECT), xfdata.STRING, xfdata.STRING, cty.c_int)
    _fl_set_input_filter = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input_filter",
        xfdata.FL_INPUTVALIDATOR, [cty.POINTER(xfdata.FL_OBJECT),
        xfdata.FL_INPUTVALIDATOR],
        """FL_INPUTVALIDATOR fl_set_input_filter(FL_OBJECT * ob,
            FL_INPUTVALIDATOR validate)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    c_InputValidator = xfdata.FL_INPUTVALIDATOR(py_InputValidator)
    libr.keep_cfunc_refs(c_InputValidator, py_InputValidator)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_set_input_filter(pFlObject, c_InputValidator)
    return retval


def fl_validate_input(pFlObject):
    """Tests if the value in an input field is valid, according to the
    pre-defined validator function.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        input object

    :return: (from xfdata.py) FL_VALID (if value is valid or if there is no
        validator function set for the input), otherwise FL_INVALID
    :rtype: int

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_validate_input = libr.cfuncproto(
        libr.load_so_libforms(), "fl_validate_input",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_validate_input(FL_OBJECT * obj)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_validate_input(pFlObject)
    return retval


fl_set_input_shortcut = flbasic.fl_set_object_shortcut


# edit keys

def fl_set_input_editkeymap(pEditKeymap):
    """Changes the default edit keymaps. Edit keymap is global and affects all
    input field within the application. All cursor keys (<Left>, <Home> etc.)
    are reserved and their meanings hard-coded, thus can?t be used in the
    mapping. For example, if you try to set del_prev_char to <Home>, pressing
    the <Home> key will not delete the previous character. In filling the
    keymap structure, ASCII characters (i.e. characters with values below 128,
    including the control characters with values below 32) should be specified
    by their ASCII codes (<Ctrl> C is 3 etc.), while all others by their
    Keysyms (XK_F1 etc.). Control and special character combinations can be
    obtained by adding xfdata.FL_CONTROL_MASK to the Keysym. To specify Meta
    add xfdata.FL_ALT_MASK to the key value.
    --

    :Parameters:
      `pEditKeymap` : pointer to xfdata.FL_EditKeymap
        class instance (filled or partially filled). If None, it restores the
        default keymap.

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_input_editkeymap = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_input_editkeymap",
        None, [cty.POINTER(xfdata.FL_EditKeymap)],
        """void fl_set_input_editkeymap(const char * keymap)""")
    libr.check_if_initialized()
    if not pEditKeymap:         # it's None
        pass
    else:
        libr.verify_otherclassptr_type(pEditKeymap, cty.POINTER( \
            xfdata.FL_EditKeymap))
    libr.keep_elem_refs(pEditKeymap)
    _fl_set_input_editkeymap(pEditKeymap)

