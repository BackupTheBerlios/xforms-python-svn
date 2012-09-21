#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" xforms-python's functions to manage chart flobjects.
"""

#    Copyright (C) 2009, 2010, 2011, 2012  Luca Lazzaroni "LukenShiro"
#    e-mail:  <lukenshiro@ngi.it>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, version 2.1 of the License,
#    or (at your option) any later version.
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

# ########################################### #
# Interface to XForms shared-object libraries #
# ########################################### #


import ctypes as cty
from xformslib import library
from xformslib import xfdata


#############################
# forms.h (chart.h)
# Object Class: Chart
#############################

# Routines

# fl_create_chart function placeholder (internal)


def fl_add_chart(charttype, xpos, ypos, width, height, label):
    """fl_add_chart(charttype, xpos, ypos, width, height, label)
    -> ptr_flobject

    Adds a chart flobject.

    Parameters
    ----------
        charttype : int
            type of chart to be created. Values (from xfdata.py)
            - FL_BAR_CHART (A vertical bar-chart),
            - FL_HORBAR_CHART (A horizontal bar-chart),
            - FL_LINE_CHART (A line-chart),
            - FL_FILL_CHART (A line-chart but the area below curve is filled),
            - FL_SPIKE_CHART (A chart with a vertical spike for each value),
            - FL_PIE_CHART (A pie-chart),
            - FL_SPECIALPIE_CHART (A pie-chart with displaced first item)
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            text label of chart

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            chart flobject added

    Examples
    --------
        >>> pchrtobj = fl_add_chart(xfdata.FL_SPIKE_CHART, 147, 168,
                250, 492, "My Chart")

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_add_chart = library.cfuncproto(
        library.load_so_libforms(), "fl_add_chart",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_chart(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_flinitialized()
    library.checkfatal_allowed_value_in_list(charttype, \
            xfdata.CHARTTYPE_list)
    i_charttype = library.convert_to_intc(charttype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_stringc(label)
    library.keep_elem_refs(charttype, xpos, ypos, width, height, label, \
            i_charttype, i_xpos, i_ypos, i_width, i_height, s_label)
    retval = _fl_add_chart(i_charttype, i_xpos, i_ypos, i_width, i_height, \
            s_label)
    return retval


def fl_clear_chart(ptr_flobject):
    """fl_clear_chart(ptr_flobject)

    Clears the contents of a chart flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            chart flobject

    Examples
    --------
        >>> fl_clear_chart(pchrtobj)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_clear_chart = library.cfuncproto(
        library.load_so_libforms(), "fl_clear_chart",
        None, [cty.POINTER(xfdata.FL_OBJECT)],
        """void fl_clear_chart(FL_OBJECT * ob)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    _fl_clear_chart(ptr_flobject)


def fl_add_chart_value(ptr_flobject, itemval, label, colr):
    """fl_add_chart_value(ptr_flobject, itemval, label, colr)

    Adds an item to the chart flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            chart flobject
        itemval : float
            value of chart item
        label : str
            text label of chart
        colr : long_pos
            XForms colormap index as color

    Examples
    --------
        >>> fl_add_chart_value(pchrtobj, 120, "Some point", xfdata.FL_BLUE)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_add_chart_value = library.cfuncproto(
        library.load_so_libforms(), "fl_add_chart_value",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, xfdata.STRING,
        xfdata.FL_COLOR],
        """void fl_add_chart_value(FL_OBJECT * ob, double val,
           const char * str, FL_COLOR col)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_itemval = library.convert_to_doublec(itemval)
    s_label = library.convert_to_stringc(label)
    ul_colr = library.convert_to_FL_COLOR(colr)
    library.keep_elem_refs(ptr_flobject, itemval, label, colr, f_itemval, \
            s_label, ul_colr)
    _fl_add_chart_value(ptr_flobject, f_itemval, s_label, ul_colr)


def fl_insert_chart_value(ptr_flobject, indx, itemval, label, colr):
    """fl_insert_chart_value(ptr_flobject, indx, itemval, label, colr)

    Inserts a new value at a particular place in a chart flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            chart flobject
        indx : int
            index before which the new item should be inserted. The first
            item is number 1.
        itemval : float
            value of new chart item
        label : str
            text label of chart
        colr : long_pos
            XForms colormap index as color

    Examples
    --------
        >>> fl_insert_chart_value(pchrtobj, 2, 123.0, "new value",
                xfdata.FL_DEEPSKYBLUE)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_insert_chart_value = library.cfuncproto(
        library.load_so_libforms(), "fl_insert_chart_value",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_double,
        xfdata.STRING, xfdata.FL_COLOR],
        """void fl_insert_chart_value(FL_OBJECT * ob, int indx,
           double val, const char * str, FL_COLOR col)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_indx = library.convert_to_intc(indx)
    f_itemval = library.convert_to_doublec(itemval)
    s_label = library.convert_to_stringc(label)
    ul_colr = library.convert_to_FL_COLOR(colr)
    library.keep_elem_refs(ptr_flobject, indx, itemval, label, colr, \
            i_indx, f_itemval, s_label, ul_colr)
    _fl_insert_chart_value(ptr_flobject, i_indx, f_itemval, s_label, ul_colr)


def fl_replace_chart_value(ptr_flobject, indx, itemval, label, colr):
    """fl_replace_chart_value(ptr_flobject, indx, itemval, label, colr)

    Replaces value of an item in the chart flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            chart flobject
        indx : int
            index position of item to be replaced. The first item is number 1
        itemval : float
            value of chart item
        label : str
            text label of chart
        colr : long_pos
            XForms colormap index as color

    Examples
    --------
        >>> fl_replace_chart_value(pchrtobj, 3, 142.0, "replaced item",
                xfdata.FL_FIREBRICK)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_replace_chart_value = library.cfuncproto(
        library.load_so_libforms(), "fl_replace_chart_value",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_double,
        xfdata.STRING, xfdata.FL_COLOR],
        """void fl_replace_chart_value(FL_OBJECT * ob, int indx,
           double val, const char * str, FL_COLOR col)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_indx = library.convert_to_intc(indx)
    f_itemval = library.convert_to_doublec(itemval)
    s_label = library.convert_to_stringc(label)
    ul_colr = library.convert_to_FL_COLOR(colr)
    library.keep_elem_refs(ptr_flobject, indx, itemval, label, colr, \
            i_indx, f_itemval, s_label, ul_colr)
    _fl_replace_chart_value(ptr_flobject, i_indx, f_itemval, s_label, \
            ul_colr)


def fl_set_chart_bounds(ptr_flobject, minbound, maxbound):
    """fl_set_chart_bounds(ptr_flobject, minbound, maxbound)

    Defines the boundaries/limits for values of a chart flobject. Normally,
    bar-charts and line-charts are automatically scaled in the vertical
    direction such that all values can be displayed.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            chart flobject
        minbound : float
            minimum value bounds to be set
        maxbound : float
            maximum value bounds to be set

    Examples
    --------
        >>> fl_set_chart_bounds(pchrtobj, 100, 950)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_set_chart_bounds = library.cfuncproto(
        library.load_so_libforms(), "fl_set_chart_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_double, cty.c_double],
        """void fl_set_chart_bounds(FL_OBJECT * ob, double min,
           double max)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_minbound = library.convert_to_doublec(minbound)
    f_maxbound = library.convert_to_doublec(maxbound)
    library.keep_elem_refs(ptr_flobject, minbound, maxbound, f_minbound, \
            f_maxbound)
    _fl_set_chart_bounds(ptr_flobject, f_minbound, f_maxbound)


def fl_get_chart_bounds(ptr_flobject):
    """fl_get_chart_bounds(ptr_flobject) -> minbound, maxbound

    Finds out the boundaries/limits set for values of a chart flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            chart flobject

    Returns
    -------
        minbound : float
            minimum value limit
        maxbound : float
            maximum value limit

    Examples
    --------
        >>> minb, maxb = fl_get_chart_bounds(pchrtobj)

    API_diversion
    ----------
        API changed from XForms, upstream is
        fl_get_chart_bounds(ptr_flobject, minbound, maxbound)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_get_chart_bounds = library.cfuncproto(
        library.load_so_libforms(), "fl_get_chart_bounds",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_double),
        cty.POINTER(cty.c_double)],
        """void fl_get_chart_bounds(FL_OBJECT * ob, double * min,
           double * max)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    f_minbound, ptr_minbound = library.make_doublec_and_pointer()
    f_maxbound, ptr_maxbound = library.make_doublec_and_pointer()
    library.keep_elem_refs(ptr_flobject, f_minbound, f_maxbound, \
            ptr_minbound, ptr_maxbound)
    _fl_get_chart_bounds(ptr_flobject, ptr_minbound, ptr_maxbound)
    return f_minbound.value, f_maxbound.value


def fl_set_chart_maxnumb(ptr_flobject, maxnumvals):
    """fl_set_chart_maxnumb(ptr_flobject, maxnumvals)

    Defines the maximum number of values displayed in the chart. Defaults
    is xfdata.FL_CHART_MAX; maximum set cannot be more than that.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            chart flobject
        maxnumvals : int
            maximum number of values to display

    Examples
    --------
        >>> fl_set_chart_maxnumb(pchrtobj, 12)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_set_chart_maxnumb = library.cfuncproto(
        library.load_so_libforms(), "fl_set_chart_maxnumb",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_chart_maxnumb(FL_OBJECT * ob, int maxnumb)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_maxnumvals = library.convert_to_intc(maxnumvals)
    library.keep_elem_refs(ptr_flobject, maxnumvals, i_maxnumvals)
    _fl_set_chart_maxnumb(ptr_flobject, i_maxnumvals)


def fl_set_chart_autosize(ptr_flobject, yesno):
    """fl_set_chart_autosize(ptr_flobject, yesno)

    Defines whether the chart should autosize along the x-axis. Normally
    width of the bars and distance between the points in a line-chart are
    normally scaled.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            chart flobject
        yesno : int
            autosize flag. Values 1 (if enabled) or 0 (if disabled).
            If it is set to 0 the width of the bars will be such that the
            maximum number of items fits in the box.

    Examples
    --------
        >>> fl_set_chart_autosize(pchrtobj, 1)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_set_chart_autosize = library.cfuncproto(
        library.load_so_libforms(), "fl_set_chart_autosize",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_chart_autosize(FL_OBJECT * ob, int autosize)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_yesno = library.convert_to_intc(yesno)
    library.keep_elem_refs(ptr_flobject, yesno, i_yesno)
    _fl_set_chart_autosize(ptr_flobject, i_yesno)


def fl_set_chart_lstyle(ptr_flobject, style):
    """fl_set_chart_lstyle(ptr_flobject, style)

    Changes the font style of a chart's label. By default the label is
    drawn in a tiny font.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            chart flobject
        style : int
            label style. Values (from xfdata.py)
            - FL_NORMAL_STYLE (Helvetica normal text),
            - FL_BOLD_STYLE (Helvetica boldface text),
            - FL_ITALIC_STYLE (Helvetica italic text),
            - FL_BOLDITALIC_STYLE (Helvetica boldface and italic text),
            - FL_FIXED_STYLE (Courier fixed width, good for tables),
            - FL_FIXEDBOLD_STYLE (Courier bold fixed text),
            - FL_FIXEDITALIC_STYLE (Courier italic fixed text),
            - FL_FIXEDBOLDITALIC_STYLE (Courier boldface and italic fixed),
            - FL_TIMES_STYLE (Times-Roman like normal font),
            - FL_TIMESBOLD_STYLE (Times-Roman like boldface text),
            - FL_TIMESITALIC_STYLE (Times-Roman like italic text),
            - FL_TIMESBOLDITALIC_STYLE (Times-Roman like boldface and italic),
            - FL_MISC_STYLE (Charter normal text),
            - FL_MISCBOLD_STYLE (Charter boldface text),
            - FL_MISCITALIC_STYLE (Charter italic text),
            - FL_SYMBOL_STYLE (Symbol text),
            - FL_SHADOW_STYLE (Text casting a shadow, modifier mask),
            - FL_ENGRAVED_STYLE (Text engraved into the form, modifier mask),
            - FL_EMBOSSED_STYLE (Text standing out, modifier mask).
            Bitwise OR with any of modifiers is allowed.

    Examples
    --------
        >>> fl_set_chart_lstyle(pchrtobj, xfdata.FL_TIMESBOLD_STYLE)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_set_chart_lstyle = library.cfuncproto(
        library.load_so_libforms(), "fl_set_chart_lstyle",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_chart_lstyle(FL_OBJECT * ob, int lstyle)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.checkfatal_allowed_value_in_list(style, xfdata.TEXTSTYLE_list)
    i_style = library.convert_to_intc(style)
    library.keep_elem_refs(ptr_flobject, style, i_style)
    _fl_set_chart_lstyle(ptr_flobject, i_style)


def fl_set_chart_lsize(ptr_flobject, size):
    """fl_set_chart_lsize(ptr_flobject, size)

    Changes the font size of chart's label. By default, the label is
    drawn in a tiny font.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            chart flobject
        size : int
            label size. Values (from xfdata.py)
            - FL_TINY_SIZE (8 points font),
            - FL_SMALL_SIZE or FL_DEFAULT_SIZE (10 points font, default),
            - FL_NORMAL_SIZE (12 points font),
            - FL_MEDIUM_SIZE (14 points font),
            - FL_LARGE_SIZE (18 points font),
            - FL_HUGE_SIZE (24 points font),
            - or other numeric odd or even value

    Examples
    --------
        >>> fl_set_chart_lsize(pchrtobj, xfdata.FL_SMALL_SIZE)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_set_chart_lsize = library.cfuncproto(
        library.load_so_libforms(), "fl_set_chart_lsize",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_chart_lsize(FL_OBJECT * ob, int lsize)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_size = library.convert_to_intc(size)
    library.keep_elem_refs(ptr_flobject, size, i_size)
    _fl_set_chart_lsize(ptr_flobject, i_size)


def fl_set_chart_lcolor(ptr_flobject, colr):
    """fl_set_chart_lcolor(ptr_flobject, colr)

    Changes the color of chart's label. By default, the label is drawn
    in black.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            chart flobject
        colr : long_pos
            XForms colormap index as color

    Examples
    --------
        >>> fl_set_chart_lcolor(pchrtobj, xfdata.FL_FORESTGREEN)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_set_chart_lcolor = library.cfuncproto(
        library.load_so_libforms(), "fl_set_chart_lcolor",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.FL_COLOR],
        """void fl_set_chart_lcolor(FL_OBJECT * ob, FL_COLOR lcol)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    #library.checknonfatal_allowed_value_in_list(colr, xfdata.COLOR_list)
    ul_colr = library.convert_to_FL_COLOR(colr)
    library.keep_elem_refs(ptr_flobject, colr, ul_colr)
    _fl_set_chart_lcolor(ptr_flobject, ul_colr)


fl_set_chart_lcol = fl_set_chart_lcolor


def fl_set_chart_baseline(ptr_flobject, yesno):
    """fl_set_chart_baseline(ptr_flobject, yesno)

    Turns on or off the chart's baseline.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            chart flobject
        yesno : int
            flag for baseline. Values 0 (if disabled) or 1 (if enabled)

    Examples
    --------
        >>> fl_set_chart_baseline(pchrtobj, 1)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_set_chart_baseline = library.cfuncproto(
        library.load_so_libforms(), "fl_set_chart_baseline",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_chart_baseline(FL_OBJECT * ob, int iYesNo)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_yesno = library.convert_to_intc(yesno)
    library.keep_elem_refs(ptr_flobject, yesno, i_yesno)
    _fl_set_chart_baseline(ptr_flobject, i_yesno)

