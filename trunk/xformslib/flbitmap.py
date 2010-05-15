#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage bitmap objects.

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
# forms.h (bitmap.h)
# Object Class: Bitmap
#######################


# Routines

# fl_create_bitmap function placeholder (internal)


def fl_add_bitmap(bitmaptype, x, y, w, h, label):
    """Adds a bitmap object.

    --

    :Parameters:
      `bitmaptype` : int
        type of bitmap to be added. Values (from xfdata.py) FL_NORMAL_BITMAP
      `x` : int
        horizontal position (upper-left corner)
      `y` : int
        vertical position of bitmap (upper-left corner)
      `w` : int
        width in coord units
      `h` : int
        height in coord units
      `label` : str
        text label of bitmap

    :returns: object created
    :rtype: pointer to xfdata.FL_OBJECT (pFlObject)

    :note: e.g. fl_add_bitmap(xfdata.FL_NORMAL_BITMAP, 320, 200, 100, 100, \
      "MyBitmap")

    :status: Tested + NoDoc + Demo = OK

    """
    _fl_add_bitmap = libr.cfuncproto(
        libr.load_so_libforms(), "fl_add_bitmap",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_bitmap(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    libr.check_if_initialized()
    libr.check_admitted_value_in_list(bitmaptype, xfdata.BITMAPTYPE_list)
    ibitmaptype = libr.convert_to_int(bitmaptype)
    ix = libr.convert_to_FL_Coord(x)
    iy = libr.convert_to_FL_Coord(y)
    iw = libr.convert_to_FL_Coord(w)
    ih = libr.convert_to_FL_Coord(h)
    slabel = libr.convert_to_string(label)
    libr.keep_elem_refs(bitmaptype, x, y, w, h, label, ibitmaptype, ix, \
                        iy, iw, ih, slabel)
    retval = _fl_add_bitmap(ibitmaptype, ix, iy, iw, ih, slabel)
    return retval


def fl_set_bitmap_data(pFlObject, w, h, xbmcontents):
    """Sets the actual bitmap being displayed from specified contents. A
    number of bitmaps can be found in '/usr/include/X11/bitmaps' or similar
    places. The X program 'bitmap' can be used to create bitmaps.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        bitmap object
      `w` : int
        width of bitmap in cood units
      `h` : int
        height of bitmap in coord units
      `xbmcontents` : str of ubytes characters
        bitmap data used for contents

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_bitmap_data = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_bitmap_data",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_int,
        cty.POINTER(cty.c_ubyte)],
        """void fl_set_bitmap_data(FL_OBJECT * ob, int w, int h,
           unsigned char * data)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    iw = libr.convert_to_int(w)
    ih = libr.convert_to_int(h)
    pxbmcontents = cty.cast(xbmcontents, cty.POINTER(cty.c_ubyte))
    libr.keep_elem_refs(pFlObject, w, h, xbmcontents, iw, ih, pxbmcontents)
    _fl_set_bitmap_data(pFlObject, iw, ih, pxbmcontents)


def fl_set_bitmap_file(pFlObject, fname):
    """Sets the actual bitmap being displayed from a specified .xbm file. A
    number of bitmaps can be found in '/usr/include/X11/bitmaps' or similar
    places. The X program 'bitmap' can be used to create bitmaps.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        bitmap object
      `fname` : str
        name (path included if necessary) of bitmap (.xbm format) file

    :note: e.g. fl_set_bitmap_file(xbmobj, "mybitmapfile.xbm")

    :status: Tested + Doc + Demo = OK

    """
    _fl_set_bitmap_file = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_bitmap_file",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.STRING],
        """void fl_set_bitmap_file(FL_OBJECT * ob, const char * fname)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    sfname = libr.convert_to_string(fname)
    libr.keep_elem_refs(pFlObject, fname, sfname)
    _fl_set_bitmap_file(pFlObject, sfname)


fl_set_bitmapbutton_file = fl_set_bitmap_file
fl_set_bitmapbutton_datafile = fl_set_bitmapbutton_file

# fl_set_bitmap_datafile placeholder (backwards)


def fl_read_bitmapfile(win, fname):
    """Makes a bitmap from a bitmap file.

    --

    :Parameters:
      `win` : long_pos
        window id
      `fname` : str
        name of bitmap (.xbm format) file

    :returns: pixmap id, w, h, hotx, hoty
    :rtype: long_pos, int_pos, int_pos, int, int

    :attention: API change from XForms - upstream was
        fl_read_bitmapfile(win, filename, w, h, hotx, hoty)

    :note: e.g. pmap, w, h, hotx, hoty = fl_read_bitmapfile(win0, \
        "xbmfile.xbm")

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_read_bitmapfile = libr.cfuncproto(
        libr.load_so_libforms(), "fl_read_bitmapfile",
        xfdata.Pixmap, [xfdata.Window, xfdata.STRING, cty.POINTER(cty.c_uint),
        cty.POINTER(cty.c_uint), cty.POINTER(cty.c_int),
        cty.POINTER(cty.c_int)],
        """Pixmap fl_read_bitmapfile(Window win, const char * file,
           unsigned int * w, unsigned int * h, int * hotx, int * hoty)""")
    libr.check_if_initialized()
    ulwin = libr.convert_to_Window(win)
    sfname = libr.convert_to_string(fname)
    w, pw = libr.make_uint_and_pointer()
    h, ph = libr.make_uint_and_pointer()
    hotx, photx = libr.make_int_and_pointer()
    hoty, photy = libr.make_int_and_pointer()
    libr.keep_elem_refs(win, fname, w, h, hotx, hoty, ulwin, sfname,
                           pw, ph, photx, photy)
    retval = _fl_read_bitmapfile(ulwin, sfname, pw, ph, photx, photy)
    return retval, w.value, h.value, hotx.value, hoty.value


def fl_create_from_bitmapdata(win, data, w, h):
    """Makes a bitmap from bitmap contents data.

    --

    :Parameters:
      `win` : long_pos
        window id
      `data` : str of ubyte
        bitmap contents data
      `w` : int_pos
        width of bitmap in coord units
      `h` : int_pos
        height of bitmap in coord units

    :returns: pixmap created
    :rtype: long_pos

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_create_from_bitmapdata = libr.cfuncproto(
        libr.load_so_libforms(), "fl_create_from_bitmapdata",
        xfdata.Pixmap, [xfdata.Window, xfdata.STRING, cty.c_int, cty.c_int],
        """Pixmap fl_create_from_bitmapdata(Window win, const
           char * data, int width, int height)""")
    libr.check_if_initialized()
    ulwin = libr.convert_to_Window(win)
    sdata = libr.convert_to_string(data)
    iw = libr.convert_to_int(w)
    ih = libr.convert_to_int(h)
    libr.keep_elem_refs(win, data, w, h, ulwin, sdata, iw, ih)
    retval = _fl_create_from_bitmapdata(ulwin, sdata, iw, ih)
    return retval


# PIXMAP stuff

# fl_create_pixmap function placeholder (internal)


def fl_add_pixmap(pixmaptype, x, y, w, h, label):
    """Adds a pixmap object.

    --

    :Parameters:
      `pixmaptype` : int
        type of pixmap to be added. Values (from xfdata.py) FL_NORMAL_PIXMAP
      `x` : int
        horizontal position (upper-left corner)
      `y` : int
        vertical position of bitmap (upper-left corner)
      `w` : int
        width in coord units
      `h` : int
        height in coord units
      `label` : str
        text label of pixmap

    :returns: object created (pFlObject)
    :rtype: pointer to xfdata.FL_OBJECT

    :note: e.g. fl_add_pixmap(xfdata.FL_NORMAL_PIXMAP, 320, 200, 100, 100, \
      "MyPixmap")

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_add_pixmap = libr.cfuncproto(
        libr.load_so_libforms(), "fl_add_pixmap",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_pixmap(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    libr.check_if_initialized()
    libr.check_admitted_value_in_list(pixmaptype, xfdata.PIXMAPTYPE_list)
    ipixmaptype = libr.convert_to_int(pixmaptype)
    ix = libr.convert_to_FL_Coord(x)
    iy = libr.convert_to_FL_Coord(y)
    iw = libr.convert_to_FL_Coord(w)
    ih = libr.convert_to_FL_Coord(h)
    slabel = libr.convert_to_string(label)
    libr.keep_elem_refs(pixmaptype, x, y, w, h, label, ipixmaptype, ix, \
                           iy, iw, ih, slabel)
    retval = _fl_add_pixmap(ipixmaptype, ix, iy, iw, ih, slabel)
    return retval


def fl_set_pixmap_data(pFlObject, bits):
    """Sets the actual bitmap being displayed from specified data. A
    number of pixmaps can be found in '/usr/include/X11/pixmaps' or similar
    places.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
         pixmap object
      `bits` : str of ubytes
        bits contents of pixmap

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_pixmap_data = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_pixmap_data",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.POINTER(xfdata.STRING)],
        """void fl_set_pixmap_data(FL_OBJECT * ob, char * * bits)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    print "bits", bits
    sbits = libr.convert_to_string(bits)
    print "sbits", sbits
    pbits = cty.pointer(sbits)   # cty.cast(bits, cty.POINTER(xfdata.STRING))
    print "pbits", pbits
    libr.keep_elem_refs(pFlObject, bits, sbits, pbits)
    _fl_set_pixmap_data(pFlObject, pbits)


def fl_set_pixmap_file(pFlObject, fname):
    """Sets the actual bitmap being displayed from a specified .xpm file. A
    number of pixmaps can be found in '/usr/include/X11/pixmaps' or similar
    places.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        pixmap object
      `fname` : str
        name (path included if necessary) of pixmap (.xpm format) file

    :note: e.g. fl_set_pixmap_file(xpmobj, "mypixmapfile.xpm")

    :status: Tested + Doc + Demo = OK

    """
    _fl_set_pixmap_file = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_pixmap_file",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.STRING],
        """void fl_set_pixmap_file(FL_OBJECT * ob, const char * fname)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    sfname = libr.convert_to_string(fname)
    libr.keep_elem_refs(pFlObject, fname, sfname)
    _fl_set_pixmap_file(pFlObject, sfname)


fl_set_pixmapbutton_file = fl_set_pixmap_file
fl_set_pixmapbutton_datafile = fl_set_pixmapbutton_file


def fl_set_pixmap_align(pFlObject, align, xmargin, ymargin):
    """Changes alignment of a pixmap. By default it is displayed centered
    inside the bounding box.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        pixmap object
      `align` : int
        alignment of pixmap. Values (from xfdata.py) FL_ALIGN_CENTER,
        FL_ALIGN_TOP, FL_ALIGN_BOTTOM, FL_ALIGN_LEFT, FL_ALIGN_RIGHT,
        FL_ALIGN_LEFT_TOP, FL_ALIGN_RIGHT_TOP, FL_ALIGN_LEFT_BOTTOM,
        FL_ALIGN_RIGHT_BOTTOM, FL_ALIGN_INSIDE, FL_ALIGN_VERT.
        Bitwise OR with FL_ALIGN_INSIDE is allowed.

    :note: e.g. fl_set_pixmap_align(xpmobj, xfdata.FL_ALIGN_CENTER, 10, 10)

    :status: Tested + Doc + Demo = OK

    """
    _fl_set_pixmap_align = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_pixmap_align",
        None, [cty.POINTER(xfdata.FL_OBJECT), cty.c_int, cty.c_int,
        cty.c_int],
        """void fl_set_pixmap_align(FL_OBJECT * ob, int align,
           int xmargin, int ymargin)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.check_admitted_value_in_list(align, xfdata.ALIGN_list)
    ialign = libr.convert_to_int(align)
    ixmargin = libr.convert_to_int(xmargin)
    iymargin = libr.convert_to_int(ymargin)
    libr.keep_elem_refs(pFlObject, align, xmargin, ymargin, ialign, ixmargin,
                   iymargin)
    _fl_set_pixmap_align(pFlObject, ialign, ixmargin, iymargin)


fl_set_pixmapbutton_align = fl_set_pixmap_align


def fl_set_pixmap_pixmap(pFlObject, idnum, mask):
    """Change the pixmap for the object with a pixmap resource id you already
    may have. It does not free the pixmap ID nor the mask already associated
    with the object.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        pixmap object
      `idnum` : long_pos
        pixmap resource id to be used
      `mask` : long_pos
        mask used for transparency. 0 if no special clipping attributes are
        desired.

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_pixmap_pixmap = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_pixmap_pixmap",
        None, [cty.POINTER(xfdata.FL_OBJECT), xfdata.Pixmap, xfdata.Pixmap],
        """void fl_set_pixmap_pixmap(FL_OBJECT * ob, Pixmap id,
           Pixmap mask)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    ulidnum = libr.convert_to_ulong(idnum)
    ulmask = libr.convert_to_ulong(mask)
    libr.keep_elem_refs(pFlObject, idnum, mask, ulidnum, ulmask)
    _fl_set_pixmap_pixmap(pFlObject, ulidnum, ulmask)


fl_set_pixmapbutton_pixmap = fl_set_pixmap_pixmap


def fl_set_pixmap_colorcloseness(red, green, blue):
    """Changes difference between the requested color and the color found
    being smaller than some pre-set threshold values between 0 and 65535 (0
    means exact match), if a pixmap has more colors than that available in
    the colormap. The library will use substitute colors that are judged
    "close enough".

    --

    :Parameters:
      `red` : int
        difference for red color. By default, closeness is 40000.
      `green` : int
        difference for green color. By default, closeness is 30000.
      `blue` : int
        difference for blue color. By default, closeness is 50000.

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_set_pixmap_colorcloseness = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_pixmap_colorcloseness",
        None, [cty.c_int, cty.c_int, cty.c_int],
        """void fl_set_pixmap_colorcloseness(int red, int green, int blue)""")
    libr.check_if_initialized()
    ired = libr.convert_to_int(red)
    igreen = libr.convert_to_int(green)
    iblue = libr.convert_to_int(blue)
    libr.keep_elem_refs(red, green, blue, ired, igreen, iblue)
    _fl_set_pixmap_colorcloseness(ired, igreen, iblue)


def fl_free_pixmap_pixmap(pFlObject):
    """Frees the old pixmap associated to object, the mask, and the colors the
    pixmap allocated.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        pixmap object

    :note: e.g. *todo*

    :status: Tested + Doc + Demo = OK

    """
    _fl_free_pixmap_pixmap = libr.cfuncproto(
        libr.load_so_libforms(), "fl_free_pixmap_pixmap",
        None, [cty.POINTER(xfdata.FL_OBJECT)],
        """void fl_free_pixmap_pixmap(FL_OBJECT * ob)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    libr.keep_elem_refs(pFlObject)
    _fl_free_pixmap_pixmap(pFlObject)


fl_free_pixmapbutton_pixmap = fl_free_pixmap_pixmap


def fl_get_pixmap_pixmap(pFlObject):
    """Obtains the pixmap ID currently being displayed.

    --

    :Parameters:
      `pFlObject` : pointer to xfdata.FL_OBJECT
        pixmap object

    :returns: pixmap id, pixmap id, pixmap mask
    :rtype: long_pos, long_pos, long_pos

    :note: e.g. *todo*

    :attention: API change from XForms - upstream was
        fl_get_pixmap_pixmap(pFlObject, p, m)

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_get_pixmap_pixmap = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_pixmap_pixmap",
        xfdata.Pixmap, [cty.POINTER(xfdata.FL_OBJECT),
        cty.POINTER(xfdata.Pixmap), cty.POINTER(xfdata.Pixmap)],
        """Pixmap fl_get_pixmap_pixmap(FL_OBJECT * ob, Pixmap * p,
           Pixmap * m)""")
    libr.check_if_initialized()
    libr.verify_flobjectptr_type(pFlObject)
    p, pp = libr.make_ulong_and_pointer()
    m, pm = libr.make_ulong_and_pointer()
    libr.keep_elem_refs(pFlObject, p, m, pp, pm)
    retval = _fl_get_pixmap_pixmap(pFlObject, pp, pm)
    return retval, p.value, m.value


fl_get_pixmapbutton_pixmap = fl_get_pixmap_pixmap


def fl_read_pixmapfile(win, fname, tran):
    """Makes a pixmap from a pixmap file.

    --

    :Parameters:
      `win` : long_pos
        window id
      `fname` : str
        name of pixmap (.xpm format) file
      `tran` : long_pos
        color value

    :returns: pixmap, w, h, shapemask, hotx, hoty
    :rtype: long_pos, int_pos, int_pos, long_pos, int, int

    :note: e.g. pmap, w, h, shapmsk, hotx, hoty = fl_read_pixmapfile(win0, \
        "xpmfile.xpm", xfdata.FL_WHITE)

    :attention: API change from XForms - upstream was
        fl_read_pixmapfile(win, filename, w, h, shape_mask, hotx, hoty, tran)

    :status: Tested + Doc + Demo = OK

    """
    _fl_read_pixmapfile = libr.cfuncproto(
        libr.load_so_libforms(), "fl_read_pixmapfile",
        xfdata.Pixmap, [xfdata.Window, xfdata.STRING, cty.POINTER(cty.c_uint),
        cty.POINTER(cty.c_uint), cty.POINTER(xfdata.Pixmap),
        cty.POINTER(cty.c_int), cty.POINTER(cty.c_int), xfdata.FL_COLOR],
        """Pixmap fl_read_pixmapfile(Window win, const char * file,
           unsigned int * w, unsigned int * h, Pixmap * shape_mask,
           int * hotx, int * hoty, FL_COLOR tran)""")
    libr.check_if_initialized()
    libr.check_admitted_value_in_list(tran, xfdata.COLOR_list)
    ulwin = libr.convert_to_Window(win)
    sfname = libr.convert_to_string(fname)
    ultran = libr.convert_to_FL_COLOR(tran)
    w, pw = libr.make_uint_and_pointer()
    h, ph = libr.make_uint_and_pointer()
    shapemask, pshapemask = libr.make_ulong_and_pointer()
    hotx, photx = libr.make_int_and_pointer()
    hoty, photy = libr.make_int_and_pointer()
    libr.keep_elem_refs(win, fname, w, h, shapemask, hotx, hoty, tran, ulwin,
                   sfname, ultran, pw, ph, pshapemask, photx, photy)
    retval = _fl_read_pixmapfile(ulwin, sfname, pw, ph, pshapemask, \
                                 photx, photy, ultran)
    return retval, w.value, h.value, shapemask.value, hotx.value, hoty.value


def fl_create_from_pixmapdata(win, data, w, h, sm, hotx, hoty, tran):
    """Makes a pixmap from pixmap contents data.

    --

    :Parameters:
      `win` : long_pos
        window id
      `data` : str of ubytes
        pixmap contents data
      `w` : int_pos
        width of pixmap in coord units
      `h` : int_pos
        height of pixmap in coord units
      `sm` : long_pos
        shape mask (of an existing pixmap) used as a clipping mask to
        achieve transparency, 0 for no transparency.
      `hotx` : int
        horizontal position of center of the pixmap (useful if the pixmap is
        to be used as a cursor)
      `hoty` : int
        vertical position of center of the pixmap (useful if the pixmap is
        to be used as a cursor)
      `tran` : long_pos
        color value (currently not used)

    :returns: pixmap id created
    :rtype: long_pos

    :note: e.g. *todo*

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_create_from_pixmapdata = libr.cfuncproto(
        libr.load_so_libforms(), "fl_create_from_pixmapdata",
        xfdata.Pixmap, [xfdata.Window, cty.POINTER(xfdata.STRING),
        cty.POINTER(cty.c_uint), cty.POINTER(cty.c_uint),
        cty.POINTER(xfdata.Pixmap), cty.POINTER(cty.c_int),
        cty.POINTER(cty.c_int), xfdata.FL_COLOR],
        """Pixmap fl_create_from_pixmapdata(Window win, char * * data,
        unsigned int * w, unsigned int * h, Pixmap * sm, int * hotx,
        int * hoty, FL_COLOR tran)""")
    libr.check_if_initialized()
    libr.check_admitted_value_in_list(tran, xfdata.COLOR_list)
    ulwin = libr.convert_to_Window(win)
    ultran = libr.convert_to_FL_COLOR(tran)
    libr.keep_elem_refs(win, data, w, h, sm, hotx, hoty, tran, ulwin, ultran)
    retval = _fl_create_from_pixmapdata(ulwin, data, w, h, sm, hotx, hoty,
                                        ultran)
    return retval


def fl_free_pixmap(idnum):
    """Frees the pixmap.

    --

    :Parameters:
      `idnum` : long_pos
        Pixmap id to be freed

    :note: e.g. fl_free_pixmap(pmap)

    :status: Untested + Doc + NoDemo = NOT OK

    """
    _fl_free_pixmap = libr.cfuncproto(
        libr.load_so_libforms(), "fl_free_pixmap",
        None, [xfdata.Pixmap],
        """void fl_free_pixmap(Pixmap id)""")
    libr.check_if_initialized()
    ulidnum = libr.convert_to_Pixmap(idnum)
    libr.keep_elem_refs(idnum, ulidnum)
    _fl_free_pixmap(ulidnum)
