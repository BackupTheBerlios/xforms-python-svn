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



######################
# forms.h (timer.h)
# Object Class: Timer
######################

# Routines

# fl_create_timer function placeholder (internal)


def fl_add_timer(timertype, x, y, w, h, label):
    """
        fl_add_timer(timertype, x, y, w, h, label) -> pFlObject

        Adds a timer object.

        @param timertype: type of timer to be added
        @param x: horizontal position (upper-left corner)
        @param x: vertical position (upper-left corner)
        @param w: width in coord units
        @param h: height in coord units
        @param label: text label of timer

        :status: Tested + NoDoc + Demo = OK
    """
    _fl_add_timer = library.cfuncproto(
        library.load_so_libforms(), "fl_add_timer",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_timer(int type, FL_Coord x, FL_Coord y,
        FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(timertype, xfdata.TIMERTYPE_list)
    itimertype = library.convert_to_int(timertype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(timertype, x, y, w, h, label, itimertype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_timer(itimertype, ix, iy, iw, ih, slabel)
    return retval


def fl_set_timer(pFlObject, total):
    """
        fl_set_timer(pFlObject, total)

        @param pFlObject: pointer to object

        :status: Tested + NoDoc + Demo = OK
    """
    _fl_set_timer = library.cfuncproto(
        library.load_so_libforms(), "fl_set_timer",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_timer(FL_OBJECT * ob, double total)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    ftotal = library.convert_to_double(total)
    library.keep_elem_refs(pFlObject, total, ftotal)
    _fl_set_timer(pFlObject, ftotal)


def fl_get_timer(pFlObject):
    """
        fl_get_timer(pFlObject) -> num.

        @param pFlObject: pointer to object

        :status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_timer = library.cfuncproto(
        library.load_so_libforms(), "fl_get_timer",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
        """double fl_get_timer(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_timer(pFlObject)
    return retval


def fl_set_timer_countup(pFlObject, yes):
    """
        fl_set_timer_countup(pFlObject, yes)

        @param pFlObject: pointer to object

        :status: Tested + NoDoc + Demo = OK
    """
    _fl_set_timer_countup = library.cfuncproto(
        library.load_so_libforms(), "fl_set_timer_countup",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_timer_countup(FL_OBJECT * ob, int yes)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    iyes = library.convert_to_int(yes)
    library.keep_elem_refs(pFlObject, yes, iyes)
    _fl_set_timer_countup(pFlObject, iyes)



def fl_set_timer_filter(pFlObject, py_TimerFilter):
    """
        fl_set_timer_filter(pFlObject, py_TimerFilter) -> timer_filter func.

        @param pFlObject: timer object
        @type pFlObject: pointer to xfdata.FL_OBJECT
        @param py_TimerFilter: python callback function, returning value
        @type py_TimerFilter: __ fn(pFlObject, float) -> str __

        :note: e.g. ?

        :status: Untested + NoDoc + NoDemo = NOT OK
    """
    #FL_TIMER_FILTER = cty.CFUNCTYPE(xfdata.STRING, cty.POINTER(xfdata.FL_OBJECT),
    #                                cty.c_double)
    _fl_set_timer_filter = library.cfuncproto(
        library.load_so_libforms(), "fl_set_timer_filter",
        xfdata.FL_TIMER_FILTER, [cty.POINTER(xfdata.FL_OBJECT), xfdata.FL_TIMER_FILTER],
        """FL_TIMER_FILTER fl_set_timer_filter(FL_OBJECT * ob,
           FL_TIMER_FILTER filter)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    c_TimerFilter = xfdata.FL_TIMER_FILTER(py_TimerFilter)
    library.keep_cfunc_refs(c_TimerFilter, py_TimerFilter)
    library.keep_elem_refs(pFlObject)
    retval = _fl_set_timer_filter(pFlObject, c_TimerFilter)
    return retval


def fl_suspend_timer(pFlObject):
    """Suspends timer, pausing time.

    @param pFlObject: timer object
    @type pFlObject: pointer to xfdata.FL_OBJECT

    :note: e.g. fl_suspend_timer(timerobj)

    :status: Tested + Doc + Demo = OK
    """
    _fl_suspend_timer = library.cfuncproto(
        library.load_so_libforms(), "fl_suspend_timer",
        None, [cty.POINTER(xfdata.FL_OBJECT)],
        """void fl_suspend_timer(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    _fl_suspend_timer(pFlObject)


def fl_resume_timer(pFlObject):
    """Resumes timer previously paused (with fl_suspend_timer).

    @param pFlObject: timer object
    @type pFlObject: pointer to xfdata.FL_OBJECT

    :note: e.g. fl_resume_timer(timerobj)

    :status: Tested + Doc + Demo = OK
    """
    _fl_resume_timer = library.cfuncproto(
        library.load_so_libforms(), "fl_resume_timer",
        None, [cty.POINTER(xfdata.FL_OBJECT)],
        """void fl_resume_timer(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    _fl_resume_timer(pFlObject)


