#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" xforms-python's functions to manage thumbwheel flobjects.
"""

#    Copyright (C) 2009-2012  Luca Lazzaroni "LukenShiro"
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


#########################
# forms.h (thumbwheel.h)
#########################

def fl_get_thumbwheel_value(ptr_flobject):
    """fl_get_thumbwheel_value(ptr_flobject) -> thwvalue

    Finds out the current value of a thumbwheel flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            thumbwheel flobject

    Returns
    -------
        thwvalue : int
            current thumbwheel value, or 1.0 (on failure)

    Examples
    --------
        >>> curval = fl_get_thumbwheel_value(pthwobj)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_get_thumbwheel_value = library.cfuncproto(
        library.load_so_libforms(), "fl_get_thumbwheel_value",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
        """double fl_get_thumbwheel_value(FL_OBJECT * ob)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_thumbwheel_value(ptr_flobject)
    return retval


def fl_set_thumbwheel_value(ptr_flobject, thwvalue):
    """fl_set_thumbwheel_value(ptr_flobject, thwvalue) -> oldthwvalue

    Defines a new value of a thumbwheel flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            thumbwheel flobject
        thwvalue : float
            new value to be set

    Returns
    -------
        oldthwvalue : float
            previous value, or 1.0 (on failure)

    Examples
    --------
        >>> oldval = fl_set_thumbwheel_value(pthwobj, 5.0)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_set_thumbwheel_value = library.cfuncproto(
        library.load_so_libforms(), "fl_set_thumbwheel_value",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """double fl_set_thumbwheel_value(FL_OBJECT * ob, double value)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_thwvalue = library.convert_to_doublec(thwvalue)
    library.keep_elem_refs(ptr_flobject, thwvalue, f_thwvalue)
    retval = _fl_set_thumbwheel_value(ptr_flobject, f_thwvalue)
    return retval


def fl_get_thumbwheel_step(ptr_flobject):
    """fl_get_thumbwheel_step(ptr_flobject) -> step

    Finds out step for thumbwheel flobject value to be rounded to.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            thumbwheel flobject

    Returns
    -------
        step : float
            step value to be rounded

    Examples
    --------
        >>> rndstep = fl_get_thumbwheel_step(pthwobj)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_get_thumbwheel_step = library.cfuncproto(
        library.load_so_libforms(), "fl_get_thumbwheel_step",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
        """double fl_get_thumbwheel_step(FL_OBJECT * ob)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_thumbwheel_step(ptr_flobject)
    return retval


def fl_set_thumbwheel_step(ptr_flobject, step):
    """fl_set_thumbwheel_step(ptr_flobject, step) -> oldstep

    Defines step for thumbwheel flobject value to be rounded to.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            thumbwheel flobject
        step : float
            step value to be set

    Returns
    -------
        oldstep : float
            previous step value

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_set_thumbwheel_step = library.cfuncproto(
        library.load_so_libforms(), "fl_set_thumbwheel_step",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """double fl_set_thumbwheel_step(FL_OBJECT * ob, double step)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_step = library.convert_to_doublec(step)
    library.keep_elem_refs(ptr_flobject, step, f_step)
    retval = _fl_set_thumbwheel_step(ptr_flobject, f_step)
    return retval


# fl_set_thumbwheel_return() function placeholder (deprecated)


# TODO: apparently unused and undocumented; maybe slated for removal? --LK
def fl_set_thumbwheel_crossover(ptr_flobject, flag):
    """fl_set_thumbwheel_crossover(ptr_flobject, flag) -> oldcrossover

    Defines crossover for thumbwheel flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            thumbwheel flobject
        flag : int
            flag for crossover

    Returns
    -------
        oldcrossover : int
            previous crossover

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_set_thumbwheel_crossover = library.cfuncproto(
        library.load_so_libforms(), "fl_set_thumbwheel_crossover",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """int fl_set_thumbwheel_crossover(FL_OBJECT * ob, int flag)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_flag = library.convert_to_intc(flag)
    library.keep_elem_refs(ptr_flobject, flag, i_flag)
    retval = _fl_set_thumbwheel_crossover(ptr_flobject, i_flag)
    return retval


def fl_set_thumbwheel_bounds(ptr_flobject, minbound, maxbound):
    """fl_set_thumbwheel_bounds(ptr_flobject, minbound, maxbound)

    Defines minimum and maximum value limits of a thumbwheel flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            thumbwheel flobject
        minbound : float
            minimum value bound of thumbwheel
        maxbound : float
            maximum value bound of thumbwheel

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_set_thumbwheel_bounds = library.cfuncproto(
        library.load_so_libforms(), "fl_set_thumbwheel_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
        """void fl_set_thumbwheel_bounds(FL_OBJECT * ob, double min,
           double max)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_minbound = library.convert_to_doublec(minbound)
    f_maxbound = library.convert_to_doublec(maxbound)
    library.keep_elem_refs(ptr_flobject, minbound, maxbound, f_minbound, \
            f_maxbound)
    _fl_set_thumbwheel_bounds(ptr_flobject, f_minbound, f_maxbound)


def fl_get_thumbwheel_bounds(ptr_flobject):
    """fl_get_thumbwheel_bounds(ptr_flobject) -> minbound, maxbound

    Finds out minimum and maximum value limits of a thumbwheel flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            thumbwheel flobject

    Returns
    -------
        minbound : float
            minimum value bound
        maxbound : float
            maximum value bound

    Examples
    --------
        >>> *todo*

    API_diversion
    -------------
        API changed from XForms, upstream is
        fl_get_thumbwheel_bounds(ptr_flobject, minbound, maxbound)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_get_thumbwheel_bounds = library.cfuncproto(
        library.load_so_libforms(), "fl_get_thumbwheel_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)],
        """void fl_get_thumbwheel_bounds(FL_OBJECT * ob, double * min,
           double * max)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_minbound, ptr_minbound = library.make_doublec_and_pointer()
    f_maxbound, ptr_maxbound = library.make_doublec_and_pointer()
    library.keep_elem_refs(ptr_flobject, f_minbound, f_maxbound, \
            ptr_minbound, ptr_maxbound)
    _fl_get_thumbwheel_bounds(ptr_flobject, ptr_minbound, ptr_maxbound)
    return f_minbound.value, f_maxbound.value


# fl_create_thumbwheel() function placeholder (internal)


def fl_add_thumbwheel(wheeltype, xpos, ypos, width, height, label):
    """fl_add_thumbwheel(wheeltype, xpos, ypos, width, height, label)
    -> ptr_flobject

    Adds a thumbwheel flobject. It is a valuator that can be useful for
    letting the user indicate a value between some fixed bounds. Both
    horizontal and vertical thumbwheels exist. They have a minimum, a maximum
    and a current value (all floating point values). The user can change the
    current value by rolling the wheel.

    Parameters
    ----------
        wheeltype : int
            type of thumbwheel to be added. Values (from xfdata.py)
            - FL_VERT_THUMBWHEEL (A vertical thumbwheel),
            - FL_HOR_THUMBWHEEL (A horizontal thumbwheel)
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
          label : str
            text label of thumbwheel

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            thumbwheel flobject added

    Examples
    --------
        >>> ptmwobj = fl_add_thumbwheel(xfdata.FL_HOR_THUMBWHEEL,
                140, 134, 250, 30, "MyThumbwheel")

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_add_thumbwheel = library.cfuncproto(
        library.load_so_libforms(), "fl_add_thumbwheel",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_thumbwheel(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_flinitialized()
    library.checkfatal_allowed_value_in_list(wheeltype, \
            xfdata.THUMBWHEELTYPE_list)
    i_wheeltype = library.convert_to_intc(wheeltype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_bytestrc(label)
    library.keep_elem_refs(wheeltype, xpos, ypos, width, height, label, \
            i_wheeltype, i_xpos, i_ypos, i_width, i_height, s_label)
    retval = _fl_add_thumbwheel(i_wheeltype, i_xpos, i_ypos, i_width, \
            i_height, s_label)
    return retval

