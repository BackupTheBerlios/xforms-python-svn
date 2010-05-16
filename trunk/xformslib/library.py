#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" Convenience functions to deal with xforms-python wrapper's functions.

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


#######################################################################
# This file contains support/private functions, that are not
# supposed to be used directly by users, except for Make_pPopupItem_*
#######################################################################


import ctypes as cty
import ctypes.util as ctyutil
import warnings
from xformslib import vers
from xformslib import xfdata


class XFormsInitError(OSError):
    """ Error in initializing library, not using fl_initialize() before
        functions who require it. """
    pass

class XFormsLoadError(OSError):
    """ Error in loading shared object library """
    pass

class XFormsTypeError(TypeError):
    """ Generic error for type mismatch """
    pass

class XFormsValueError(ValueError):
    """ Generic error for unexpected value"""
    pass


header_filename = "/usr/include/forms.h"

def get_xforms_version():
    """ Returns version string of installed XForms library/header """
    complete_xf_version = ""
    try:
        formshdr = open(header_filename, "r")
    except IOError:
        raise XFormsLoadError("XForms library toolkit header file is" \
                              " not installed properly: not existent?")
    else:
        try:
            # a reasonable size to catch version values
            fconten = formshdr.read(2500)
        except IOError:
            raise XFormsLoadError("XForms library toolkit header is" \
                                  "not installed properly: corrupted or " \
                                  "incomplete?")
        else:
            formshdr.close()
            listconten = fconten.split("\n")
            for singline in listconten:
                idx_ver = singline.find("FL_VERSION")
                if idx_ver != -1:
                    strg_ver1 = singline[idx_ver:len(singline)]
                    strg_ver = strg_ver1.replace("FL_VERSION", "").strip(" ")
                    break
            for singline in listconten:
                idx_rev = singline.find("FL_REVISION")
                if idx_rev != -1:
                    strg_rev1 = singline[idx_rev:len(singline)]
                    strg_rev = strg_rev1.replace("FL_REVISION", "").strip(" ")
                    break
            for singline in listconten:
                idx_fix = singline.find("FL_FIXLEVEL")
                if idx_fix != -1:
                    strg_fix1 = singline[idx_fix:len(singline)]
                    strg_fix = strg_fix1.replace("FL_FIXLEVEL", \
                                                 "").strip(" ").strip('"')
                    break
            complete_xf_version = strg_ver + "." + strg_rev + "." + strg_fix

    return complete_xf_version


def verify_version_compatibility():
    """ verify compatibility between xforms-python and XForms versions """
    xforms_vers = get_xforms_version()
    if vers.__vers_against_xforms__ != xforms_vers:      # no match
        warningmsg = "xforms-python is implemented against XForms version " \
                    "%s and does not match XForms installed version (%s)." \
                    "Some compatibility problems may arise if XForms" \
                    " public interface has been modified." % \
                    (vers.__vers_against_xforms__, xforms_vers)
        warnings.warn(warningmsg, UserWarning)


def func_notexisting_placeholder(cfunction):
    """ Print a warning if called function doesn't exist """
    warningmsg = "C function %s does NOT exist, hence it is not " \
                 "wrappable and callable in python and its call " \
                 "is ignored. Maybe removed or disabled?" % cfunction
    warnings.warn(warningmsg, UserWarning)
    return None


# placeholders to keep reference to c functions
# keeps global to avoid garbage collector's' unpredictable behaviour
_cfunc_refs = []
# just in case, maintains elements used as parameters, too
_elem_refs = []

def keep_cfunc_refs(*cfunclist):
    """ Adds a reference for _cfunc_refs list of values """
    for singvalue in cfunclist:
        _cfunc_refs.append(singvalue)


def keep_elem_refs(*elemlist):
    """ Adds a reference for _elem_refs list of values """
    for singvalue in elemlist:
        _elem_refs.append(singvalue)


loaded_xlibraries = {'libforms' : None, 'libflimage' : None, \
                    'libformsgl' : None, 'libx11' : None}


def load_so_libforms():
    """ Load libforms.so else raise an error -> library instance """
    if loaded_xlibraries['libforms'] is None:
        libfbase = ctyutil.find_library("forms")
        if not libfbase:    # not installed
            raise XFormsLoadError("XForms library toolkit (libforms.so) is"
                                  " not installed properly")
        else:
            loaded_xlibraries['libforms'] = cty.cdll.LoadLibrary(libfbase)
    return loaded_xlibraries['libforms']


def load_so_libflimage():
    """ Load libflimage.so else raise an error -> library instance """
    if loaded_xlibraries['libflimage'] is None:
        libfimg = ctyutil.find_library("flimage")
        if not libfimg:    # not installed
            raise XFormsLoadError("XForms library toolkit (libflimage.so) is"
                                  " not installed properly")
        else:
            loaded_xlibraries['libflimage'] = cty.cdll.LoadLibrary(libfimg)
    return loaded_xlibraries['libflimage']


def load_so_libformsgl():
    """ Load libformsGL.so else raise an error -> library instance """
    if loaded_xlibraries['libformsgl'] is None:
        libfgl = ctyutil.find_library("formsGL")
        if not libfgl:    # not installed
            raise XFormsLoadError("XForms library toolkit (libformsGL.so) " \
                                  "is not installed properly. Did you " \
                                  "compile it without OpenGL support?")
        else:
            loaded_xlibraries['libformsgl'] = cty.cdll.LoadLibrary(libfgl)
    return loaded_xlibraries['libformsgl']


def load_so_libx11():
    """ Load libX11.so.6 else raise an error -> library instance """
    if loaded_xlibraries['libx11'] is None:
        libx11 = ctyutil.find_library("X11")
        if not libx11:    # not installed
            raise XFormsLoadError("X11 libraries (libx11.so) are not" \
                                  " installed properly")
        else:
            loaded_xlibraries['libx11'] = cty.cdll.LoadLibrary(libx11)
    return loaded_xlibraries['libx11']


def cfuncproto(library, cfuncname, retval, arglist, doc=""):
    """ Prototype for C functions to be wrapped in python """
    loadedfunc = None
    try:
        loadedfunc = getattr(library, cfuncname)
    except AttributeError:
        # function doesn't exist
        loadedfunc = func_notexisting_placeholder(cfuncname)
    else:
        loadedfunc.restype = retval
        loadedfunc.argtypes = arglist
        loadedfunc.__doc__ = doc

    return loadedfunc


flinitialized = False           # if fl_initialize() not called before

def check_if_initialized():
    """ Check if fl_initialize() has been called before caller function.
        Needed for most functions, except those supposed to be used
        *BEFORE* initialization. """
    if not flinitialized:       # fl_initialize() not called
        raise XFormsInitError("You must call fl_initialize() before using" \
                              " this function.")

def set_initialized():
    """ fl_initialize() has beeen called """
    global flinitialized
    flinitialized = True


# functions to convert a parameter into a python type then into the
# equivalent ctypes type

def convert_to_string(paramname):
    """ Converts paramname to python str and to ctypes c_char_p """
    try:
        retv0 = str(paramname)
    except ValueError:
        raise XFormsTypeError("Parameter '%s' is of type %s and cannot" \
                              " be converted into 'str'/'c_char_p'" % \
                              (paramname, type(paramname)))
    retv = cty.c_char_p(retv0)
    return retv


def convert_to_int(paramname):
    """ Converts paramname to python int and to ctypes c_int """
    if not isinstance(paramname, cty.c_int):
        try:
            retv0 = int(paramname)
        except ValueError:
            raise XFormsTypeError("Parameter '%s' is of type %s and cannot" \
                              " be converted into 'int'/'c_int'" % \
                              (paramname, type(paramname)))
        retv = cty.c_int(retv0)
        return retv
    else:
        return paramname

convert_to_FL_Coord = convert_to_int


def convert_to_uint(paramname):
    """ Converts paramname to python int and to ctypes c_uint """
    if not isinstance(paramname, cty.c_int):
        try:
            retv0 = int(paramname)
        except ValueError:
            raise XFormsTypeError("Parameter '%s' is of type %s and cannot" \
                              " be converted into 'int'/'c_uint'" % \
                              (paramname, type(paramname)))
        else:
            retv = cty.c_uint(retv0)
            return retv
    else:
        return paramname


def convert_to_long(paramname):
    """ Converts paramname to python long and to ctypes c_long """
    if not isinstance(paramname, cty.c_long):
        try:
            retv0 = long(paramname)
        except ValueError:
            raise XFormsTypeError("Parameter '%s' is of type %s and cannot" \
                              " be converted into 'long'/'c_long'" % \
                              (paramname, type(paramname)))
        else:
            retv = cty.c_long(retv0)
            return retv
    else:
        return paramname


def convert_to_ulong(paramname):
    """ Converts paramname to python long and to ctypes c_ulong """
    if not isinstance(paramname, cty.c_ulong):
        try:
            retv0 = long(paramname)
        except ValueError:
            raise XFormsTypeError("Parameter '%s' is of type %s and cannot" \
                              " be converted into 'long'/'c_ulong'" % \
                              (paramname, type(paramname)))
        else:
            retv = cty.c_ulong(retv0)
            return retv
    else:
        return paramname

convert_to_FL_COLOR = convert_to_ulong
convert_to_Window = convert_to_ulong
convert_to_Pixmap = convert_to_ulong


def convert_to_double(paramname):
    """ Converts paramname to python float and to ctypes c_double """
    if not isinstance(paramname, cty.c_double):
        try:
            retv0 = float(paramname)
        except ValueError:
            raise XFormsTypeError("Parameter '%s' is of type %s and cannot" \
                              " be converted into 'float'/'c_double'" % \
                              (paramname, type(paramname)))
        else:
            retv = cty.c_double(retv0)
            #print "double", paramname, retv0, retv
            return retv
    else:
        return paramname


def convert_to_float(paramname):
    """ Converts paramname to python float and to ctypes c_float """
    if not isinstance(paramname, cty.c_float):
        try:
            retv0 = float(paramname)
        except ValueError:
            raise XFormsTypeError("Parameter '%s' is of type %s and cannot" \
                              " be converted into 'float'/'c_float'" % \
                              (paramname, type(paramname)))
        else:
            retv = cty.c_float(retv0)
            #print "float", paramname, retv0, retv
            return retv
    else:
        return paramname


def convert_to_ubyte(paramname):
    """ Converts paramname to ctypes c_ubyte """
    retv = cty.c_ubyte(paramname)
    return retv


def make_int_and_pointer():
    """ Makes a ctypes c_int and its pointer, and returns both """
    baseval = cty.c_int()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval

make_FL_Coord_and_pointer = make_int_and_pointer


def make_uint_and_pointer():
    """ Makes a ctypes c_uint and its pointer, and returns both """
    baseval = cty.c_uint()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval


def make_long_and_pointer():
    """ Makes a ctypes c_long and its pointer, and returns both """
    baseval = cty.c_long()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval


def make_ulong_and_pointer():
    """ Makes a ctypes c_ulong and its pointer, and returns both """
    baseval = cty.c_ulong()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval

make_Pixmap_and_pointer = make_ulong_and_pointer
make_FL_COLOR_and_pointer = make_ulong_and_pointer


def make_float_and_pointer():
    """ Makes a ctypes c_float and its pointer, and returns both """
    baseval = cty.c_float()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval


def make_double_and_pointer():
    """ Makes a ctypes c_double and its pointer, and returns both """
    baseval = cty.c_double()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval


def make_ubyte_and_pointer():
    """ Makes a ctypes c_ubyte and its pointer, and returns both """
    baseval = cty.c_ubyte()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval


def make_ushort_and_pointer():
    """ Makes a ctypes c_ushort and its pointer, and returns both """
    baseval = cty.c_ushort()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval


def check_admitted_value_in_list(paramname, valueslist):
    """ Check if paramname value is valid in accordance to a list or tuple
        of admissible values."""
    if isinstance(valueslist, list) or isinstance(valueslist, tuple):
        if paramname not in valueslist:
            raise XFormsValueError("Parameter %s value of type %s must be " \
                    "one of those included in list/tuple %s." % \
                    (paramname, type(paramname), valueslist))

def verify_tuplelist_type(paramname):
    """Check if paramname is a valid list or tuple."""
    if not isinstance(paramname, list) and not isinstance(paramname, tuple):
        raise XFormsTypeError("Parameter %s of type %s must be a " \
                        "list or a tuple." % (paramname, type(paramname)))


def verify_flobjectptr_type(paramname):
    """Check if paramname is a valid pointer to xfdata.FL_OBJECT."""
    if not isinstance(paramname, cty.POINTER(xfdata.FL_OBJECT)):
        raise XFormsTypeError("Parameter %s of type %s must be a " \
                        "pointer to xfdata.FL_OBJECT." % \
                        (paramname, type(paramname)))


def verify_flformptr_type(paramname):
    """Check if paramname is a valid pointer to xfdata.FL_FORM."""
    if not isinstance(paramname, cty.POINTER(xfdata.FL_FORM)):
        raise XFormsTypeError("Parameter %s of type %s must be a " \
                        "pointer to xfdata.FL_FORM." % \
                        (paramname, type(paramname)))


def verify_flflimageptr_type(paramname):
    """Check if paramname is a valid pointer to xfdata.FL_IMAGE."""
    if not isinstance(paramname, cty.POINTER(xfdata.FL_IMAGE)):
        raise XFormsTypeError("Parameter %s of type %s must be a " \
                        "pointer to xfdata.FL_IMAGE." % \
                        (paramname, type(paramname)))


def verify_flflpopupptr_type(paramname):
    """Check if paramname is a valid pointer to xfdata.FL_POPUP."""
    if not isinstance(paramname, cty.POINTER(xfdata.FL_POPUP)):
        raise XFormsTypeError("Parameter %s of type %s must be a " \
                        "pointer to xfdata.FL_POPUP." % \
                        (paramname, type(paramname)))


def verify_flpopupentryptr_type(paramname):
    """Check if paramname is a valid pointer to xfdata.FL_POPUP_ENTRY."""
    if not isinstance(paramname, cty.POINTER(xfdata.FL_POPUP_ENTRY)):
        raise XFormsTypeError("Parameter %s of type %s must be a " \
                        "pointer to xfdata.FL_POPUP_ENTRY." % \
                        (paramname, type(paramname)))


def verify_flpopupreturnptr_type(paramname):
    """Check if paramname is a valid pointer to xfdata.FL_POPUP_RETURN."""
    if not isinstance(paramname, cty.POINTER(xfdata.FL_POPUP_RETURN)):
        raise XFormsTypeError("Parameter %s of type %s must be a " \
                        "pointer to xfdata.FL_POPUP_RETURN." % \
                        (paramname, type(paramname)))


def verify_flpopupitemptr_type(paramname):
    """Check if paramname is a valid pointer to xfdata.FL_POPUP_ITEM."""
    if not isinstance(paramname, cty.POINTER(xfdata.FL_POPUP_ITEM)):
        raise XFormsTypeError("Parameter %s of type %s must be a " \
                        "pointer to xfdata.FL_POPUP_ITEM." % \
                        (paramname, type(paramname)))


def verify_function_type(paramname):
    """ Check if paramname value is a valid python function to be passed as
    e.g. callback in a public function."""
    if not hasattr(paramname, '__call__'):
        raise XFormsTypeError("Parameter %s of type %s must be a " \
                        "python function." % (paramname, type(paramname)))


def verify_otherclassptr_type(paramname, pstructinst):
    """ Check if paramname value is a valid pointer to a provided 'Structure'
    class instance, different from previous classes."""
    if not isinstance(paramname, pstructinst):
        raise XFormsTypeError("Parameter %s of type %s must be a " \
                        "pointer to %s 'Structure' class instance." % \
                        (paramname, type(paramname), pstructinst))


def donothing_popupcb(pPopupReturn):
    """ It replaces a callback function not defined for class instances
    as e.g. xfdata.FL_POPUP_ITEM    *temporary* """
    return 0


def make_pPopupItem_from_dict(dictofpopupitems):
    """ make_pPopupItem_from_dict(dictofpopupitems) -> pPopupItem

    Taking a python dict (for one dict item ONLY) with a structure similar
    to xfdata.FL_POPUP_ITEM prepares and returns a C-compatible pointer
    to xfdata.FL_POPUP_ITEM. """
    if not isinstance(dictofpopupitems, dict):
        raise XFormsTypeError("Parameter must be a dict")
        return None, None

    pyclstext = dictofpopupitems['text']
    spitext = convert_to_string(pyclstext)
    pyclscallback = dictofpopupitems['callback']
    c_picallback = xfdata.FL_POPUP_CB(pyclscallback)
    pyclsshortcut = dictofpopupitems['shortcut']
    spishortcut = convert_to_string(pyclsshortcut)
    pyclstype = dictofpopupitems['type']
    check_admitted_value_in_list(pyclstype, xfdata.POPUPTYPE_list)
    ipitype = convert_to_int(pyclstype)
    pyclsstate = dictofpopupitems['state']
    check_admitted_value_in_list(pyclstype, xfdata.POPUPSTATE_list)
    ipistate = convert_to_int(pyclsstate)

    popupitem = (xfdata.FL_POPUP_ITEM * 2)()
    popupitem[0].text = spitext
    popupitem[0].callback = c_picallback
    popupitem[0].shortcut = spishortcut
    popupitem[0].type = ipitype
    popupitem[0].state = ipistate
    popupitem[1].text = None        # this ends array, preventing SegFault

    ppopupitem = cty.pointer(popupitem[0])
    keep_cfunc_refs(pyclscallback, c_picallback)
    keep_elem_refs(dictofpopupitems, pyclsshortcut, pyclstype,
                   pyclstext, spitext, pyclsshortcut,
                   spishortcut, pyclstype, ipitype, pyclsstate,
                   ipistate, popupitem, ppopupitem)
    return ppopupitem


def make_pPopupItem_from_list(listofpopupitems):
    """ make_pPopupItem_from_list(listofpopupitems) -> pPopupItem

    Taking a python single list/several lists of popup items, with
    elements in the same order as xfdata.FL_POPUP_ITEM prepares and
    returns a C-compatible pointer to xfdata.FL_POPUP_ITEM."""
    # hack to manage both single list and several lists passed as arguments
    try:
        tmpval = listofpopupitems[1][0]
        tmpval = tmpval

    except TypeError:
        # only one list passed (array of 2 member)
        popupitem = (xfdata.FL_POPUP_ITEM * 2)()   # 1 list and 1 None

        spitext = convert_to_string(listofpopupitems[0])
        popupitem[0].text = spitext
        c_picallback = xfdata.FL_POPUP_CB(listofpopupitems[1])
        popupitem[0].callback = c_picallback
        spishortcut = convert_to_string(listofpopupitems[2])
        popupitem[0].shortcut = spishortcut
        check_admitted_value_in_list(listofpopupitems[3], \
            xfdata.POPUPTYPE_list)
        ipitype = convert_to_int(listofpopupitems[3])
        popupitem[0].type = ipitype
        check_admitted_value_in_list(listofpopupitems[4], \
            xfdata.POPUPSTATE_list)
        ipistate = convert_to_int(listofpopupitems[4])
        popupitem[0].state = ipistate

        popupitem[1].text = None      # ends array, preventing SegFault

        keep_cfunc_refs(listofpopupitems[1], c_picallback)
        keep_elem_refs(popupitem, spitext, spishortcut,
                       ipitype, ipistate)

        ppopupitem = cty.pointer(popupitem[0])
        keep_elem_refs(listofpopupitems, popupitem, ppopupitem)
        return ppopupitem
        # end of 1 list

    else:
        # series of lists passed (array of n+1 members)
        numarray = len(listofpopupitems)
        lngarray = numarray + 1         # consider final None
        popupitem = (xfdata.FL_POPUP_ITEM * lngarray)()
        curitem = 0

        for indx in range(0, numarray):
            spitext = convert_to_string(listofpopupitems[indx][0])
            popupitem[indx].text = spitext
            c_picallback = xfdata.FL_POPUP_CB(listofpopupitems[indx][1])
            popupitem[indx].callback = c_picallback
            spishortcut = convert_to_string(listofpopupitems[indx][2])
            popupitem[indx].shortcut = spishortcut
            check_admitted_value_in_list(listofpopupitems[indx][3], \
                                      xfdata.POPUPTYPE_list)
            ipitype = convert_to_int(listofpopupitems[indx][3])
            popupitem[indx].type = ipitype
            check_admitted_value_in_list(listofpopupitems[indx][4], \
                                      xfdata.POPUPSTATE_list)
            ipistate = convert_to_int(listofpopupitems[indx][4])
            popupitem[indx].state = ipistate

            keep_cfunc_refs(listofpopupitems[indx][1], c_picallback)
            keep_elem_refs(popupitem[indx], spitext, spishortcut,
                           ipitype, ipistate)
            curitem = indx

        curitem += 1
        popupitem[curitem].text = None    # ends array, preventing SegFault
        ppopupitem = cty.pointer(popupitem[0])
        keep_elem_refs(listofpopupitems, popupitem, ppopupitem)
        return ppopupitem
        # end of series of lists
