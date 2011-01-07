#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" Convenience/internal functions to deal with xforms-python wrapper's
    functions.

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
# This file contains support private functions, that are not
# supposed to be used directly by users.
#######################################################################


import sys
import ctypes as cty
import ctypes.util as ctyutil
import warnings
from xformslib import vers
from xformslib import xfdata


class XFormsLoadError(OSError):
    """ Fatal error in loading shared flobject library """
    pass

class XFormsInitError(OSError):
    """ Fatal error in initializing library, not using fl_initialize()
        before functions who require it. """
    pass

class XFormsTypeError(TypeError):
    """ Fatal generic error for type mismatch """
    pass

class XFormsValueError(ValueError):
    """ Fatal generic error for unexpected value"""
    pass

class XFormsGenericError(OSError):
    """ Fatal generic error"""
    pass

class XFormsFuncNotSupported(ValueError):
    """ Fatal error for XForms functions not supported or not yet
        stabilized in xforms-python. """
    pass

class XFormsWarning(Warning):
    """ Generic warning for non fatal errors"""
    pass


def get_xforms_version():
    """ Returns version string of installed XForms library. """
    from xformslib.flbasic import fl_library_full_version
    try:
        fconsolver, ver, rev, fixlvl, extrafixlvl = \
                fl_library_full_version()
    except TypeError:           # not existing function
        complete_xf_version = ""
    else:
        complete_xf_version = "%s.%s.%s%s" % \
                (str(ver), str(rev), str(fixlvl), extrafixlvl)
    return complete_xf_version


header_filename = "/usr/include/forms.h"

def get_xforms_version_fallback():
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
                    "not installed properly: corrupted or incomplete?")
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
    if not xforms_vers:                 # no chance for direct version getter
        xforms_vers = get_xforms_version_fallback()
    if vers.__vers_against_xforms__ != xforms_vers:      # no match
        warningmsg = "xforms-python is implemented against XForms version " \
                "%s and does not match XForms installed version (%s)." \
                " Some compatibility problems may arise if XForms public" \
                " interface has been modified." % \
                (vers.__vers_against_xforms__, xforms_vers)
        warnings.warn(warningmsg, XFormsWarning)


def func_notexisting_placeholder(cfunction):
    """ Print a warning if called function does not exist """
    warningmsg = "C function %s does NOT exist, hence it is not wrappable" \
            " and callable in python and its call is ignored. Maybe " \
            "removed, disabled or not implemented yet?" % cfunction
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
            raise XFormsLoadError("XForms library toolkit (libformsGL.so)" \
                    " is not installed properly. Did you compile it" \
                    " without OpenGL support?")
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
        # function does not exist
        loadedfunc = func_notexisting_placeholder(cfuncname)
    else:
        loadedfunc.restype = retval
        loadedfunc.__doc__ = doc
        uniqueargslist = []
        for argelems in arglist:
            if isinstance(argelems, list):    # if an elem is a list itself
                for argsubelems in argelems:
                    uniqueargslist.append(argsubelems)
            else:
                uniqueargslist.append(argelems) # if it is not
        loadedfunc.argtypes = uniqueargslist

    return loadedfunc


flinitialized = False           # if fl_initialize() not called before

def check_if_initialized():
    """ Check if fl_initialize() has been called before caller function.
        Needed for most functions, except those supposed to be used
        *BEFORE* initialization or those freely useable. """
    if not flinitialized:       # fl_initialize() not called
        raise XFormsInitError("fl_initialize() should be called before " \
                "using this function.")

def set_initialized():
    """ fl_initialize() has been called """
    global flinitialized
    flinitialized = True


# functions to convert a parameter into a python type then into the
# equivalent ctypes type

def convert_to_stringc(paramname):
    """ Converts paramname to python str and to ctypes c_char_p """
    if sys.version_info[0] > 2:
        stringtype = str
    else:
        stringtype = basestring
    if isinstance(paramname, cty.c_char_p):
        return paramname
    elif isinstance(paramname, stringtype):
        retv = cty.c_char_p(paramname)
        return retv
    else:               # not a str / unicode str / c_char_p
        raise XFormsTypeError("Provided parameter '%s' has %s type, "
                "but a 'str'/'c_char_p' type should be used." % \
                (paramname, type(paramname)))


def convert_to_ptr_stringc(paramname):
    """ Converts paramname (list of str) to a ctypes pointer to c_char_p """
    if sys.version_info[0] > 2:
        stringtype = str
    else:
        stringtype = basestring
    if isinstance(paramname, list):     # list of str
        for idx in range(0, len(paramname)):
            if not isinstance(paramname[idx], stringtype):
                # every part must be a str
                raise XFormsTypeError("Provided parameter '%s' has %s type,"
                        " but a 'list of str'/'pointer to c_char_p' type"
                        " should be used." % (paramname, type(paramname)))
        retv = (cty.c_char_p * len(paramname))(*paramname)    # already a ptr
        return retv
    else:               # not a list
        raise XFormsTypeError("Provided parameter '%s' has %s type, "
                "but a 'list of str'/'array of c_char_p' type should "
                "be used." % (paramname, type(paramname)))


def convert_to_intc(paramname):
    """ Converts paramname to python int and to ctypes c_int """
    if not isinstance(paramname, cty.c_int):
        try:
            retv0 = int(paramname)
        except ValueError:
            raise XFormsTypeError("Provided parameter '%s' has %s type, "
                    "but an 'int'/'c_int' type should be used." % \
                    (paramname, type(paramname)))
        retv = cty.c_int(retv0)
        return retv
    else:
        return paramname

convert_to_FL_Coord = convert_to_intc


def convert_to_ptr_intc(paramname):
    """ Converts paramname (list of int) to a ctypes pointer to c_int """
    if sys.version_info[0] > 2:
        longtype = int
    else:
        longtype = (long, int)
    if isinstance(paramname, list):     # list of int
        for idx in range(0, len(paramname)):
            if not isinstance(paramname[idx], longtype):
                # every part must be an int/long
                raise XFormsTypeError("Provided parameter '%s' has %s type,"
                        " but a 'list of int'/'pointer to c_int' type"
                        " should be used." % (paramname, type(paramname)))
        retv = (cty.c_int * len(paramname))(*paramname)    # already a ptr
        return retv
    else:               # not a list
        raise XFormsTypeError("Provided parameter '%s' has %s type,"
                " but a 'list of int'/'pointer to c_int' type"
                " should be used." % (paramname, type(paramname)))


def convert_to_uintc(paramname):
    """ Converts paramname to python int and to ctypes c_uint """
    if not isinstance(paramname, cty.c_int):
        try:
            retv0 = int(paramname)
        except ValueError:
            raise XFormsTypeError("Provided parameter '%s' has %s type, "
                    "but an 'int_pos'/'c_uint' type should be used." % \
                    (paramname, type(paramname)))
        else:
            retv = cty.c_uint(retv0)
            return retv
    else:
        return paramname


def convert_to_shortc(paramname):
    """ Converts paramname to python int and to ctypes c_short """
    if not isinstance(paramname, cty.c_short):
        try:
            retv0 = int(paramname)
        except ValueError:
            raise XFormsTypeError("Provided parameter '%s' has %s type, "
                    "but an 'int'/'c_short' type should be used." % \
                    (paramname, type(paramname)))
        retv = cty.c_short(retv0)
        return retv
    else:
        return paramname


def convert_to_longc(paramname):
    """ Converts paramname to python long and to ctypes c_long """
    if sys.version_info[0] > 2:
        longtype = int
    else:
        longtype = long
    if not isinstance(paramname, cty.c_long):
        try:
            retv0 = longtype(paramname)
        except ValueError:
            raise XFormsTypeError("Provided parameter '%s' has %s type, "
                    "but a 'long'/'c_long' type should be used." % \
                    (paramname, type(paramname)))
        else:
            retv = cty.c_long(retv0)
            return retv
    else:
        return paramname


def convert_to_ulongc(paramname):
    """ Converts paramname to python long and to ctypes c_ulong """
    if sys.version_info[0] > 2:
        longtype = int
    else:
        longtype = long
    if not isinstance(paramname, cty.c_ulong):
        try:
            retv0 = longtype(paramname)
        except ValueError:
            raise XFormsTypeError("Provided parameter '%s' has %s type, "
                    "but a 'long_pos'/'c_ulong' type should be used." % \
                    (paramname, type(paramname)))
        else:
            retv = cty.c_ulong(retv0)
            return retv
    else:
        return paramname

convert_to_FL_COLOR = convert_to_ulongc
convert_to_Window = convert_to_ulongc
convert_to_Pixmap = convert_to_ulongc


def convert_to_ptr_ulongc(paramname):
    """ Converts paramname (list of long) to a ctypes pointer to c_ulong """
    if sys.version_info[0] > 2:
        longtype = int
    else:
        longtype = (long, int)
    if isinstance(paramname, list):     # list of long
        for idx in range(0, len(paramname)):
            if not isinstance(paramname[idx], longtype):
                # every part must be an int/long
                raise XFormsTypeError("Provided parameter '%s' has %s type,"
                        " but a 'list of long'/'pointer to c_ulong' type"
                        " should be used." % (paramname, type(paramname)))
        retv = (cty.c_ulong * len(paramname))(*paramname)    # already a ptr
        return retv
    else:               # not a list
        raise XFormsTypeError("Provided parameter '%s' has %s type,"
                " but a 'list of long'/'pointer to c_ulong' type"
                " should be used." % (paramname, type(paramname)))


def convert_to_doublec(paramname):
    """ Converts paramname to python float and to ctypes c_double """
    if not isinstance(paramname, cty.c_double):
        try:
            retv0 = float(paramname)
        except ValueError:
            raise XFormsTypeError("Provided parameter '%s' has %s type, "
                    "but a 'float'/'c_double' type should be used." % \
                    (paramname, type(paramname)))
        else:
            retv = cty.c_double(retv0)
            #print "double", paramname, retv0, retv
            return retv
    else:
        return paramname


def convert_to_ptr_doublec(paramname):
    """ Converts paramname (list of float) to a ctypes pointer to c_double """
    if isinstance(paramname, list):     # list of double
        for idx in range(0, len(paramname)):
            if not isinstance(paramname[idx], float):
                # every part must be a float
                raise XFormsTypeError("Provided parameter '%s' has %s type,"
                        " but a 'list of float'/'pointer to c_double' type"
                        " should be used." % (paramname, type(paramname)))
        retv = (cty.c_float * len(paramname))(*paramname)    # already a ptr
        return retv
    else:               # not a list
        raise XFormsTypeError("Provided parameter '%s' has %s type,"
                " but a 'list of float'/'pointer to c_double' type"
                " should be used." % (paramname, type(paramname)))


def convert_to_floatc(paramname):
    """ Converts paramname to python float and to ctypes c_float """
    if not isinstance(paramname, cty.c_float):
        try:
            retv0 = float(paramname)
        except ValueError:
            raise XFormsTypeError("Provided parameter '%s' has %s type, "
                    "but a 'float'/'c_float' type should be used." % \
                    (paramname, type(paramname)))
        else:
            retv = cty.c_float(retv0)
            #print "float", paramname, retv0, retv
            return retv
    else:
        return paramname


def convert_to_ptr_floatc(paramname):
    """ Converts paramname (list of float) to a ctypes pointer to c_float """
    if isinstance(paramname, list):     # list of float
        for idx in range(0, len(paramname)):
            if not isinstance(paramname[idx], float):
                # every part must be a float
                raise XFormsTypeError("Provided parameter '%s' has %s type,"
                        " but a 'list of float'/'pointer to c_float' type"
                        " should be used." % (paramname, type(paramname)))
        retv = (cty.c_float * len(paramname))(*paramname)    # already a ptr
        return retv
    else:               # not a list
        raise XFormsTypeError("Provided parameter '%s' has %s type,"
                " but a 'list of float'/'pointer to c_float' type"
                " should be used." % (paramname, type(paramname)))


def convert_to_ubytec_array(paramname):
    """ Converts paramname to a ctypes c_ubyte array"""
    if isinstance(paramname, list):     # list of int
        lenparam = len(paramname)
        retv = (cty.c_ubyte * lenparam)()      # it's already a pointer
        for n in range(0, lenparam-1):
            retv[n] = paramname[n]
        return retv
    else:               # not a list
        raise XFormsTypeError("Provided parameter '%s' has %s type, "
                "but a 'list of int'/'c_ubyte' type should be used." % \
                (paramname, type(paramname)))


def make_intc_and_pointer():
    """ Makes a ctypes c_int and its pointer, and returns both """
    baseval = cty.c_int()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval

make_FL_Coord_and_pointer = make_intc_and_pointer


def make_uintc_and_pointer():
    """ Makes a ctypes c_uint and its pointer, and returns both """
    baseval = cty.c_uint()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval


def make_longc_and_pointer():
    """ Makes a ctypes c_long and its pointer, and returns both """
    baseval = cty.c_long()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval


def make_ulongc_and_pointer():
    """ Makes a ctypes c_ulong and its pointer, and returns both """
    baseval = cty.c_ulong()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval

make_Pixmap_and_pointer = make_ulongc_and_pointer
make_FL_COLOR_and_pointer = make_ulongc_and_pointer


def make_floatc_and_pointer():
    """ Makes a ctypes c_float and its pointer, and returns both """
    baseval = cty.c_float()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval


def make_doublec_and_pointer():
    """ Makes a ctypes c_double and its pointer, and returns both """
    baseval = cty.c_double()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval


def make_ubytec_and_pointer():
    """ Makes a ctypes c_ubyte and its pointer, and returns both """
    baseval = cty.c_ubyte()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval


def make_ushortc_and_pointer():
    """ Makes a ctypes c_ushort and its pointer, and returns both """
    baseval = cty.c_ushort()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval


def make_stringc_and_pointer():
    """ Makes a ctypes c_char_p and its pointer, and returns both """
    baseval = cty.c_char_p()
    ptrbaseval = cty.byref(baseval)
    return baseval, ptrbaseval


def checkfatal_allowed_value_in_list(paramname, valueslist):
    """ Checks if paramname value is valid in accordance to a list or tuple
        of admissible values, otherwise raises a fatal error."""
    if isinstance(valueslist, (list, tuple)):
        if paramname not in valueslist:
            raise XFormsValueError("Parameter %s value (whose type is %s)"
                    " should be one of those included in list/tuple %s." % \
                    (paramname, type(paramname), valueslist))

def checknonfatal_allowed_value_in_list(paramname, valueslist):
    """ Checks if paramname value is valid in accordance to a list or tuple
        of admissible values, otherwise issues a warning."""
    if isinstance(valueslist, (list, tuple)):
        if paramname not in valueslist:
            nonfatalwarnmsg = "Parameter %s value (whose type is %s) is" \
                    " not one of those included in list/tuple %s." % \
                    (paramname, type(paramname), valueslist)
            warnings.warn(nonfatalwarnmsg, XFormsWarning, 3)

# TODO: verify where can be used
#def check_param_length(paramname, predeflen):
#    """ Checks if paramname's length equals to a predefined length,
#        otherwise raises a fatal error."""
#    paramlen = len(paramname)
#    if paramlen != predeflen:
#        raise XFormsValueError("Length of parameter %s is %d, but it should"
#	         " be %d, in accordance to other parameters in called "
#		 "function." % (paramname, paramlen, predeflen))

def verify_tuplelist_type(paramname):
    """Checks if paramname is a valid list or tuple."""
    if not isinstance(paramname, (list, tuple)):
        raise XFormsTypeError("Provided parameter %s has %s type, but " \
                " a list or a tuple type should be used." % \
                (paramname, type(paramname)))
    else:
        return True


def verify_flobjectptr_type(paramname):
    """Checks if paramname is a valid pointer to xfdata.FL_OBJECT."""
    if not isinstance(paramname, cty.POINTER(xfdata.FL_OBJECT)):
        raise XFormsTypeError("Provided parameter %s has %s type, but " \
                "a pointer to xfdata.FL_OBJECT type should be used." % \
                (paramname, type(paramname)))


def verify_flformptr_type(paramname):
    """Checks if paramname is a valid pointer to xfdata.FL_FORM."""
    if not isinstance(paramname, cty.POINTER(xfdata.FL_FORM)):
        raise XFormsTypeError("Provided parameter %s has %s type, but " \
                "a pointer to xfdata.FL_FORM type should be used." % \
                (paramname, type(paramname)))


def verify_flflimageptr_type(paramname):
    """Checks if paramname is a valid pointer to xfdata.FL_IMAGE."""
    if not isinstance(paramname, cty.POINTER(xfdata.FL_IMAGE)):
        raise XFormsTypeError("Provided parameter %s has %s type, but " \
                "a pointer to xfdata.FL_IMAGE type should be used." % \
                (paramname, type(paramname)))


def verify_flpopupptr_type(paramname):
    """Checks if paramname is a valid pointer to xfdata.FL_POPUP."""
    if not isinstance(paramname, cty.POINTER(xfdata.FL_POPUP)):
        raise XFormsTypeError("Provided parameter %s has %s type, but " \
                "a pointer to xfdata.FL_POPUP type should be used." % \
                (paramname, type(paramname)))


def verify_flpopupentryptr_type(paramname):
    """Checks if paramname is a valid pointer to xfdata.FL_POPUP_ENTRY."""
    if not isinstance(paramname, cty.POINTER(xfdata.FL_POPUP_ENTRY)):
        raise XFormsTypeError("Provided parameter %s has %s type, but " \
                "a pointer to xfdata.FL_POPUP_ENTRY type should be used." % \
                (paramname, type(paramname)))


def verify_flpopupreturnptr_type(paramname):
    """Checks if paramname is a valid pointer to xfdata.FL_POPUP_RETURN."""
    if not isinstance(paramname, cty.POINTER(xfdata.FL_POPUP_RETURN)):
        raise XFormsTypeError("Provided parameter %s has %s type, but " \
                "a pointer to xfdata.FL_POPUP_RETURN type should be used." % \
                (paramname, type(paramname)))


def verify_flpopupitemptr_type(paramname):
    """Checks if paramname is a valid pointer to xfdata.FL_POPUP_ITEM."""
    if not isinstance(paramname, cty.POINTER(xfdata.FL_POPUP_ITEM)):
        raise XFormsTypeError("Provided parameter %s has %s type, but " \
                "a pointer to xfdata.FL_POPUP_ITEM type should be used." % \
                (paramname, type(paramname)))


def verify_function_type(paramname):
    """ Checks if paramname value is a valid python function to be passed as
    e.g. callback in a public function."""
    if not hasattr(paramname, '__call__'):
        raise XFormsTypeError("Provided parameter %s has %s type, but " \
                "a python function type should be used." % \
                (paramname, type(paramname)))


def verify_otherclassptr_type(paramname, pstructinst):
    """ Checks if paramname value is a valid pointer to a provided 'Structure'
    class instance, different from previous classes."""
    if not isinstance(paramname, pstructinst):
        raise XFormsTypeError("Provided parameter %s has %s type, but " \
                "a pointer to %s 'Structure' class instance should be " \
                "used." %  (paramname, type(paramname), pstructinst))

