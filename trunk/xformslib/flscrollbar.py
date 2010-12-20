#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage scrollbar flobjects.
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


########################
# forms.h (xfdata.h)
########################

# fl_create_scrollbar function placeholder (internal)


def fl_add_scrollbar(scrolltype, xpos, ypos, width, height, label):
    """fl_add_scrollbar(scrolltype, xpos, ypos, width, height, label)
    -> ptr_flobject
    
    Adds a scrollbar flobject to a form.

    Parameters
    ----------
        scrolltype : int
            type of scrollbar to be added. Values (from xfdata.py)
            FL_VERT_SCROLLBAR, FL_HOR_SCROLLBAR, FL_VERT_THIN_SCROLLBAR
            FL_HOR_THIN_SCROLLBAR, FL_VERT_NICE_SCROLLBAR,
            FL_HOR_NICE_SCROLLBAR, FL_VERT_PLAIN_SCROLLBAR,
            FL_HOR_PLAIN_SCROLLBAR, FL_HOR_BASIC_SCROLLBAR,
            FL_VERT_BASIC_SCROLLBAR, FL_NORMAL_SCROLLBAR,
            FL_THIN_SCROLLBAR, FL_NICE_SCROLLBAR, FL_PLAIN_SCROLLBAR
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            label text of scrollbar

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            scrollbar flobject added

    Examples
    --------
        >>> scrbobj = fl_add_scrollbar(scrolltype, 182, 140, 50, 150,
                "MyScrollbar")

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_add_scrollbar = library.cfuncproto(
        library.load_so_libforms(), "fl_add_scrollbar",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_scrollbar(int type, FL_Coord x, FL_Coord y,
            FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.checkfatal_allowed_value_in_list(scrolltype, \
            xfdata.SCROLLTYPE_list)
    i_scrolltype = library.convert_to_intc(scrolltype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_stringc(label)
    library.keep_elem_refs(scrolltype, xpos, ypos, width, height, label, \
            i_scrolltype, i_xpos, i_ypos, i_width, i_height, s_label)
    retval = _fl_add_scrollbar(i_scrolltype, i_xpos, i_ypos, i_width, \
            i_height, s_label)
    return retval


def fl_get_scrollbar_value(ptr_flobject):
    """fl_get_scrollbar_value(ptr_flobject) -> scrvalue
    
    Finds out the current value of a scrollbar flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            scrollbar flobject

    Returns
    -------
        scrvalue : float
            scrollbar value

    Examples
    --------
        >>> val = fl_get_scrollbar_value(scrbobj)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_scrollbar_value = library.cfuncproto(
        library.load_so_libforms(), "fl_get_scrollbar_value",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
        """double fl_get_scrollbar_value(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_scrollbar_value(ptr_flobject)
    return retval


def fl_set_scrollbar_value(ptr_flobject, scrvalue):
    """fl_set_scrollbar_value(ptr_flobject, scrvalue)
    
    Defines the value of a scrollbar flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            scrollbar flobject
        scrvalue : float
            value of the scrollbar to be set. By default it is 0.5.

    Examples
    --------
        >>> fl_set_scrollbar_value(scrbobj, 0.75)

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_set_scrollbar_value = library.cfuncproto(
        library.load_so_libforms(), "fl_set_scrollbar_value",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_scrollbar_value(FL_OBJECT * ob, double val)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_scrvalue = library.convert_to_doublec(scrvalue)
    library.keep_elem_refs(ptr_flobject, scrvalue, f_scrvalue)
    _fl_set_scrollbar_value(ptr_flobject, f_scrvalue)


def fl_set_scrollbar_size(ptr_flobject, barsize):
    """fl_set_scrollbar_size(ptr_flobject, barsize)
    
    Controls the size of the sliding bar inside the box. This function
    does nothing if applied to scrollbars of type xfdata.FL_NICE_SCROLLBAR.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            scrollbar flobject
        barsize : float
            size of bar. Values between 0.0 and 1.0. The default is
            xfdata.FL_SLIDER_WIDTH (which is 0.15 for all scrollbars). If it
            is 1.0, the scrollbar covers the box completely and can no longer
            be moved.

    Examples
    --------
        >>> fl_set_scrollbar_size(scrbobj, 0.2)

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_set_scrollbar_size = library.cfuncproto(
        library.load_so_libforms(), "fl_set_scrollbar_size",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_scrollbar_size(FL_OBJECT * ob, double val)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_barsize= library.convert_to_doublec(barsize)
    library.keep_elem_refs(ptr_flobject, barsize, f_barsize)
    _fl_set_scrollbar_size(ptr_flobject, f_barsize)


def fl_set_scrollbar_increment(ptr_flobject, leftbtnval, midlbtnval):
    """fl_set_scrollbar_increment(ptr_flobject, leftbtnval, midlbtnval)
    
    Defines the size of the steps of a scrollbar jump. By default, if the
    mouse is pressed beside the the sliding bar, the bar starts to jumps
    in the direction of the mouse position.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            scrollbar flobject
        leftbtnval : float
            value to increment if the left mouse button is pressed
        midlbtnval : float
            value to increment if the middle mouse button is pressed

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_scrollbar_increment = library.cfuncproto(
        library.load_so_libforms(), "fl_set_scrollbar_increment",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
        """void fl_set_scrollbar_increment(FL_OBJECT * ob, double l,
           double r)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_leftbtnval = library.convert_to_doublec(leftbtnval)
    f_midlbtnval = library.convert_to_doublec(midlbtnval)
    library.keep_elem_refs(ptr_flobject, leftbtnval, midlbtnval, \
            f_leftbtnval, f_midlbtnval)
    _fl_set_scrollbar_increment(ptr_flobject, f_leftbtnval, f_midlbtnval)


def fl_get_scrollbar_increment(ptr_flobject):
    """fl_get_scrollbar_increment(ptr_flobject) -> leftbtnval, midbtnval
    
    Finds out the increment of size of a scrollbar for left and middle
    mouse buttons.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            scrollbar flobject

    Returns
    -------
        leftbtnval : float
            left button increment
        midbtnval : float
            middle button increment

    Examples
    --------
        >>> leftbv, midbv = fl_get_scrollbar_increment(scrbobj)

    API_diversion
    -------------
        API changed from XForms, upstream is
        fl_get_scrollbar_increment(ptr_flobject, leftbtnval, midlbtnval)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_scrollbar_increment = library.cfuncproto(
        library.load_so_libforms(), "fl_get_scrollbar_increment",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)],
        """void fl_get_scrollbar_increment(FL_OBJECT * ob, double * a,
           double * b)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_leftbtnval, ptr_leftbtnval = library.make_doublec_and_pointer()
    f_midlbtnval, ptr_midlbtnval = library.make_doublec_and_pointer()
    library.keep_elem_refs(ptr_flobject, f_leftbtnval, f_midlbtnval, \
            ptr_leftbtnval, ptr_midlbtnval)
    _fl_get_scrollbar_increment(ptr_flobject, ptr_leftbtnval, ptr_midlbtnval)
    return f_leftbtnval.value, f_midlbtnval.value


def fl_set_scrollbar_bounds(ptr_flobject, minbound, maxbound):
    """fl_set_scrollbar_bounds(ptr_flobject, minbound, maxbound)
    
    Defines the minimum and maximum value limits of a scrollbar flobject. For
    vertical sliders the slider position for the minimum value is at the left,
    for horizontal sliders at the top of the slider. By setting min to a
    larger value than max in a call of fl_set_scrollbar_bounds() this can be
    reversed. When this function is called, if the actual value of a scrollbar
    is not within the range of the new bounds, its value gets adjusted to the
    nearest limit.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            scrollbar flobject
        minbound : float
            minimum value bound of scrollbar. By default, the minimum
            value for a slider is 0.0.
        maxbound : float
            maximum value bound of scrollbar. By default, the maximum
            value for a slider is 1.0.

    Examples
    --------
        >>> fl_set_scrollbar_bounds(scrbobj, 1.0, 2.0)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_scrollbar_bounds = library.cfuncproto(
        library.load_so_libforms(), "fl_set_scrollbar_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
        """void fl_set_scrollbar_bounds(FL_OBJECT * ob, double b1, double
           b2)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_minbound = library.convert_to_doublec(minbound)
    f_maxbound = library.convert_to_doublec(maxbound)
    library.keep_elem_refs(ptr_flobject, minbound, maxbound, f_minbound, \
            f_maxbound)
    _fl_set_scrollbar_bounds(ptr_flobject, f_minbound, f_maxbound)


def fl_get_scrollbar_bounds(ptr_flobject):
    """fl_get_scrollbar_bounds(ptr_flobject) -> minbound, maxbound
    
    Finds out minimum and maximum value limits of a scrollbar flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            scrollbar flobject

    Returns
    -------
        minbound : float
            minimum value bound
        maxbound : float
            maximum value bound

    Examples
    --------
        >>> minb, maxb = fl_get_scrollbar_bounds(scrbobj)

    API_diversion
    -------------
        API changed from XForms, upstream is
        fl_get_scrollbar_bounds(ptr_flobject, b1, b2)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_scrollbar_bounds = library.cfuncproto(
        library.load_so_libforms(), "fl_get_scrollbar_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)],
        """void fl_get_scrollbar_bounds(FL_OBJECT * ob, double * b1,
           double * b2)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_minbound, ptr_minbound = library.make_doublec_and_pointer()
    f_maxbound, ptr_maxbound = library.make_doublec_and_pointer()
    library.keep_elem_refs(ptr_flobject, f_minbound, ptr_minbound, \
            f_maxbound, ptr_maxbound)
    _fl_get_scrollbar_bounds(ptr_flobject, ptr_minbound, ptr_maxbound)
    return f_minbound.value, f_maxbound.value


# fl_set_scrollbar_return function placeholder (internal)


def fl_set_scrollbar_step(ptr_flobject, step):
    """fl_set_scrollbar_step(ptr_flobject, step)
    
    Defines the step size of a scrollbar to which values are rounded.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            scrollbar flobject
        step : float
            rounded value.

    Examples
    --------
        >>> fl_set_scrollbar_step(scrbobj, 1)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_scrollbar_step = library.cfuncproto(
        library.load_so_libforms(), "fl_set_scrollbar_step",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_scrollbar_step(FL_OBJECT * ob, double step)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_step = library.convert_to_doublec(step)
    library.keep_elem_refs(ptr_flobject, step, f_step)
    _fl_set_scrollbar_step(ptr_flobject, f_step)

