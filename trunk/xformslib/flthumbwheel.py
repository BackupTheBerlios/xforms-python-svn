#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

"""
    xforms-python - Python wrapper for XForms (X11) GUI C toolkit library
    using ctypes

    Copyright (C) 2009, 2010  Luca Lazzaroni "LukenShiro"
        <lukenshiro@ngi.it>

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


__docformat__ = "epytext en"    # to be used with epydoc doc


# originally generated by 'h2xml+gccxml' and 'xml2py'
# then heavily reordered and reworked

# ############################################# #
# Interface to XForms shared object libraries   #
# ############################################# #


import ctypes as cty
from xformslib import library
from xformslib import xfdata




#########################
# forms.h (thumbwheel.h)
#########################

def fl_get_thumbwheel_value(pFlObject):
    """
        fl_get_thumbwheel_value(pFlObject) -> num.

        @param pFlObject: pointer to object

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_get_thumbwheel_value = library.cfuncproto(
        library.load_so_libforms(), "fl_get_thumbwheel_value",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
        """double fl_get_thumbwheel_value(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_thumbwheel_value(pFlObject)
    return retval


def fl_set_thumbwheel_value(pFlObject, value):
    """
        fl_set_thumbwheel_value(pFlObject, value)

        @param pFlObject: pointer to object
    """
    _fl_set_thumbwheel_value = library.cfuncproto(
        library.load_so_libforms(), "fl_set_thumbwheel_value",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """double fl_set_thumbwheel_value(FL_OBJECT * ob, double value)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    fvalue = library.convert_to_double(value)
    library.keep_elem_refs(pFlObject, value, fvalue)
    retval = _fl_set_thumbwheel_value(pFlObject, fvalue)
    return retval


def fl_get_thumbwheel_step(pFlObject):
    """
        fl_get_thumbwheel_step(pFlObject) -> num.

        @param pFlObject: pointer to object

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_thumbwheel_step = library.cfuncproto(
        library.load_so_libforms(), "fl_get_thumbwheel_step",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
        """double fl_get_thumbwheel_step(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_thumbwheel_step(pFlObject)
    return retval


def fl_set_thumbwheel_step(pFlObject, step):
    """
        fl_set_thumbwheel_step(pFlObject, step) -> num.

        @param pFlObject: pointer to object

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_set_thumbwheel_step = library.cfuncproto(
        library.load_so_libforms(), "fl_set_thumbwheel_step",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """double fl_set_thumbwheel_step(FL_OBJECT * ob, double step)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    fstep = library.convert_to_double(step)
    library.keep_elem_refs(pFlObject, step, fstep)
    retval = _fl_set_thumbwheel_step(pFlObject, fstep)
    return retval


def fl_set_thumbwheel_return(pFlObject, when):
    """
        fl_set_thumbwheel_return(pFlObject, when) -> num.

        @param pFlObject: pointer to object
        @param when: return type (when it returns)
        @type when: [num./int] FL_RETURN_NONE, FL_RETURN_CHANGED,
                    FL_RETURN_END, FL_RETURN_END_CHANGED,
                    FL_RETURN_SELECTION, FL_RETURN_DESELECTION,
                    FL_RETURN_TRIGGERED, FL_RETURN_ALWAYS

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_set_thumbwheel_return = library.cfuncproto(
        library.load_so_libforms(), "fl_set_thumbwheel_return",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_uint],
        """int fl_set_thumbwheel_return(FL_OBJECT * ob, unsigned
           int how)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.check_admitted_listvalues(when, xfdata.RETURN_list)
    uiwhen = library.convert_to_uint(when)
    library.keep_elem_refs(pFlObject, when, uiwhen)
    retval = _fl_set_thumbwheel_return(pFlObject, uiwhen)
    return retval


def fl_set_thumbwheel_crossover(pFlObject, flag):
    """
        fl_set_thumbwheel_crossover(pFlObject, flag) -> num.

        @param pFlObject: pointer to object

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_set_thumbwheel_crossover = library.cfuncproto(
        library.load_so_libforms(), "fl_set_thumbwheel_crossover",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """int fl_set_thumbwheel_crossover(FL_OBJECT * ob, int flag)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    iflag = library.convert_to_int(flag)
    library.keep_elem_refs(pFlObject, flag, iflag)
    retval = _fl_set_thumbwheel_crossover(pFlObject, iflag)
    return retval


def fl_set_thumbwheel_bounds(pFlObject, minbound, maxbound):
    """
        fl_set_thumbwheel_bounds(pFlObject, minbound, maxbound)

        @param pFlObject: pointer to object

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_set_thumbwheel_bounds = library.cfuncproto(
        library.load_so_libforms(), "fl_set_thumbwheel_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
        """void fl_set_thumbwheel_bounds(FL_OBJECT * ob, double min,
           double max)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    fminbound = library.convert_to_double(minbound)
    fmaxbound = library.convert_to_double(maxbound)
    library.keep_elem_refs(pFlObject, minbound, maxbound, fminbound, fmaxbound)
    _fl_set_thumbwheel_bounds(pFlObject, fminbound, fmaxbound)


def fl_get_thumbwheel_bounds(pFlObject):
    """ fl_get_thumbwheel_bounds(pFlObject) -> minbound, maxbound

        @param pFlObject: pointer to thumbwheel object

        @attention: API change from XForms - upstream was
                    fl_get_thumbwheel_bounds(pFlObject, minbound, maxbound)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_thumbwheel_bounds = library.cfuncproto(
        library.load_so_libforms(), "fl_get_thumbwheel_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)],
        """void fl_get_thumbwheel_bounds(FL_OBJECT * ob, double * min,
           double * max)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    minbound, pminbound = library.make_double_and_pointer()
    maxbound, pmaxbound = library.make_double_and_pointer()
    library.keep_elem_refs(pFlObject, minbound, maxbound, pminbound, pmaxbound)
    _fl_get_thumbwheel_bounds(pFlObject, pminbound, pmaxbound)
    return minbound.value, maxbound.value


# fl_create_thumbwheel function placeholder (internal)


def fl_add_thumbwheel(wheeltype, x, y, w, h, label):
    """
        fl_add_thumbwheel(wheeltype, x, y, w, h, label) -> pFlObject

        Adds a thumbwheel object.

        @param wheeltype: type of thumbwheel to be added
        @param x: horizontal position (upper-left corner)
        @param x: vertical position (upper-left corner)
        @param w: width in coord units
        @param h: height in coord units
        @param label: text label of thumbwheel

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_add_thumbwheel = library.cfuncproto(
        library.load_so_libforms(), "fl_add_thumbwheel",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_thumbwheel(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(wheeltype, xfdata.THUMBWHEELTYPE_list)
    iwheeltype = library.convert_to_int(wheeltype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(wheeltype, x, y, w, h, label, iwheeltype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_thumbwheel(iwheeltype, ix, iy, iw, ih, slabel)
    return retval


