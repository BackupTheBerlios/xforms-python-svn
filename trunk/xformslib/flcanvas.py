#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" xforms-python's functions to manage canvas flobjects.
"""

#    Copyright (C) 2009-2012  Luca Lazzaroni "LukenShiro"
#    e-mail: <lukenshiro@ngi.it>
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


#######################
# forms.h (canvas.h)
# Header for FL_CANVAS
#######################

# Interfaces

# fl_create_generic_canvas function placeholder (internal)


def fl_add_canvas(canvastype, xpos, ypos, width, height, label):
    """fl_add_canvas(canvastype, xpos, ypos, width, height, label)
    -> ptr_flobject

    Adds a canvas flobject.

    Parameters
    ----------
        canvastype : int
            type of canvas to be added. Values (from xfdata.py)
            FL_NORMAL_CANVAS (normal canvas flobject type), FL_SCROLLED_CANVAS
            (not enabled)
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            text label of canvas

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            canvas flobject added

    Examples
    --------
        >>> pcanvobj = fl_add_canvas(xfdata.FL_NORMAL_CANVAS, 150, 210,
                320, 200, "My Canvas")

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_add_canvas = library.cfuncproto(
        library.load_so_libforms(), "fl_add_canvas",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_canvas(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_flinitialized()
    library.checkfatal_allowed_value_in_list(canvastype, \
            xfdata.CANVASTYPE_list)
    i_canvastype = library.convert_to_intc(canvastype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_bytestrc(label)
    library.keep_elem_refs(canvastype, xpos, ypos, width, height, label, \
            i_canvastype, i_xpos, i_ypos, i_width, i_height, s_label)
    retval = _fl_add_canvas(i_canvastype, i_xpos, i_ypos, i_width, \
            i_height, s_label)
    return retval


# fl_create_canvas function placeholder (internal)
# fl_set_canvas_decoration placeholder (backwards)


def fl_set_canvas_colormap(ptr_flobject, colormap):
    """fl_set_canvas_colormap(ptr_flobject, colormap)

    Defines the color property of canvas. Caution: when the canvas window
    goes away, e.g. as a result of a call of fl_hide_form(), the colormap
    associated with the canvas is freed (destroyed); this likely will cause
    problems if a single colormap is used for multiple canvases as each
    canvas will attempt to free the same colormap, resulting in an X error.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            canvas flobject
        colormap : long_pos
            colormap of canvas

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_set_canvas_colormap = library.cfuncproto(
        library.load_so_libforms(), "fl_set_canvas_colormap",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.Colormap],
        """void fl_set_canvas_colormap(FL_OBJECT * ob, Colormap colormap)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    ul_colormap = library.convert_to_ulongc(colormap)
    library.keep_elem_refs(ptr_flobject, colormap, ul_colormap)
    _fl_set_canvas_colormap(ptr_flobject, ul_colormap)


def fl_set_canvas_visual(ptr_flobject, ptr_visual):
    """fl_set_canvas_visual(ptr_flobject, ptr_visual)

    Defines visual property of canvas flobject. Changing visual does not
    generally make sense once the canvas window is created (which happens
    when the parent form is shown). Also, typically if you change the canvas
    visual, you probably should also change the canvas depth to match the
    visual.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            canvas flobject
        ptr_visual : pointer to xfdata.Visual
            xfdata.Visual class instance

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_set_canvas_visual = library.cfuncproto(
            library.load_so_libforms(), "fl_set_canvas_visual",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(xfdata.Visual)],
            """void fl_set_canvas_visual(FL_OBJECT * obj, Visual * vi)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.verify_otherclassptr_type(ptr_visual, cty.POINTER(xfdata.Visual))
    library.keep_elem_refs(ptr_flobject, ptr_visual)
    _fl_set_canvas_visual(ptr_flobject, ptr_visual)


def fl_set_canvas_depth(ptr_flobject, depth):
    """fl_set_canvas_depth(ptr_flobject, depth)

    Defines the depth of canvas flobject. Changing depth does not generally
    make sense once the canvas window is created (which happens when the
    parent form is shown).

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            canvas flobject
        depth : int
            depth value of canvas. Values e.g. 8, 16, 24?, 32, ...

    Examples
    --------
        >>> fl_set_canvas_depth(pcanvobj, 32)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_set_canvas_depth = library.cfuncproto(
        library.load_so_libforms(), "fl_set_canvas_depth",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_canvas_depth(FL_OBJECT * obj, int depth)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_depth = library.convert_to_intc(depth)
    library.keep_elem_refs(ptr_flobject, depth, i_depth)
    _fl_set_canvas_depth(ptr_flobject, i_depth)


def fl_set_canvas_attributes(ptr_flobject, mask, ptr_xsetwindowattributes):
    """fl_set_canvas_attributes(ptr_flobject, mask, ptr_xsetwindowattributes)

    Modifies attributes of a canvas flobject (e.g. visual, depth and
    colormap etc.). By default, upon canvas creation, all its window related
    attributes are inherited from its parent (i.e. the window of the form the
    canvas belongs to). You should not use this function to modify events.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            canvas flobject
        mask : int_pos
            mask num.
        ptr_xsetwindowattributes : pointer to xfdata.XSetWindowAttributes
            xfdata.XSetWindowAttributes class instance

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_set_canvas_attributes = library.cfuncproto(
            library.load_so_libforms(), "fl_set_canvas_attributes",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_uint,
            cty.POINTER(xfdata.XSetWindowAttributes)],
            """void fl_set_canvas_attributes(FL_OBJECT * ob,
               unsigned int mask, XSetWindowAttributes * xswa)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    ui_mask = library.convert_to_uintc(mask)
    library.verify_otherclassptr_type(ptr_xsetwindowattributes, \
            cty.POINTER(xfdata.XSetWindowAttributes))
    library.keep_elem_refs(ptr_flobject, mask, ptr_xsetwindowattributes, \
            ui_mask)
    _fl_set_canvas_attributes(ptr_flobject, ui_mask, \
            ptr_xsetwindowattributes)


# TODO: take note in xfdata.py which X events belong here.
def fl_add_canvas_handler(ptr_flobject, evtnum, pyfn_HandleCanvas, userdata):
    """fl_add_canvas_handler(ptr_flobject, evtnum, pyfn_HandleCanvas,
    userdata) -> HandleCnavas

    Defines a callback to be invoked in a canvas flobject for a specific
    X event.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            canvas flobject
        evtnum : int
            X event number. Values (from xfdata.py): Expose, KeyPress,
            KeyRelease, ButtonRelease, etc..
        pyfn_HandleCanvas : python function to handle canvas, returned value
            name referring to function(ptr_flobject, [long_pos]win,
            [int]width, [int]height, ptr_xevent, [pointer to void]pvdata)
            -> [int]num
        userdata : any type (e.g. None, int, str, etc..)
            user data to be passed to function; invoked callback has to take
            care of type check and re-cast from ptr_void to chosen type using
            appropriate xfstruct.fls_convert_ptrvoid_to_*() function

    Returns
    -------
        HandleCanvas : xfdata.FL_HANDLE_CANVAS
            old canvas handler function

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    #FL_HANDLE_CANVAS = cty.CFUNCTYPE(cty.c_int, cty.POINTER(xfdata.FL_OBJECT),
    #       xfdata.Window, cty.c_int, cty.c_int, cty.POINTER(xfdata.XEvent),
    #       cty.c_void_p)
    _fl_add_canvas_handler = library.cfuncproto(
        library.load_so_libforms(), "fl_add_canvas_handler",
        xfdata.FL_HANDLE_CANVAS, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int,
        xfdata.FL_HANDLE_CANVAS, cty.c_void_p],
        """FL_HANDLE_CANVAS fl_add_canvas_handler(FL_OBJECT * ob, int ev,
           FL_HANDLE_CANVAS h, void * udata)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_evtnum = library.convert_to_intc(evtnum)
    library.verify_function_type(pyfn_HandleCanvas)
    cfn_HandleCanvas = xfdata.FL_HANDLE_CANVAS(pyfn_HandleCanvas)
    ptr_vdata = library.convert_userdata_to_ptrvoid(userdata)
    library.keep_cfunc_refs(cfn_HandleCanvas, pyfn_HandleCanvas)
    library.keep_elem_refs(ptr_flobject, evtnum, userdata, i_evtnum, \
            ptr_vdata)
    retval = _fl_add_canvas_handler(ptr_flobject, i_evtnum, \
            cfn_HandleCanvas, ptr_vdata)
    return retval


def fl_get_canvas_id(ptr_flobject):
    """fl_get_canvas_id(ptr_flobject) -> win

    Finds out the window id of the canvas flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            canvas flobject

    Returns
    -------
        win : long_pos
            window id

    Examples
    --------
        >>> canvwin = fl_get_canvas_id(pcanvobj)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_get_canvas_id = library.cfuncproto(
        library.load_so_libforms(), "fl_get_canvas_id",
        xfdata.Window, [cty.POINTER(xfdata.FL_OBJECT)],
        """Window fl_get_canvas_id(FL_OBJECT * ob)""")
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_canvas_id(ptr_flobject)
    return retval


def fl_get_canvas_colormap(ptr_flobject):
    """fl_get_canvas_colormap(ptr_flobject) -> colormap

    Finds out the colormap of a canvas flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            canvas flobject

    Returns
    -------
        colormap : long_pos
            canvas colormap

    Examples
    --------
        >>> ccmap = fl_get_canvas_colormap(pcanvobj)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_get_canvas_colormap = library.cfuncproto(
        library.load_so_libforms(), "fl_get_canvas_colormap",
        xfdata.Colormap, [cty.POINTER(xfdata.FL_OBJECT)],
        """Colormap fl_get_canvas_colormap(FL_OBJECT * ob)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_canvas_colormap(ptr_flobject)
    return retval


def fl_get_canvas_depth(ptr_flobject):
    """fl_get_canvas_depth(ptr_flobject) -> depth

    Finds out the depth of a canvas flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            canvas flobject

    Returns
    -------
        depth : int
            canvas depth (e.g. 8, 16, 24?, 32 ..)

    Examples
    --------
        >>> canvdph = fl_get_canvas_depth(pcanvobj)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_get_canvas_depth = library.cfuncproto(
        library.load_so_libforms(), "fl_get_canvas_depth",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_canvas_depth(FL_OBJECT * obj)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_canvas_depth(ptr_flobject)
    return retval


def fl_remove_canvas_handler(ptr_flobject, evtnum, pyfn_HandleCanvas):
    """fl_remove_canvas_handler(ptr_flobject, evtnum, pyfn_HandleCanvas)

    Removes a particular handler for a specified X event, previously
    created with fl_add_canvas_handler().

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            canvas flobject
        evtnum : int
            X event number. Values (from xfdata.py): Expose, KeyPress,
            KeyRelease, ButtonRelease, etc.. If it is invalid, removes all
            handlers and their corresponding event mask.
        pyfn_HandleCanvas : python function to handle canvas, returned value
            name referring to function(ptr_flobject, [long_pos]win,
            [int]width, [int]height, ptr_xevent, [pointer to void]vdata)
            -> [int]num

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    #FL_HANDLE_CANVAS = cty.CFUNCTYPE(cty.c_int, cty.POINTER(xfdata.FL_OBJECT),
    #                             xfdata.Window, cty.c_int, cty.c_int,
    #                             cty.POINTER(xfdata.XEvent), cty.c_void_p)
    _fl_remove_canvas_handler = library.cfuncproto(
        library.load_so_libforms(), "fl_remove_canvas_handler",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int,
        xfdata.FL_HANDLE_CANVAS],
        """void fl_remove_canvas_handler(FL_OBJECT * ob, int ev,
           FL_HANDLE_CANVAS h)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_evtnum = library.convert_to_intc(evtnum)
    library.verify_function_type(pyfn_HandleCanvas)
    cfn_HandleCanvas = xfdata.FL_HANDLE_CANVAS(pyfn_HandleCanvas)
    library.keep_cfunc_refs(cfn_HandleCanvas, pyfn_HandleCanvas)
    library.keep_elem_refs(ptr_flobject, evtnum, i_evtnum)
    _fl_remove_canvas_handler(ptr_flobject, i_evtnum, cfn_HandleCanvas)


def fl_hide_canvas(ptr_flobject):
    """fl_hide_canvas(ptr_flobject)

    Hides a canvas flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            canvas flobject

    Examples
    --------
        >>> fl_hide_canvas(pcanvobj)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_hide_canvas = library.cfuncproto(
        library.load_so_libforms(), "fl_hide_canvas",
        None, [cty.POINTER(xfdata.FL_OBJECT)],
        """void fl_hide_canvas(FL_OBJECT * ob)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    _fl_hide_canvas(ptr_flobject)


def fl_share_canvas_colormap(ptr_flobject, colormap):
    """fl_share_canvas_colormap(ptr_flobject, colormap)

    Defines the color property of canvas flobject. It also sets an internal
    flag so the colormap is not freed when the canvas goes away.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            canvas flobject
        colormap : long_pos
            colormap of canvas

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_share_canvas_colormap = library.cfuncproto(
        library.load_so_libforms(), "fl_share_canvas_colormap",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.Colormap],
        """void fl_share_canvas_colormap(FL_OBJECT * ob, Colormap colormap)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    ul_colormap = library.convert_to_ulongc(colormap)
    library.keep_elem_refs(ptr_flobject, colormap, ul_colormap)
    _fl_share_canvas_colormap(ptr_flobject, ul_colormap)


def fl_clear_canvas(ptr_flobject):
    """fl_clear_canvas(ptr_flobject)

    Clears the canvas to the background color. If no background is defined,
    uses black.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            canvas flobject

    Examples
    --------
        >>> fl_clear_canvas(pcanvobj)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_clear_canvas = library.cfuncproto(
        library.load_so_libforms(), "fl_clear_canvas",
        None, [cty.POINTER(xfdata.FL_OBJECT)],
        """void fl_clear_canvas(FL_OBJECT * ob)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    _fl_clear_canvas(ptr_flobject)


# TODO: figure out what is its purpose.
def fl_modify_canvas_prop(ptr_flobject, pyfn_initModifyCanvasProp,
            pyfn_activateModifyCanvasProp, pyfn_cleanupModifyCanvasProp):
    """fl_modify_canvas_prop(ptr_flobject, pyfn_initModifyCanvasProp,
    pyfn_activateModifyCanvasProp, pyfn_cleanupModifyCanvasProp)

    Modifies init, activate and cleanup handler properties of a canvas
    flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            canvas flobject
        pyfn_initModifyCanvasProp : python function callback, returned value
            name referring to function(ptr_flobject) -> [int]num
        pyfn_activateModifyCanvasProp : python func. callback, returned value
            name referring to function(ptr_flobject) -> [int]num.
        pyfn_cleanupModifyCanvasProp : python func. callback, returned value
            name referring to function(ptr_flobject) -> [int]num.

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    #FL_MODIFY_CANVAS_PROP = cty.CFUNCTYPE(cty.c_int,
    #                              cty.POINTER(xfdata.FL_OBJECT))
    _fl_modify_canvas_prop = library.cfuncproto(
        library.load_so_libforms(), "fl_modify_canvas_prop",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.FL_MODIFY_CANVAS_PROP,
        xfdata.FL_MODIFY_CANVAS_PROP, xfdata.FL_MODIFY_CANVAS_PROP],
        """void fl_modify_canvas_prop(FL_OBJECT * obj,
           FL_MODIFY_CANVAS_PROP init, FL_MODIFY_CANVAS_PROP activate,
           FL_MODIFY_CANVAS_PROP cleanup)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.verify_function_type(pyfn_initModifyCanvasProp)
    cfn_initModifyCanvasProp = xfdata.FL_MODIFY_CANVAS_PROP( \
            pyfn_initModifyCanvasProp)
    library.verify_function_type(pyfn_activateModifyCanvasProp)
    cfn_activateModifyCanvasProp = xfdata.FL_MODIFY_CANVAS_PROP( \
                pyfn_activateModifyCanvasProp)
    library.verify_function_type(pyfn_cleanupModifyCanvasProp)
    cfn_cleanupModifyCanvasProp = xfdata.FL_MODIFY_CANVAS_PROP( \
                pyfn_cleanupModifyCanvasProp)
    library.keep_cfunc_refs(cfn_initModifyCanvasProp, \
            pyfn_initModifyCanvasProp, cfn_activateModifyCanvasProp, \
            pyfn_activateModifyCanvasProp, cfn_cleanupModifyCanvasProp, \
            pyfn_cleanupModifyCanvasProp)
    library.keep_elem_refs(ptr_flobject)
    _fl_modify_canvas_prop(ptr_flobject, cfn_initModifyCanvasProp,
            cfn_activateModifyCanvasProp, cfn_cleanupModifyCanvasProp)


def fl_canvas_yield_to_shortcut(ptr_flobject, yesno):
    """fl_canvas_yield_to_shortcut(ptr_flobject, yesno)

    Enables or disables keyboard input's stealing by canvas. By default,
    flobjects with shortcuts appearing on the same form as the canvas will
    "steal" keyboard inputs if they match the shortcuts.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            canvas flobject
        yesno : int
            flag to enable/disable keyboard input's stealing by canvas.
            Values 0 (to disable) or 1 (to enable)

    Examples
    --------
        >>> fl_canvas_yield_to_shortcut(pcanvobj, 1)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_canvas_yield_to_shortcut = library.cfuncproto(
        library.load_so_libforms(), "fl_canvas_yield_to_shortcut",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_canvas_yield_to_shortcut(FL_OBJECT * ob, int yes)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_yesno = library.convert_to_intc(yesno)
    library.keep_elem_refs(ptr_flobject, yesno, i_yesno)
    _fl_canvas_yield_to_shortcut(ptr_flobject, i_yesno)

