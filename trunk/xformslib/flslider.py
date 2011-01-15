#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage slider flobjects.
"""

#    Copyright (C) 2009, 2010, 2011  Luca Lazzaroni "LukenShiro"
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
# Interface to XForms shared flobject libraries   #
# ############################################# #


import ctypes as cty
from xformslib import library
from xformslib import xfdata


#######################
# forms.h (slider.h)
# Object Class: Slider
#######################

# Routines

# fl_create_slider() function placeholder (internal)


def fl_add_slider(slidertype, xpos, ypos, width, height, label):
    """fl_add_slider(slidertype, xpos, ypos, width, height, label)
    -> ptr_flobject

    Adds a slider to a form. No value is displayed.

    Parameters
    ----------
        slidertype : int
            type of slider to be added. Values (from xfdata.py) FL_VERT_SLIDER
            (normal slider), FL_HOR_SLIDER (horizontal slider),
            FL_VERT_FILL_SLIDER (filled slider), FL_HOR_FILL_SLIDER (horizontal
            filled slider), FL_VERT_NICE_SLIDER (*todo*), FL_HOR_NICE_SLIDER
            (horizontal *todo*), FL_VERT_BROWSER_SLIDER (*todo*),
            FL_HOR_BROWSER_SLIDER (horizontal *todo*), FL_VERT_BROWSER_SLIDER2
            (for vertical scrollbar only), FL_HOR_BROWSER_SLIDER2 (for
            horizontal scrollbar only), FL_VERT_THIN_SLIDER (for vertical thin
            scrollbar only), FL_HOR_THIN_SLIDER (for horizontal thin scrollbar
            only), FL_VERT_NICE_SLIDER2 (for vertical nice scrollbar only),
            FL_HOR_NICE_SLIDER2 (for horizontal nice scrollbar only),
            FL_VERT_BASIC_SLIDER (for vertical plain scrollbar only),
            FL_HOR_BASIC_SLIDER (for horizontal plain scrollbar only).
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : int
            label of the slider (placed below it by default)

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            slider flobject added

    Examples
    --------
        >>> sldobj = fl_add_slider(xfdata.FL_VERT_SLIDER, 200, 120,
                30, 100, "MySlider")

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_add_slider = library.cfuncproto(
        library.load_so_libforms(), "fl_add_slider",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_slider(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_flinitialized()
    library.checkfatal_allowed_value_in_list(slidertype, \
            xfdata.SLIDERTYPE_list)
    i_slidertype = library.convert_to_intc(slidertype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_stringc(label)
    library.keep_elem_refs(slidertype, xpos, ypos, width, height, label, \
            i_slidertype, i_xpos, i_ypos, i_width, i_height, s_label)
    retval = _fl_add_slider(i_slidertype, i_xpos, i_ypos, i_width, \
            i_height, s_label)
    return retval


# fl_create_valslider() function placeholder (internal)


def fl_add_valslider(slidertype, xpos, ypos, width, height, label):
    """fl_add_valslider(slidertype, xpos, ypos, width, height, label)
    -> ptr_flobject

    Adds a slider to a form. Its value is displayed above or to the left of
    the slider.

    Parameters
    ----------
        slidertype : int
            type of the slider to be added. Values (from xfdata.py)
            FL_VERT_SLIDER (normal slider), FL_HOR_SLIDER (horizontal slider),
            FL_VERT_FILL_SLIDER (filled slider), FL_HOR_FILL_SLIDER (horizontal
            filled slider), FL_VERT_NICE_SLIDER (*todo*), FL_HOR_NICE_SLIDER
            (horizontal *todo*), FL_VERT_BROWSER_SLIDER (*todo*),
            FL_HOR_BROWSER_SLIDER (horizontal *todo*), FL_VERT_BROWSER_SLIDER2
            (for vertical scrollbar only), FL_HOR_BROWSER_SLIDER2 (for
            horizontal scrollbar only), FL_VERT_THIN_SLIDER (for vertical thin
            scrollbar only), FL_HOR_THIN_SLIDER (for horizontal thin scrollbar
            only), FL_VERT_NICE_SLIDER2 (for vertical nice scrollbar only),
            FL_HOR_NICE_SLIDER2 (for horizontal nice scrollbar only),
            FL_VERT_BASIC_SLIDER (for vertical plain scrollbar only),
            FL_HOR_BASIC_SLIDER (for horizontal plain scrollbar only).
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            text label of slider

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            slider with value flobject added

    Examples
    --------
        >>> sldobj = fl_add_valslider(xfdata.FL_VERT_SLIDER, 200, 120,
                30, 100, "MyValSlider")

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_add_valslider = library.cfuncproto(
        library.load_so_libforms(), "fl_add_valslider",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_valslider(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_flinitialized()
    library.checkfatal_allowed_value_in_list(slidertype, \
            xfdata.SLIDERTYPE_list)
    i_slidertype = library.convert_to_intc(slidertype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_stringc(label)
    library.keep_elem_refs(slidertype, xpos, ypos, width, height, label, \
            i_slidertype, i_xpos, i_ypos, i_width, i_height, s_label)
    retval = _fl_add_valslider(i_slidertype, i_xpos, i_ypos, i_width, \
            i_height, s_label)
    return retval


def fl_set_slider_value(ptr_flobject, slvalue):
    """fl_set_slider_value(ptr_flobject, slvalue)

    Changes the value of a slider.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            slider flobject
        slvalue : float
            new value of slider

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_set_slider_value = library.cfuncproto(
        library.load_so_libforms(), "fl_set_slider_value",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_slider_value(FL_OBJECT * ob, double val)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_slvalue = library.convert_to_doublec(slvalue)
    library.keep_elem_refs(ptr_flobject, slvalue, f_slvalue)
    _fl_set_slider_value(ptr_flobject, f_slvalue)


def fl_get_slider_value(ptr_flobject):
    """fl_get_slider_value(ptr_flobject) -> slvalue

    Finds out value of a slider.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            slider flobject

    Returns
    -------
        slvalue : float
            current value

    Examples
    --------
        >>> val = fl_get_slider_value(sldobj)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_get_slider_value = library.cfuncproto(
        library.load_so_libforms(), "fl_get_slider_value",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
        """double fl_get_slider_value(FL_OBJECT * ob)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_slider_value(ptr_flobject)
    return retval


def fl_set_slider_bounds(ptr_flobject, minbound, maxbound):
    """fl_set_slider_bounds(ptr_flobject, minbound, maxbound)

    Defines minimum and maximum value limits of a slider flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            slider flobject
        minbound : float
            minimum value bound of slider
        maxbound : float
            maximum value bound of slider

    Examples
    --------
        >>> fl_set_slider_bounds(sldobj, 10.0, 20.0)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_set_slider_bounds = library.cfuncproto(
        library.load_so_libforms(), "fl_set_slider_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
        """void fl_set_slider_bounds(FL_OBJECT * ob, double min,
           double max)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_minbound = library.convert_to_doublec(minbound)
    f_maxbound = library.convert_to_doublec(maxbound)
    library.keep_elem_refs(ptr_flobject, minbound, maxbound, f_minbound, \
            f_maxbound)
    _fl_set_slider_bounds(ptr_flobject, f_minbound, f_maxbound)


def fl_get_slider_bounds(ptr_flobject):
    """fl_get_slider_bounds(ptr_flobject) -> minbound, maxbound

    Finds out minimum and maximum value limits of a slider.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            slider flobject

    Returns
    -------
        minbound : float
            minimum bound
        maxbound : float
            maximum bound

    Examples
    --------
        >>> minb, maxb = fl_get_slider_bounds(sldobj)

    API_diversion
    ----------
        API changed from XForms, upstream is
        fl_get_slider_bounds(ptr_flobject, minbound, maxbound)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_get_slider_bounds = library.cfuncproto(
        library.load_so_libforms(), "fl_get_slider_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)],
        """void fl_get_slider_bounds(FL_OBJECT * ob, double * min,
           double * max)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_minbound, ptr_minbound = library.make_doublec_and_pointer()
    f_maxbound, ptr_maxbound = library.make_doublec_and_pointer()
    library.keep_elem_refs(ptr_flobject, f_minbound, f_maxbound, \
            ptr_minbound, ptr_maxbound)
    _fl_get_slider_bounds(ptr_flobject, ptr_minbound, ptr_maxbound)
    return f_minbound.value, f_maxbound.value


# fl_set_slider_return() function placeholder (deprecated)


def fl_set_slider_step(ptr_flobject, step):
    """fl_set_slider_step(ptr_flobject, step)

    Defines the step size to which values are rounded in the
    slider flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            slider flobject
        step : float
            step value

    Examples
    --------
        >>> fl_set_slider_step(sldobj, 0.5)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_set_slider_step = library.cfuncproto(
        library.load_so_libforms(), "fl_set_slider_step",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_slider_step(FL_OBJECT * ob, double value)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_step = library.convert_to_doublec(step)
    library.keep_elem_refs(ptr_flobject, step, f_step)
    _fl_set_slider_step(ptr_flobject, f_step)


def fl_set_slider_increment(ptr_flobject, leftbtnval, midbtnval):
    """fl_set_slider_increment(ptr_flobject, leftbtnval, midbtnval)

    Defines slider increments for clicks with left and middle mouse button.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            slider flobject
        leftbtnval : float
            value to increment if the left mouse button is pressed
        midbtnval : float
            value to increment if the middle mouse button is pressed

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_set_slider_increment = library.cfuncproto(
        library.load_so_libforms(), "fl_set_slider_increment",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
        """void fl_set_slider_increment(FL_OBJECT * ob, double l,
           double r)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_leftbtnval = library.convert_to_doublec(leftbtnval)
    f_midbtnval = library.convert_to_doublec(midbtnval)
    library.keep_elem_refs(ptr_flobject, leftbtnval, midbtnval, \
            f_leftbtnval, f_midbtnval)
    _fl_set_slider_increment(ptr_flobject, f_leftbtnval, f_midbtnval)


def fl_get_slider_increment(ptr_flobject):
    """fl_get_slider_increment(ptr_flobject) -> leftbtnval, midbtnval

    Finds out current slider increments for clicks with left and middle mouse
    buttons.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            slider flobject

    Returns
    -------
        leftbtnval : float
            left button increment
        midbtnval : float
            middle button increment

    Examples
    --------
        >>> *todo*

    API_diversion
    ----------
        API changed from XForms, upstream is
        fl_get_slider_increment(ptr_flobject, leftbtnval, midlbtnval)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_get_slider_increment = library.cfuncproto(
        library.load_so_libforms(), "fl_get_slider_increment",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)], \
        """void fl_get_slider_increment(FL_OBJECT * ob, double * l,
           double * r)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_leftbtnval, ptr_leftbtnval = library.make_doublec_and_pointer()
    f_midlbtnval, ptr_midlbtnval = library.make_doublec_and_pointer()
    library.keep_elem_refs(ptr_flobject, f_leftbtnval, f_midlbtnval, \
            ptr_leftbtnval, ptr_midlbtnval)
    _fl_get_slider_increment(ptr_flobject, ptr_leftbtnval, ptr_midlbtnval)
    return f_leftbtnval.value, f_midlbtnval.value


def fl_set_slider_size(ptr_flobject, size):
    """fl_set_slider_size(ptr_flobject, size)

    Defines the size of a slider flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            slider flobject
        size : float
            value of size of the slider

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_set_slider_size = library.cfuncproto(
        library.load_so_libforms(), "fl_set_slider_size",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_slider_size(FL_OBJECT * ob, double size)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_size = library.convert_to_doublec(size)
    library.keep_elem_refs(ptr_flobject, size, f_size)
    _fl_set_slider_size(ptr_flobject, f_size)


def fl_set_slider_precision(ptr_flobject, precis):
    """fl_set_slider_precision(ptr_flobject, precis)

    Defines the precision which value a valslider is shown with.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            slider flobject
        precis : int
            precision number of shown value after the dot.

    Examples
    --------
        >>> fl_set_slider_precision(sldobj, 3)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_set_slider_precision = library.cfuncproto(
        library.load_so_libforms(), "fl_set_slider_precision",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_slider_precision(FL_OBJECT * ob, int prec)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_precis = library.convert_to_intc(precis)
    library.keep_elem_refs(ptr_flobject, precis, i_precis)
    _fl_set_slider_precision(ptr_flobject, i_precis)


def fl_set_slider_filter(ptr_flobject, pyfn_ValFilter):
    """fl_set_slider_filter(ptr_flobject, pyfn_ValFilter)

    Registers a filter function to show values in a slider flobject. By
    default, slider value shown in floating point format.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            slider flobject
        pyfn_ValFilter : python function, returned value
            name referring to function(ptr_flobject, [float]value, [int]precis)
            -> [str]text
            function to show values in slider, text is what will be shown

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    # FL_VAL_FILTER = cty.CFUNCTYPE(xfdata.STRING, cty.POINTER(FL_OBJECT),
    #            cty.c_double, cty.c_int)
    _fl_set_slider_filter = library.cfuncproto(
        library.load_so_libforms(), "fl_set_slider_filter",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.FL_VAL_FILTER],
        """void fl_set_slider_filter(FL_OBJECT * ob, FL_VAL_FILTER filter)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.verify_function_type(pyfn_ValFilter)
    cfn_ValFilter = xfdata.FL_VAL_FILTER(pyfn_ValFilter)
    library.keep_cfunc_refs(cfn_ValFilter, pyfn_ValFilter)
    library.keep_elem_refs(ptr_flobject)
    _fl_set_slider_filter(ptr_flobject, cfn_ValFilter)


def fl_get_slider_repeat(ptr_flobject):
    """fl_get_slider_repeat(ptr_flobject) -> tdelay

    Finds out the time delay (in milliseconds) between jumps of the scrollbar
    knob when the mouse button is kept pressed down on the scrollbar outside
    of the knobs area. The delay for the very first jump is twice that long in
    order to avoid jumping to start too soon when only a single click was
    intended but the user is a bit slow in releasing the mouse button.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            slider flobject

    Returns
    -------
        tdelay : int
            time delay in millisecs

    Examples
    --------
        >>> msecs = fl_get_slider_repeat(pslobj)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_get_slider_repeat = library.cfuncproto(
        library.load_so_libforms(), "fl_get_slider_repeat",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_slider_repeat(FL_OBJECT * obj)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_slider_repeat(ptr_flobject)
    return retval


def fl_set_slider_repeat(ptr_flobject, tdelay):
    """fl_set_slider_repeat(ptr_flobject, tdelay)

    Defines the time delay between jumps of the scrollbar knob when the mouse
    button is kept pressed down on the scrollbar outside of the knobs area.
    The delay for the very first jump is twice that long in order to avoid
    jumping to start too soon when only a single click was intended but the
    user is a bit slow in releasing the mouse button.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            slider flobject
        tdelay : int
            time delay (in milliseconds) to be set. Default value is 100 ms

    Examples
    --------
        >>> fl_set_slider_repeat(pslobj, 200)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_set_slider_repeat = library.cfuncproto(
        library.load_so_libforms(), "fl_set_slider_repeat",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_get_slider_repeat(FL_OBJECT * obj, int)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_tdelay = library.convert_to_intc(tdelay)
    library.keep_elem_refs(ptr_flobject, tdelay, i_tdelay)
    _fl_set_slider_repeat(ptr_flobject, i_tdelay)

