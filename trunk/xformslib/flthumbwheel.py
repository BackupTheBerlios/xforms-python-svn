#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage thumbwheel objects.

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


#########################
# forms.h (thumbwheel.h)
#########################

def fl_get_thumbwheel_value(pFlObject):
    """*todo*

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        thumbwheel object

    :return: num.
    :rtype: int

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_get_thumbwheel_value = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_thumbwheel_value",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
        """double fl_get_thumbwheel_value(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_thumbwheel_value(pFlObject)
    return retval


def fl_set_thumbwheel_value(pFlObject, value):
    """*todo*

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        thumbwheel object
      `value` : float
        value to be set

    :return: num.
    :rtype: float

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_thumbwheel_value = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_thumbwheel_value",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """double fl_set_thumbwheel_value(FL_OBJECT * ob, double value)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    fvalue = libr.convert_to_double(value)
    libr.keep_elem_refs(pFlObject, value, fvalue)
    retval = _fl_set_thumbwheel_value(pFlObject, fvalue)
    return retval


def fl_get_thumbwheel_step(pFlObject):
    """*todo*

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        thumbwheel object

    :return: step value
    :rtype: double

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_thumbwheel_step = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_thumbwheel_step",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
        """double fl_get_thumbwheel_step(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_thumbwheel_step(pFlObject)
    return retval


def fl_set_thumbwheel_step(pFlObject, step):
    """*todo*

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        thumbwheel object
      `step` : float
        step value to be set

    :return: num.
    :rtype: float

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_set_thumbwheel_step = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_thumbwheel_step",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """double fl_set_thumbwheel_step(FL_OBJECT * ob, double step)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    fstep = libr.convert_to_double(step)
    libr.keep_elem_refs(pFlObject, step, fstep)
    retval = _fl_set_thumbwheel_step(pFlObject, fstep)
    return retval


def fl_set_thumbwheel_return(pFlObject, when):
    """*todo*

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        thumbwheel object
      `when` : int
        return type (when it returns). Values (from xfdata.py) FL_RETURN_NONE,
        FL_RETURN_CHANGED, FL_RETURN_END, FL_RETURN_END_CHANGED,
        FL_RETURN_SELECTION, FL_RETURN_DESELECTION, FL_RETURN_TRIGGERED,
        FL_RETURN_ALWAYS

    :return: num.
    :rtype: int

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_set_thumbwheel_return = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_thumbwheel_return",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_uint],
        """int fl_set_thumbwheel_return(FL_OBJECT * ob, unsigned
           int how)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.checkfatal_allowed_value_in_list(when, xfdata.RETURN_list)
    uiwhen = libr.convert_to_uint(when)
    libr.keep_elem_refs(pFlObject, when, uiwhen)
    retval = _fl_set_thumbwheel_return(pFlObject, uiwhen)
    return retval


def fl_set_thumbwheel_crossover(pFlObject, flag):
    """*todo*

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        thumbwheel object
      `flag` : int
        *todo*

    :return: num.
    :rtype: int

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_thumbwheel_crossover = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_thumbwheel_crossover",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """int fl_set_thumbwheel_crossover(FL_OBJECT * ob, int flag)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    iflag = libr.convert_to_int(flag)
    libr.keep_elem_refs(pFlObject, flag, iflag)
    retval = _fl_set_thumbwheel_crossover(pFlObject, iflag)
    return retval


def fl_set_thumbwheel_bounds(pFlObject, minbound, maxbound):
    """*todo*

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        thumbwheel object
      `minbound` : float
        minimum bound of slider
      `maxbound` : float
        maximum bound of slider

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_thumbwheel_bounds = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_thumbwheel_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
        """void fl_set_thumbwheel_bounds(FL_OBJECT * ob, double min,
           double max)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    fminbound = libr.convert_to_double(minbound)
    fmaxbound = libr.convert_to_double(maxbound)
    libr.keep_elem_refs(pFlObject, minbound, maxbound, fminbound, fmaxbound)
    _fl_set_thumbwheel_bounds(pFlObject, fminbound, fmaxbound)


def fl_get_thumbwheel_bounds(pFlObject):
    """*todo*

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        thumbwheel object

    :return: minimum bound, maximum bound
    :rtype: float, float

    :note: e.g. *todo*

    :attention: API change from XForms - upstream was
        fl_get_thumbwheel_bounds(pFlObject, minbound, maxbound)

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_thumbwheel_bounds = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_thumbwheel_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)],
        """void fl_get_thumbwheel_bounds(FL_OBJECT * ob, double * min,
           double * max)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    minbound, pminbound = libr.make_double_and_pointer()
    maxbound, pmaxbound = libr.make_double_and_pointer()
    libr.keep_elem_refs(pFlObject, minbound, maxbound, pminbound, pmaxbound)
    _fl_get_thumbwheel_bounds(pFlObject, pminbound, pmaxbound)
    return minbound.value, maxbound.value


# fl_create_thumbwheel function placeholder (internal)


def fl_add_thumbwheel(wheeltype, x, y, w, h, label):
    """Adds a thumbwheel object.

    --

    :Parameters:
      `wheeltype` : int
        type of thumbwheel to be added. Values (from xfdata.py)
        FL_VERT_THUMBWHEEL, FL_HOR_THUMBWHEEL
      `x` : int
        horizontal position (upper-left corner)
      `y` : int
        vertical position (upper-left corner)
      `w` : int
        width in coord units
      `h` : int
        height in coord units
      `label` : str
        text label of thumbwheel

    :return: thumbwheel object added (pFlObject)
    :rtype: pointer to xfdata.FL_OBJECT

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_add_thumbwheel = libr.cfuncproto(
        libr.load_so_libforms(), "fl_add_thumbwheel",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_thumbwheel(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    libr.check_if_initialized()
    libr.checkfatal_allowed_value_in_list(wheeltype, xfdata.THUMBWHEELTYPE_list)
    iwheeltype = libr.convert_to_int(wheeltype)
    ix = libr.convert_to_FL_Coord(x)
    iy = libr.convert_to_FL_Coord(y)
    iw = libr.convert_to_FL_Coord(w)
    ih = libr.convert_to_FL_Coord(h)
    slabel = libr.convert_to_string(label)
    libr.keep_elem_refs(wheeltype, x, y, w, h, label, iwheeltype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_thumbwheel(iwheeltype, ix, iy, iw, ih, slabel)
    return retval
