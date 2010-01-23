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




########################
# forms.h (tabfolder.h)
########################

# fl_create_tabfolder function placeholde (internal)


def fl_add_tabfolder(foldertype, x, y, w, h, label):
    """
        fl_add_tabfolder(foldertype, x, y, w, h, label) -> pFlObject

        Adds a tabfolder object.

        @param foldertype: type of tabfolder to be added
        @param x: horizontal position (upper-left corner)
        @param x: vertical position (upper-left corner)
        @param w: width in coord units
        @param h: height in coord units
        @param label: text label of tabfolder

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_add_tabfolder = library.cfuncproto(
        library.load_so_libforms(), "fl_add_tabfolder",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_tabfolder(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_initialized()
    library.check_admitted_listvalues(foldertype, xfdata.TABFOLDERTYPE_list)
    ifoldertype = library.convert_to_int(foldertype)
    ix = library.convert_to_FL_Coord(x)
    iy = library.convert_to_FL_Coord(y)
    iw = library.convert_to_FL_Coord(w)
    ih = library.convert_to_FL_Coord(h)
    slabel = library.convert_to_string(label)
    library.keep_elem_refs(foldertype, x, y, w, h, label, ifoldertype, ix, iy,
                   iw, ih, slabel)
    retval = _fl_add_tabfolder(ifoldertype, ix, iy, iw, ih, slabel)
    return retval


def fl_addto_tabfolder(pFlObject, title, pFlForm):
    """
        fl_addto_tabfolder(pFlObject, title, pFlForm) -> pFlObject

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_addto_tabfolder = library.cfuncproto(
        library.load_so_libforms(), "fl_addto_tabfolder",
        cty.POINTER(xfdata.FL_OBJECT), [cty.POINTER(xfdata.FL_OBJECT),
        xfdata.STRING, cty.POINTER(xfdata.FL_FORM)],
        """FL_OBJECT * fl_addto_tabfolder(FL_OBJECT * ob,
           const char * title, FL_FORM * form)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    stitle = library.convert_to_string(title)
    library.keep_elem_refs(pFlObject, title, pFlForm, stitle)
    retval = _fl_addto_tabfolder(pFlObject, stitle, pFlForm)
    return retval


def fl_get_tabfolder_folder_bynumber(pFlObject, num):
    """
        fl_get_tabfolder_folder_bynumber(pFlObject, num) -> pFlForm

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_tabfolder_folder_bynumber = library.cfuncproto(
        library.load_so_libforms(), "fl_get_tabfolder_folder_bynumber",
        cty.POINTER(xfdata.FL_FORM), [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """FL_FORM * fl_get_tabfolder_folder_bynumber(FL_OBJECT * ob,
           int num)""")
    library.check_if_FL_OBJECT_ptr(pFlObject)
    inum = library.convert_to_int(num)
    library.keep_elem_refs(pFlObject, num, inum)
    retval = _fl_get_tabfolder_folder_bynumber(pFlObject, inum)
    return retval


def fl_get_tabfolder_folder_byname(pFlObject, name):
    """
        fl_get_tabfolder_folder_byname(pFlObject, name) -> pFlForm

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_tabfolder_folder_byname = library.cfuncproto(
        library.load_so_libforms(), "fl_get_tabfolder_folder_byname",
        cty.POINTER(xfdata.FL_FORM), [cty.POINTER(xfdata.FL_OBJECT), xfdata.STRING],
        """FL_FORM * fl_get_tabfolder_folder_byname(FL_OBJECT * ob,
           const char * name)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    sname = library.convert_to_string(name)
    library.keep_elem_refs(pFlObject, name, sname)
    retval = _fl_get_tabfolder_folder_byname(pFlObject, sname)
    return retval


def fl_delete_folder(pFlObject, pFlForm):
    """
        fl_delete_folder(pFlObject, pFlForm)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_delete_folder = library.cfuncproto(
        library.load_so_libforms(), "fl_delete_folder",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(xfdata.FL_FORM)],
        """void fl_delete_folder(FL_OBJECT * ob, FL_FORM * form)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject, pFlForm)
    _fl_delete_folder(pFlObject, pFlForm)


def fl_delete_folder_bynumber(pFlObject, num):
    """
        fl_delete_folder_bynumber(pFlObject, num)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_delete_folder_bynumber = library.cfuncproto(
        library.load_so_libforms(), "fl_delete_folder_bynumber",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_delete_folder_bynumber(FL_OBJECT * ob, int num)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    inum = library.convert_to_int(num)
    library.keep_elem_refs(pFlObject, num, inum)
    _fl_delete_folder_bynumber(pFlObject, inum)


def fl_delete_folder_byname(pFlObject, name):
    """
        fl_delete_folder_byname(pFlObject, name)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_delete_folder_byname = library.cfuncproto(
        library.load_so_libforms(), "fl_delete_folder_byname",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.STRING],
        """void fl_delete_folder_byname(FL_OBJECT * ob, const char * name)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    sname = library.convert_to_string(name)
    library.keep_elem_refs(pFlObject, name, sname)
    _fl_delete_folder_byname(pFlObject, sname)


def fl_set_folder(pFlObject, pFlForm):
    """ fl_set_folder(pFlObject, pFlForm)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_set_folder = library.cfuncproto(
        library.load_so_libforms(), "fl_set_folder",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(xfdata.FL_FORM)],
        """void fl_set_folder(FL_OBJECT * ob, FL_FORM * form)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.check_if_FL_FORM_ptr(pFlForm)
    library.keep_elem_refs(pFlObject, pFlForm)
    _fl_set_folder(pFlObject, pFlForm)


def fl_set_folder_byname(pFlObject, name):
    """ fl_set_folder_byname(pFlObject, name)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_set_folder_byname = library.cfuncproto(
        library.load_so_libforms(), "fl_set_folder_byname",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.STRING],
        """void fl_set_folder_byname(FL_OBJECT * ob, const char * name)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    sname = library.convert_to_string(name)
    library.keep_elem_refs(pFlObject, name, sname)
    _fl_set_folder_byname(pFlObject, name)


def fl_set_folder_bynumber(pFlObject, num):
    """
        fl_set_folder_bynumber(pFlObject, num)

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_set_folder_bynumber = library.cfuncproto(
        library.load_so_libforms(), "fl_set_folder_bynumber",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """void fl_set_folder_bynumber(FL_OBJECT * ob, int num)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    inum = library.convert_to_int(num)
    library.keep_elem_refs(pFlObject, num, inum)
    _fl_set_folder_bynumber(pFlObject, inum)


def fl_get_folder(pFlObject):
    """
        fl_get_folder(pFlObject) -> pFlForm

        @param pFlObject: pointer to object

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_folder = library.cfuncproto(
        library.load_so_libforms(), "fl_get_folder",
        cty.POINTER(xfdata.FL_FORM), [cty.POINTER(xfdata.FL_OBJECT)],
        """FL_FORM * fl_get_folder(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_folder(pFlObject)
    return retval


def fl_get_folder_number(pFlObject):
    """
        fl_get_folder_number(pFlObject) -> folder num.

        @param pFlObject: pointer to object

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_folder_number = library.cfuncproto(
        library.load_so_libforms(), "fl_get_folder_number",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_folder_number(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_folder_number(pFlObject)
    return retval


def fl_get_folder_name(pFlObject):
    """
        fl_get_folder_name(pFlObject) -> name string

        @param pFlObject: pointer to object

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_folder_name = library.cfuncproto(
        library.load_so_libforms(), "fl_get_folder_name",
        xfdata.STRING, [cty.POINTER(xfdata.FL_OBJECT)],
        """const char * fl_get_folder_name(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_folder_name(pFlObject)
    return retval


def fl_get_tabfolder_numfolders(pFlObject):
    """
        fl_get_tabfolder_numfolders(pFlObject) -> num.

        @param pFlObject: pointer to object

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_tabfolder_numfolders = library.cfuncproto(
        library.load_so_libforms(), "fl_get_tabfolder_numfolders",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_tabfolder_numfolders(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_tabfolder_numfolders(pFlObject)
    return retval


def fl_get_active_folder(pFlObject):
    """
        fl_get_active_folder(pFlObject) -> pFlForm

        @param pFlObject: pointer to object

        @status: Tested + NoDoc + Demo = OK
    """
    _fl_get_active_folder = library.cfuncproto(
        library.load_so_libforms(), "fl_get_active_folder",
        cty.POINTER(xfdata.FL_FORM), [cty.POINTER(xfdata.FL_OBJECT)],
        """FL_FORM * fl_get_active_folder(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_active_folder(pFlObject)
    return retval


def fl_get_active_folder_number(pFlObject):
    """
        fl_get_active_folder_number(pFlObject) -> num.

        @param pFlObject: pointer to object

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_active_folder_number = library.cfuncproto(
        library.load_so_libforms(), "fl_get_active_folder_number",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT)],
        """int fl_get_active_folder_number(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_active_folder_number(pFlObject)
    return retval


def fl_get_active_folder_name(pFlObject):
    """
        fl_get_active_folder_name(pFlObject) -> name string

        @param pFlObject: pointer to object

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_active_folder_name = library.cfuncproto(
        library.load_so_libforms(), "fl_get_active_folder_name",
        xfdata.STRING, [cty.POINTER(xfdata.FL_OBJECT)],
        """const char * fl_get_active_folder_name(FL_OBJECT * ob)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    library.keep_elem_refs(pFlObject)
    retval = _fl_get_active_folder_name(pFlObject)
    return retval


def fl_get_folder_area(pFlObject):
    """
        fl_get_folder_area(pFlObject) -> x, y, w, h

        @param pFlObject: pointer to object

        @attention: API change from XForms - upstream was
                    fl_get_folder_area(pFlObject, x, y, w, h)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_get_folder_area = library.cfuncproto(
        library.load_so_libforms(), "fl_get_folder_area",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(xfdata.FL_Coord),
        cty.POINTER(xfdata.FL_Coord), cty.POINTER(xfdata.FL_Coord),
        cty.POINTER(xfdata.FL_Coord)],
        """void fl_get_folder_area(FL_OBJECT * ob, FL_Coord * x,
           FL_Coord * y, FL_Coord * w, FL_Coord * h)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    x, px = library.make_int_and_pointer()
    y, py = library.make_int_and_pointer()
    w, pw = library.make_int_and_pointer()
    h, ph = library.make_int_and_pointer()
    library.keep_elem_refs(pFlObject, x, y, w, h, px, py, pw, ph)
    _fl_get_folder_area(pFlObject, px, py, pw, ph)
    return x.value, y.value, w.value, h.value


def fl_replace_folder_bynumber(pFlObject, num, pFlForm):
    """
        fl_replace_folder_bynumber(pFlObject, num, pFlForm)

        @param pFlObject: pointer to object

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_replace_folder_bynumber = library.cfuncproto(
        library.load_so_libforms(), "fl_replace_folder_bynumber",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.POINTER(xfdata.FL_FORM)],
        """void fl_replace_folder_bynumber(FL_OBJECT * ob, int num,
           FL_FORM * form)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    inum = library.convert_to_int(num)
    library.keep_elem_refs(pFlObject, num, pFlForm, inum)
    _fl_replace_folder_bynumber(pFlObject, inum, pFlForm)


def fl_set_tabfolder_autofit(pFlObject, num):
    """
        fl_set_tabfolder_autofit(pFlObject, num) -> num.

        @param pFlObject: pointer to object

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_set_tabfolder_autofit = library.cfuncproto(
        library.load_so_libforms(), "fl_set_tabfolder_autofit",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """int fl_set_tabfolder_autofit(FL_OBJECT * ob, int y)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    inum = library.convert_to_int(num)
    library.keep_elem_refs(pFlObject, num, inum)
    retval = _fl_set_tabfolder_autofit(pFlObject, inum)
    return retval


def fl_set_default_tabfolder_corner(npixels):
    """
        fl_set_default_tabfolder_corner(npixels) -> old pixels num.

        Adjusts the corner pixels, changing appearance of the tabs.

        @param npixels: number of corner pixels (default 3)

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_set_default_tabfolder_corner = library.cfuncproto(
        library.load_so_libforms(), "fl_set_default_tabfolder_corner",
        cty.c_int, [cty.c_int],
        """int fl_set_default_tabfolder_corner(int n):""")
    library.check_if_initialized()
    ipixels = library.convert_to_int(npixels)
    library.keep_elem_refs(npixels, ipixels)
    retval = _fl_set_default_tabfolder_corner(ipixels)
    return retval


def fl_set_tabfolder_offset(pFlObject, offset):
    """
        fl_set_tabfolder_offset(pFlObject, offset) -> num.

        @param pFlObject: pointer to tabfolder object

        @status: Untested + NoDoc + NoDemo = NOT OK
    """
    _fl_set_tabfolder_offset = library.cfuncproto(
        library.load_so_libforms(), "fl_set_tabfolder_offset",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int],
        """int fl_set_tabfolder_offset(FL_OBJECT * ob, int offset)""")
    library.check_if_initialized()
    library.check_if_FL_OBJECT_ptr(pFlObject)
    ioffset = library.convert_to_int(offset)
    library.keep_elem_refs(pFlObject, offset, ioffset)
    retval = _fl_set_tabfolder_offset(pFlObject, ioffset)
    return retval

