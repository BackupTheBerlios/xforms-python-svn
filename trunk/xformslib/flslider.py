#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage slider objects.
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
# Interface to XForms shared object libraries   #
# ############################################# #


import ctypes as cty
from xformslib import library
from xformslib import xfdata


#######################
# forms.h (slider.h)
# Object Class: Slider
#######################

# Routines

# fl_create_slider function placeholder (internal)


def fl_add_slider(slidertype, x, y, w, h, label):
    """fl_add_slider(slidertype, x, y, w, h, label)
    
    Adds a slider to a form. No value is displayed.

    Parameters
    ----------
        slidertype : int
            type of slider to be added. Values (from xfdata.py)
            FL_VERT_SLIDER, FL_HOR_SLIDER, FL_VERT_FILL_SLIDER,
            FL_HOR_FILL_SLIDER, FL_VERT_NICE_SLIDER, FL_HOR_NICE_SLIDER,
            FL_VERT_BROWSER_SLIDER, FL_HOR_BROWSER_SLIDER,
            FL_VERT_BROWSER_SLIDER2,FL_HOR_BROWSER_SLIDER2,
            FL_VERT_THIN_SLIDER, FL_HOR_THIN_SLIDER, FL_VERT_THIN_SLIDER,
            FL_HOR_THIN_SLIDER, FL_VERT_NICE_SLIDER2, FL_HOR_NICE_SLIDER2,
            FL_VERT_BASIC_SLIDER, FL_HOR_BASIC_SLIDER
        x : int
            horizontal position (upper-left corner)
        y : int
            vertical position (upper-left corner)
        w : int
            width in coord units
        h : int
            height in coord units
        label : int
            label of the slider (placed below it by default)

    Returns
    -------
        pFlObject : pointer to xfdata.FL_OBJECT
            slider object added 

    Examples
    --------
        >>> sldobj = fl_add_slider(xfdata.FL_VERT_SLIDER, 200, 120, \
                30, 100, "MySlider")

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_add_slider = library.cfuncproto(
        library.load_so_libforms(), "fl_add_slider",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_slider(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.checkfatal_allowed_value_in_list(slidertype, \
            xfdata.SLIDERTYPE_list)
    islidertype = library.convert_to_int(slidertype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(slidertype, x, y, w, h, label, islidertype, \
            ix, iy, iw, ih, slabel)
    retval = _fl_add_slider(islidertype, ix, iy, iw, ih, slabel)
    return retval


# fl_create_valslider function placeholder (internal)


def fl_add_valslider(slidertype, x, y, w, h, label):
    """fl_add_valslider(slidertype, x, y, w, h, label)
    
    Adds a slider to a form. Its value is displayed above or to the left
    of the slider.

    Parameters
    ----------
        slidertype : int
            type of the slider. Values (from xfdata.py) FL_VERT_SLIDER,
            FL_HOR_SLIDER, FL_VERT_FILL_SLIDER, FL_HOR_FILL_SLIDER,
            FL_VERT_NICE_SLIDER, FL_HOR_NICE_SLIDER, FL_VERT_BROWSER_SLIDER,
            FL_HOR_BROWSER_SLIDER, FL_VERT_BROWSER_SLIDER2,
            FL_HOR_BROWSER_SLIDER2, FL_VERT_THIN_SLIDER, FL_HOR_THIN_SLIDER,
            FL_VERT_THIN_SLIDER, FL_HOR_THIN_SLIDER, FL_VERT_NICE_SLIDER2,
            FL_HOR_NICE_SLIDER2, FL_VERT_BASIC_SLIDER, FL_HOR_BASIC_SLIDER
        x : int
            horizontal position (upper-left corner)
        y : int
            vertical position (upper-left corner)
        w : int
            width in coord units
        h : int
            height in coord units
        label : str
            text label of slider

    Returns
    -------
        pFlObject : pointer to xfdata.FL_OBJECT
            slider with value object added

    Examples
    --------
        >>> sldobj = fl_add_valslider(xfdata.FL_VERT_SLIDER, 200, 120, \
                30, 100, "MyValSlider")

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_add_valslider = library.cfuncproto(
        library.load_so_libforms(), "fl_add_valslider",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_valslider(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.checkfatal_allowed_value_in_list(slidertype, \
            xfdata.SLIDERTYPE_list)
    islidertype = library.convert_to_int(slidertype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(slidertype, x, y, w, h, label, islidertype, \
            ix, iy, iw, ih, slabel)
    retval = _fl_add_valslider(islidertype, ix, iy, iw, ih, slabel)
    return retval


def fl_set_slider_value(pFlObject, val):
    """fl_set_slider_value(pFlObject, val)
    
    Changes the value of a slider.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            slider object
        val : float
            new value of slider

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_set_slider_value = library.cfuncproto(
        library.load_so_libforms(), "fl_set_slider_value",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_slider_value(FL_OBJECT * ob, double val)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    fval = library.convert_to_double(val)
    library.keep_elem_refs(pFlObject, val, fval)
    _fl_set_slider_value(pFlObject, fval)


def fl_get_slider_value(pFlObject):
    """fl_get_slider_value(pFlObject)
    
    Obtains value of a slider.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            slider object

    Returns
    -------
        val : float
            current value

    Examples
    --------
        >>> val = fl_get_slider_value(sldobj)

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_get_slider_value = library.cfuncproto(
        library.load_so_libforms(), "fl_get_slider_value",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
        """double fl_get_slider_value(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_slider_value(pFlObject)
    return retval


def fl_set_slider_bounds(pFlObject, minbound, maxbound):
    """fl_set_slider_bounds(pFlObject, minbound, maxbound)
    
    Sets minimum and maximum bounds/limits of a slider.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            slider object
        minbound : float
            minimum bound of slider
        maxbound : float
            maximum bound of slider

    Examples
    --------
        >>> fl_set_slider_bounds(sldobj, 10.0, 20.0)

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_set_slider_bounds = library.cfuncproto(
        library.load_so_libforms(), "fl_set_slider_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
        """void fl_set_slider_bounds(FL_OBJECT * ob, double min,
           double max)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    fminbound = library.convert_to_double(minbound)
    fmaxbound = library.convert_to_double(maxbound)
    library.keep_elem_refs(pFlObject, minbound, maxbound, fminbound, \
            fmaxbound)
    _fl_set_slider_bounds(pFlObject, fminbound, fmaxbound)


def fl_get_slider_bounds(pFlObject):
    """fl_get_slider_bounds(pFlObject)
    
    Obtains minimum and maximum bounds/limits of a slider.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            slider object

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
        API changed from XForms, upstream was
        fl_get_slider_bounds(pFlObject, minbound, maxbound)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_slider_bounds = library.cfuncproto(
        library.load_so_libforms(), "fl_get_slider_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)],
        """void fl_get_slider_bounds(FL_OBJECT * ob, double * min,
           double * max)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    minbound, pminbound = library.make_double_and_pointer()
    maxbound, pmaxbound = library.make_double_and_pointer()
    library.keep_elem_refs(pFlObject, minbound, maxbound, pminbound, \
            pmaxbound)
    _fl_get_slider_bounds(pFlObject, pminbound, pmaxbound)
    return minbound.value, maxbound.value


# fl_set_slider_return function placeholder (deprecated)


def fl_set_slider_step(pFlObject, step):
    """fl_set_slider_step(pFlObject, step)
    
    *todo*

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            slider object
        step : float
            step value

    Examples
    --------
        >>> fl_set_slider_step(sldobj, 0.5)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_slider_step = library.cfuncproto(
        library.load_so_libforms(), "fl_set_slider_step",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_slider_step(FL_OBJECT * ob, double value)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    fstep = library.convert_to_double(step)
    library.keep_elem_refs(pFlObject, step, fstep)
    _fl_set_slider_step(pFlObject, fstep)


def fl_set_slider_increment(pFlObject, leftbtnval, midbtnval):
    """fl_set_slider_increment(pFlObject, leftbtnval, midbtnval)
    
    *todo*

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            slider object
        leftbtnval : float
            value to increment if the left mouse button is pressed
        midbtnval : float
            value to increment if the middle mouse button is pressed

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_slider_increment = library.cfuncproto(
        library.load_so_libforms(), "fl_set_slider_increment",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
        """void fl_set_slider_increment(FL_OBJECT * ob, double l,
           double r)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    fleftbtnval = library.convert_to_double(leftbtnval)
    fmidbtnval = library.convert_to_double(midbtnval)
    library.keep_elem_refs(pFlObject, leftbtnval, midbtnval, fleftbtnval,
            fmidbtnval)
    _fl_set_slider_increment(pFlObject, fleftbtnval, fmidbtnval)


def fl_get_slider_increment(pFlObject):
    """fl_get_slider_increment(pFlObject)
    
    *todo*

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            slider object

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
        API changed from XForms, upstream was
        fl_get_slider_increment(pFlObject, leftbtnval, midlbtnval)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_slider_increment = library.cfuncproto(
        library.load_so_libforms(), "fl_get_slider_increment",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)], \
        """void fl_get_slider_increment(FL_OBJECT * ob, double * l,
           double * r)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    leftbtnval, pleftbtnval = library.make_double_and_pointer()
    midlbtnval, pmidlbtnval = library.make_double_and_pointer()
    library.keep_elem_refs(pFlObject, leftbtnval, midlbtnval, pleftbtnval,
            pmidlbtnval)
    _fl_get_slider_increment(pFlObject, pleftbtnval, pmidlbtnval)
    return leftbtnval.value, midlbtnval.value


def fl_set_slider_size(pFlObject, size):
    """fl_set_slider_size(pFlObject, size)
    
    Sets the size of a slider.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            slider object
        size : float
            value of size of the slider

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_set_slider_size = library.cfuncproto(
        library.load_so_libforms(), "fl_set_slider_size",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_slider_size(FL_OBJECT * ob, double size)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    fsize = library.convert_to_double(size)
    library.keep_elem_refs(pFlObject, size, fsize)
    _fl_set_slider_size(pFlObject, fsize)


def fl_set_slider_precision(pFlObject, precnum):
    """fl_set_slider_precision(pFlObject, prec)
    
    Sets precision which value a valslider is shown with.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            slider object
        prec : int
            precision of shown value

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_slider_precision = library.cfuncproto(
        library.load_so_libforms(), "fl_set_slider_precision",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_slider_precision(FL_OBJECT * ob, int prec)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    iprecnum = library.convert_to_int(precnum)
    library.keep_elem_refs(pFlObject, precnum, iprecnum)
    _fl_set_slider_precision(pFlObject, iprecnum)


def fl_set_slider_filter(pFlObject, py_ValFilter):
    """fl_set_slider_filter(pFlObject, py_ValFilter)
    
    Registers a filter function to show alues in a slider object. By
    default, slider value shown in floating point format)

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            slider object
        py_ValFilter : python function to show values in slider, returned value
            name referring to function(pFlObject, valfloat, intprecis) ->
            string

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    # FL_VAL_FILTER = cty.CFUNCTYPE(STRING, cty.POINTER(FL_OBJECT),
    #                               cty.c_double, cty.c_int)
    _fl_set_slider_filter = library.cfuncproto(
        library.load_so_libforms(), "fl_set_slider_filter",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.FL_VAL_FILTER],
        """void fl_set_slider_filter(FL_OBJECT * ob, FL_VAL_FILTER filter)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    library.verify_function_type(py_ValFilter)
    c_ValFilter = xfdata.FL_VAL_FILTER(py_ValFilter)
    library.keep_cfunc_refs(c_ValFilter, py_ValFilter)
    library.keep_elem_refs(pFlObject)
    _fl_set_slider_filter(pFlObject, c_ValFilter)


def fl_get_slider_repeat(pFlObject):
    """fl_get_slider_repeat(pFlObject)
    
    Obtains the time delay (in milliseconds) between jumps of the
    scrollbar knob when the mouse button is kept pressed down on the
    scrollbar outside of the knobs area. The delay for the very first
    jump is twice that long in order to avoid jumping to start too soon
    when only a single click was intended but the user is a bit slow in
    releasing the mouse button.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            slider object

    Returns
    -------
        tdelay : int
            time delay

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_slider_repeat = library.cfuncproto(
        library.load_so_libforms(), "fl_get_slider_repeat",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_slider_repeat(FL_OBJECT * obj)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_slider_repeat(pFlObject)
    return retval


def fl_set_slider_repeat(pFlObject, delay):
    """fl_set_slider_repeat(pFlObject, delay)
    
    Sets the time delay between jumps of the scrollbar knob when the
    mouse button is kept pressed down on the scrollbar outside of the
    knobs area. The delay for the very first jump is twice that long in
    order to avoid jumping to start too soon when only a single click
    was intended but the user is a bit slow in releasing the mouse button.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            slider object
        delay : int
            time delay (in milliseconds) to be set. The default value is
            100 ms.

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_slider_repeat = library.cfuncproto(
        library.load_so_libforms(), "fl_set_slider_repeat",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_get_slider_repeat(FL_OBJECT * obj, int)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    idelay = library.convert_to_int(delay)
    library.keep_elem_refs(pFlObject, delay, idelay)
    _fl_set_slider_repeat(pFlObject, idelay)

