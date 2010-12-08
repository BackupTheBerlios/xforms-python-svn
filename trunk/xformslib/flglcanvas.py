#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage GLcanvas objects.
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
# Interface to XForms shared object libraries   #
# ############################################# #


import ctypes as cty
from xformslib import library
from xformslib import xfdata


#############
# glcanvas.h
#############

# OpenGL canvases

# fl_create_glcanvas function placeholder (internal)


def fl_add_glcanvas(canvastype, x, y, w, h, label):
    """fl_add_glcanvas(canvastype, x, y, w, h, label)
    
    Adds a glcanvas object to the form.

    Parameters
    ----------
        canvastype : int
            type of glcanvas to be added. Values (from xfdata.py)
            FL_NORMAL_CANVAS, FL_SCROLLED_CANVAS (not enabled)
        x : int
            horizontal position (upper-left corner)
        y : int
            vertical position (upper-left corner)
        w : int
            width in coord units
        h : int
            height in coord units
        label : str
            text label of glcanvas

    Returns
    -------
        pFlObject : pointer to xfdata.FL_OBJECT
            glcanvas object added

    Examples
    -------- fl_add_glcanvas(xfdata.FL_NORMAL_CANVAS, 14, 21, 654, 457,
        "My Gl Canvas")

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_add_glcanvas = library.cfuncproto(
        library.load_so_libformsgl(), "fl_add_glcanvas",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_glcanvas(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.checkfatal_allowed_value_in_list(canvastype, \
            xfdata.CANVASTYPE_list)
    icanvastype = library.convert_to_int(canvastype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(canvastype, x, y, w, h, label, icanvastype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_glcanvas(icanvastype, ix, iy, iw, ih, slabel)
    return retval


def fl_set_glcanvas_defaults(config):
    """fl_set_glcanvas_defaults(config)
    
    Modifies the global default attributes for glcanvas, before the
    creation of glcanvases.

    Parameters
    ----------
        config : int
            configuration settings. Attributes are those defined in OpenGL
            glXChooseVisual() function *todo*

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_glcanvas_defaults = library.cfuncproto(
        library.load_so_libformsgl(), "fl_set_glcanvas_defaults",
        None, [cty.POINTER(cty.c_int)],
        """void fl_set_glcanvas_defaults(const int * config)""")
    library.check_if_initialized()     # unsure
    pconfig = cty.cast(config, cty.POINTER(cty.c_int))
    library.keep_elem_refs(config, pconfig)
    _fl_set_glcanvas_defaults(pconfig)


def fl_get_glcanvas_defaults():
    """fl_get_glcanvas_defaults()
    
    Obtains the global defaults attributes for glcanvas.

    Returns
    -------
        config : int
            configuration settings

    Examples
    --------
        >>> cnfset = fl_get_glcanvas_defaults()

    API_diversion
    ----------
        API changed from XForms, upstream was
        fl_get_glcanvas_defaults(config)

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_get_glcanvas_defaults = library.cfuncproto(
        library.load_so_libformsgl(), "fl_get_glcanvas_defaults",
        None, [cty.POINTER(cty.c_int)],
        """void fl_get_glcanvas_defaults(int config[ ])""")
    library.check_if_initialized()     # unsure
    config, pconfig = library.make_int_and_pointer()
    library.keep_elem_refs(config, pconfig)
    _fl_get_glcanvas_defaults(pconfig)
    return config.value


def fl_set_glcanvas_attributes(pFlObject, config):
    """fl_set_glcanvas_attributes(pFlObject, config)
    
    Modifies the default configuration of a particular glcanvas
    object. You can change a glcanvas attribute on the fly even if
    the canvas is already visible and active.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            glcanvas object
        config : int
            configuration settings to be set. Attributes are those defined
            in OpenGL glXChooseVisual() function *todo*

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + NoDoc + NoDemo = NOT OK

    """
    _fl_set_glcanvas_attributes = library.cfuncproto(
        library.load_so_libformsgl(), "fl_set_glcanvas_attributes",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int)],
        """void fl_set_glcanvas_attributes(FL_OBJECT * ob,
           const int * config)""")
    library.check_if_initialized()     # unsure
    library.verify_flobjectptr_type(pFlObject)
    pconfig = cty.cast(config, cty.POINTER(cty.c_int))
    library.keep_elem_refs(pFlObject, config, pconfig)
    _fl_set_glcanvas_attributes(pFlObject, pconfig)


def fl_get_glcanvas_attributes(pFlObject):
    """fl_get_glcanvas_attributes(pFlObject)
    
    Obtains the attributes of a glcanvas object.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            glcanvas object

    Returns
    -------
        attribs : int
            glcanvas attributes

    Examples
    --------
        >>> attrb = fl_get_glcanvas_attributes(glcanobj)

    API_diversion
    ----------
        API changed from XForms, upstream was
        fl_get_glcanvas_attributes(pFlObject, attributes)

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_get_glcanvas_attributes = library.cfuncproto(
        library.load_so_libformsgl(), "fl_get_glcanvas_attributes",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int)],
        """void fl_get_glcanvas_attributes(FL_OBJECT * ob,
           int * attributes)""")
    library.check_if_initialized()     # unsure
    library.verify_flobjectptr_type(pFlObject)
    attributes, pattributes = library.make_int_and_pointer()
    library.keep_elem_refs(pFlObject, attributes, pattributes)
    _fl_get_glcanvas_attributes(pFlObject, pattributes)
    return attributes.value


def fl_set_glcanvas_direct(pFlObject, yesno):
    """fl_set_glcanvas_direct(pFlObject, yesno)
    
    Changes the rendering context created by a glcanvas. By default it
    uses direct rendering (i.e. by-passing the Xserver).

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            glcanvas object
        yesno : int
            flag to use direct or through-Xserver rendering. Values 0 (to
            use Xserver rendering) or 1 (to use direct rendering)

    Examples
    --------
        >>> fl_set_glcanvas_direct(glcanobj, 0)

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_set_glcanvas_direct = library.cfuncproto(
        library.load_so_libformsgl(), "fl_set_glcanvas_direct",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_glcanvas_direct(FL_OBJECT * ob, int direct)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    iyesno = library.convert_to_int(yesno)
    library.keep_elem_refs(pFlObject, yesno, iyesno)
    _fl_set_glcanvas_direct(pFlObject, iyesno)


def fl_activate_glcanvas(pFlObject):
    """fl_activate_glcanvas(pFlObject)
    
    Activates a glcanvas object before drawing into glcanvas object. OpenGL
    drawing routines always draw into the window the current context is bound
    to. For application with a single canvas, this is not a problem. In case
    of multiple canvases, the canvas driver takes care of setting the proper
    context before invoking the expose handler. In some cases, the
    application may want to draw into canvases actively. In this case, use
    this function for explicit drawing context switching.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            glcanvas object

    Examples
    --------
        >>> fl_activate_glcanvas(glcanobj)

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_activate_glcanvas = library.cfuncproto(
        library.load_so_libformsgl(), "fl_activate_glcanvas",
        None, [cty.POINTER(xfdata.FL_OBJECT)],
        """void fl_activate_glcanvas(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    library.keep_elem_refs(pFlObject)
    _fl_activate_glcanvas(pFlObject)


def fl_get_glcanvas_xvisualinfo(pFlObject):
    """fl_get_glcanvas_xvisualinfo(pFlObject)
    
    Obtains the XVisual information that is used to create the context
    of a glcanvas object.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            glcanvas object

    Returns
    -------
        pXVisualInfo : pointer to xfdata.XVisualInfo
            XVisualInfo instance class

    Examples
    --------
        >>> pxviscls = fl_get_glcanvas_xvisualinfo(glcanobj)

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_get_glcanvas_xvisualinfo = library.cfuncproto(
        library.load_so_libformsgl(), "fl_get_glcanvas_xvisualinfo",
        cty.POINTER(xfdata.XVisualInfo), [cty.POINTER(xfdata.FL_OBJECT)],
        """XVisualInfo * fl_get_glcanvas_xvisualinfo(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_glcanvas_xvisualinfo(pFlObject)
    return retval


def fl_get_glcanvas_context(pFlObject):
    """fl_get_glcanvas_context(pFlObject)
    
    Obtains GLXContext of a glcanvas object.

    Parameters
    ----------
        pFlObject : pointer to xfdata.FL_OBJECT
            glcanvas object

    Returns
    -------
        pGLXContext : pointer to xfdata.GLXContext
            glxcontext class instance

    Examples
    --------
        >>> glxcont = fl_get_glcanvas_context(glcanobj)

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_get_glcanvas_context = library.cfuncproto(
        library.load_so_libformsgl(), "fl_get_glcanvas_context",
        xfdata.GLXContext, [cty.POINTER(xfdata.FL_OBJECT)],
        """GLXContext fl_get_glcanvas_context(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.verify_flobjectptr_type(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_glcanvas_context(pFlObject)
    return retval


def fl_glwincreate(config, glxcontext, w, h):
    """fl_glwincreate(config, glxcontext, w, h)
    
    Creates a toplevel OpenGl window.

    Parameters
    ----------
        config : int
            GL configuration settings
        glxcontext : xfdata.GLXContext instance
            glxcontext class instance
        w : int
            width of GL window in coord units
        h : int
            height of GL window in coord units

    Returns
    -------
        win : long_pos
            window created

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Tested + Doc + NoDemo = OK

    """
    _fl_glwincreate = library.cfuncproto(
        library.load_so_libformsgl(), "fl_glwincreate",
        xfdata.Window, [cty.POINTER(cty.c_int), cty.POINTER(xfdata.GLXContext),
        cty.c_int, cty.c_int],
        """Window fl_glwincreate(int * config, GLXContext * context,
           int w, int h)""")
    pGLXContext = cty.cast(glxcontext, cty.POINTER(xfdata.GLXContext))
    iw = library.convert_to_int(w)
    ih = library.convert_to_int(h)
    library.keep_elem_refs(config, pGLXContext, w, h, iw, ih)
    retval = _fl_glwincreate(config, pGLXContext, iw, ih)
    return retval


def fl_glwinopen(config, glxcontext, w, h):
    """fl_glwinopen(config, glxcontext, w, h)
    
    Opens a toplevel OpenGL window.

    Parameters
    ----------
        config : int
            GL configuration settings
        glxcontext : pointer to xfdata.GLXContext
            glxcontext class instance
        w : int
            width of GL window in coord units
        h : int
            height of GL window in coord units

    Returns
    -------
        win : long_pos
            window opened

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_glwinopen = library.cfuncproto(
        library.load_so_libformsgl(), "fl_glwinopen",
        xfdata.Window, [cty.POINTER(cty.c_int),
        cty.POINTER(xfdata.GLXContext), cty.c_int, cty.c_int],
        """Window fl_glwinopen(int * config, GLXContext * context,
           int w, int h""")
    library.check_if_initialized()
    pGLXContext = cty.cast(glxcontext, cty.POINTER(xfdata.GLXContext))
    iw = library.convert_to_int(w)
    ih = library.convert_to_int(h)
    library.keep_elem_refs(config, pGLXContext, w, h, iw, ih)
    retval = _fl_glwinopen(config, pGLXContext, iw, ih)
    return retval

