#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" xforms-python's functions to manage files and directories.

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


############################################
# forms.h (filesys.h)
# Convenience functions to read a directory
############################################

# read dir with pattern filtering. All dirs read might be cached.
# must not change dirlist in anyway.

def fl_get_dirlist(dirname, pattern, rescan):
    """Gets a listing of specified directory.

    --

    :Parameters:
      `dirname` : str
        name of directory
      `pattern` : str
        regular expression that is used to filter the directory entries
      `rescan` : flag to request a re-read or not. Values 0 (no re-read)
        or non-zero (does a re-read)

    :return: an array of DirList class instances (pDirList) and number of
        files (total number of entries in directory dirname that match the
        pattern specified by pattern)
    :rtype: pointer to xfdata.FL_DIRLIST, int

    :note: e.g. pdirlist, nfiles = dirlistfl_get_dirlist("/home", "*.*", 1)
    :note: e.g. print pdirlist[1].name

    :attention: API change from XForms - upstream was
       fl_get_dirlist(directory, pattern, n, rescan)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_get_dirlist = libr.cfuncproto(
        libr.load_so_libforms(), "fl_get_dirlist",
        cty.POINTER(xfdata.FL_Dirlist), [xfdata.STRING, xfdata.STRING,
        cty.POINTER(cty.c_int), cty.c_int],
        """const char * fl_get_dirlist(const char * dir,
           const char * pattern, int * n, int rescan)""")
    libr.check_if_initialized()
    sdirname = libr.convert_to_string(dirname)
    spattern = libr.convert_to_string(pattern)
    n, pn = libr.make_int_and_pointer()
    irescan = libr.convert_to_int(rescan)
    libr.keep_elem_refs(dirname, pattern, n, rescan, sdirname, spattern,
                   pn, irescan)
    retval = _fl_get_dirlist(sdirname, spattern, pn, irescan)
    return retval, n.value


def fl_set_dirlist_filter(py_DirFilter):
    """Changes the default filter by which file types are returned.
    By default not all types of files are returned (only directories,
    normal files and link files).

    --

    :Parameters:
      `py_DirFilter` : python function used to filter types, returned value
        name referring to function (strname, inttype) -> (non-zero if is to
        be included, 0 otherwise)

    :return: old dirlist filter function
    :rtype: xfdata.FL_DIRLIST_FILTER class instance

    :note: e.g. def dirfilter(fname, ftype)
    :note: e.g. > return type == xfdata.FT_DIR || return type == \
    :note: e.g. > xfdata.FT_FILE || return type == xfdata.FT_SOCK || \
    :note: e.g. > return type == xfdata.FT_FIFO || return type == \
    :note: e.g. > xfdata.FT_LINK || return type == xfdata.FT_BLK || \
    :note: e.g. > return type == xfdata.FT_CHR || return type == \
    :note: e.g. > xfdata.FT_OTHER
    :note: e.g. olddirfiltfunc = fl_set_dirlist_filter(dirfilter)

    :status: Tested + Doc + NoDemo = OK

    """
    #FL_DIRLIST_FILTER = cty.CFUNCTYPE(cty.c_int, xfdata.STRING, cty.c_int)
    _fl_set_dirlist_filter = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_dirlist_filter",
        xfdata.FL_DIRLIST_FILTER, [xfdata.FL_DIRLIST_FILTER],
        """FL_DIRLIST_FILTER fl_set_dirlist_filter( \
           FL_DIRLIST_FILTER filter)""")
    libr.check_if_initialized()
    libr.verify_function_type(py_DirFilter)
    c_DirFilter = xfdata.FL_DIRLIST_FILTER(py_DirFilter)
    libr.keep_cfunc_refs(c_DirFilter, py_DirFilter)
    retval = _fl_set_dirlist_filter(c_DirFilter)
    return retval


def fl_set_dirlist_sort(method):
    """Changes the default sorting of files in directory. By default the
    files returned are sorted alphabetically.

    --

    :Parameters:
      `method` : int
        method of sorting. Values (from xfdata.py) FL_NONE, FL_ALPHASORT,
        FL_RALPHASORT, FL_MTIMESORT, FL_RMTIMESORT,  FL_SIZESORT, FL_RSIZESORT,
        FL_CASEALPHASORT, FL_RCASEALPHASORT

    :return: old sort method
    :rtype: int

    :note: e.g. num = fl_set_dirlist_sort(xfdata.FL_CASEALPHASORT)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_set_dirlist_sort = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_dirlist_sort",
        cty.c_int, [cty.c_int],
        """int fl_set_dirlist_sort(int method)""")
    libr.check_if_initialized()
    imethod = libr.convert_to_int(method)
    libr.keep_elem_refs(method, imethod)
    retval = _fl_set_dirlist_sort(imethod)
    return retval


def fl_set_dirlist_filterdir(yesno):
    """Change the filter to include the directories. By default directories
     are not subject to filtering.

    --

    :Parameters:
      `yesno` : int
        flag to enable/disable directory filter. Values 1 (enabled) or 0
        (disabled)

    :return: old filter setting
    :rtype: int

    :note: e.g. olddirfilt = fl_set_dirlist_filterdir(1)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_set_dirlist_filterdir = libr.cfuncproto(
        libr.load_so_libforms(), "fl_set_dirlist_filterdir",
        cty.c_int, [cty.c_int],
        """int fl_set_dirlist_filterdir(int yes)""")
    libr.check_if_initialized()
    iyesno = libr.convert_to_int(yesno)
    libr.keep_elem_refs(yesno, iyesno)
    retval = _fl_set_dirlist_filterdir(iyesno)
    return retval


def fl_free_dirlist(pDirList):
    """Frees the list cache returned by fl_get_dirlist().

    --

    :Parameters:
      `pDirList` : pointer to xfdata.FL_DirList
        instance of DirList class

    :note: e.g. fl_free_dirlist(pdirlist)

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_free_dirlist = libr.cfuncproto(
        libr.load_so_libforms(), "fl_free_dirlist",
        None, [cty.POINTER(xfdata.FL_Dirlist)],
        """void fl_free_dirlist(FL_Dirlist * dl)""")
    libr.check_if_initialized()
    libr.verify_otherclassptr_type(pDirList, cty.POINTER( \
                                xfdata.FL_Dirlist))
    libr.keep_elem_refs(pDirList)
    _fl_free_dirlist(pDirList)


# Free all directory caches

def fl_free_all_dirlist():
    """Frees all the list caches returned by fl_get_dirlist().

    --

    :note: e.g. fl_free_all_dirlist()

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_free_all_dirlist = libr.cfuncproto(
        libr.load_so_libforms(), "fl_free_all_dirlist",
        None, [],
        """void fl_free_all_dirlist()""")
    libr.check_if_initialized()
    _fl_free_all_dirlist()


def fl_is_valid_dir(dirname):
    """Checks if dirname is a valid name of a directory.

    --

    :Parameters:
      `dirname` : str
        name of the directory to evaluate

    :return: 1 (if valid) or 0 (if invalid)
    :rtype: int

    :note: e.g. fl_is_valid_dir(name) -> num.

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_is_valid_dir = libr.cfuncproto(
        libr.load_so_libforms(), "fl_is_valid_dir",
        cty.c_int, [xfdata.STRING],
        """int fl_is_valid_dir(const char * name)""")
    libr.check_if_initialized()
    sdirname = libr.convert_to_string(dirname)
    libr.keep_elem_refs(dirname, sdirname)
    retval = _fl_is_valid_dir(sdirname)
    return retval


def fl_fmtime(fname):
    """Returns the modification time of a specified file.

    --

    :Parameters:
      `fname` : str
        name of the file

    :return: file modification time
    :rtype: long_pos

    :note: e.g. fmtime = fl_fmtime("/home/user/somefile")

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_fmtime = libr.cfuncproto(
        libr.load_so_libforms(), "fl_fmtime",
        cty.c_ulong, [xfdata.STRING],
        """long unsigned int fl_fmtime(const char * s)""")
    libr.check_if_initialized()
    sfname = libr.convert_to_string(fname)
    libr.keep_elem_refs(fname, sfname)
    retval = _fl_fmtime(sfname)
    return retval


def fl_fix_dirname(dirname):
    """Fixes the name of a directory that has a relative path ("..") in it.

    --

    :Parameters:
      `dirname` : str
        name of the directory to evaluate

    :return: fixed directory name
    :rtype: str

    :note: e.g. newdirnam = fl_fix_dirname("../../mydir/")

    :status: Tested + Doc + NoDemo = OK

    """
    _fl_fix_dirname = libr.cfuncproto(
        libr.load_so_libforms(), "fl_fix_dirname",
        xfdata.STRING, [xfdata.STRING],
        """char * fl_fix_dirname(char * dir)""")
    libr.check_if_initialized()
    sdirname = libr.convert_to_string(dirname)
    libr.keep_elem_refs(dirname, sdirname)
    retval = _fl_fix_dirname(sdirname)
    return retval
