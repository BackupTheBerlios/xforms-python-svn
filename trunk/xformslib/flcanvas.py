#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage canvas objects.

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


#######################
# forms.h (canvas.h)
# Header for FL_CANVAS
#######################

# Interfaces

def fl_create_generic_canvas(canvasclass, canvastype, x, y, w, h, label):
    """Creates a generic canvas object.

    --

    :Parameters:
      `canvasclass` : int
        value of a new canvas class
      `canvastype` : int
        type of canvas to be created. Values (from xfdata.py) FL_NORMAL_CANVAS,
        FL_SCROLLED_CANVAS (not enabled)
      `x` : int
        horizontal position (upper-left corner)
      `y` : int
        vertical position (upper-left corner)
      `w` : int
        width in coord units
      `h` : int
        height in coord units
      `label` : str
        text label of canvas

    :return: canvas object created (pFlObject)
    :rtype: pointer to xfdata.FL_OBJECT

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_create_generic_canvas = libr.cfuncproto(
        libr.load_so_libforms(), "fl_create_generic_canvas",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_create_generic_canvas(int canvas_class,
           int type, FL_Coord x, FL_Coord y, FL_Coord w, FL_Coord h,
           const char * label)""")
    libr.check_if_initialized()
    libr.check_admitted_value_in_list(canvastype, xfdata.CANVASTYPE_list)
    icanvasclass = libr.convert_to_int(canvasclass)
    icanvastype = libr.convert_to_int(canvastype)
    ix = libr.convert_to_FL_Coord(x)
    iy = libr.convert_to_FL_Coord(y)
    iw = libr.convert_to_FL_Coord(w)
    ih = libr.convert_to_FL_Coord(h)
    slabel = libr.convert_to_string(label)
    libr.keep_elem_refs(canvasclass, canvastype, x, y, w, h, label, \
                           icanvasclass, icanvastype, ix, iy, iw, ih, slabel)
    retval = _fl_create_generic_canvas(icanvasclass, icanvastype, ix, iy, \
                                       iw, ih, slabel)
    return retval


def fl_add_canvas(canvastype, x, y, w, h, label):
    """Adds a canvas object.

    --

    :Parameters:
      `canvastype` : int
        type of canvas to be added. Values (from xfdata.py) FL_NORMAL_CANVAS,
        FL_SCROLLED_CANVAS (not enabled)
      `x` : int
        horizontal position (upper-left corner)
      `y` : int
        vertical position (upper-left corner)
      `w` : int
        width in coord units
      `h` : int
        height in coord units
      `label` : str
        text label of canvas

    :return: canvas object added (pFlObject)
    :rtype: pointer to xfdata.FL_OBJECT

    :note: e.g. canvobj = fl_add_canvas(xfdata.FL_NORMAL_CANVAS, 150, 210,
        320, 200, "My Canvas")

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_add_canvas = libr.cfuncproto(
        libr.load_so_libforms(), "fl_add_canvas",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_canvas(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    libr.check_if_initialized()
    libr.check_admitted_value_in_list(canvastype, xfdata.CANVASTYPE_list)
    icanvastype = libr.convert_to_int(canvastype)
    ix = libr.convert_to_FL_Coord(x)
    iy = libr.convert_to_FL_Coord(y)
    iw = libr.convert_to_FL_Coord(w)
    ih = libr.convert_to_FL_Coord(h)
    slabel = libr.convert_to_string(label)
    libr.keep_elem_refs(canvastype, x, y, w, h, label, icanvastype, ix, iy,
                           iw, ih, slabel)
    retval = _fl_add_canvas(icanvastype, ix, iy, iw, ih, slabel)
    return retval


# fl_create_canvas function placeholder (internal)
# fl_set_canvas_decoration placeholder (backwards)


def fl_set_canvas_colormap(pFlObject, colormap):
    """Sets the color property of canvas. Caution: when the canvas window goes
    away, e.g. as a result of a call of fl_hide_form(), the colormap associated
    with the canvas is freed (destroyed); this likely will cause problems if a
    single colormap is used for multiple canvases as each canvas will attempt
    to free the same colormap, resulting in an X error.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        canvas object
      `colormap` : long_pos
        colormap of canvas

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_canvas_colormap = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_canvas_colormap",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.Colormap],
        """void fl_set_canvas_colormap(FL_OBJECT * ob, Colormap colormap)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    ulcolormap = libr.convert_to_ulong(colormap)
    libr.keep_elem_refs(pFlObject, colormap, ulcolormap)
    _fl_set_canvas_colormap(pFlObject, ulcolormap)


def fl_set_canvas_visual(pFlObject, pVisual):
    """Sets visual property of canvas. Changing visual does not generally make
     sense once the canvas window is created (which happens when the parent
     form is shown). Also, typically if you change the canvas visual, you
     probably should also change the canvas depth to match the visual.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        canvas object
      `pVisual` : pointer to xfdata.Visual
        class instance

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_canvas_visual = libr.cfuncproto(
            libr.load_so_libforms(), "fl_set_canvas_visual",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(xfdata.Visual)],
            """void fl_set_canvas_visual(FL_OBJECT * obj, Visual * vi)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.verify_otherclassptr_type(pVisual, cty.POINTER( \
                                            xfdata.Visual))
    libr.keep_elem_refs(pFlObject, pVisual)
    _fl_set_canvas_visual(pFlObject, pVisual)


def fl_set_canvas_depth(pFlObject, depth):
    """Sets the depth of canvas object. Changing depth does not generally make
    sense once the canvas window is created (which happens when the parent
    form is shown).

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        canvas object
      `depth` : int
        depth value of canvas. Values (from xfdata.py) e.g. 8, 16, 24?, 32, ...

    :note: e.g. fl_set_canvas_depth(canvobj, 32)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_set_canvas_depth = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_canvas_depth",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_canvas_depth(FL_OBJECT * obj, int depth)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    idepth = libr.convert_to_int(depth)
    libr.keep_elem_refs(pFlObject, depth, idepth)
    _fl_set_canvas_depth(pFlObject, idepth)


def fl_set_canvas_attributes(pFlObject, mask, pXSetWindowAttributes):
    """Modifies attributes of a canvas object (e.g. visual, depth and
     colormap etc.). By default, upon canvas creation, all its window related
     attributes are inherited from its parent (i.e. the window of the form the
     canvas belongs to). You should not use this function to modify events.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        canvas object
      `mask` : int_pos
        mask num.
      `pXSetWindowAttributes` : pointer to xfdata.XSetWindowAttributes
        class instance

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_canvas_attributes = libr.cfuncproto(
            libr.load_so_libforms(), "fl_set_canvas_attributes",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_uint,
            cty.POINTER(xfdata.XSetWindowAttributes)],
            """void fl_set_canvas_attributes(FL_OBJECT * ob,
               unsigned int mask, XSetWindowAttributes * xswa)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    uimask = libr.convert_to_uint(mask)
    libr.verify_otherclassptr_type(pXSetWindowAttributes, \
                                cty.POINTER(xfdata.XSetWindowAttributes))
    libr.keep_elem_refs(pFlObject, mask, pXSetWindowAttributes, uimask)
    _fl_set_canvas_attributes(pFlObject, uimask, pXSetWindowAttributes)


# TODO: take note in xfdata.py which X events belong here.
def fl_add_canvas_handler(pFlObject, xev, py_HandleCanvas, udata):
    """Sets a callback to be invoked for a specific X event.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        canvas object
      `xev` : int
        X event number. Values (from X11): Expose, etc.. ??
      `py_HandleCanvas` : python function to handle canvas
        name referring to function(pFlObject, win, num, num, pXEvent,
        ptr_void) -> num

    :return: old xfdata.FL_HANDLE_CANVAS handler function

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    #FL_HANDLE_CANVAS = cty.CFUNCTYPE(cty.c_int, cty.POINTER(xfdata.FL_OBJECT),
    #                             xfdata.Window, cty.c_int, cty.c_int,
    #                             cty.POINTER(xfdata.XEvent), cty.c_void_p)
    _fl_add_canvas_handler = libr.cfuncproto(
        libr.load_so_libforms(), "fl_add_canvas_handler",
        xfdata.FL_HANDLE_CANVAS, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int,
        xfdata.FL_HANDLE_CANVAS, cty.c_void_p],
        """FL_HANDLE_CANVAS fl_add_canvas_handler(FL_OBJECT * ob, int ev,
           FL_HANDLE_CANVAS h, void * udata)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    ixev = libr.convert_to_int(xev)
    c_HandleCanvas = xfdata.FL_HANDLE_CANVAS(py_HandleCanvas)
    pudata = cty.cast(udata, cty.c_void_p)
    libr.keep_cfunc_refs(c_HandleCanvas, py_HandleCanvas)
    libr.keep_elem_refs(pFlObject, xev, udata, ixev, pudata)
    retval = _fl_add_canvas_handler(pFlObject, ixev, c_HandleCanvas, pudata)
    return retval


def fl_get_canvas_id(pFlObject):
    """Returns the window id of the canvas object.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        canvas object

    :return: window id (win)
    :rtype: long_pos

    :note: e.g. canvwin = fl_get_canvas_id(pobj)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_get_canvas_id = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_canvas_id",
        xfdata.Window, [cty.POINTER(xfdata.FL_OBJECT)],
        """Window fl_get_canvas_id(FL_OBJECT * ob)""")
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_canvas_id(pFlObject)
    return retval


def fl_get_canvas_colormap(pFlObject):
    """Obtains the colormap of a canvas object.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        canvas object

    :return: colormap
    :rtype: long_pos

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_get_canvas_colormap = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_canvas_colormap",
        xfdata.Colormap, [cty.POINTER(xfdata.FL_OBJECT)],
        """Colormap fl_get_canvas_colormap(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_canvas_colormap(pFlObject)
    return retval


def fl_get_canvas_depth(pFlObject):
    """Obtains the depth of a canvas object (e.g. 8, 16, 24?, 32 ..).

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        canvas object

    :return: depth num.
    :rtype: int

    :note: e.g. canvdph = fl_get_canvas_depth(canvobj)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_get_canvas_depth = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_canvas_depth",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_canvas_depth(FL_OBJECT * obj)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    retval = _fl_get_canvas_depth(pFlObject)
    return retval


def fl_remove_canvas_handler(pFlObject, xev, py_HandleCanvas):
    """Removes a particular handler for a specified X event.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        canvas object
      `xev` : int
        X event number. If it is invalid, removes all handlers and their
        corresponding event mask.
      `py_HandleCanvas` : python function to handle canvas
        name referring to  function(pFlObject, win, num, num, pXEvent,
        ptr_void) -> num

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    #FL_HANDLE_CANVAS = cty.CFUNCTYPE(cty.c_int, cty.POINTER(xfdata.FL_OBJECT),
    #                             xfdata.Window, cty.c_int, cty.c_int,
    #                             cty.POINTER(xfdata.XEvent), cty.c_void_p)
    _fl_remove_canvas_handler = libr.cfuncproto(
        libr.load_so_libforms(), "fl_remove_canvas_handler",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int,
        xfdata.FL_HANDLE_CANVAS],
        """void fl_remove_canvas_handler(FL_OBJECT * ob, int ev,
           FL_HANDLE_CANVAS h)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    ixev = libr.convert_to_int(xev)
    c_HandleCanvas = xfdata.FL_HANDLE_CANVAS(py_HandleCanvas)
    libr.keep_cfunc_refs(c_HandleCanvas, py_HandleCanvas)
    libr.keep_elem_refs(pFlObject, xev, ixev)
    _fl_remove_canvas_handler(pFlObject, ixev, c_HandleCanvas)


def fl_hide_canvas(pFlObject):
    """Hides a canvas object.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        canvas object

    :note: e.g. fl_hide_canvas(canvobj)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_hide_canvas = libr.cfuncproto(
        libr.load_so_libforms(), "fl_hide_canvas",
        None, [cty.POINTER(xfdata.FL_OBJECT)],
        """void fl_hide_canvas(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    _fl_hide_canvas(pFlObject)


def fl_share_canvas_colormap(pFlObject, colormap):
    """Sets the color property of canvas. It also sets a internal flag so the
    colormap isn't freed when the canvas goes away.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        canvas object
      `colormap` : long_pos
        color map

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_share_canvas_colormap = libr.cfuncproto(
        libr.load_so_libforms(), "fl_share_canvas_colormap",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.Colormap],
        """void fl_share_canvas_colormap(FL_OBJECT * ob, Colormap colormap)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    ulcolormap = libr.convert_to_ulong(colormap)
    libr.keep_elem_refs(pFlObject, colormap, ulcolormap)
    _fl_share_canvas_colormap(pFlObject, ulcolormap)


def fl_clear_canvas(pFlObject):
    """Clears the canvas to the background color. If no background is
    defined uses black.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        canvas object

    :note: e.g. fl_clear_canvas(canvobj)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_clear_canvas = libr.cfuncproto(
        libr.load_so_libforms(), "fl_clear_canvas",
        None, [cty.POINTER(xfdata.FL_OBJECT)],
        """void fl_clear_canvas(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    _fl_clear_canvas(pFlObject)


# TODO: figure out what is its purpose.
def fl_modify_canvas_prop(pFlObject, py_initModifyCanvasProp,
     py_activateModifyCanvasProp, py_cleanupModifyCanvasProp):
    """Modifies init, activate and cleanup handler properties of a canvas
    object.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        canvas object
      `py_initModifyCanvasProp` : python function callback, returned value
        name referring to function(pFlObject) -> num.
      `py_activateModifyCanvasProp` : python function callback, returned value
        name referring to function(pFlObject) -> num.
      `py_cleanupModifyCanvasProp` : python function callback, returned value
        name referring to function(pFlObject) -> num.

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    #FL_MODIFY_CANVAS_PROP = cty.CFUNCTYPE(cty.c_int,
    #                              cty.POINTER(xfdata.FL_OBJECT))
    _fl_modify_canvas_prop = libr.cfuncproto(
        libr.load_so_libforms(), "fl_modify_canvas_prop",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.FL_MODIFY_CANVAS_PROP,
        xfdata.FL_MODIFY_CANVAS_PROP, xfdata.FL_MODIFY_CANVAS_PROP],
        """void fl_modify_canvas_prop(FL_OBJECT * obj,
           FL_MODIFY_CANVAS_PROP init, FL_MODIFY_CANVAS_PROP activate,
           FL_MODIFY_CANVAS_PROP cleanup)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    c_initModifyCanvasProp = xfdata.FL_MODIFY_CANVAS_PROP( \
            py_initModifyCanvasProp)
    c_activateModifyCanvasProp = xfdata.FL_MODIFY_CANVAS_PROP( \
                py_activateModifyCanvasProp)
    c_cleanupModifyCanvasProp = xfdata.FL_MODIFY_CANVAS_PROP( \
                py_cleanupModifyCanvasProp)
    libr.keep_cfunc_refs(c_initModifyCanvasProp, py_initModifyCanvasProp, \
                c_activateModifyCanvasProp, py_activateModifyCanvasProp, \
                c_cleanupModifyCanvasProp, py_cleanupModifyCanvasProp)
    libr.keep_elem_refs(pFlObject)
    _fl_modify_canvas_prop(pFlObject, c_initModifyCanvasProp,
                    c_activateModifyCanvasProp, c_cleanupModifyCanvasProp)


def fl_canvas_yield_to_shortcut(pFlObject, yesno):
    """Enables or disables keyboard inputs stealing by canvas. By default,
    objects with shortcuts appearing on the same form as the canvas will
    "steal" keyboard inputs if they match the shortcuts.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        canvas object
      `yesno` : int
        flag to enable/disable keyboard inputs stealing by canvas. Values 0
        (to disable) or 1 (to enable)

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_canvas_yield_to_shortcut = libr.cfuncproto(
        libr.load_so_libforms(), "fl_canvas_yield_to_shortcut",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_canvas_yield_to_shortcut(FL_OBJECT * ob, int yes)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    iyesno = libr.convert_to_int(yesno)
    libr.keep_elem_refs(pFlObject, yesno, iyesno)
    _fl_canvas_yield_to_shortcut(pFlObject, iyesno)
