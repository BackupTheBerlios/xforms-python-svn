#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage counters.

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


######################
# forms.h (counter.h)
######################

# Routines

# fl_create_counter function placeholder (internal)


def fl_add_counter(countertype, x, y, w, h, label):
    """Adds a counter object.

    --

    :Parameters:
      `countertype` : int
        type of counter to be added. Values (from xfdata.py) FL_NORMAL_COUNTER,
        FL_SIMPLE_COUNTER
      `x` : int
        horizontal position (upper-left corner)
      `y` : int
        vertical position (upper-left corner)
      `w` : int
        width in coord units
      `h` : int
        height in coord units
      `label` : str
        text label of counter

    :return: counter object added (pFlObject)
    :rtype: pointer to xfdata.FL_OBJECT

    :note: e.g. ctrobj = fl_add_counter(FL_NORMAL_COUNTER, 142, 230, 142,
        100, "My Counter")

    :status: Tested + Doc + Demo = OK

    """
    _fl_add_counter = libr.cfuncproto(
        libr.load_so_libforms(), "fl_add_counter",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_counter(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    libr.check_if_initialized()
    libr.check_admitted_value_in_list(countertype, xfdata.COUNTERTYPE_list)
    icountertype = libr.convert_to_int(countertype)
    ix = libr.convert_to_FL_Coord(x)
    iy = libr.convert_to_FL_Coord(y)
    iw = libr.convert_to_FL_Coord(w)
    ih = libr.convert_to_FL_Coord(h)
    slabel = libr.convert_to_string(label)
    libr.keep_elem_refs(countertype, x, y, w, h, label, icountertype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_counter(icountertype, ix, iy, iw, ih, slabel)
    return retval


def fl_set_counter_value(pFlObject, val):
    """Sets the value of the counter.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        counter object
      `val` : float
        value to be set. By default it is 0.

    :note: e.g. fl_set_counter_value(ctrobj, 42.0)

    :status: Tested + Doc + Demo = OK

    """
    _fl_set_counter_value = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_counter_value",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_counter_value(FL_OBJECT * ob, double val)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    fval = libr.convert_to_double(val)
    libr.keep_elem_refs(pFlObject, val, fval)
    _fl_set_counter_value(pFlObject, fval)


def fl_set_counter_bounds(pFlObject, minbound, maxbound):
    """Sets the minimum and maximum values that the counter will take. For
    conficting settings bound take precedence over value.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        counter object
      `minbound` : float
        minimum value to be set. By default it is -1000000.
      `maxbound` : float
        maximum value to be set. By default it is 1000000.

    :note: e.g. fl_set_counter_bounds(ctrobj, -100.0, 100.0)

    :status: Tested + Doc + Demo = OK

    """
    _fl_set_counter_bounds = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_counter_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
        """void fl_set_counter_bounds(FL_OBJECT * ob, double min,
           double max)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    fminbound = libr.convert_to_double(minbound)
    fmaxbound = libr.convert_to_double(maxbound)
    libr.keep_elem_refs(pFlObject, minbound, maxbound, fminbound, fmaxbound)
    _fl_set_counter_bounds(pFlObject, fminbound, fmaxbound)


def fl_set_counter_step(pFlObject, small, large):
    """Sets the sizes of the small and large steps of a counter. For simple
    counters only the small step is used.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        counter object
      `small` : float
        small step's size. By default it is 0.1.
      `large` : float
        large step's size. By default it is 1.

    :note: e.g. fl_set_counter_step(ctrobj, 0.2, 2)

    :status: Tested + Doc + Demo = OK

    """
    _fl_set_counter_step = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_counter_step",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
        """void fl_set_counter_step(FL_OBJECT * ob, double s, double l)""")
    libr.verify_flobjectptr_type(pFlObject)
    fsmall = libr.convert_to_double(small)
    flarge = libr.convert_to_double(large)
    libr.keep_elem_refs(pFlObject, small, large, fsmall, flarge)
    _fl_set_counter_step(pFlObject, fsmall, flarge)


def fl_set_counter_precision(pFlObject, prec):
    """Sets the precision (number of digits after the dot) with which
    the counter value is displayed.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        counter object
      `prec` : int
        precision to be set

    :note: e.g. fl_set_counter_precision(ctrobj, 2)

    :status: Tested + Doc + Demo = OK

    """
    _fl_set_counter_precision = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_counter_precision",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_counter_precision(FL_OBJECT * ob, int prec)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    iprec = libr.convert_to_int(prec)
    libr.keep_elem_refs(pFlObject, prec, iprec)
    _fl_set_counter_precision(pFlObject, iprec)


def fl_get_counter_precision(pFlObject):
    """Determines the current value of the precision (number of digits
    after the dot) of the counter.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        counter object

    :return: number of digits after the dot
    :rtype: int

    :note: e.g. currprec = fl_get_counter_precision(ctrobj)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_get_counter_precision = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_counter_precision",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_counter_precision(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_counter_precision(pFlObject)
    return retval


# fl_set_counter_return function placeholder (deprecated)


def fl_get_counter_value(pFlObject):
    """Obtains the current value of the counter.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        counter object

    :return: current value
    :rtype: float

    :note: e.g. currvalue = fl_get_counter_value(ctrobj)

    :status: Tested + Doc + Demo = OK

    """
    _fl_get_counter_value = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_counter_value",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
        """double fl_get_counter_value(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_counter_value(pFlObject)
    return retval


def fl_get_counter_bounds(pFlObject):
    """Obtains the current minimum and maximum bounds of the counter.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        counter object

    :return: minimum bound, maximum bound
    :rtype: float, float

    :note: e.g. minb, maxb = fl_get_counter_bounds(ctrobj)

    :attention: API change from XForms - upstream was
        fl_get_counter_bounds(pFlObject, minbound, maxbound)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_get_counter_bounds = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_counter_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)],
        """void fl_get_counter_bounds(FL_OBJECT * ob, double * min,
           double * max)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    minbound, pminbound = libr.make_double_and_pointer()
    maxbound, pmaxbound = libr.make_double_and_pointer()
    libr.keep_elem_refs(pFlObject, minbound, maxbound, pminbound, pmaxbound)
    _fl_get_counter_bounds(pFlObject, pminbound, pmaxbound)
    return minbound.value, maxbound.value


def fl_get_counter_step(pFlObject):
    """Obtains the current small and large step's sizes of a counter.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        counter object

    :return: small step size, large step size
    :rtype: float, float

    :note: e.g. minb, maxb = fl_get_counter_step(ctrobj)

    :attention: API change from XForms - upstream was
        fl_get_counter_step(pFlObject, sml, lrg)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_get_counter_step = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_counter_step",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)],
        """void fl_get_counter_step(FL_OBJECT * ob, double * s,
           double * l)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    small, psmall = libr.make_double_and_pointer()
    large, plarge = libr.make_double_and_pointer()
    libr.keep_elem_refs(pFlObject, small, large, psmall, plarge)
    _fl_get_counter_step(pFlObject, psmall, plarge)
    return small.value, large.value


def fl_set_counter_filter(pFlObject, py_ValFilter):
    """Overrides the format and value shown by the counter. By default the
    value is shown in floating point format.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        counter object
      `py_ValFilter` : python callback function, returning value
        name referring to function(pObject, valfloat, intprec) -> str

    :note: e.g. def ctrvalfilt(pobj, fvalue, prec): > ... ; return string
    :note: e.g. fl_set_counter_filter(ctrobj, ctrvalfilt)

    :status: Tested + Doc + NoDemo = OK

    """
    #FL_VAL_FILTER = cty.CFUNCTYPE(xfdata.STRING, \
    #           cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_int)
    _fl_set_counter_filter = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_counter_filter",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.FL_VAL_FILTER],
        """void fl_set_counter_filter(FL_OBJECT * ob,
           FL_VAL_FILTER filter)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.verify_function_type(py_ValFilter)
    c_ValFilter = xfdata.FL_VAL_FILTER(py_ValFilter)
    libr.keep_cfunc_refs(c_ValFilter, py_ValFilter)
    libr.keep_elem_refs(pFlObject)
    _fl_set_counter_filter(pFlObject, c_ValFilter)


# Functions to set and get the timeout value used by the
# counter code to control modification of the counter value.

def fl_get_counter_repeat(pFlObject):
    """Returns the initial delay of the counter.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        counter object

    :return: initial delay in milliseconds
    :rtype: int

    :note: e.g. intdly = fl_get_counter_repeat(ctrobj)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_get_counter_repeat = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_counter_repeat",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_counter_repeat(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_counter_repeat(pFlObject)
    return retval


def fl_set_counter_repeat(pFlObject, msec):
    """Sets the initial delay of a counter. By default the counter value
    changes first slowly and the rate of change then accelerates until a
    final speed is reached. The default delay between the value changing
    is 600 ms at the start.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        counter object
      `msec` : int
        initial delay in milliseconds

    :note: e.g. fl_set_counter_repeat(ctrobj, 200)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_set_counter_repeat = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_counter_repeat",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_counter_repeat(FL_OBJECT * ob, int millisec)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    imsec = libr.convert_to_int(msec)
    libr.keep_elem_refs(pFlObject, msec, imsec)
    _fl_set_counter_repeat(pFlObject, imsec)


def fl_get_counter_min_repeat(pFlObject):
    """Returns the final delay of a counter object.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        counter object

    :return: final delay in milliseconds
    :rtype: int

    :note: e.g. fnldly = fl_get_counter_min_repeat(ctrobj)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_get_counter_min_repeat = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_counter_min_repeat",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_counter_min_repeat(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_counter_min_repeat(pFlObject)
    return retval


def fl_set_counter_min_repeat(pFlObject, msec):
    """Sets the final delay of a counter. By default the counter value
    changes first slowly and the rate of change then accelerates until
    a final speed is reached. The default the final delay is 50 ms.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        counter object
      `msec` : int
        final delay in milliseconds

    :note: e.g. fl_set_counter_min_repeat(ctrobj, 100)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_set_counter_min_repeat = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_counter_min_repeat",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_counter_min_repeat(FL_OBJECT * ob, int millisec)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    imsec = libr.convert_to_int(msec)
    libr.keep_elem_refs(pFlObject, msec, imsec)
    _fl_set_counter_min_repeat(pFlObject, imsec)


def fl_get_counter_speedjump(pFlObject):
    """Determines the setting for speedjumping.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        counter object

    :return: setting flag of speedjump (1 if set, or 0 if unset)
    :rtype: int

    :note: e.g. isspdjmp = fl_get_counter_speedjump(ctrobj)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_get_counter_speedjump = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_counter_speedjump",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_counter_speedjump(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_counter_speedjump(pFlObject)
    return retval


def fl_set_counter_speedjump(pFlObject, yesno):
    """Makes only the first change of the counter has a different delay
    from all the following ones. The delay for the first change of the
    counter value will then be the one set by fl_set_counter_repeat()
    and the following delays last as long as set by
    fl_set_counter_min_repeat().

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        counter object
      `yesno` : int
        flag. Values 1 (to set speedjump) or 0 (to unset speedjump)

    :note: e.g. fl_set_counter_speedjump(ctrobj, 1)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_set_counter_speedjump = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_counter_speedjump",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_counter_speedjump(FL_OBJECT * ob, int yes_no)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    iyesno = libr.convert_to_int(yesno)
    libr.keep_elem_refs(pFlObject, yesno, iyesno)
    _fl_set_counter_speedjump(pFlObject, iyesno)
