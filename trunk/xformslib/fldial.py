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




###################
# forms.h (dial.h)
###################

# Routines

# fl_create_dial function placeholder (internal)


def fl_add_dial(dialtype, x, y, w, h, label):
    """ fl_add_dial(dialtype, x, y, w, h, label) -> pFlObject

        Adds a dial object.

        @param dialtype: type of dial to be added
        @type dialtype: [num./int] from xfdata module FL_NORMAL_DIAL,
                        FL_LINE_DIAL, FL_FILL_DIAL
        @param x: horizontal position (upper-left corner)
        @param y: vertical position (upper-left corner)
        @param w: width in coord units
        @param h: height in coord units
        @param label: text label of dial

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_add_dial = library.cfuncproto(
        library.load_so_libforms(), "fl_add_dial",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_dial(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(dialtype, xfdata.DIALTYPE_list)
    idialtype = library.convert_to_int(dialtype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(dialtype, x, y, w, h, label, idialtype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_dial(idialtype, ix, iy, iw, ih, slabel)
    return retval


def fl_set_dial_value(pFlObject, val):
    """ fl_set_dial_value(pFlObject, val)

        @param pFlObject: pointer to object
@type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Tested + NoDoc + Demo = OK
    """

    _fl_set_dial_value = library.cfuncproto(
            library.load_so_libforms(), "fl_set_dial_value",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
            """void fl_set_dial_value(FL_OBJECT * ob, double val)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    fval = library.convert_to_double(val)
    library.keep_elem_refs(pFlObject, val, fval)
    _fl_set_dial_value(pFlObject, fval)


def fl_get_dial_value(pFlObject):
    """ fl_get_dial_value(pFlObject) -> num.

        @param pFlObject: pointer to dial object
@type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Tested + NoDoc + Demo = OK
    """

    _fl_get_dial_value = library.cfuncproto(
            library.load_so_libforms(), "fl_get_dial_value",
            cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
            """double fl_get_dial_value(FL_OBJECT * ob)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_dial_value(pFlObject)
    return retval


def fl_set_dial_bounds(pFlObject, minbound, maxbound):
    """ fl_set_dial_bounds(pFlObject, minbound, maxbound)

        @param pFlObject: pointer to object
@type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Tested + NoDoc + Demo = OK
    """

    _fl_set_dial_bounds = library.cfuncproto(
            library.load_so_libforms(), "fl_set_dial_bounds",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
            """void fl_set_dial_bounds(FL_OBJECT * ob, double min,
               double max)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    fminbound = library.convert_to_double(minbound)
    fmaxbound = library.convert_to_double(maxbound)
    library.keep_elem_refs(pFlObject, minbound, maxbound, fminbound, fmaxbound)
    _fl_set_dial_bounds(pFlObject, fminbound, fmaxbound)


def fl_get_dial_bounds(pFlObject):
    """ fl_get_dial_bounds(pFlObject) -> minbound, maxbound

        @param pFlObject: pointer to object
@type pFlObject: pointer to xfdata.FL_OBJECT

        @attention: API change from XForms - upstream was
                    fl_get_dial_bounds(pFlObject, minbound, maxbound)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_get_dial_bounds = library.cfuncproto(
            library.load_so_libforms(), "fl_get_dial_bounds",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
            cty.POINTER(cty.c_double)],
            """void fl_get_dial_bounds(FL_OBJECT * ob, double * min,
               double * max)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    minbound, pminbound = library.make_double_and_pointer()
    maxbound, pmaxbound = library.make_double_and_pointer()
    library.keep_elem_refs(pFlObject, minbound, maxbound, pminbound, pmaxbound)
    _fl_get_dial_bounds(pFlObject, pminbound, pmaxbound)
    return minbound.value, maxbound.value


def fl_set_dial_step(pFlObject, value):
    """ fl_set_dial_step(pFlObject, value)

        @param pFlObject: pointer to object
@type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_set_dial_step = library.cfuncproto(
            library.load_so_libforms(), "fl_set_dial_step",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
            """void fl_set_dial_step(FL_OBJECT * ob, double value)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    fvalue = library.convert_to_double(value)
    library.keep_elem_refs(pFlObject, value, fvalue)
    _fl_set_dial_step(pFlObject, fvalue)


def fl_set_dial_return(pFlObject, value):
    """ fl_set_dial_return(pFlObject, value)

        @param pFlObject: pointer to object
@type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_set_dial_return = library.cfuncproto(
            library.load_so_libforms(), "fl_set_dial_return",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_uint],
            """void fl_set_dial_return(FL_OBJECT * ob, unsigned
               int value)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    uivalue = library.convert_to_uint(value)
    library.keep_elem_refs(pFlObject, value, uivalue)
    _fl_set_dial_return(pFlObject, uivalue)


def fl_set_dial_angles(pFlObject, angmin, angmax):
    """ fl_set_dial_angles(pFlObject, angmin, angmax)

        @param pFlObject: pointer to object
@type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Tested + NoDoc + Demo = OK
    """

    _fl_set_dial_angles = library.cfuncproto(
            library.load_so_libforms(), "fl_set_dial_angles",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
            """void fl_set_dial_angles(FL_OBJECT * ob, double amin,
               double amax)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    fangmin = library.convert_to_double(angmin)
    fangmax = library.convert_to_double(angmax)
    library.keep_elem_refs(pFlObject, angmin, angmax, fangmin, fangmax)
    _fl_set_dial_angles(pFlObject, fangmin, fangmax)


def fl_set_dial_cross(pFlObject, flag):
    """
        fl_set_dial_cross(pFlObject, flag)

        @param pFlObject: pointer to object
@type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_set_dial_cross = library.cfuncproto(
            library.load_so_libforms(), "fl_set_dial_cross",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
            """void fl_set_dial_cross(FL_OBJECT * ob, int flag)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    iflag = library.convert_to_int(flag)
    library.keep_elem_refs(pFlObject, flag, iflag)
    _fl_set_dial_cross(pFlObject, iflag)


fl_set_dial_crossover = fl_set_dial_cross


def fl_set_dial_direction(pFlObject, directn):
    """
        fl_set_dial_direction(pFlObject, directn)

        @param pFlObject: pointer to object
@type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Tested + NoDoc + Demo = OK
    """

    _fl_set_dial_direction = library.cfuncproto(
            library.load_so_libforms(), "fl_set_dial_direction",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
            """void fl_set_dial_direction(FL_OBJECT * ob, int dir)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    idirectn = library.convert_to_int(directn)
    library.keep_elem_refs(pFlObject, directn, idirectn)
    _fl_set_dial_direction(pFlObject, idirectn)

