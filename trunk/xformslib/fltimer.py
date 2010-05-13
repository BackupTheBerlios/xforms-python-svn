#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

"""
    fltimer.py - xforms-python's functions to manage timer objects.

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
# forms.h (timer.h)
# Object Class: Timer
######################

# Routines

# fl_create_timer function placeholder (internal)


def fl_add_timer(timertype, x, y, w, h, label):
    """Adds a timer object.

    --

    :Parameters:
      `timertype: int
        type of timer to be added. Values (from xfdata.py) FL_NORMAL_TIMER,
        FL_VALUE_TIMER, FL_HIDDEN_TIMER
      `x: int
        horizontal position (upper-left corner)
      `y: int
        vertical position (upper-left corner)
      `w: int
        width in coord units
      `h: int
        height in coord units
      `label: str
        text label of timer

    :return: timer object added (pFlObject)
    :rtype: pointer to xfdata.FL_OBJECT

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_add_timer = libr.cfuncproto(
        libr.load_so_libforms(), "fl_add_timer",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_timer(int type, FL_Coord x, FL_Coord y,
        FL_Coord w, FL_Coord h, const char * label)""")
    libr.check_if_initialized()
    libr.check_admitted_value_in_list(timertype, xfdata.TIMERTYPE_list)
    itimertype = libr.convert_to_int(timertype)
    ix = libr.convert_to_FL_Coord(x)
    iy = libr.convert_to_FL_Coord(y)
    iw = libr.convert_to_FL_Coord(w)
    ih = libr.convert_to_FL_Coord(h)
    slabel = libr.convert_to_string(label)
    libr.keep_elem_refs(timertype, x, y, w, h, label, itimertype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_timer(itimertype, ix, iy, iw, ih, slabel)
    return retval


def fl_set_timer(pFlObject, total):
    """*todo*

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        timer object
      `total` : float
        total?
        

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_set_timer = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_timer",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_timer(FL_OBJECT * ob, double total)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    ftotal = libr.convert_to_double(total)
    libr.keep_elem_refs(pFlObject, total, ftotal)
    _fl_set_timer(pFlObject, ftotal)


def fl_get_timer(pFlObject):
    """*todo*

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        timer object

    :return: num.
    :rtype: float

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_timer = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_timer",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
        """double fl_get_timer(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_timer(pFlObject)
    return retval


def fl_set_timer_countup(pFlObject, yes):
    """*todo*

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        timer object
      `yes` : int
        *todo*

    :note: e.g. *todo*

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_set_timer_countup = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_timer_countup",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_timer_countup(FL_OBJECT * ob, int yes)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    iyes = libr.convert_to_int(yes)
    libr.keep_elem_refs(pFlObject, yes, iyes)
    _fl_set_timer_countup(pFlObject, iyes)



def fl_set_timer_filter(pFlObject, py_TimerFilter):
    """*todo*

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        timer object
      `py_TimerFilter` : python callback function, returning value
        name referring to function(pFlObject, valfloat) -> str

    :return: old timer filter function
    :rtype: pointer to xfdata.FL_TIMER_FILTER

    :note: e.g. *todo*

    :status: Untested + NoDoc + NoDemo = NOT OK

    """
    #FL_TIMER_FILTER = cty.CFUNCTYPE(xfdata.STRING, cty.POINTER(xfdata.FL_OBJECT),
    #                                cty.c_double)
    _fl_set_timer_filter = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_timer_filter",
        xfdata.FL_TIMER_FILTER, [cty.POINTER(xfdata.FL_OBJECT),
        xfdata.FL_TIMER_FILTER],
        """FL_TIMER_FILTER fl_set_timer_filter(FL_OBJECT * ob,
           FL_TIMER_FILTER filter)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    c_TimerFilter = xfdata.FL_TIMER_FILTER(py_TimerFilter)
    libr.keep_cfunc_refs(c_TimerFilter, py_TimerFilter)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_set_timer_filter(pFlObject, c_TimerFilter)
    return retval


def fl_suspend_timer(pFlObject):
    """Suspends timer, pausing time.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        timer object

    :note: e.g. fl_suspend_timer(timerobj)

    :status: Tested + Doc + Demo = OK

    """
    _fl_suspend_timer = libr.cfuncproto(
        libr.load_so_libforms(), "fl_suspend_timer",
        None, [cty.POINTER(xfdata.FL_OBJECT)],
        """void fl_suspend_timer(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    _fl_suspend_timer(pFlObject)


def fl_resume_timer(pFlObject):
    """Resumes timer previously paused (with fl_suspend_timer).

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        timer object

    :note: e.g. fl_resume_timer(timerobj)

    :status: Tested + Doc + Demo = OK

    """
    _fl_resume_timer = libr.cfuncproto(
        libr.load_so_libforms(), "fl_resume_timer",
        None, [cty.POINTER(xfdata.FL_OBJECT)],
        """void fl_resume_timer(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    _fl_resume_timer(pFlObject)


