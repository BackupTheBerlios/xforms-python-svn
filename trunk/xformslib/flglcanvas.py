#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" xforms-python's functions to manage GLcanvas flobjects.
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


#############
# glcanvas.h
#############

# OpenGL canvases

# fl_create_glcanvas function placeholder (internal)


def fl_add_glcanvas(canvastype, xpos, ypos, width, height, label):
    """fl_add_glcanvas(canvastype, xpos, ypos, width, height, label)
    -> ptr_flobject

    Adds a glcanvas flobject to the form.

    Parameters
    ----------
        canvastype : int
            type of glcanvas to be added. Values (from xfdata.py)
            - FL_NORMAL_CANVAS (normal canvas type),
            - FL_SCROLLED_CANVAS (not enabled)
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            text label of glcanvas

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            glcanvas flobject added

    Examples
    --------
        >>> pglcnvobj =  fl_add_glcanvas(xfdata.FL_NORMAL_CANVAS, 14, 21,
                654, 457, "My Gl Canvas")

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_add_glcanvas = library.cfuncproto(
        library.load_so_libformsgl(), "fl_add_glcanvas",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_glcanvas(int type, FL_Coord x, FL_Coord y,
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
    retval = _fl_add_glcanvas(i_canvastype, i_xpos, i_ypos, i_width, \
            i_height, s_label)
    return retval


def fl_set_glcanvas_defaults(glconfig):
    """fl_set_glcanvas_defaults(glconfig)

    Modifies the global default attributes for glcanvas, before the creation
    of glcanvases. By default they are the following (from xfdata.py):
    GLX_RGBA, GLX_DEPTH_SIZE, 1, GLX_RED_SIZE, 1, GLX_GREEN_SIZE, 1,
    GLX_BLUE_SIZE, 1, GLX_DOUBLEBUFFER. Pairs is (variable-only) or
    (variable, value).

    Parameters
    ----------
        glconfig : list of int
            configuration settings, ending with -1. Attributes are, as defined
            in OpenGL glXChooseVisual() function, GLX_USE_GL, GLX_BUFFER_SIZE,
            GLX_LEVEL, GLX_RGBA, GLX_DOUBLEBUFFER, GLX_STEREO, GLX_AUX_BUFFERS,
            GLX_RED_SIZE, GLX_GREEN_SIZE, GLX_BLUE_SIZE, GLX_ALPHA_SIZE,
            GLX_DEPTH_SIZE, GLX_STENCIL_SIZE, GLX_ACCUM_RED_SIZE,
            GLX_ACCUM_GREEN_SIZE, GLX_ACCUM_BLUE_SIZE, GLX_ACCUM_ALPHA_SIZE.
            See xfdata.py for values.

    Examples
    --------
        >>> fl_set_glcanvas_defaults([GLX_RGBA, GLX_DEPTH_SIZE, 2,
                GLX_RED_SIZE, 2, GLX_GREEN_SIZE, 2, GLX_BLUE_SIZE, 2])

    Notes
    -----
        Status: NA-UTest + NoDoc + NoDemo = Maybe

    """
    _fl_set_glcanvas_defaults = library.cfuncproto(
        library.load_so_libformsgl(), "fl_set_glcanvas_defaults",
        None, [cty.POINTER(cty.c_int)],
        """void fl_set_glcanvas_defaults(const int * config)""")
    library.check_if_flinitialized()
    #ptr_glconfig = cty.cast(config, cty.POINTER(cty.c_int))  # to be verified
    ptr_glconfig = library.convert_to_ptr_intc(glconfig)
    library.keep_elem_refs(glconfig, ptr_glconfig)
    _fl_set_glcanvas_defaults(ptr_glconfig)


def fl_get_glcanvas_defaults():
    """fl_get_glcanvas_defaults() -> glconfig

    Finds out the global defaults attributes for glcanvas.

    Returns
    -------
        glconfig : array of int
            configuration settings, ending with -1. Attributes are, as defined
            in OpenGL glXChooseVisual() function, GLX_USE_GL, GLX_BUFFER_SIZE,
            GLX_LEVEL, GLX_RGBA, GLX_DOUBLEBUFFER, GLX_STEREO, GLX_AUX_BUFFERS,
            GLX_RED_SIZE, GLX_GREEN_SIZE, GLX_BLUE_SIZE, GLX_ALPHA_SIZE,
            GLX_DEPTH_SIZE, GLX_STENCIL_SIZE, GLX_ACCUM_RED_SIZE,
            GLX_ACCUM_GREEN_SIZE, GLX_ACCUM_BLUE_SIZE, GLX_ACCUM_ALPHA_SIZE.
            See xfdata.py for values.

    Examples
    --------
        >>> cnfset = fl_get_glcanvas_defaults()

    API_diversion
    ----------
        API changed from XForms, upstream is fl_get_glcanvas_defaults(config)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_get_glcanvas_defaults = library.cfuncproto(
        library.load_so_libformsgl(), "fl_get_glcanvas_defaults",
        None, [cty.POINTER(cty.c_int)],
        """void fl_get_glcanvas_defaults(int config[ ])""")
    library.check_if_flinitialized()     # unsure
    i_glconfig, ptr_glconfig = library.make_intc_and_pointer()
    library.keep_elem_refs(i_glconfig, ptr_glconfig)
    _fl_get_glcanvas_defaults(ptr_glconfig)
    return i_glconfig.value


def fl_set_glcanvas_attributes(ptr_flobject, glconfig):
    """fl_set_glcanvas_attributes(ptr_flobject, glconfig)

    Modifies the default configuration of a particular glcanvas flobject.
    You can change a glcanvas attribute on the fly even if the canvas is
    already visible and active. By default they are the following (from
    xfdata.py): GLX_RGBA, GLX_DEPTH_SIZE, 1, GLX_RED_SIZE, 1, GLX_GREEN_SIZE,
    1, GLX_BLUE_SIZE, 1, GLX_DOUBLEBUFFER. Pairs is (variable-only) or
    (variable, value).

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            glcanvas flobject
        glconfig : list of int
            configuration settings to be set. Attributes are, as defined in
            OpenGL glXChooseVisual() function, GLX_USE_GL, GLX_BUFFER_SIZE,
            GLX_LEVEL, GLX_RGBA, GLX_DOUBLEBUFFER, GLX_STEREO, GLX_AUX_BUFFERS,
            GLX_RED_SIZE, GLX_GREEN_SIZE, GLX_BLUE_SIZE, GLX_ALPHA_SIZE,
            GLX_DEPTH_SIZE, GLX_STENCIL_SIZE, GLX_ACCUM_RED_SIZE,
            GLX_ACCUM_GREEN_SIZE, GLX_ACCUM_BLUE_SIZE, GLX_ACCUM_ALPHA_SIZE.
            See xfdata.py for values.

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + NoDoc + NoDemo = Maybe

    """
    _fl_set_glcanvas_attributes = library.cfuncproto(
        library.load_so_libformsgl(), "fl_set_glcanvas_attributes",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int)],
        """void fl_set_glcanvas_attributes(FL_OBJECT * ob,
           const int * config)""")
    library.check_if_flinitialized()     # unsure
    library.verify_flobjectptr_type(ptr_flobject)
    #ptr_glconfig = cty.cast(glconfig, cty.POINTER(cty.c_int))
    ptr_glconfig = library.convert_to_ptr_intc(glconfig)
    library.keep_elem_refs(ptr_flobject, glconfig, ptr_glconfig)
    _fl_set_glcanvas_attributes(ptr_flobject, ptr_glconfig)


def fl_get_glcanvas_attributes(ptr_flobject):
    """fl_get_glcanvas_attributes(ptr_flobject) -> glconfig

    Finds out the attributes of a glcanvas flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            glcanvas flobject

    Returns
    -------
        glconfig : int
            glcanvas configuration settings. Attributes are, as defined in
            OpenGL glXChooseVisual() function, GLX_USE_GL, GLX_BUFFER_SIZE,
            GLX_LEVEL, GLX_RGBA, GLX_DOUBLEBUFFER, GLX_STEREO, GLX_AUX_BUFFERS,
            GLX_RED_SIZE, GLX_GREEN_SIZE, GLX_BLUE_SIZE, GLX_ALPHA_SIZE,
            GLX_DEPTH_SIZE, GLX_STENCIL_SIZE, GLX_ACCUM_RED_SIZE,
            GLX_ACCUM_GREEN_SIZE, GLX_ACCUM_BLUE_SIZE, GLX_ACCUM_ALPHA_SIZE.
            See xfdata.py for values.

    Examples
    --------
        >>> attrb = fl_get_glcanvas_attributes(pglcnvobj)

    API_diversion
    ----------
        API changed from XForms, upstream is
        fl_get_glcanvas_attributes(ptr_flobject, attributes)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_get_glcanvas_attributes = library.cfuncproto(
        library.load_so_libformsgl(), "fl_get_glcanvas_attributes",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int)],
        """void fl_get_glcanvas_attributes(FL_OBJECT * ob,
           int * attributes)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    glconfig, ptr_glconfig = library.make_intc_and_pointer()
    library.keep_elem_refs(ptr_flobject, glconfig, ptr_glconfig)
    _fl_get_glcanvas_attributes(ptr_flobject, ptr_glconfig)
    return glconfig.value


def fl_set_glcanvas_direct(ptr_flobject, yesno):
    """fl_set_glcanvas_direct(ptr_flobject, yesno)

    Changes the rendering context created by a glcanvas flobject. By default
    it uses direct rendering (i.e. by-passing the Xserver).

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            glcanvas flobject
        yesno : int
            flag to use direct or through-Xserver rendering. Values 0 (to use
            Xserver rendering) or 1 (to use direct rendering)

    Examples
    --------
        >>> fl_set_glcanvas_direct(pglcnvobj, 0)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_set_glcanvas_direct = library.cfuncproto(
        library.load_so_libformsgl(), "fl_set_glcanvas_direct",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_glcanvas_direct(FL_OBJECT * ob, int direct)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_yesno = library.convert_to_intc(yesno)
    library.keep_elem_refs(ptr_flobject, yesno, i_yesno)
    _fl_set_glcanvas_direct(ptr_flobject, i_yesno)


def fl_activate_glcanvas(ptr_flobject):
    """fl_activate_glcanvas(ptr_flobject)

    Activates a glcanvas flobject before drawing into glcanvas flobject.
    OpenGL drawing routines always draw into the window the current context
    is bound to. For application with a single canvas, this is not a problem.
    In case of multiple canvases, the canvas driver takes care of setting the
    proper context before invoking the expose handler. In some cases, the
    application may want to draw into canvases actively. In this case, use
    this function for explicit drawing context switching.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            glcanvas flobject

    Examples
    --------
        >>> fl_activate_glcanvas(pglcnvobj)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_activate_glcanvas = library.cfuncproto(
        library.load_so_libformsgl(), "fl_activate_glcanvas",
        None, [cty.POINTER(xfdata.FL_OBJECT)],
        """void fl_activate_glcanvas(FL_OBJECT * ob)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    _fl_activate_glcanvas(ptr_flobject)


def fl_get_glcanvas_xvisualinfo(ptr_flobject):
    """fl_get_glcanvas_xvisualinfo(ptr_flobject) -> ptr_xvisualinfo

    Finds out the XVisual information that is used to create the context of
    a glcanvas flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            glcanvas flobject

    Returns
    -------
        ptr_xvisualinfo : pointer to xfdata.XVisualInfo
            XVisualInfo instance class

    Examples
    --------
        >>> pxviscls = fl_get_glcanvas_xvisualinfo(pglcnvobj)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_get_glcanvas_xvisualinfo = library.cfuncproto(
        library.load_so_libformsgl(), "fl_get_glcanvas_xvisualinfo",
        cty.POINTER(xfdata.XVisualInfo), [cty.POINTER(xfdata.FL_OBJECT)],
        """XVisualInfo * fl_get_glcanvas_xvisualinfo(FL_OBJECT * ob)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_glcanvas_xvisualinfo(ptr_flobject)
    return retval


def fl_get_glcanvas_context(ptr_flobject):
    """fl_get_glcanvas_context(ptr_flobject) -> glxcontext

    Finds out GLXContext of a glcanvas flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            glcanvas flobject

    Returns
    -------
        glxcontext : xfdata.GLXContext
            glxcontext class instance

    Examples
    --------
        >>> glxcont = fl_get_glcanvas_context(pglcnvobj)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_get_glcanvas_context = library.cfuncproto(
        library.load_so_libformsgl(), "fl_get_glcanvas_context",
        xfdata.GLXContext, [cty.POINTER(xfdata.FL_OBJECT)],
        """GLXContext fl_get_glcanvas_context(FL_OBJECT * ob)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    retval = _fl_get_glcanvas_context(ptr_flobject)
    return retval


# TODO: verify correctness of params
def fl_glwincreate(glconfig, ptr_glxcontext, width, height):
    """fl_glwincreate(glconfig, ptr_glxcontext, width, height) -> win

    Creates a toplevel OpenGL window.

    Parameters
    ----------
        glconfig : int
            GL configuration settings. See xfdata.py for values
        ptr_glxcontext : pointer to xfdata.GLXContext?? *todo*
            glxcontext class instance
        width : int
            width of GL window in coord units
        height : int
            height of GL window in coord units

    Returns
    -------
        win : long_pos
            window id created

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + NoDoc + NoDemo = KO

    """
    _fl_glwincreate = library.cfuncproto(
        library.load_so_libformsgl(), "fl_glwincreate",
        xfdata.Window, [cty.POINTER(cty.c_int), cty.POINTER(xfdata.GLXContext),
        cty.c_int, cty.c_int],
        """Window fl_glwincreate(int * config, GLXContext * context,
           int w, int h)""")
    ptr_glconfig = cty.cast(glconfig, cty.POINTER(cty.c_int)) # to be verified
    #pGLXContext = cty.cast(glxcontext, cty.POINTER(xfdata.GLXContext)
    library.verify_otherclassptr_type(ptr_glxcontext, \
            cty.POINTER(xfdata.GLXContext))
    i_width = library.convert_to_intc(width)
    i_height = library.convert_to_intc(height)
    library.keep_elem_refs(glconfig, ptr_glxcontext, width, height, i_width, \
            i_height, ptr_glconfig)
    retval = _fl_glwincreate(ptr_glconfig, ptr_glxcontext, i_width, i_height)
    return retval


# TODO: verify correctness of params
def fl_glwinopen(glconfig, ptr_glxcontext, width, height):
    """fl_glwinopen(glconfig, ptr_glxcontext, width, height)

    Opens a toplevel OpenGL window.

    Parameters
    ----------
        glconfig : int
            GL configuration settings. See xfdata.py for values
        ptr_glxcontext : pointer to xfdata.GLXContext *todo*
            glxcontext class instance??
        width : int
            width of GL window in coord units
        height : int
            height of GL window in coord units

    Returns
    -------
        win : long_pos
            window id opened

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + NoDoc + NoDemo = KO

    """
    _fl_glwinopen = library.cfuncproto(
        library.load_so_libformsgl(), "fl_glwinopen",
        xfdata.Window, [cty.POINTER(cty.c_int),
        cty.POINTER(xfdata.GLXContext), cty.c_int, cty.c_int],
        """Window fl_glwinopen(int * config, GLXContext * context,
           int w, int h""")
    library.check_if_flinitialized()
    ptr_glconfig = cty.cast(glconfig, cty.POINTER(cty.c_int)) # to be verified
    #pGLXContext = cty.cast(glxcontext, cty.POINTER(xfdata.GLXContext))
    library.verify_otherclassptr_type(ptr_glxcontext, \
            cty.POINTER(xfdata.GLXContext))
    i_width = library.convert_to_intc(width)
    i_height = library.convert_to_intc(height)
    library.keep_elem_refs(glconfig, ptr_glxcontext, width, height, \
            i_width, i_height, ptr_glconfig)
    retval = _fl_glwinopen(ptr_glconfig, ptr_glxcontext, i_width, i_height)
    return retval

