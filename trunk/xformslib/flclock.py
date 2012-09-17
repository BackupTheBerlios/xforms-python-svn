#!/usr/bin/env python3
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage clock flobjects.
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


#################################
# forms.h (clock.h)
#################################

# fl_create_clock function placeholder (internal)


def fl_add_clock(clocktype, xpos, ypos, width, height, label):
    """fl_add_clock(clocktype, xpos, ypos, width, height, label)
    -> ptr_flobject

    Adds a clock flobject.

    Parameters
    ----------
        clocktype : int
            type of clock to be added. Values (from xfdata.py)
            - FL_ANALOG_CLOCK (An analog clock complete with the second hand),
            - FL_DIGITAL_CLOCK (A digital clock)
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            text label of clock

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            clock flobject added

    Examples
    --------
        >>> pclkobj = fl_add_clock(xfdata.FL_ANALOG_CLOCK, 150, 210,
                220, 200, "My great clock")

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_add_clock = library.cfuncproto(
        library.load_so_libforms(), "fl_add_clock",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_clock(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * s)""")
    library.check_if_flinitialized()
    library.checkfatal_allowed_value_in_list(clocktype, \
            xfdata.CLOCKTYPE_list)
    i_clocktype = library.convert_to_intc(clocktype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_stringc(label)
    library.keep_elem_refs(clocktype, xpos, ypos, width, height, label, \
            i_clocktype, i_xpos, i_ypos, i_width, i_height, s_label)
    retval = _fl_add_clock(i_clocktype, i_xpos, i_ypos, i_width, i_height, \
            s_label)
    return retval


def fl_get_clock(ptr_flobject):
    """fl_get_clock(ptr_flobject) -> hrs, mins, secs

    Finds out time values from a clock flobject, with hours in 0-23, minutes
    in 0-59 and seconds in 0-59.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            clock flobject

    Returns
    -------
        hrs : int
            hours
        mins : int
            minutes
        secs : int
            seconds

    Examples
    --------
        >>> hou, mnu, sec = fl_get_clock(pclkobj)

    API_diversion
    ----------
        API changed from XForms, upstream is
        fl_get_clock(ptr_flobject, hr, mn, sec)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_get_clock = library.cfuncproto(
        library.load_so_libforms(), "fl_get_clock",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int),
        cty.POINTER(cty.c_int), cty.POINTER(cty.c_int)],
        """void fl_get_clock(FL_OBJECT * ob, int * h, int * m, int * s)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_hrs, ptr_hrs = library.make_intc_and_pointer()
    i_mins, ptr_mins = library.make_intc_and_pointer()
    i_secs, ptr_secs = library.make_intc_and_pointer()
    library.keep_elem_refs(ptr_flobject, i_hrs, i_mins, i_secs, ptr_hrs, \
            ptr_mins, ptr_secs)
    _fl_get_clock(ptr_flobject, ptr_hrs, ptr_mins, ptr_secs)
    return i_hrs.value, i_mins.value, i_secs.value


def fl_set_clock_adjustment(ptr_flobject, offset):
    """fl_set_clock_adjustment(ptr_flobject, offset) -> oldadjust

    Adjusts the clock to display a time other than local time.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            clock flobject
        offset : long
            adjustment value in seconds

    Returns
    -------
        oldadjust : long
            old adjustment value

    Examples
    --------
        >>> oldadj = fl_set_clock_adjustment(pclkobj, 3600)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = OK

    """
    _fl_set_clock_adjustment = library.cfuncproto(
        library.load_so_libforms(), "fl_set_clock_adjustment",
        cty.c_long, [cty.POINTER(xfdata.FL_OBJECT), cty.c_long],
        """long int fl_set_clock_adjustment(FL_OBJECT * ob,
           long int offset)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    l_offset = library.convert_to_longc(offset)
    library.keep_elem_refs(ptr_flobject, offset, l_offset)
    retval = _fl_set_clock_adjustment(ptr_flobject, l_offset)
    return retval


def fl_set_clock_ampm(ptr_flobject, yesno):
    """fl_set_clock_ampm(ptr_flobject, yesno)

    Switches the display to 12hr system (am-pm). By default, the
    digital clock uses 24hr system.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            clock flobject
        yesno : int
            flag. Values 1 (12hr system used) or 0 (24hr system used)

    Examples
    --------
        >>> fl_set_clock_ampm(pclkobj, 1)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_set_clock_ampm = library.cfuncproto(
        library.load_so_libforms(), "fl_set_clock_ampm",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_clock_ampm(FL_OBJECT * ob, int y)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_yesno = library.convert_to_intc(yesno)
    library.keep_elem_refs(ptr_flobject, yesno, i_yesno)
    _fl_set_clock_ampm(ptr_flobject, i_yesno)

