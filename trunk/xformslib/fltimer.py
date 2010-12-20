#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage timer flobjects.
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
# Interface to XForms shared flobject libraries #
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


def fl_add_timer(timertype, xpos, ypos, width, height, label):
    """fl_add_timer(timertype, xpos, ypos, width, height, label)
    -> ptr_flobject
    
    Adds a timer flobject.

    Parameters
    ----------
        timertype : int
            type of timer to be added. Values (from xfdata.py)
            FL_NORMAL_TIMER, FL_VALUE_TIMER, FL_HIDDEN_TIMER
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            text label of timer

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            timer flobject added

    Examples
    --------
        >>> ptimerobj = fl_add_timer(xfdata.FL_NORMAL_TIMER, 120, 120,
                210, 210, "My Timer")

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_add_timer = library.cfuncproto(
        library.load_so_libforms(), "fl_add_timer",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_timer(int type, FL_Coord x, FL_Coord y,
        FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.checkfatal_allowed_value_in_list(timertype, \
            xfdata.TIMERTYPE_list)
    i_timertype = library.convert_to_intc(timertype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_stringc(label)
    library.keep_elem_refs(timertype, xpos, ypos, width, height, label, \
            i_timertype, i_xpos, i_ypos, i_width, i_height, s_label)
    retval = _fl_add_timer(i_timertype, i_xpos, i_ypos, i_width, \
            i_height, s_label)
    return retval


def fl_set_timer(ptr_flobject, tdelay):
    """fl_set_timer(ptr_flobject, tdelay)
    
    Defines the timer to a particular value.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            timer flobject
        tdelay : float
            number of seconds the timer should run. If it is 0.0,
            resets/de-blinks the timer.

    Examples
    --------
        >>> fl_set_timer(ptimerobj, 20)

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_set_timer = library.cfuncproto(
        library.load_so_libforms(), "fl_set_timer",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double],
        """void fl_set_timer(FL_OBJECT * ob, double total)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_tdelay = library.convert_to_doublec(tdelay)
    library.keep_elem_refs(ptr_flobject, tdelay, f_tdelay)
    _fl_set_timer(ptr_flobject, f_tdelay)


def fl_get_timer(ptr_flobject):
    """fl_get_timer(ptr_flobject) -> lefttime
    
    Finds out the time left in the timer.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            timer flobject

    Returns
    -------
        lefttime : float
            time left

    Examples
    --------
        >>> lefttim = fl_get_timer(ptimerobj)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_get_timer = library.cfuncproto(
        library.load_so_libforms(), "fl_get_timer",
        cty.c_double, [cty.POINTER(xfdata.FL_OBJECT)],
        """double fl_get_timer(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_timer(ptr_flobject)
    return retval


def fl_set_timer_countup(ptr_flobject, yesno):
    """fl_set_timer_countup(ptr_flobject, yesno)
    
    Changes timer behavior so the timer counts up and shows elapsed time.
    By default, a timer counts down toward zero and the value shown (for
    xfdata.FL_VALUE_TIMERs) is the time left until the timer expires.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            timer flobject
        yesno : int
            flag to set count up or down. Values 0 (counts down and shows
            time left) or 1 (counts up and shows elapsed time)

    Examples
    --------
        >>> fl_set_timer_countup(ptimerobj, 1)

    Notes
    -----
        Status: Tested + NoDoc + Demo = OK

    """
    _fl_set_timer_countup = library.cfuncproto(
        library.load_so_libforms(), "fl_set_timer_countup",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_timer_countup(FL_OBJECT * ob, int yes)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_yesno = library.convert_to_intc(yesno)
    library.keep_elem_refs(ptr_flobject, yesno, i_yesno)
    _fl_set_timer_countup(ptr_flobject, i_yesno)



def fl_set_timer_filter(ptr_flobject, pyfn_TimerFilter):
    """fl_set_timer_filter(ptr_flobject, pyfn_TimerFilter) -> TimerFilter
    
    Defines a function to change the way the time is presented in
    xfdata.FL_VALUE_TIMER. By default, it gives the time in a
    hour:minutes:seconds.fraction format

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            timer flobject
        pyfn_TimerFilter : python callback function, returned value
            name referring to function(ptr_flobject, floatsecs) -> str
            Parameter floatsecs is time left for count-down timers and the
            elapsed time for up-counting timers (in units of seconds).
            It gives string representation of time.

    Returns
    -------
        TimerFilter : pointer to xfdata.FL_TIMER_FILTER
            old timer filter function

    Examples
    --------
        >>> def timefilt(pobj, elapsedsecs):
        >>> ... <something>
        >>> ... return newstr
        >>> oldtimerfunc = fl_set_timer_filter(ptimerobj, timefilt)

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    #FL_TIMER_FILTER = cty.CFUNCTYPE(xfdata.STRING,
    #           cty.POINTER(xfdata.FL_OBJECT), cty.c_double)
    _fl_set_timer_filter = library.cfuncproto(
        library.load_so_libforms(), "fl_set_timer_filter",
        xfdata.FL_TIMER_FILTER, [cty.POINTER(xfdata.FL_OBJECT),
        xfdata.FL_TIMER_FILTER],
        """FL_TIMER_FILTER fl_set_timer_filter(FL_OBJECT * ob,
           FL_TIMER_FILTER filter)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.verify_function_type(pyfn_TimerFilter)
    cfn_TimerFilter = xfdata.FL_TIMER_FILTER(pyfn_TimerFilter)
    library.keep_cfunc_refs(cfn_TimerFilter, pyfn_TimerFilter)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_set_timer_filter(ptr_flobject, cfn_TimerFilter)
    return retval


def fl_suspend_timer(ptr_flobject):
    """fl_suspend_timer(ptr_flobject)
    
    Suspends timer, pausing time.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            timer flobject

    Examples
    --------
        >>> fl_suspend_timer(ptimerobj)

    Notes
    -----
        Status: Tested + Doc + Demo = OK

    """
    _fl_suspend_timer = library.cfuncproto(
        library.load_so_libforms(), "fl_suspend_timer",
        None, [cty.POINTER(xfdata.FL_OBJECT)],
        """void fl_suspend_timer(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    _fl_suspend_timer(ptr_flobject)


def fl_resume_timer(ptr_flobject):
    """fl_resume_timer(ptr_flobject)
    
    Resumes timer previously paused (with fl_suspend_timer). Unlike
    fl_set_timer() a suspended timer keeps its internal state (total
    delay, time left etc.), so when it is resumed, it starts from
    where it was suspended.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            timer flobject

    Examples
    --------
        >>> fl_resume_timer(ptimobj)

    Notes
    -----
        Status: Tested + Doc + Demo = OK

    """
    _fl_resume_timer = library.cfuncproto(
        library.load_so_libforms(), "fl_resume_timer",
        None, [cty.POINTER(xfdata.FL_OBJECT)],
        """void fl_resume_timer(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    _fl_resume_timer(ptr_flobject)

