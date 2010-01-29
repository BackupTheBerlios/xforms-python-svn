#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

"""
    xforms-python - Python wrapper for XForms (X11) GUI C toolkit library
    using ctypes

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
from xformslib import library
from xformslib import xfdata



#########################
# forms.h (positioner.h)
#########################

# Routines

# fl_create_positioner function placeholder (internal)


def fl_add_positioner(postype, x, y, w, h, label):
    """
        fl_add_positioner(postype, x, y, w, h, label) -> pFlObject

        Adds a positioner object.

        @param postype: type of positioner to be added
        @param x: horizontal position (upper-left corner)
        @param y: vertical position (upper-left corner)
        @param w: width in coord units
        @param h: height in coord units
        @param label: text label of positioner

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_add_positioner = library.cfuncproto(
        library.load_so_libforms(), "fl_add_positioner",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_positioner(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(postype, xfdata.POSITIONERTYPE_list)
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
    """
        fl_set_positioner_xvalue(pFlObject, val)

        @param pFlObject: positioner object
        @type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_set_positioner_xvalue = library.cfuncproto(
        library.load_so_libforms(), "fl_set_positioner_xvalue",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_positioner_xvalue(FL_OBJECT * ob, double val)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    fval = library.convert_to_double(val)
    library.keep_elem_refs(pFlObject, val, fval)
    _fl_set_positioner_xvalue(pFlObject, fval)


def fl_get_positioner_xvalue(pFlObject):
    """
        fl_get_positioner_xvalue(pFlObject) -> floatnum

        @param pFlObject: positioner object
        @type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Tested + NoDoc + Demo = OK
    """

    _fl_get_positioner_xvalue = library.cfuncproto(
            library.load_so_libforms(), "fl_get_positioner_xvalue",
            cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
            """double fl_get_positioner_xvalue(FL_OBJECT * ob)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_positioner_xvalue(pFlObject)
    return retval


def fl_set_positioner_xbounds(pFlObject, minbound, maxbound):
    """
        fl_set_positioner_xbounds(pFlObject, minbound, maxbound)

        @param pFlObject: positioner object
        @type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Tested + NoDoc + Demo = OK
    """

    _fl_set_positioner_xbounds = library.cfuncproto(
            library.load_so_libforms(), "fl_set_positioner_xbounds",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
            """void fl_set_positioner_xbounds(FL_OBJECT * ob, double min,
               double max)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    fminbound = library.convert_to_double(minbound)
    fmaxbound = library.convert_to_double(maxbound)
    library.keep_elem_refs(pFlObject, minbound, maxbound, fminbound, fmaxbound)
    _fl_set_positioner_xbounds(pFlObject, fminbound, fmaxbound)


def fl_get_positioner_xbounds(pFlObject):
    """
        fl_get_positioner_xbounds(pFlObject) -> minbound, maxbound

        @param pFlObject: positioner object
        @type pFlObject: pointer to xfdata.FL_OBJECT

        @attention: API change from XForms - upstream was
                    fl_get_positioner_xbounds(pFlObject, minbound, maxbound)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_get_positioner_xbounds = library.cfuncproto(
            library.load_so_libforms(), "fl_get_positioner_xbounds",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
            cty.POINTER(cty.c_double)],
            """void fl_get_positioner_xbounds(FL_OBJECT * ob, double * min,
            double * max)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    minbound, pminbound = library.make_double_and_pointer()
    maxbound, pmaxbound = library.make_double_and_pointer()
    library.keep_elem_refs(pFlObject, minbound, maxbound, pminbound, pmaxbound)
    _fl_get_positioner_xbounds(pFlObject, pminbound, pmaxbound)
    return minbound.value, maxbound.value


def fl_set_positioner_yvalue(pFlObject, val):
    """
        fl_set_positioner_yvalue(pFlObject, val)

        @param pFlObject: positioner object
        @type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Tested + NoDoc + Demo = OK
    """

    _fl_set_positioner_yvalue = library.cfuncproto(
            library.load_so_libforms(), "fl_set_positioner_yvalue",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
            """void fl_set_positioner_yvalue(FL_OBJECT * ob, double val)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    fval = library.convert_to_double(val)
    library.keep_elem_refs(pFlObject, val, fval)
    _fl_set_positioner_yvalue(pFlObject, fval)


def fl_get_positioner_yvalue(pFlObject):
    """
        fl_get_positioner_yvalue(pFlObject) -> floatnum

        @param pFlObject: positioner object
        @type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_get_positioner_yvalue = library.cfuncproto(
            library.load_so_libforms(), "fl_get_positioner_yvalue",
            cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
            """double fl_get_positioner_yvalue(FL_OBJECT * ob)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_positioner_yvalue(pFlObject)
    return retval


def fl_set_positioner_ybounds(pFlObject, minbound, maxbound):
    """
        fl_set_positioner_ybounds(pFlObject, minbound, maxbound)

        @param pFlObject: positioner object
        @type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Tested + NoDoc + Demo = OK
    """

    _fl_set_positioner_ybounds = library.cfuncproto(
            library.load_so_libforms(), "fl_set_positioner_ybounds",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
            """void fl_set_positioner_ybounds(FL_OBJECT * ob, double min,
               double max)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    fminbound = library.convert_to_double(minbound)
    fmaxbound = library.convert_to_double(maxbound)
    library.keep_elem_refs(pFlObject, minbound, maxbound, fminbound, fmaxbound)
    _fl_set_positioner_ybounds(pFlObject, fminbound, fmaxbound)


def fl_get_positioner_ybounds(pFlObject):
    """
        fl_get_positioner_ybounds(pFlObject) -> minbound, maxbound

        @param pFlObject: positioner object
        @type pFlObject: pointer to xfdata.FL_OBJECT

        @attention: API change from XForms - upstream was
                    fl_get_positioner_ybounds(pFlObject, minbound, maxbound)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_positioner_ybounds = library.cfuncproto(
        library.load_so_libforms(), "fl_get_positioner_ybounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)],
        """void fl_get_positioner_ybounds(FL_OBJECT * ob, double * min,
           double * max)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    minbound, pminbound = library.make_double_and_pointer()
    maxbound, pmaxbound = library.make_double_and_pointer()
    library.keep_elem_refs(pFlObject, minbound, maxbound, pminbound, pmaxbound)
    _fl_get_positioner_ybounds(pFlObject, pminbound, pmaxbound)
    return minbound.value, maxbound.value


def fl_set_positioner_xstep(pFlObject, value):
    """
    fl_set_positioner_xstep(pFlObject, value)

    @param pFlObject: positioner object
    @type pFlObject: pointer to xfdata.FL_OBJECT

    @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_set_positioner_xstep = library.cfuncproto(
        library.load_so_libforms(), "fl_set_positioner_xstep",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_positioner_xstep(FL_OBJECT * ob, double value)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    fvalue = library.convert_to_double(value)
    library.keep_elem_refs(pFlObject, value, fvalue)
    _fl_set_positioner_xstep(pFlObject, fvalue)


def fl_set_positioner_ystep(pFlObject, value):
    """
    fl_set_positioner_ystep(pFlObject, value)

    @param pFlObject: positioner object
    @type pFlObject: pointer to xfdata.FL_OBJECT

    @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_set_positioner_ystep = library.cfuncproto(
        library.load_so_libforms(), "fl_set_positioner_ystep",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_positioner_ystep(FL_OBJECT * ob, double value)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    fvalue = library.convert_to_double(value)
    library.keep_elem_refs(pFlObject, value, fvalue)
    _fl_set_positioner_ystep(pFlObject, fvalue)


def fl_set_positioner_return(pFlObject, when):
    """
    fl_set_positioner_return(pFlObject, when)

    @param pFlObject: positioner object
    @type pFlObject: pointer to xfdata.FL_OBJECT
    @param when: return type (when it returns)
    @type when: int_pos

    @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_set_positioner_return = library.cfuncproto(
        library.load_so_libforms(), "fl_set_positioner_return",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_uint],
        """void fl_set_positioner_return(FL_OBJECT * ob, unsigned
           int value)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.check_admitted_listvalues(when, xfdata.RETURN_list)
    uiwhen = library.convert_to_uint(when)
    library.keep_elem_refs(pFlObject, when, uiwhen)
    _fl_set_positioner_return(pFlObject, uiwhen)


