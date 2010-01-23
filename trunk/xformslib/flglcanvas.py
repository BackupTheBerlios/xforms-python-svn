#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

"""
    xforms-python - Python wrapper for XForms (X11) GUI C toolkit library
    using ctypes

    Copyright (C) 2009, 2010  Luca Lazzaroni "LukenShiro"
        <lukenshiro@ngi.it>

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

    *****************************************************************


    @newfield example: Example, Example
"""


__docformat__ = "epytext en"    # to be used with epydoc doc


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

# This is an attempt to maintain some sort of backwards compatibility
# with old code whilst also getting rid of the old, system-specific
# hack.

# OpenGL canvases

# fl_create_glcanvas function placeholder (internal)


def fl_add_glcanvas(canvastype, x, y, w, h, label):
    """
    fl_add_glcanvas(canvastype, x, y, w, h, label) -> pFlObject

    Adds a glcanvas object to the form.

    @param canvastype: type of glcanvas to be added. Values (from xfdata
        module) i.e. FL_NORMAL_CANVAS, FL_SCROLLED_CANVAS (not enabled)
    @type canvastype: int
    @param x: horizontal position (upper-left corner)
    @type x: int
    @param y: vertical position (upper-left corner)
    @type y: int
    @param w: width in coord units
    @type w: int
    @param h: height in coord units
    @type h: int
    @param label: text label of glcanvas
    @type label: str

    @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_add_glcanvas = library.cfuncproto(
            library.load_so_libformsgl(), "fl_add_glcanvas",
            cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
            xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
            """FL_OBJECT * fl_add_glcanvas(int type, FL_Coord x, FL_Coord y,
               FL_Coord w, FL_Coord h, const char * label)
""")
    library.check_if_initialized()
    library.check_admitted_listvalues(canvastype, xfdata.CANVASTYPE_list)
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
    """
    fl_set_glcanvas_defaults(config)

    Modifies the global defaults for glcanvas.

    @param config: configuration settings
    @type config: int

    @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_set_glcanvas_defaults = library.cfuncproto(
            library.load_so_libformsgl(), "fl_set_glcanvas_defaults",
            None, [cty.POINTER(cty.c_int)],
            """void fl_set_glcanvas_defaults(const int * config):
""")
    pconfig = cty.cast(config, cty.POINTER(cty.c_int))
    library.keep_elem_refs(config, pconfig)
    _fl_set_glcanvas_defaults(pconfig)


def fl_get_glcanvas_defaults():
    """
    fl_get_glcanvas_defaults() -> int

    Returns the global defaults for glcanvas.

    @returns: configuration settings
    @attention: API change from XForms - upstream was
        fl_get_glcanvas_defaults(config)

    @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_get_glcanvas_defaults = library.cfuncproto(
            library.load_so_libformsgl(), "fl_get_glcanvas_defaults",
            None, [cty.POINTER(cty.c_int)],
            """void fl_get_glcanvas_defaults(int config[ ]):
""")
    config, pconfig = library.make_int_and_pointer()
    library.keep_elem_refs(config, pconfig)
    _fl_get_glcanvas_defaults(pconfig)
    return config.value


def fl_set_glcanvas_attributes(pFlObject, config):
    """ fl_set_glcanvas_attributes(pFlObject, config)

        Modifies the default configuration of a particular glcanvas
        object.

        @param pFlObject: pointer to glcanvas object
@type pFlObject: pointer to xfdata.FL_OBJECT
        @param config: configuration settings to be set

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_set_glcanvas_attributes = library.cfuncproto(
            library.load_so_libformsgl(), "fl_set_glcanvas_attributes",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int)],
            """void fl_set_glcanvas_attributes(FL_OBJECT * ob,
               const int * config)
""")
    library.check_if_FL_OBJECT_ptr(pFlObject)
    pconfig = cty.cast(config, cty.POINTER(cty.c_int))
    library.keep_elem_refs(pFlObject, config, pconfig)
    _fl_set_glcanvas_attributes(pFlObject, pconfig)


def fl_get_glcanvas_attributes(pFlObject):
    """ fl_get_glcanvas_attributes(pFlObject) -> attributes

        Returns the attributes of a glcanvas object.

        @param pFlObject: glcanvas object
        @type pFlObject: pointer to xfdata.FL_OBJECT

        @attention: API change from XForms - upstream was
                    fl_get_glcanvas_attributes(pFlObject, attributes)
    """

    _fl_get_glcanvas_attributes = library.cfuncproto(
            library.load_so_libformsgl(), "fl_get_glcanvas_attributes",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(cty.c_int)],
            """void fl_get_glcanvas_attributes(FL_OBJECT * ob,
               int * attributes)
""")
    library.check_if_FL_OBJECT_ptr(pFlObject)
    attributes, pattributes = library.make_int_and_pointer()
    library.keep_elem_refs(pFlObject, attributes, pattributes)
    _fl_get_glcanvas_attributes(pFlObject, pattributes)
    return attributes.value


def fl_set_glcanvas_direct(pFlObject, direct):
    """ fl_set_glcanvas_direct(pFlObject, direct)

        @param pFlObject: pointer to glcanvas object
@type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_set_glcanvas_direct = library.cfuncproto(
            library.load_so_libformsgl(), "fl_set_glcanvas_direct",
            None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
            """void fl_set_glcanvas_direct(FL_OBJECT * ob, int direct)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    idirect = library.convert_to_int(direct)
    library.keep_elem_refs(pFlObject, direct, idirect)
    _fl_set_glcanvas_direct(pFlObject, idirect)


def fl_activate_glcanvas(pFlObject):
    """ fl_activate_glcanvas(pFlObject)

        Activates a glcanvas object, allowing user interaction.

        @param pFlObject: pointer to glcanvas object
@type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_activate_glcanvas = library.cfuncproto(
            library.load_so_libformsgl(), "fl_activate_glcanvas",
            None, [cty.POINTER(xfdata.FL_OBJECT)],
            """void fl_activate_glcanvas(FL_OBJECT * ob)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    _fl_activate_glcanvas(pFlObject)


def fl_get_glcanvas_xvisualinfo(pFlObject):
    """ fl_get_glcanvas_xvisualinfo(pFlObject) -> xvisualinfo class

        Returns XVisualInfo class of a glcanvas object.

        @param pFlObject: pointer to glcanvas object
@type pFlObject: pointer to xfdata.FL_OBJECT

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_get_glcanvas_xvisualinfo = library.cfuncproto(
            library.load_so_libformsgl(), "fl_get_glcanvas_xvisualinfo",
            cty.POINTER(xfdata.XVisualInfo), [cty.POINTER(xfdata.FL_OBJECT)],
            """XVisualInfo * fl_get_glcanvas_xvisualinfo(FL_OBJECT * ob)
""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_glcanvas_xvisualinfo(pFlObject)
    return retval


def fl_get_glcanvas_context(pFlObject):
    """ fl_get_glcanvas_context(pFlObject) -> glxcontext class

    @param pFlObject: pointer to glcanvas object
    @type pFlObject: pointer to xfdata.FL_OBJECT

    @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_glcanvas_context = library.cfuncproto(
        library.load_so_libformsgl(), "fl_get_glcanvas_context",
        xfdata.GLXContext, [cty.POINTER(xfdata.FL_OBJECT)],
        """GLXContext fl_get_glcanvas_context(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_glcanvas_context(pFlObject)
    return retval


def fl_glwincreate(config, glxcontext, w, h):
    """ fl_glwincreate(config, glxcontext, w, h) -> window

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_glwincreate = library.cfuncproto(
            library.load_so_libformsgl(), "fl_glwincreate",
            xfdata.Window, [cty.POINTER(cty.c_int), cty.POINTER(xfdata.GLXContext),
            cty.c_int, cty.c_int],
            """Window fl_glwincreate(int * config, GLXContext * context,
               int w, int h)
""")
    pGLXContext = cty.cast(glxcontext, cty.POINTER(xfdata.GLXContext))
    iw = library.convert_to_int(w)
    ih = library.convert_to_int(h)
    library.keep_elem_refs(config, pGLXContext, w, h, iw, ih)
    retval = _fl_glwincreate(config, pGLXContext, iw, ih)
    return retval


def fl_glwinopen(config, glxcontext, w, h):
    """ fl_glwinopen(config, glxcontext, w, h) -> window

        @status: Untested + NoDoc + NoDemo = NOT OK
    """

    _fl_glwinopen = library.cfuncproto(
            library.load_so_libformsgl(), "fl_glwinopen",
            xfdata.Window, [cty.POINTER(cty.c_int), cty.POINTER(xfdata.GLXContext),
            cty.c_int, cty.c_int],
            """Window fl_glwinopen(int * config, GLXContext * context,
               int w, int h
""")
    library.check_if_initialized()
    pGLXContext = cty.cast(glxcontext, cty.POINTER(xfdata.GLXContext))
    iw = library.convert_to_int(w)
    ih = library.convert_to_int(h)
    library.keep_elem_refs(config, pGLXContext, w, h, iw, ih)
    retval = _fl_glwinopen(config, pGLXContext, iw, ih)
    return retval


