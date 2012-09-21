#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" xforms-python's functions to manage bitmap flobjects.
"""

#    Copyright (C) 2009, 2010, 2011, 2012  Luca Lazzaroni "LukenShiro"
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
# forms.h (bitmap.h)
# Object Class: Bitmap
#######################


# Routines

# fl_create_bitmap function placeholder (internal)


def fl_add_bitmap(bitmaptype, xpos, ypos, width, height, label):
    """fl_add_bitmap(bitmaptype, xpos, ypos, width, height, label)
    -> ptr_flobject

    Adds a bitmap (a plain text monochrome image format) flobject
    to a form. The bitmap is empty on creation.

    Parameters
    ----------
        bitmaptype : int
            type of bitmap to be added. Values (from xfdata.py)
            FL_NORMAL_BITMAP (normal bitmap flobject type)
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position of bitmap (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            text label of bitmap

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            created flobject

    Examples
    --------
        >>> pxbmobj = fl_add_bitmap(xfdata.FL_NORMAL_BITMAP, 320, 200,
                100, 100, "MyBitmap")

    Notes
    -----
        Status: UnitTest + Doc + Demo = OK

    """
    _fl_add_bitmap = library.cfuncproto(
        library.load_so_libforms(), "fl_add_bitmap",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_bitmap(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_flinitialized()
    library.checkfatal_allowed_value_in_list(bitmaptype, \
            xfdata.BITMAPTYPE_list)
    i_bitmaptype = library.convert_to_intc(bitmaptype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_stringc(label)
    library.keep_elem_refs(bitmaptype, xpos, ypos, width, height, \
            label, i_bitmaptype, i_xpos, i_ypos, i_width, i_height, s_label)
    retval = _fl_add_bitmap(i_bitmaptype, i_xpos, i_ypos, i_width, \
            i_height, s_label)
    return retval


def fl_set_bitmap_data(ptr_flobject, width, height, xbmcontentslist):
    """fl_set_bitmap_data(ptr_flobject, width, height, xbmcontentslist)

    Defines the actual bitmap being displayed from specified contents. A
    number of bitmaps can be found in '/usr/include/X11/bitmaps' or similar
    places. The X program 'bitmap' can be used to create bitmaps.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            bitmap flobject
        width : int
            width of bitmap in cood units
        height : int
            height of bitmap in coord units
        xbmcontentslist : list of ubytes
            bitmap data used for contents

    Examples
    --------
        >>> bitmapcontents = [0x01, 0x1a, 0x27, 0x34, 0x41, 0x4e, 0x5b,
        >>>         0x68, 0x75, 0x82, 0x8f, 0x9c, 0xa9, 0xb6, 0xc3, 0xd0]
        >>> fl_set_bitmap_data(pxbmobj, 4, 4, bitmapcontents)

    Notes
    -----
        Status: UnitTest + Doc + Demo = OK

    """
    _fl_set_bitmap_data = library.cfuncproto(
        library.load_so_libforms(), "fl_set_bitmap_data",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_int,
        cty.POINTER(cty.c_ubyte)],
        """void fl_set_bitmap_data(FL_OBJECT * ob, int w, int h,
           unsigned char * data)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    i_width = library.convert_to_intc(width)
    i_height = library.convert_to_intc(height)
    ptr_xbmcontentslist = library.convert_to_ubytec_array(xbmcontentslist)
    #pxbmcontents = cty.cast(xbmcontents, cty.POINTER(cty.c_ubyte))
    library.keep_elem_refs(ptr_flobject, width, height, xbmcontentslist, \
            i_width, i_height, ptr_xbmcontentslist)
    _fl_set_bitmap_data(ptr_flobject, i_width, i_height, \
            ptr_xbmcontentslist)


def fl_set_bitmap_file(ptr_flobject, fname):
    """fl_set_bitmap_file(ptr_flobject, fname)

    Defines the actual bitmap being displayed from a specified .xbm file.
    A number of bitmaps can be found in '/usr/include/X11/bitmaps' or
    similar places. The X program 'bitmap' can be used to create bitmaps.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            bitmap flobject
        fname : str
            name (path included if necessary) of bitmap (.xbm format) file

    Examples
    --------
        >>> fl_set_bitmap_file(xbmobj, "mybitmapfile.xbm")

    Notes
    -----
        Status: UnitTest + Doc + Demo = OK

    """
    _fl_set_bitmap_file = library.cfuncproto(
        library.load_so_libforms(), "fl_set_bitmap_file",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.STRING],
        """void fl_set_bitmap_file(FL_OBJECT * ob, const char * fname)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    s_fname = library.convert_to_stringc(fname)
    library.keep_elem_refs(ptr_flobject, fname, s_fname)
    _fl_set_bitmap_file(ptr_flobject, s_fname)


fl_set_bitmapbutton_file = fl_set_bitmap_file
fl_set_bitmapbutton_datafile = fl_set_bitmapbutton_file

# fl_set_bitmap_datafile placeholder (backwards)


def fl_read_bitmapfile(win, fname):
    """fl_read_bitmapfile(win, fname) -> pixmapid, width, height, hotx, hoty

    Makes a bitmap from a bitmap (.xpm format) file.

    Parameters
    ----------
        win : long_pos
            window id
        fname : str
            name of bitmap (.xbm format) file

    Returns
    -------
        pixmapid : long_pos
            pixmap resource id
        width : int_pos
            width
        height : int_pos
            height
        hotx : int
            hotspot horizontal position
        hoty : int
            hotspot vertical position

    Examples
    --------
        >>> pmap, w, h, hotx, hoty = fl_read_bitmapfile(win0, "xbmfile.xbm")

    API_diversion
    ----------
        API changed from XForms, upstream is
        fl_read_bitmapfile(win, filename, width, height, hotx, hoty)

    Notes
    -----
        Status: UnitTest + Doc + NoDemo = OK

    """
    _fl_read_bitmapfile = library.cfuncproto(
        library.load_so_libforms(), "fl_read_bitmapfile",
        xfdata.Pixmap, [xfdata.Window, xfdata.STRING, cty.POINTER(cty.c_uint),
        cty.POINTER(cty.c_uint), cty.POINTER(cty.c_int),
        cty.POINTER(cty.c_int)],
        """Pixmap fl_read_bitmapfile(Window win, const char * file,
           unsigned int * w, unsigned int * h, int * hotx, int * hoty)""")
    library.check_if_flinitialized()
    ul_win = library.convert_to_Window(win)
    s_fname = library.convert_to_stringc(fname)
    i_width, ptr_width = library.make_uintc_and_pointer()
    i_height, ptr_height = library.make_uintc_and_pointer()
    i_hotx, ptr_hotx = library.make_intc_and_pointer()
    i_hoty, ptr_hoty = library.make_intc_and_pointer()
    library.keep_elem_refs(win, fname, i_width, i_height, i_hotx, i_hoty, \
            ul_win, s_fname, ptr_width, ptr_height, ptr_hotx, ptr_hoty)
    retval = _fl_read_bitmapfile(ul_win, s_fname, ptr_width, ptr_height, \
            ptr_hotx, ptr_hoty)
    return retval, i_width.value, i_height.value, i_hotx.value, i_hoty.value


def fl_create_from_bitmapdata(win, xbmdata, width, height):
    """fl_create_from_bitmapdata(win, xbmdata, width, height) -> pixmapid

    Makes a bitmap from bitmap contents data.

    Parameters
    ----------
        win : long_pos
            window id
        xbmdata : str
            bitmap data used for contents
        width : int_pos
            width of bitmap in coord units
        height : int_pos
            height of bitmap in coord units

    Returns
    -------
        pixmapid : long_pos
            created pixmap resource id

    Examples
    --------
        >>> xbmdata = "\x10\x18\x1f\x20\x28x\x2f\x30\x38\x3f\x40\x48\x4f\x50"
        >>> pmap = fl_create_from_bitmapdata(win0, xbmdata, 20, 20)

    Notes
    -----
        Status: UnitTest + Doc + NoDemo = OK

    """
    _fl_create_from_bitmapdata = library.cfuncproto(
        library.load_so_libforms(), "fl_create_from_bitmapdata",
        xfdata.Pixmap, [xfdata.Window, xfdata.STRING, cty.c_int, cty.c_int],
        """Pixmap fl_create_from_bitmapdata(Window win, const
           char * data, int width, int height)""")
    library.check_if_flinitialized()
    ul_win = library.convert_to_Window(win)
    s_xbmdata = library.convert_to_stringc(xbmdata)
    i_width = library.convert_to_intc(width)
    i_height = library.convert_to_intc(height)
    library.keep_elem_refs(win, xbmdata, width, height, ul_win, \
            s_xbmdata, i_width, i_height)
    retval = _fl_create_from_bitmapdata(ul_win, s_xbmdata, i_width, \
            i_height)
    return retval


# PIXMAP stuff

# fl_create_pixmap() function placeholder (internal)


def fl_add_pixmap(pixmaptype, xpos, ypos, width, height, label):
    """fl_add_pixmap(pixmaptype, xpos, ypos, width, height, label)
    -> ptr_flobject

    Adds a pixmap flobject (plain text multi-color image format). The
    label is by default placed below the pixmap. The pixmap is empty
    on creation.

    Parameters
    ----------
        pixmaptype : int
            type of pixmap to be added. Values (from xfdata.py)
            FL_NORMAL_PIXMAP (normal pixmap flobject type)
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position of bitmap (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            text label of pixmap

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            flobject created

    Examples
    --------
        >>> fl_add_pixmap(xfdata.FL_NORMAL_PIXMAP, 320, 200, 100, 100,
                "MyPixmap")

    Notes
    -----
        Status: UnitTest + Doc + Demo = OK

    """
    _fl_add_pixmap = library.cfuncproto(
        library.load_so_libforms(), "fl_add_pixmap",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_pixmap(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_flinitialized()
    library.checkfatal_allowed_value_in_list(pixmaptype, \
            xfdata.PIXMAPTYPE_list)
    i_pixmaptype = library.convert_to_intc(pixmaptype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_stringc(label)
    library.keep_elem_refs(pixmaptype, xpos, ypos, width, height, \
            label, i_pixmaptype, i_xpos, i_ypos, i_width, i_height, \
            s_label)
    retval = _fl_add_pixmap(i_pixmaptype, i_xpos, i_ypos, i_width, \
            i_height, s_label)
    return retval


def fl_set_pixmap_data(ptr_flobject, xpmdatalist):
    """fl_set_pixmap_data(ptr_flobject, xpmdatalist)

    Defines the actual pixmap being displayed from specified data. A
    number of pixmaps can be found in '/usr/include/X11/pixmaps' or
    similar places.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
             pixmap flobject
        xpmdatalist : list of str
            bits contents of pixmap

    Examples
    --------
        >>> xpmdata = ["28 28 6 2 . white x orange s s_SteelBlue * black",
                ". . . . . . * * * * . . . . . . . . . * * * * . . . . . ",
                ". . . . + * x x * . . . . . . . . . . + * x x * . . . . ",
                ". . . + * x x * . . . . . . . . . . . . + * x x * . . . ",
                ". . + * x * . . . * . . . . . . . . . * . . + * x * . . ",
                ". . + * x * . . + * . . . . . . . . + * . . + * x * . . ",
                ". . + * x * . + * * . . . . . . . . + * * . + * x * . . ",
                ". . + * x * + * * . . . . . . . . . . + * * + * x * . . ",
                ". . + * x * * * . . . . . . . . . . . . + * * x x * . . ",
                ...etc...]
        >>> fl_set_pixmap_data(pxmobj, xpmdata)

    Notes
    -----
        Status: Half-UTest + Doc + Demo = OK

    """
    _fl_set_pixmap_data = library.cfuncproto(
        library.load_so_libforms(), "fl_set_pixmap_data",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(xfdata.STRING)],
        """void fl_set_pixmap_data(FL_OBJECT * ob, char * * bits)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    ptr_xpmdatalist = library.convert_to_ptr_stringc(xpmdatalist)
    library.keep_elem_refs(ptr_flobject, xpmdatalist, ptr_xpmdatalist)
    _fl_set_pixmap_data(ptr_flobject, ptr_xpmdatalist)


def fl_set_pixmap_file(ptr_flobject, fname):
    """fl_set_pixmap_file(ptr_flobject, fname)

    Defines the actual bitmap being displayed from a specified .xpm file. A
    number of pixmaps can be found in '/usr/include/X11/pixmaps' or similar
    places.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            pixmap flobject
        fname : str
            name (path included if necessary) of pixmap (.xpm format) file

    Examples
    --------
        >>> fl_set_pixmap_file(pxpmobj, "mypixmapfile.xpm")

    Notes
    -----
        Status: UnitTest + Doc + Demo = OK

    """
    _fl_set_pixmap_file = library.cfuncproto(
        library.load_so_libforms(), "fl_set_pixmap_file",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.STRING],
        """void fl_set_pixmap_file(FL_OBJECT * ob, const char * fname)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    s_fname = library.convert_to_stringc(fname)
    library.keep_elem_refs(ptr_flobject, fname, s_fname)
    _fl_set_pixmap_file(ptr_flobject, s_fname)


fl_set_pixmapbutton_file = fl_set_pixmap_file
fl_set_pixmapbutton_datafile = fl_set_pixmapbutton_file


def fl_set_pixmap_align(ptr_flobject, align, xmargin, ymargin):
    """fl_set_pixmap_align(ptr_flobject, align, xmargin, ymargin)

    Changes alignment of a pixmap. By default it is displayed centered
    inside the bounding box; although you can place a pixmap outside of
    the bounding box, it probably is not a good idea.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            pixmap flobject
        align : int
            alignment of pixmap. Values (from xfdata.py)
            - FL_ALIGN_CENTER (In the middle of the box, inside it),
            - FL_ALIGN_TOP (To the top of the box, outside it),
            - FL_ALIGN_BOTTOM (To the bottom of the box, outside it),
            - FL_ALIGN_LEFT (To the left of the box, outside it),
            - FL_ALIGN_RIGHT (To the right of the box, outside it),
            - FL_ALIGN_LEFT_TOP (To the left and top of the box, outside it),
            - FL_ALIGN_RIGHT_TOP (To the right and top of the box, outside it),
            - FL_ALIGN_LEFT_BOTTOM (To the left and bottom of box, outside),
            - FL_ALIGN_RIGHT_BOTTOM (To the right and bottom of box, outside),
            - FL_ALIGN_INSIDE (places the text inside the box),
            - FL_ALIGN_VERT (not functional yet).
            Bitwise OR with FL_ALIGN_INSIDE is allowed.
        xmargin : int
            extra margin to leave in addition to the flobject border
            width. By default it is 3.
        ymargin : int
            extra margin to leave in addition to the flobject border
            height. By default it is 3.

    Examples
    --------
        >>> fl_set_pixmap_align(xpmobj, xfdata.FL_ALIGN_CENTER, 10, 10)

    Notes
    -----
        Status: UnitTest + Doc + Demo = OK

    """
    _fl_set_pixmap_align = library.cfuncproto(
        library.load_so_libforms(), "fl_set_pixmap_align",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_int,
        cty.c_int],
        """void fl_set_pixmap_align(FL_OBJECT * ob, int align,
           int xmargin, int ymargin)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.checkfatal_allowed_value_in_list(align, xfdata.ALIGN_list)
    i_align = library.convert_to_intc(align)
    i_xmargin = library.convert_to_intc(xmargin)
    i_ymargin = library.convert_to_intc(ymargin)
    library.keep_elem_refs(ptr_flobject, align, xmargin, ymargin, \
            i_align, i_xmargin, i_ymargin)
    _fl_set_pixmap_align(ptr_flobject, i_align, i_xmargin, i_ymargin)


fl_set_pixmapbutton_align = fl_set_pixmap_align


def fl_set_pixmap_pixmap(ptr_flobject, pixmapid, mask):
    """fl_set_pixmap_pixmap(ptr_flobject, pixmapid, mask)

    Changes the pixmap for the flobject with a pixmap resource id you
    already may have. It does not free the pixmap ID nor the mask
    already associated with the flobject.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            pixmap flobject
        pixmapid : long_pos
            pixmap resource id to be used
        mask : long_pos
            mask used for transparency. If no special clipping
            attributes are desired, use 0.

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_set_pixmap_pixmap = library.cfuncproto(
        library.load_so_libforms(), "fl_set_pixmap_pixmap",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.Pixmap, xfdata.Pixmap],
        """void fl_set_pixmap_pixmap(FL_OBJECT * ob, Pixmap id,
           Pixmap mask)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    ul_pixmapid = library.convert_to_ulongc(pixmapid)
    ul_mask = library.convert_to_ulongc(mask)
    library.keep_elem_refs(ptr_flobject, pixmapid, mask, \
            ul_pixmapid, ul_mask)
    _fl_set_pixmap_pixmap(ptr_flobject, ul_pixmapid, ul_mask)


fl_set_pixmapbutton_pixmap = fl_set_pixmap_pixmap


def fl_set_pixmap_colorcloseness(red, green, blue):
    """fl_set_pixmap_colorcloseness(red, green, blue)

    Changes difference between the requested color and the color found
    being smaller than some pre-set threshold values between 0 and 65535 (0
    means exact match), if a pixmap has more colors than that available in
    the colormap. XForms will use substitute colors that are judged
    "close enough".

    Parameters
    ----------
        red : int
            difference for red color. By default, closeness is 40000.
        green : int
            difference for green color. By default, closeness is 30000.
        blue : int
            difference for blue color. By default, closeness is 50000.

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_set_pixmap_colorcloseness = library.cfuncproto(
        library.load_so_libforms(), "fl_set_pixmap_colorcloseness",
        None, [cty.c_int, cty.c_int, cty.c_int],
        """void fl_set_pixmap_colorcloseness(int red, int green, int blue)""")
    library.check_if_flinitialized()
    i_red = library.convert_to_intc(red)
    i_green = library.convert_to_intc(green)
    i_blue = library.convert_to_intc(blue)
    library.keep_elem_refs(red, green, blue, i_red, i_green, i_blue)
    _fl_set_pixmap_colorcloseness(i_red, i_green, i_blue)


def fl_free_pixmap_pixmap(ptr_flobject):
    """fl_free_pixmap_pixmap(ptr_flobject)

    Frees the old pixmap associated to flobject, the mask, and the
    colors the pixmap allocated.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            pixmap flobject

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_free_pixmap_pixmap = library.cfuncproto(
        library.load_so_libforms(), "fl_free_pixmap_pixmap",
        None, [cty.POINTER(xfdata.FL_OBJECT)],
        """void fl_free_pixmap_pixmap(FL_OBJECT * ob)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    library.keep_elem_refs(ptr_flobject)
    _fl_free_pixmap_pixmap(ptr_flobject)


fl_free_pixmapbutton_pixmap = fl_free_pixmap_pixmap


def fl_get_pixmap_pixmap(ptr_flobject):
    """fl_get_pixmap_pixmap(ptr_flobject) -> pixmapid1, pixmapid2, pmask

    Finds out the pixmap resource id currently being displayed.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            pixmap flobject

    Returns
    -------
        pixmapid1 : long_pos
            pixmap resource id
        pixmapid2 : long_pos
            pixmap resource id
        pmask : long_pos
            pixmap mask

    Examples
    --------
        >>> *todo*

    API_diversion
    ----------
        API changed from XForms, upstream is
        fl_get_pixmap_pixmap(ptr_flobject, p, m)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_get_pixmap_pixmap = library.cfuncproto(
        library.load_so_libforms(), "fl_get_pixmap_pixmap",
        xfdata.Pixmap, [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.Pixmap), cty.POINTER(xfdata.Pixmap)],
        """Pixmap fl_get_pixmap_pixmap(FL_OBJECT * ob, Pixmap * p,
           Pixmap * m)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    ul_pixmapid2, ptr_pixmapid2 = library.make_ulongc_and_pointer()
    ul_pmask, ptr_pmask = library.make_ulongc_and_pointer()
    library.keep_elem_refs(ptr_flobject, ul_pixmapid2, ul_pmask, \
            ptr_pixmapid2, ptr_pmask)
    retval = _fl_get_pixmap_pixmap(ptr_flobject, ptr_pixmapid2, ptr_pmask)
    return retval, ul_pixmapid2.value, ul_pmask.value


fl_get_pixmapbutton_pixmap = fl_get_pixmap_pixmap


def fl_read_pixmapfile(win, fname, tran):
    """fl_read_pixmapfile(win, fname, tran) -> pixmapid, width, height,
    smask, hotx, hoty

    Makes a pixmap from a pixmap (.xpm format) file.

    Parameters
    ----------
        win : long_pos
            window id
        fname : str
            name of pixmap (.xpm format) file
        tran : long_pos
            XForms colormap index as color

    Returns
    -------
        pixmap : long_pos
            pixmap resource id
        width : int_pos
            width
        height : int_pos
            height
        smask : long_pos
            shapemask
        hotx : int
            hotspot horizontal position
        hoty : int
            hotspot vertical position

    Examples
    --------
        >>> pmap, w, h, shapmsk, hotx, hoty = fl_read_pixmapfile(win0,
                "xpmfile.xpm", xfdata.FL_WHITE)

    API_diversion
    ----------
        API changed from XForms, upstream is fl_read_pixmapfile(win,
        filename, width, height, shape_mask, hotx, hoty, tran)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_read_pixmapfile = library.cfuncproto(
        library.load_so_libforms(), "fl_read_pixmapfile",
        xfdata.Pixmap, [xfdata.Window, xfdata.STRING, cty.POINTER(cty.c_uint),
        cty.POINTER(cty.c_uint), cty.POINTER(xfdata.Pixmap),
        cty.POINTER(cty.c_int), cty.POINTER(cty.c_int), xfdata.FL_COLOR],
        """Pixmap fl_read_pixmapfile(Window win, const char * file,
           unsigned int * w, unsigned int * h, Pixmap * shape_mask,
           int * hotx, int * hoty, FL_COLOR tran)""")
    library.check_if_flinitialized()
    ul_win = library.convert_to_Window(win)
    s_fname = library.convert_to_stringc(fname)
    #library.checknonfatal_allowed_value_in_list(tran, xfdata.COLOR_list)
    ul_tran = library.convert_to_FL_COLOR(tran)
    ui_width, ptr_width = library.make_uintc_and_pointer()
    ui_height, ptr_height = library.make_uintc_and_pointer()
    ul_shapemask, ptr_shapemask = library.make_ulongc_and_pointer()
    i_hotx, ptr_hotx = library.make_intc_and_pointer()
    i_hoty, ptr_hoty = library.make_intc_and_pointer()
    library.keep_elem_refs(win, fname, ui_width, ui_height, ul_shapemask, \
            i_hotx, i_hoty, tran, ul_win, s_fname, ul_tran, ptr_width, \
            ptr_height, ptr_shapemask, ptr_hotx, ptr_hoty)
    retval = _fl_read_pixmapfile(ul_win, s_fname, ptr_width, ptr_height, \
            ptr_shapemask, ptr_hotx, ptr_hoty, ul_tran)
    return retval, ui_width.value, ui_height.value, ul_shapemask.value, \
            i_hotx.value, i_hoty.value


def fl_create_from_pixmapdata(win, xpmdata, tran):
    """fl_create_from_pixmapdata(win, xpmdata, tran) -> pixmapid, width,
    height, smask, hotx, hoty

    Makes a pixmap from pixmap contents data.

    Parameters
    ----------
        win : long_pos
            window id
        xpmdata : str of ubytes
            pixmap contents data
        tran : long_pos
            XForms colormap index as color (currently not used)

    Returns
    -------
        pixmapid : long_pos
            created pixmap resource id
        width : int_pos
            width of pixmap in coord units
        height : int_pos
            height of pixmap in coord units
        smask : long_pos
            shape mask (of an existing pixmap) used as a clipping mask
            to achieve transparency, 0 for no transparency.
        hotx : int
            horizontal position of center of the pixmap (useful if the
            pixmap is to be used as a cursor)
        hoty : int
            vertical position of center of the pixmap (useful if the
            pixmap is to be used as a cursor)

    Examples
    --------
        >>> *todo*

     API_diversion
    -------------
        API changed from XForms, upstream is fl_create_from_pixmapdata(win,
        xpmdata, width, height, smask, hotx, hoty, tran)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_create_from_pixmapdata = library.cfuncproto(
        library.load_so_libforms(), "fl_create_from_pixmapdata",
        xfdata.Pixmap, [xfdata.Window, cty.POINTER(xfdata.STRING),
        cty.POINTER(cty.c_uint), cty.POINTER(cty.c_uint),
        cty.POINTER(xfdata.Pixmap), cty.POINTER(cty.c_int),
        cty.POINTER(cty.c_int), xfdata.FL_COLOR],
        """Pixmap fl_create_from_pixmapdata(Window win, char * * data,
        unsigned int * w, unsigned int * h, Pixmap * sm, int * hotx,
        int * hoty, FL_COLOR tran)""")
    library.check_if_flinitialized()
    ul_win = library.convert_to_Window(win)
    ptr_xpmdata = library.convert_to_ptr_stringc(xpmdata)
    ui_width, ptr_width = library.make_uintc_and_pointer()
    ui_height, ptr_height = library.make_uintc_and_pointer()
    ul_smask, ptr_smask = library.make_ulongc_and_pointer()
    i_hotx, ptr_hotx = library.make_intc_and_pointer()
    i_hoty, ptr_hoty = library.make_intc_and_pointer()
    #library.checknonfatal_allowed_value_in_list(tran, xfdata.COLOR_list)
    ul_tran = library.convert_to_FL_COLOR(tran)
    library.keep_elem_refs(win, xpmdata, ui_width, ptr_width, ui_height, \
            ptr_height, ul_smask, i_hotx, i_hoty, tran, ptr_xpmdata, ul_win, \
            ptr_smask, ptr_hotx, ptr_hoty, ul_tran)
    retval = _fl_create_from_pixmapdata(ul_win, ptr_xpmdata, ptr_width, \
            ptr_height, ptr_smask, ptr_hotx, ptr_hoty, ul_tran)
    return retval, ui_width.value, ui_height.value, ul_smask.value, \
            i_hotx.value, i_hoty.value


def fl_free_pixmap(pixmapid):
    """fl_free_pixmap(pixmapid)

    Frees the pixmap.

    Parameters
    ----------
        pixmapid : long_pos
            pixmap resource id to be freed

    Examples
    --------
        >>> fl_free_pixmap(pmap)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_free_pixmap = library.cfuncproto(
        library.load_so_libforms(), "fl_free_pixmap",
        None, [xfdata.Pixmap],
        """void fl_free_pixmap(Pixmap id)""")
    library.check_if_flinitialized()
    ul_pixmapid = library.convert_to_Pixmap(pixmapid)
    library.keep_elem_refs(pixmapid, ul_pixmapid)
    _fl_free_pixmap(ul_pixmapid)

