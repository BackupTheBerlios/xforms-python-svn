#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage counters.
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


######################
# forms.h (counter.h)
######################

# Routines

# fl_create_counter function placeholder (internal)


def fl_add_counter(countertype, xpos, ypos, width, height, label):
    """fl_add_counter(countertype, xpos, ypos, width, height, label)
    -> ptr_flobject
    Adds a counter flobject.

    Parameters
    ----------
        countertype : int
            type of counter to be added. Values (from xfdata.py)
            FL_NORMAL_COUNTER (A counter with two buttons on each side),
            FL_SIMPLE_COUNTER (A counter with one button on each side).
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            text label of counter

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            counter flobject added

    Examples
    --------
        >>> ctrobj = fl_add_counter(FL_NORMAL_COUNTER, 142, 230, 142,
                100, "My Counter")

    Notes
    -----
        Status: Tested + Doc + Demo = OK

    """
    _fl_add_counter = library.cfuncproto(
        library.load_so_libforms(), "fl_add_counter",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_counter(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.checkfatal_allowed_value_in_list(countertype, \
            xfdata.COUNTERTYPE_list)
    i_countertype = library.convert_to_intc(countertype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_stringc(label)
    library.keep_elem_refs(countertype, xpos, ypos, width, height, label, \
            i_countertype, i_xpos, i_ypos, i_width, i_height, s_label)
    retval = _fl_add_counter(i_countertype, i_xpos, i_ypos, i_width, \
            i_height, s_label)
    return retval


def fl_set_counter_value(ptr_flobject, val):
    """fl_set_counter_value(ptr_flobject, val)

    Defines the value of the counter flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            counter flobject
        val : float
            value to be set. By default it is 0.

    Examples
    --------
        >>> fl_set_counter_value(ctrobj, 42.0)

    Notes
    -----
        Status: Tested + Doc + Demo = OK

    """
    _fl_set_counter_value = library.cfuncproto(
        library.load_so_libforms(), "fl_set_counter_value",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_counter_value(FL_OBJECT * ob, double val)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_val = library.convert_to_doublec(val)
    library.keep_elem_refs(ptr_flobject, val, f_val)
    _fl_set_counter_value(ptr_flobject, f_val)


def fl_set_counter_bounds(ptr_flobject, minbound, maxbound):
    """fl_set_counter_bounds(ptr_flobject, minbound, maxbound)

    Defines the minimum and maximum values that the counter will take. For
    conflicting settings bound takes precedence over value.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            counter flobject
        minbound : float
            minimum value to be set. By default it is -1000000.
        maxbound : float
            maximum value to be set. By default it is 1000000.

    Examples
    --------
        >>> fl_set_counter_bounds(ctrobj, -100.0, 100.0)

    Notes
    -----
        Status: Tested + Doc + Demo = OK

    """
    _fl_set_counter_bounds = library.cfuncproto(
        library.load_so_libforms(), "fl_set_counter_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
        """void fl_set_counter_bounds(FL_OBJECT * ob, double min,
           double max)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_minbound = library.convert_to_doublec(minbound)
    f_maxbound = library.convert_to_doublec(maxbound)
    library.keep_elem_refs(ptr_flobject, minbound, maxbound, f_minbound, \
            f_maxbound)
    _fl_set_counter_bounds(ptr_flobject, f_minbound, f_maxbound)


def fl_set_counter_step(ptr_flobject, smallsize, largesize):
    """fl_set_counter_step(ptr_flobject, smallsize, largesize)

    Defines the sizes of the small and large steps of a counter. For simple
    counters only the small step is used.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            counter flobject
        smallsize : float
            small step's size. By default it is 0.1.
        largesize : float
            large step's size. By default it is 1.

    Examples
    --------
        >>> fl_set_counter_step(ctrobj, 0.2, 2)

    Notes
    -----
        Status: Tested + Doc + Demo = OK

    """
    _fl_set_counter_step = library.cfuncproto(
        library.load_so_libforms(), "fl_set_counter_step",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
        """void fl_set_counter_step(FL_OBJECT * ob, double s, double l)""")
    library.verify_flobjectptr_type(ptr_flobject)
    f_smallsize = library.convert_to_doublec(smallsize)
    f_largesize = library.convert_to_doublec(largesize)
    library.keep_elem_refs(ptr_flobject, smallsize, largesize, f_smallsize,
            f_largesize)
    _fl_set_counter_step(ptr_flobject, f_smallsize, f_largesize)


def fl_set_counter_precision(ptr_flobject, precis):
    """fl_set_counter_precision(ptr_flobject, precis)

    Defines the precision (number of digits after the dot) with which
    the counter value is displayed.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            counter flobject
        precis : int
            precision to be set

    Examples
    --------
        >>> fl_set_counter_precision(ctrobj, 2)

    Notes
    -----
        Status: Tested + Doc + Demo = OK

    """
    _fl_set_counter_precision = library.cfuncproto(
        library.load_so_libforms(), "fl_set_counter_precision",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_counter_precision(FL_OBJECT * ob, int prec)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_precis = library.convert_to_intc(precis)
    library.keep_elem_refs(ptr_flobject, precis, i_precis)
    _fl_set_counter_precision(ptr_flobject, i_precis)


def fl_get_counter_precision(ptr_flobject):
    """fl_get_counter_precision(ptr_flobject) -> precis

    Finds out the current value of the precision (number of digits after
    the dot) of the counter.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            counter flobject

    Returns
    -------
        precis : int
            number of digits after the dot

    Examples
    --------
        >>> currprec = fl_get_counter_precision(ctrobj)

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_get_counter_precision = library.cfuncproto(
        library.load_so_libforms(), "fl_get_counter_precision",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_counter_precision(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_counter_precision(ptr_flobject)
    return retval


# fl_set_counter_return function placeholder (deprecated)


def fl_get_counter_value(ptr_flobject):
    """fl_get_counter_value(ptr_flobject) -> value

    Finds out the current value of the counter.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            counter flobject

    Returns
    -------
        value : float
            current value of counter

    Examples
    --------
        >>> currvalue = fl_get_counter_value(ctrobj)

    Notes
    -----
        Status: Tested + Doc + Demo = OK

    """
    _fl_get_counter_value = library.cfuncproto(
        library.load_so_libforms(), "fl_get_counter_value",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
        """double fl_get_counter_value(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_counter_value(ptr_flobject)
    return retval


def fl_get_counter_bounds(ptr_flobject):
    """fl_get_counter_bounds(ptr_flobject) -> minbound, maxbound

    Finds out the current minimum and maximum bounds of the counter.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            counter flobject

    Returns
    -------
        minbound : float
            minimum limit
        maxbound : float
            maximum limit

    Examples
    --------
        >>> minb, maxb = fl_get_counter_bounds(ctrobj)

    API_diversion
    ----------
        API changed from XForms, upstream is
        fl_get_counter_bounds(ptr_flobject, minbound, maxbound)

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_get_counter_bounds = library.cfuncproto(
        library.load_so_libforms(), "fl_get_counter_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)],
        """void fl_get_counter_bounds(FL_OBJECT * ob, double * min,
           double * max)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_minbound, ptr_minbound = library.make_doublec_and_pointer()
    f_maxbound, ptr_maxbound = library.make_doublec_and_pointer()
    library.keep_elem_refs(ptr_flobject, f_minbound, f_maxbound, \
            ptr_minbound, ptr_maxbound)
    _fl_get_counter_bounds(ptr_flobject, ptr_minbound, ptr_maxbound)
    return f_minbound.value, f_maxbound.value


def fl_get_counter_step(ptr_flobject):
    """fl_get_counter_step(ptr_flobject) -> smallsize, largesize

    Finds out the current small and large step's sizes of a counter.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            counter flobject

    Returns
    -------
        smallsize : float
            small step size
        largesize : float
            large step size

    Examples
    --------
        >>> smlsz, lrgsz = fl_get_counter_step(ctrobj)

    API_diversion
    ----------
        API changed from XForms, upstream is
        fl_get_counter_step(ptr_flobject, sml, lrg)

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_get_counter_step = library.cfuncproto(
        library.load_so_libforms(), "fl_get_counter_step",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)],
        """void fl_get_counter_step(FL_OBJECT * ob, double * s,
           double * l)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_smallsize, ptr_smallsize = library.make_doublec_and_pointer()
    f_largesize, ptr_largesize = library.make_doublec_and_pointer()
    library.keep_elem_refs(ptr_flobject, f_smallsize, f_largesize, \
            ptr_smallsize, ptr_largesize)
    _fl_get_counter_step(ptr_flobject, ptr_smallsize, ptr_largesize)
    return f_smallsize.value, f_largesize.value


def fl_set_counter_filter(ptr_flobject, pyfn_ValFilter):
    """fl_set_counter_filter(ptr_flobject, pyfn_ValFilter)

    Overrides the format and value shown by the counter. By default the
    value is shown in floating point format.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            counter flobject
        pyfn_ValFilter : python callback function, returned value
            name referring to function(ptr_flobject, valfloat, intprec) -> str

    Examples
    --------
        >>> def ctrvalfilt(pobj, fvalue, prec):
        >>> ... <something>
        >>> ... return string
        >>> fl_set_counter_filter(ctrobj, ctrvalfilt)

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    #FL_VAL_FILTER = cty.CFUNCTYPE(xfdata.STRING, \
    #           cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_int)
    _fl_set_counter_filter = library.cfuncproto(
        library.load_so_libforms(), "fl_set_counter_filter",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.FL_VAL_FILTER],
        """void fl_set_counter_filter(FL_OBJECT * ob,
           FL_VAL_FILTER filter)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.verify_function_type(pyfn_ValFilter)
    cfn_ValFilter = xfdata.FL_VAL_FILTER(pyfn_ValFilter)
    library.keep_cfunc_refs(cfn_ValFilter, pyfn_ValFilter)
    library.keep_elem_refs(ptr_flobject)
    _fl_set_counter_filter(ptr_flobject, cfn_ValFilter)


# Functions to set and get the timeout value used by the
# counter code to control modification of the counter value.

def fl_get_counter_repeat(ptr_flobject):
    """fl_get_counter_repeat(ptr_flobject) -> tdelay

    Finds out the initial delay of the counter.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            counter flobject

    Returns
    -------
        tdelay : int
            initial delay in milliseconds

    Examples
    --------
        >>> intdly = fl_get_counter_repeat(ctrobj)

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_get_counter_repeat = library.cfuncproto(
        library.load_so_libforms(), "fl_get_counter_repeat",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_counter_repeat(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_counter_repeat(ptr_flobject)
    return retval


def fl_set_counter_repeat(ptr_flobject, tdelay):
    """fl_set_counter_repeat(ptr_flobject, tdelay)

    Defines the initial delay of a counter. By default the counter value
    changes first slowly and the rate of change then accelerates until a
    final speed is reached. The default delay between the value changing
    is 600 ms at the start.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            counter flobject
        tdelay : int
            initial delay in milliseconds

    Examples
    --------
        >>> fl_set_counter_repeat(ctrobj, 200)

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_set_counter_repeat = library.cfuncproto(
        library.load_so_libforms(), "fl_set_counter_repeat",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_counter_repeat(FL_OBJECT * ob, int millisec)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_tdelay = library.convert_to_intc(tdelay)
    library.keep_elem_refs(ptr_flobject, tdelay, i_tdelay)
    _fl_set_counter_repeat(ptr_flobject, i_tdelay)


def fl_get_counter_min_repeat(ptr_flobject):
    """fl_get_counter_min_repeat(ptr_flobject) -> fdelay

    Finds out the final delay of a counter flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            counter flobject

    Returns
    -------
        fdelay : int
            final delay in milliseconds

    Examples
    --------
        >>> fnldly = fl_get_counter_min_repeat(ctrobj)

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_get_counter_min_repeat = library.cfuncproto(
        library.load_so_libforms(), "fl_get_counter_min_repeat",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_counter_min_repeat(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_counter_min_repeat(ptr_flobject)
    return retval


def fl_set_counter_min_repeat(ptr_flobject, fdelay):
    """fl_set_counter_min_repeat(ptr_flobject, fdelay)

    Defines the final delay of a counter. By default the counter value
    changes first slowly and the rate of change then accelerates until
    a final speed is reached. The default the final delay is 50 ms.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            counter flobject
        fdelay : int
            final delay in milliseconds

    Examples
    --------
        >>> fl_set_counter_min_repeat(ctrobj, 100)

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_set_counter_min_repeat = library.cfuncproto(
        library.load_so_libforms(), "fl_set_counter_min_repeat",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_counter_min_repeat(FL_OBJECT * ob, int millisec)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_fdelay = library.convert_to_intc(fdelay)
    library.keep_elem_refs(ptr_flobject, fdelay, i_fdelay)
    _fl_set_counter_min_repeat(ptr_flobject, i_fdelay)


def fl_get_counter_speedjump(ptr_flobject):
    """fl_get_counter_speedjump(ptr_flobject)

    Finds out the setting for speedjumping.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            counter flobject

    Returns
    -------
        speedjmp : int
            setting flag of speedjump (1 if set, or 0 if unset)

    Examples
    --------
        >>> isspdjmp = fl_get_counter_speedjump(ctrobj)

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_get_counter_speedjump = library.cfuncproto(
        library.load_so_libforms(), "fl_get_counter_speedjump",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_counter_speedjump(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_counter_speedjump(ptr_flobject)
    return retval


def fl_set_counter_speedjump(ptr_flobject, yesno):
    """fl_set_counter_speedjump(ptr_flobject, yesno)

    Makes only the first change of the counter has a different delay
    from all the following ones. The delay for the first change of the
    counter value will then be the one set by fl_set_counter_repeat()
    and the following delays last as long as set by
    fl_set_counter_min_repeat().

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            counter flobject
        yesno : int
            flag. Values 1 (to set speedjump) or 0 (to unset speedjump)

    Examples
    --------
        >>> fl_set_counter_speedjump(ctrobj, 1)

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_set_counter_speedjump = library.cfuncproto(
        library.load_so_libforms(), "fl_set_counter_speedjump",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_counter_speedjump(FL_OBJECT * ob, int yes_no)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_yesno = library.convert_to_intc(yesno)
    library.keep_elem_refs(ptr_flobject, yesno, i_yesno)
    _fl_set_counter_speedjump(ptr_flobject, i_yesno)

