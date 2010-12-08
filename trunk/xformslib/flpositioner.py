#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage positioner objects.
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


#########################
# forms.h (positioner.h)
#########################

# Routines

# fl_create_positioner function placeholder (internal)


def fl_add_positioner(postype, x, y, w, h, label):
    """fl_add_positioner(postype, x, y, w, h, label)
    
    Adds a positioner object. By default the label is placed below
    the box.

    Parameters
    ----------
        postype : int
            type of positioner to be added. Values (from xfdata.py)
            FL_NORMAL_POSITIONER, FL_OVERLAY_POSITIONER,
            FL_INVISIBLE_POSITIONER
        x : int
            horizontal position (upper-left corner)
        y : int
            vertical position (upper-left corner)
        w : int
            width in coord units
        h : int
            height in coord units
        label : str
            text label of positioner.

    Returns
    -------
        pFlObject : pointer to xfdata.FL_OBJECT
            positioner object added

    Examples
    --------
        >>> pstobj = fl_add_positioner(xfdata.FL_NORMAL_POSITIONER, \
                140, 120, 180, 180, "MyPositioner")

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_add_positioner = library.cfuncproto(
        library.load_so_libforms(), "fl_add_positioner",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_positioner(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.checkfatal_allowed_value_in_list(postype, \
            xfdata.POSITIONERTYPE_list)
    ipostype = library.convert_to_int(postype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(postype, x, y, w, h, label, ipostype, ix, iy,
            iw, ih, slabel)
    retval = _fl_add_positioner(ipostype, ix, iy, iw, ih, slabel)
    return retval


def fl_set_positioner_xvalue(pFlObject, val):
    """fl_set_positioner_xvalue(pFlObject, val)
    
    Sets the actual value of positioner object in horizontal direction.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            positioner object
        val : float
            value to be set. By default it is 0.5.

    Examples
    --------
        >>> fl_set_positioner_xvalue(pstobj, 0.1)

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_set_positioner_xvalue = library.cfuncproto(
        library.load_so_libforms(), "fl_set_positioner_xvalue",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_positioner_xvalue(FL_OBJECT * ob, double val)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    fval = library.convert_to_double(val)
    library.keep_elem_refs(pFlObject, val, fval)
    _fl_set_positioner_xvalue(pFlObject, fval)


def fl_get_positioner_xvalue(pFlObject):
    """fl_get_positioner_xvalue(pFlObject)
    
    Obtains value of positioner object in horizontal direction.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            positioner object

    Returns
    -------
        value : float
            value in horizontal direction

    Examples
    --------
        >>> val = fl_get_positioner_xvalue(pstobj)

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_get_positioner_xvalue = library.cfuncproto(
        library.load_so_libforms(), "fl_get_positioner_xvalue",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
        """double fl_get_positioner_xvalue(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_positioner_xvalue(pFlObject)
    return retval


def fl_set_positioner_xbounds(pFlObject, minbound, maxbound):
    """fl_set_positioner_xbounds(pFlObject, minbound, maxbound)
    
    Sets minimum and maximum bounds/limits of a positioner in horizontal
    direction.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            positioner object
        minbound : float
            minimum bound to be set. By default the minimum value is 0.0.
        maxbound : float
            maximum bound to be set. By default the maximum value is 1.0.

    Examples
    --------
        >>> fl_set_positioner_xbounds(pstobj, 1.0, 1.5)

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_set_positioner_xbounds = library.cfuncproto(
        library.load_so_libforms(), "fl_set_positioner_xbounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
        """void fl_set_positioner_xbounds(FL_OBJECT * ob, double min,
            double max)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    fminbound = library.convert_to_double(minbound)
    fmaxbound = library.convert_to_double(maxbound)
    library.keep_elem_refs(pFlObject, minbound, maxbound, fminbound, \
            fmaxbound)
    _fl_set_positioner_xbounds(pFlObject, fminbound, fmaxbound)


def fl_get_positioner_xbounds(pFlObject):
    """fl_get_positioner_xbounds(pFlObject)
    
    Obtain minumum and maximum bounds/limits of a positioner in horizontal
    direction.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            positioner object

    Returns
    -------
        minbound : float
            minimum bound
        maxbound : float
            maximum bound

    Examples
    --------
        >>> minb, maxb = fl_get_positioner_xbounds(pstobj)

    API_diversion
    ----------
        API changed from XForms, upstream was
        fl_get_positioner_xbounds(pFlObject, minbound, maxbound)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_positioner_xbounds = library.cfuncproto(
        library.load_so_libforms(), "fl_get_positioner_xbounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)],
        """void fl_get_positioner_xbounds(FL_OBJECT * ob, double * min,
        double * max)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    minbound, pminbound = library.make_double_and_pointer()
    maxbound, pmaxbound = library.make_double_and_pointer()
    library.keep_elem_refs(pFlObject, minbound, maxbound, pminbound,
                        pmaxbound)
    _fl_get_positioner_xbounds(pFlObject, pminbound, pmaxbound)
    return minbound.value, maxbound.value


def fl_set_positioner_yvalue(pFlObject, val):
    """fl_set_positioner_yvalue(pFlObject, val)
    
    Sets the actual value of positioner object in vertical direction.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            positioner object
        val : float
            value to be set. By default it is 0.5.

    Examples
    --------
        >>> fl_set_positioner_yvalue(pstobj, 1.0)

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_set_positioner_yvalue = library.cfuncproto(
        library.load_so_libforms(), "fl_set_positioner_yvalue",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_positioner_yvalue(FL_OBJECT * ob, double val)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    fval = library.convert_to_double(val)
    library.keep_elem_refs(pFlObject, val, fval)
    _fl_set_positioner_yvalue(pFlObject, fval)


def fl_get_positioner_yvalue(pFlObject):
    """fl_get_positioner_yvalue(pFlObject)
    
    Obtains value of positioner object in vertical direction.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            positioner object

    Returns
    -------
        value : float
            value in vertical direction

    Examples
    --------
        >>> val = fl_get_positioner_yvalue(pstobj)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_positioner_yvalue = library.cfuncproto(
        library.load_so_libforms(), "fl_get_positioner_yvalue",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
        """double fl_get_positioner_yvalue(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_positioner_yvalue(pFlObject)
    return retval


def fl_set_positioner_ybounds(pFlObject, minbound, maxbound):
    """fl_set_positioner_ybounds(pFlObject, minbound, maxbound)
    
    Sets minimum and maximum bounds/limits of a positioner in vertical
    direction.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            positioner object
        minbound : float
            minimum bound to be set. By default the minimum value is 0.0.
        maxbound : float
            maximum bound to be set. By default the maximum value is 1.0.

    Examples
    --------
        >>> fl_set_positioner_ybounds(pstobj, 0.5, 1.5)

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_set_positioner_ybounds = library.cfuncproto(
        library.load_so_libforms(), "fl_set_positioner_ybounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
        """void fl_set_positioner_ybounds(FL_OBJECT * ob, double min,
           double max)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    fminbound = library.convert_to_double(minbound)
    fmaxbound = library.convert_to_double(maxbound)
    library.keep_elem_refs(pFlObject, minbound, maxbound, fminbound,
                        fmaxbound)
    _fl_set_positioner_ybounds(pFlObject, fminbound, fmaxbound)


def fl_get_positioner_ybounds(pFlObject):
    """fl_get_positioner_ybounds(pFlObject)
    
    Obtain minimum and maximum bounds/limits of a positioner in vertical
    direction.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            positioner object

    Returns
    -------
        minbound : float
            minimum bound
        maxbound : float
            maximum bound

    Examples
    --------
        >>> minb, maxb = fl_get_positioner_ybounds(pstobj)

    API_diversion
    ----------
        API changed from XForms, upstream was
        fl_get_positioner_ybounds(pFlObject, minbound, maxbound)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_positioner_ybounds = library.cfuncproto(
        library.load_so_libforms(), "fl_get_positioner_ybounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)],
        """void fl_get_positioner_ybounds(FL_OBJECT * ob, double * min,
           double * max)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    minbound, pminbound = library.make_double_and_pointer()
    maxbound, pmaxbound = library.make_double_and_pointer()
    library.keep_elem_refs(pFlObject, minbound, maxbound, pminbound, \
            pmaxbound)
    _fl_get_positioner_ybounds(pFlObject, pminbound, pmaxbound)
    return minbound.value, maxbound.value


def fl_set_positioner_xstep(pFlObject, step):
    """fl_set_positioner_xstep(pFlObject, step)
    
    Handles positioner values in horizontal direction to be rounded to some
    values (multiples of step), e.g. to integer values.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            positioner object
        step : float
            rounded value. If it is 0.0, switch off rounding.

    Examples
    --------
        >>> fl_set_positioner_xstep(pstobj, 0.0)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_positioner_xstep = library.cfuncproto(
        library.load_so_libforms(), "fl_set_positioner_xstep",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_positioner_xstep(FL_OBJECT * ob, double value)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    fstep = library.convert_to_double(step)
    library.keep_elem_refs(pFlObject, step, fstep)
    _fl_set_positioner_xstep(pFlObject, fstep)


def fl_set_positioner_ystep(pFlObject, step):
    """fl_set_positioner_ystep(pFlObject, step)
    
    Handles positioner values in vertical direction to be rounded to some
    values (multiples of step), e.g. to integer values.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            positioner object
        step : float
            rounded value. If it is 0.0, switch off rounding.

    Examples
    --------
        >>> fl_set_positioner_ystep(pstobj, 0.0)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_positioner_ystep = library.cfuncproto(
        library.load_so_libforms(), "fl_set_positioner_ystep",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_positioner_ystep(FL_OBJECT * ob, double value)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    fstep = library.convert_to_double(step)
    library.keep_elem_refs(pFlObject, step, fstep)
    _fl_set_positioner_ystep(pFlObject, fstep)

# fl_set_positioner_return function placeholder (deprecated)

