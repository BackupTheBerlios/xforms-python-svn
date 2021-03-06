#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" xforms-python's functions to manage files and directories.
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


############################################
# forms.h (filesys.h)
# Convenience functions to read a directory
############################################

# read dir with pattern filtering. All dirs read might be cached.
# must not change dirlist in anyway.

def fl_get_dirlist(dirname, pattern, rescan):
    """fl_get_dirlist(dirname, pattern, rescan) -> ptr_dirlist, numfiles

    Finds out a listing of specified directory.

    Parameters
    ----------
        dirname : str
            name of directory
        pattern : str
            regular expression that is used to filter the directory entries
        rescan : int
            flag to request a re-read or not. Values 0 (no re-read) or
            non-zero (to do a re-read)

    Returns
    -------
        ptr_dirlist : pointer to xfdata.FL_DIRLIST
            array of DirList class instances
        numfiles : int
            number of files (total number of entries in directory dirname
            that match the pattern specified by pattern)

    Examples
    --------
        >>> pdirlist, nfiles = fl_get_dirlist("/home/userdir", "*.*", 1)
        >>> print(pdirlist[1].name)

    API_diversion
    ----------
        API changed from XForms, upstream is
        fl_get_dirlist(directory, pattern, n, rescan)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_get_dirlist = library.cfuncproto(
        library.load_so_libforms(), "fl_get_dirlist",
        cty.POINTER(xfdata.FL_Dirlist), [xfdata.STRING, xfdata.STRING,
        cty.POINTER(cty.c_int), cty.c_int],
        """const FL_Dirlist * fl_get_dirlist(const char * dir,
           const char * pattern, int * n, int rescan)""")
    library.check_if_flinitialized()
    s_dirname = library.convert_to_bytestrc(dirname)
    s_pattern = library.convert_to_bytestrc(pattern)
    i_numfiles, ptr_numfiles = library.make_intc_and_pointer()
    i_rescan = library.convert_to_intc(rescan)
    library.keep_elem_refs(dirname, pattern, i_numfiles, rescan, s_dirname, \
            s_pattern, ptr_numfiles, i_rescan)
    retval = _fl_get_dirlist(s_dirname, s_pattern, ptr_numfiles, i_rescan)
    return retval, i_numfiles.value


def fl_set_dirlist_filter(pyfn_DirFilter):
    """fl_set_dirlist_filter(pyfn_DirFilter) -> DirFilter

    Changes the default filter by which file types are returned.
    By default not all types of files are returned (only directories,
    normal files and link files).

    Parameters
    ----------
        pyfn_DirFilter : python function, returned value
            name referring to function ([str]name, [int]type) -> (non-zero if
            is to be included, 0 otherwise)
            Function used to filter types

    Returns
    -------
        DirFilter : xfdata.FL_DIRLIST_FILTER class instance
            old dirlist filter function

    Examples
    --------
        >>> def dirfiltercb(fname, ftype):
        >>> ... return (ftype == xfdata.FT_DIR || ftype == xfdata.FT_FILE ||
        >>>     ftype == xfdata.FT_SOCK || ftype == xfdata.FT_FIFO ||
        >>>     ftype == xfdata.FT_LINK || ftype == xfdata.FT_BLK ||
        >>>     ftype == xfdata.FT_CHR || type == xfdata.FT_OTHER)
        >>> olddirfiltfunc = fl_set_dirlist_filter(dirfiltercb)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    #FL_DIRLIST_FILTER = cty.CFUNCTYPE(cty.c_int, xfdata.STRING, cty.c_int)
    _fl_set_dirlist_filter = library.cfuncproto(
        library.load_so_libforms(), "fl_set_dirlist_filter",
        xfdata.FL_DIRLIST_FILTER, [xfdata.FL_DIRLIST_FILTER],
        """FL_DIRLIST_FILTER fl_set_dirlist_filter( \
           FL_DIRLIST_FILTER filter)""")
    library.check_if_flinitialized()
    library.verify_function_type(pyfn_DirFilter)
    cfn_DirFilter = xfdata.FL_DIRLIST_FILTER(pyfn_DirFilter)
    library.keep_cfunc_refs(cfn_DirFilter, pyfn_DirFilter)
    retval = _fl_set_dirlist_filter(cfn_DirFilter)
    return retval


def fl_set_dirlist_sort(method):
    """fl_set_dirlist_sort(method) -> oldmethod

    Changes the default sorting of files in directory. By default the files
    returned are sorted alphabetically.

    Parameters
    ----------
        method : int
            method of sorting. Values (from xfdata.py)
            - FL_NONE (Do not sort the entries),
            - FL_ALPHASORT (Sorts the entries in alphabetic order, default),
            - FL_RALPHASORT (Sorts the entries in reverse alphabetic order),
            - FL_MTIMESORT (Sorts the entries according to modification time),
            - FL_RMTIMESORT (Sorts the entries according to modification time,
              but reverse the order, i.e., latest first),
            - FL_SIZESORT (Sorts the entries in increasing size order),
            - FL_RSIZESORT (Sorts the entries in decreasing size order),
            - FL_CASEALPHASORT (Sorts the entries in alphabetic order with no
              regard to case),
            - FL_RCASEALPHASORT (Sorts the entries in reverse alphabetic order
              with no regard to case).

    Returns
    -------
        oldmethod : int
            old sort method

    Examples
    --------
        >>> num = fl_set_dirlist_sort(xfdata.FL_CASEALPHASORT)

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_set_dirlist_sort = library.cfuncproto(
        library.load_so_libforms(), "fl_set_dirlist_sort",
        cty.c_int, [cty.c_int],
        """int fl_set_dirlist_sort(int method)""")
    library.check_if_flinitialized()
    i_method = library.convert_to_intc(method)
    library.keep_elem_refs(method, i_method)
    retval = _fl_set_dirlist_sort(i_method)
    return retval


def fl_set_dirlist_filterdir(yesno):
    """fl_set_dirlist_filterdir(yesno) -> oldfilt

    Changes the filter to include the directories. By default directories
    are not subject to filtering.

    Parameters
    ----------
        yesno : int
            flag to enable/disable directory filter. Values 1 (enabled)
            or 0 (disabled)

    Returns
    -------
        oldfilt : int
            old filter setting

    Examples
    --------
        >>> olddirfilt = fl_set_dirlist_filterdir(1)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_set_dirlist_filterdir = library.cfuncproto(
        library.load_so_libforms(), "fl_set_dirlist_filterdir",
        cty.c_int, [cty.c_int],
        """int fl_set_dirlist_filterdir(int yes)""")
    library.check_if_flinitialized()
    i_yesno = library.convert_to_intc(yesno)
    library.keep_elem_refs(yesno, i_yesno)
    retval = _fl_set_dirlist_filterdir(i_yesno)
    return retval


def fl_free_dirlist(ptr_dirlist):
    """fl_free_dirlist(ptr_dirlist)

    Frees the list cache returned by fl_get_dirlist().

    Parameters
    ----------
        ptr_dirlist : pointer to xfdata.FL_DirList
            instance of DirList class

    Examples
    --------
        >>> fl_free_dirlist(pdirlist)

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_free_dirlist = library.cfuncproto(
        library.load_so_libforms(), "fl_free_dirlist",
        None, [cty.POINTER(xfdata.FL_Dirlist)],
        """void fl_free_dirlist(FL_Dirlist * dl)""")
    library.check_if_flinitialized()
    library.verify_otherclassptr_type(ptr_dirlist, \
            cty.POINTER(xfdata.FL_Dirlist))
    library.keep_elem_refs(ptr_dirlist)
    _fl_free_dirlist(ptr_dirlist)


# Free all directory caches

def fl_free_all_dirlist():
    """fl_free_all_dirlist()

    Frees all the list caches returned by fl_get_dirlist().

    Examples
    --------
        >>> fl_free_all_dirlist()

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_free_all_dirlist = library.cfuncproto(
        library.load_so_libforms(), "fl_free_all_dirlist",
        None, [],
        """void fl_free_all_dirlist()""")
    library.check_if_flinitialized()
    _fl_free_all_dirlist()


def fl_is_valid_dir(dirname):
    """fl_is_valid_dir(dirname) -> yesno

    Checks if dirname is a valid name of a directory. You can use python's
    os.path.isdir(), instead.

    Parameters
    ----------
        dirname : str
            name of the directory to evaluate

    Returns
    -------
        yesno : int
            1 (if valid) or 0 (if invalid)

    Examples
    --------
        >>> isvalid = fl_is_valid_dir("/etc/mydirname")
        >>> if not isvalid:
        >>> ... <something>

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_is_valid_dir = library.cfuncproto(
        library.load_so_libforms(), "fl_is_valid_dir",
        cty.c_int, [xfdata.STRING],
        """int fl_is_valid_dir(const char * name)""")
    library.check_if_flinitialized()
    s_dirname = library.convert_to_bytestrc(dirname)
    library.keep_elem_refs(dirname, s_dirname)
    retval = _fl_is_valid_dir(s_dirname)
    return retval


def fl_fmtime(fname):
    """fl_fmtime(fname) -> mtime

    Finds out the modification time of a specified file. You can then use
    python time.ctime() to have a textual representation of time.

    Parameters
    ----------
        fname : str
            name of the file

    Returns
    -------
        mtime : long_pos
            file modification time

    Examples
    --------
        >>> fmtime = fl_fmtime("/home/user/somefile")

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_fmtime = library.cfuncproto(
        library.load_so_libforms(), "fl_fmtime",
        cty.c_ulong, [xfdata.STRING],
        """long unsigned int fl_fmtime(const char * s)""")
    library.check_if_flinitialized()
    s_fname = library.convert_to_bytestrc(fname)
    library.keep_elem_refs(fname, s_fname)
    retval = _fl_fmtime(s_fname)
    return retval


def fl_fix_dirname(dirname):
    """fl_fix_dirname(dirname) -> fixdirname

    Fixes the name of a directory that has a relative path ("..") in it.
    You can use os.path.normnpath(), instead.

    Parameters
    ----------
        dirname : str
            name of the directory to evaluate

    Returns
    -------
        fixdirname : str
            fixed directory name

    Examples
    --------
        >>> newdirnam = fl_fix_dirname("../../home/user/../user/mydir/")

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    _fl_fix_dirname = library.cfuncproto(
        library.load_so_libforms(), "fl_fix_dirname",
        xfdata.STRING, [xfdata.STRING],
        """char * fl_fix_dirname(char * dir)""")
    library.check_if_flinitialized()
    s_dirname = library.convert_to_bytestrc(dirname)
    library.keep_elem_refs(dirname, s_dirname)
    retval = _fl_fix_dirname(s_dirname)
    if isinstance(retval, bytes):
        return retval.decode('utf-8')
    else:       # str
        return retval

