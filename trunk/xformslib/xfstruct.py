#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" Support functions to deal with xforms-python wrapper's functions.
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

#######################################################################
# This file contains support functions to manage Structures contained
# in xfdata who can be passed directly to a function..
#######################################################################


import os
import ctypes as cty
from xformslib import xfdata
from xformslib import library


def fls_make_ptr_flpopupitem(dictpopupitems):
    """fls_make_ptr_flpopupitem(dictpopupitems) -> ptr_flpopupitem

    Taking a python dict (for one dict item) or a python list of dicts (for
    more than one dict item) with keys corresponding to xfdata.FL_POPUP_ITEM
    attributes, prepares and returns a C-compatible pointer to
    xfdata.FL_POPUP_ITEM. Keys are: 'text', 'callback', 'shortcut', 'type'
    and 'state'."""

    # one dict
    if isinstance(dictpopupitems, dict):

        if not 'text' in dictpopupitems:      # no text passed
            raise library.XFormsTypeError("fls_make_ptr_flpopupitem dict (" \
                    "whose contents is %s) should have a 'text' key" % \
                    dictpopupitems)
        else:
            pyclstext = dictpopupitems['text']
            s_clstext = library.convert_to_stringc(pyclstext)

        if not 'callback' in dictpopupitems:  # no callback passed
            pyclscallback = donothing_flpopupcb
        else:
            pyclscallback = dictpopupitems['callback']
        cfn_clscallback = xfdata.FL_POPUP_CB(pyclscallback)

        if not 'shortcut' in dictpopupitems:    # no shortcut passed
            raise library.XFormsTypeError("make_ptr_flpopupitem dict (whose "
                    "contents is %s) should have a 'shortcut' key" % \
                    dictpopupitems)
        else:
            pyclsshortcut = dictpopupitems['shortcut']
            s_clsshortcut = library.convert_to_stringc(pyclsshortcut)

        if not 'type' in dictpopupitems:    # no type passed
            pyclstype = xfdata.FL_POPUP_NORMAL
        else:
            pyclstype = dictpopupitems['type']
        library.checkfatal_allowed_value_in_list(pyclstype, \
                xfdata.POPUPTYPE_list)
        i_clstype = library.convert_to_intc(pyclstype)

        if not 'state' in dictpopupitems:    # no state passed
            pyclsstate = xfdata.FL_POPUP_NONE
        else:
            pyclsstate = dictpopupitems['state']
        library.checkfatal_allowed_value_in_list(pyclsstate, \
                xfdata.POPUPSTATE_list)
        i_clsstate = library.convert_to_intc(pyclsstate)

        popupitem = (xfdata.FL_POPUP_ITEM * 2)()
        popupitem[0].text = s_clstext
        popupitem[0].callback = cfn_clscallback
        popupitem[0].shortcut = s_clsshortcut
        popupitem[0].type = i_clstype
        popupitem[0].state = i_clsstate
        popupitem[1].text = None    # this ends array, preventing SegFault

        ptr_popupitem = cty.pointer(popupitem[0])
        library.keep_cfunc_refs(pyclscallback, cfn_clscallback)
        library.keep_elem_refs(dictpopupitems, pyclstext, s_clstext, \
                pyclsshortcut, s_clsshortcut, pyclstype, i_clstype, \
                pyclsstate, i_clsstate, popupitem, ptr_popupitem)
        return ptr_popupitem

    # more dicts
    elif isinstance(dictpopupitems, list):

        dictlength = len(dictpopupitems)
        popupitem = (xfdata.FL_POPUP_ITEM * (dictlength+1))()
        pyclstext = s_clstext = [" "] * dictlength
        pyclscallback = cfn_clscallback = [None] * dictlength
        pyclsshortcut = s_clsshortcut = [" "] * dictlength
        pyclstype = i_clstype = [0] * dictlength
        pyclsstate = i_clsstate = [0] * dictlength

        for numb in range(0, dictlength):
            if not 'text' in dictpopupitems[numb]:      # no text passed
                raise library.XFormsTypeError("fls_make_ptr_flpopupitem " \
                        "dict (whose contents is %s) should have a 'text'" \
                        " key" % dictpopupitems[numb])
            else:
                pyclstext[numb] = dictpopupitems[numb]['text']
                s_clstext[numb] = library.convert_to_stringc(pyclstext[numb])
            if not 'callback' in dictpopupitems[numb]:
                pyclscallback[numb] = donothing_flpopupcb
            else:                       # no callback passed
                pyclscallback[numb] = dictpopupitems[numb]['callback']
                cfn_clscallback[numb] = xfdata.FL_POPUP_CB(pyclscallback[numb])
            if not 'shortcut' in dictpopupitems[numb]:  # no shortcut passed
                raise library.XFormsTypeError("fls_make_ptr_flpopupitem " \
                        "dict (whose contents is %s) should have a " \
                        "'shortcut' key" % dictpopupitems[numb])
            else:
                pyclsshortcut[numb] = dictpopupitems[numb]['shortcut']
                s_clsshortcut[numb] = library.convert_to_stringc( \
                        pyclsshortcut[numb])
            if not 'type' in dictpopupitems[numb]:    # no type passed
                pyclstype[numb] = xfdata.FL_POPUP_NORMAL
            else:
                pyclstype[numb] = dictpopupitems[numb]['type']
            library.checkfatal_allowed_value_in_list(pyclstype[numb], \
                    xfdata.POPUPTYPE_list)
            i_clstype[numb] = library.convert_to_intc(pyclstype[numb])
            if not 'state' in dictpopupitems[numb]:    # no state passed
                pyclsstate[numb] = xfdata.FL_POPUP_NONE
            else:
                pyclsstate[numb] = dictpopupitems[numb]['state']
            library.checkfatal_allowed_value_in_list(pyclsstate[numb], \
                    xfdata.POPUPSTATE_list)
            i_clsstate[numb] = library.convert_to_intc(pyclsstate[numb])

            popupitem[numb].text = s_clstext[numb]
            popupitem[numb].callback = cfn_clscallback[numb]
            popupitem[numb].shortcut = s_clsshortcut[numb]
            popupitem[numb].type = i_clstype[numb]
            popupitem[numb].state = i_clsstate[numb]

            library.keep_cfunc_refs(pyclscallback[numb], cfn_clscallback[numb])
            library.keep_elem_refs(pyclstext[numb], s_clstext[numb], \
                pyclsshortcut[numb], s_clsshortcut[numb], pyclstype[numb], \
                i_clstype[numb], pyclsstate[numb], i_clsstate[numb],)

        popupitem[-1].text = None    # this ends array, preventing SegFault

        ptr_popupitem = cty.pointer(popupitem[0])
        library.keep_elem_refs(dictpopupitems, popupitem, ptr_popupitem)

        return ptr_popupitem

    else:
        raise library.XFormsTypeError("Parameter %s (of type %s) must be a " \
                "python dict or a python list of dicts" % \
                (dictpopupitems, type(dictpopupitems)))


def fls_make_ptr_fliopt(dictfliopt):
    """fls_make_ptr_fliopt(dictfliopt) -> ptr_fliopt

    Taking a python dict (for one dict item) with keys corresponding to
    xfdata.FL_IOPT elements prepares and returns a C-compatible pointer
    to xfdata.FL_IOPT. Not all elements have necessarily to be passed.
    Keys are: 'rgamma', 'ggamma', 'bgamma', 'debug', 'sync', 'depth',
    'vclass', 'doubleBuffer', 'ulPropWidth', 'ulThickness', 'buttonFontSize',
    'sliderFontSize', 'inputFontSize', 'browserFontSize', 'menuFontSize',
    'choiceFontSize', 'labelFontSize', 'pupFontSize', 'privateColormap',
    'sharedColormap', 'standardColormap', 'scrollbarType', 'backingStore',
    'coordUnit', 'borderWidth', 'safe', 'rgbfile', 'vname'."""

    # one dict
    if isinstance(dictfliopt, dict):

        pyrgamma = f_rgamma = pyggamma = f_ggamma = pybgamma = f_bgamma = 0.0
        pydebug = i_debug = pysync = i_sync = pydepth = i_depth = pyvclass = 0
        i_vclass = pydoubleBuffer = i_doubleBuffer = pyulPropWidth = 0
        i_ulPropWidth = pyulThickness = i_ulThickness = pybuttonFontSize = 0
        i_buttonFontSize = pysliderFontSize = i_sliderFontSize = 0
        pyinputFontSize = i_inputFontSize = pybrowserFontSize = 0
        i_browserFontSize = pymenuFontSize = i_menuFontSize = 0
        pychoiceFontSize = i_choiceFontSize = pylabelFontSize = 0
        i_labelFontSize = pypupFontSize = i_pupFontSize = pyprivateColormap = 0
        i_privateColormap = pysharedColormap = i_sharedColormap = 0
        pystandardColormap = i_standardColormap = pyscrollbarType = 0
        i_scrollbarType = pybackingStore = i_backingStore = pycoordUnit = 0
        i_coordUnit = pyborderWidth = i_borderWidth = pysafe = i_safe = 0
        pyrgbfile = s_rgbfile = pyvname = s_vname = ""

        fliopt = xfdata.FL_IOPT()

        if 'rgamma' in dictfliopt:
            pyrgamma = dictfliopt['rgamma']
            f_rgamma = library.convert_to_floatc(pyrgamma)
            fliopt[0].rgamma = f_rgamma
        if 'ggamma' in dictfliopt:
            pyggamma = dictfliopt['ggamma']
            f_ggamma = library.convert_to_floatc(pyggamma)
            fliopt[0].ggamma = f_ggamma
        if 'bgamma' in dictfliopt:
            pybgamma = dictfliopt['bgamma']
            f_bgamma = library.convert_to_floatc(pybgamma)
            fliopt[0].bgamma = f_bgamma
        if 'debug' in dictfliopt:
            pydebug = dictfliopt['debug']
            i_debug = library.convert_to_intc(pydebug)
            fliopt[0].debug = i_debug
        if 'sync' in dictfliopt:
            pysync = dictfliopt['sync']
            i_sync = library.convert_to_intc(pysync)
            fliopt[0].sync = i_sync
        if 'depth' in dictfliopt:
            pydepth = dictfliopt['depth']
            i_depth = library.convert_to_intc(pydepth)
            fliopt[0].depth = i_depth
        if 'vclass' in dictfliopt:
            pyvclass = dictfliopt['vclass']
            i_vclass = library.convert_to_intc(pyvclass)
            fliopt[0].vclass = i_vclass
        if 'doubleBuffer' in dictfliopt:
            pydoubleBuffer = dictfliopt['doubleBuffer']
            i_doubleBuffer = library.convert_to_intc(pydoubleBuffer)
            fliopt[0].doubleBuffer = i_doubleBuffer
        if 'ulPropWidth' in dictfliopt:
            pyulPropWidth = dictfliopt['ulPropWidth']
            i_ulPropWidth = library.convert_to_intc(pyulPropWidth)
            fliopt[0].ulPropWidth = i_ulPropWidth
        if 'ulThickness' in dictfliopt:
            pyulThickness = dictfliopt['ulThickness']
            i_ulThickness = library.convert_to_intc(pyulThickness)
            fliopt[0].ulThickness = i_ulThickness
        if 'buttonFontSize' in dictfliopt:
            pybuttonFontSize = dictfliopt['buttonFontSize']
            i_buttonFontSize = library.convert_to_intc(pybuttonFontSize)
            fliopt[0].buttonFontSize = i_buttonFontSize
        if 'sliderFontSize' in dictfliopt:
            pysliderFontSize = dictfliopt['sliderFontSize']
            i_sliderFontSize = library.convert_to_intc(pysliderFontSize)
            fliopt[0].sliderFontSize = i_sliderFontSize
        if 'inputFontSize' in dictfliopt:
            pyinputFontSize = dictfliopt['inputFontSize']
            i_inputFontSize = library.convert_to_intc(pyinputFontSize)
            fliopt[0].inputFontSize = i_inputFontSize
        if 'browserFontSize' in dictfliopt:
            pybrowserFontSize = dictfliopt['browserFontSize']
            i_browserFontSize = library.convert_to_intc(pybrowserFontSize)
            fliopt[0].browserFontSize = i_browserFontSize
        if 'menuFontSize' in dictfliopt:
            pymenuFontSize = dictfliopt['menuFontSize']
            i_menuFontSize = library.convert_to_intc(pymenuFontSize)
            fliopt[0].menuFontSize = i_menuFontSize
        if 'choiceFontSize' in dictfliopt:
            pychoiceFontSize = dictfliopt['choiceFontSize']
            i_choiceFontSize = library.convert_to_intc(pychoiceFontSize)
            fliopt[0].choiceFontSize = i_choiceFontSize
        if 'labelFontSize' in dictfliopt:
            pylabelFontSize = dictfliopt['labelFontSize']
            i_labelFontSize = library.convert_to_intc(pylabelFontSize)
            fliopt[0].labelFontSize = i_labelFontSize
        if 'pupFontSize' in dictfliopt:
            pypupFontSize = dictfliopt['pupFontSize']
            i_pupFontSize = library.convert_to_intc(pypupFontSize)
            fliopt[0].pupFontSize = i_pupFontSize
        if 'privateColormap' in dictfliopt:
            pyprivateColormap = dictfliopt['privateColormap']
            i_privateColormap = library.convert_to_intc(pyprivateColormap)
            fliopt[0].privateColormap = i_privateColormap
        if 'sharedColormap' in dictfliopt:
            pysharedColormap = dictfliopt['sharedColormap']
            i_sharedColormap = library.convert_to_intc(pysharedColormap)
            fliopt[0].sharedColormap = i_sharedColormap
        if 'standardColormap' in dictfliopt:
            pystandardColormap = dictfliopt['standardColormap']
            i_standardColormap = library.convert_to_intc(pystandardColormap)
            fliopt[0].standardColormap = i_standardColormap
        if 'scrollbarType' in dictfliopt:
            pyscrollbarType = dictfliopt['scrollbarType']
            i_scrollbarType = library.convert_to_intc(pyscrollbarType)
            fliopt[0].scrollbarType = i_scrollbarType
        if 'backingStore' in dictfliopt:
            pybackingStore = dictfliopt['backingStore']
            i_backingStore = library.convert_to_intc(pybackingStore)
            fliopt[0].backingStore = i_backingStore
        if 'coordUnit' in dictfliopt:
            pycoordUnit = dictfliopt['coordUnit']
            i_coordUnit = library.convert_to_intc(pycoordUnit)
            fliopt[0].coordUnit = i_coordUnit
        if 'borderWidth' in dictfliopt:
            pyborderWidth = dictfliopt['borderWidth']
            i_borderWidth = library.convert_to_intc(pyborderWidth)
            fliopt[0].borderWidth = i_borderWidth
        if 'safe' in dictfliopt:
            pysafe = dictfliopt['safe']
            i_safe = library.convert_to_intc(pysafe)
            fliopt[0].safe = i_safe
        if 'rgbfile' in dictfliopt:
            pyrgbfile = dictfliopt['rgbfile']
            s_rgbfile = library.convert_to_stringc(pyrgbfile)
            fliopt[0].rgbfile = s_rgbfile
        if 'vname' in dictfliopt:
            pyvname = dictfliopt['vname']
            s_vname = library.convert_to_stringc(pyvname)
            fliopt[0].vname = s_vname

        ptr_fliopt = cty.pointer(fliopt[0])
        library.keep_elem_refs(dictfliopt, fliopt, ptr_fliopt, pyrgamma, \
                f_rgamma, pyggamma, f_ggamma, pybgamma, f_bgamma, pydebug, \
                i_debug, pysync, i_sync, pydepth, i_depth, pyvclass, \
                i_vclass, pydoubleBuffer, i_doubleBuffer, pyulPropWidth, \
                i_ulPropWidth, pyulThickness, i_ulThickness, \
                pybuttonFontSize, i_buttonFontSize, pysliderFontSize, \
                i_sliderFontSize, pyinputFontSize, i_inputFontSize, \
                pybrowserFontSize, i_browserFontSize, pymenuFontSize, \
                i_menuFontSize, pychoiceFontSize, i_choiceFontSize, \
                pylabelFontSize, i_labelFontSize, pypupFontSize, \
                i_pupFontSize, pyprivateColormap, i_privateColormap, \
                pysharedColormap, i_sharedColormap, pystandardColormap, \
                i_standardColormap, pyscrollbarType, i_scrollbarType, \
                pybackingStore, i_backingStore, pycoordUnit, i_coordUnit, \
                pyborderWidth, i_borderWidth, pysafe, i_safe, pyrgbfile, \
                s_rgbfile, pyvname, s_vname)
        return ptr_fliopt

    else:
        raise library.XFormsTypeError("Parameter %s (of type %s) must be a " \
                "python dict" % (dictfliopt, type(dictfliopt)))


def fls_make_ptr_flcmdopt(dictflcmdopt):
    """fls_make_ptr_flcmdopt(dictflcmdopt) -> ptr_flcmdopt

    Taking a python dict (for one dict item) or a list of dicts (for more
    than one dict item) with keys corresponding to xfdata.FL_CMD_OPT
    attributes, prepares and returns a C-compatible pointer to
    xfdata.FL_CMD_OPT. Keys are: 'option', 'specifier', 'argKind',
    'value'."""

    # one dict
    if isinstance(dictflcmdopt, dict):

        if not 'option' in dictflcmdopt:      # no option passed
            raise library.XFormsTypeError("fls_make_ptr_flcmdopt dict (" \
                    "whose contents is %s) should have a 'option' key" % \
                    dictflcmdopt)
        else:
            pyoption = dictflcmdopt['option']
            s_option = library.convert_to_stringc(pyoption)

        if not 'specifier' in dictflcmdopt:   # no specifier passed
            raise library.XFormsTypeError("fls_make_ptr_flcmdopt dict (" \
                    "whose contents is %s) should have a 'specifier' " \
                    "key" % dictflcmdopt)
        else:
            pyspecifier = dictflcmdopt['specifier']
            s_specifier = library.convert_to_stringc(pyspecifier)

        if not 'argKind' in dictflcmdopt:     # no argKind passed
            raise library.XFormsTypeError("fls_make_ptr_flcmdopt dict (" \
                    "whose contents is %s) should have a 'argKind' " \
                    "key" % dictflcmdopt)
        else:
            pyargKind = dictflcmdopt['argKind']
            i_argKind = library.convert_to_intc(pyargKind)

        if not 'value' in dictflcmdopt:       # no value passed
            raise library.XFormsTypeError("fls_make_ptr_flcmdopt dict (" \
                    "whose contents is %s) should have a 'value' key" % \
                    dictflcmdopt)
        else:
            pyvalue = dictflcmdopt['value']
            s_value = library.convert_to_stringc(pyvalue)

        flcmdopt = xfdata.FL_CMD_OPT()      # * 2)()
        flcmdopt.option = s_option
        flcmdopt.specifier = s_specifier
        flcmdopt.argKind = i_argKind
        flcmdopt.value = s_value
        #flcmdopt[1].option = None    # this ends array, preventing SegFault

        ptr_flcmdopt = cty.pointer(flcmdopt)
        library.keep_elem_refs(dictflcmdopt, flcmdopt, ptr_flcmdopt, \
                pyoption, s_option, pyspecifier, s_specifier, pyargKind, \
                i_argKind, pyvalue, s_value)
        return ptr_flcmdopt

    # more dicts
    elif isinstance(dictflcmdopt, list):

        dictlength = len(dictflcmdopt)
        flcmdopt = (xfdata.FL_CMD_OPT * (dictlength))()       # dict+1
        pyoption = s_option = [" "] * dictlength
        pyspecifier = s_specifier = [" "] * dictlength
        pyargKind = i_argKind = [0] * dictlength
        pyvalue = s_value = [" "] * dictlength

        for numb in range(0, dictlength):

            if not 'option' in dictflcmdopt[numb]:      # no option passed
                raise library.XFormsTypeError("fls_make_ptr_flcmdopt " \
                        "dict (whose contents is %s) should have a " \
                        "'option' key" % dictflcmdopt[numb])
            else:
                pyoption[numb] = dictflcmdopt[numb]['option']
                s_option[numb] = library.convert_to_stringc(pyoption[numb])
            if not 'specifier' in dictflcmdopt[numb]:   # no specifier passed
                raise library.XFormsTypeError("fls_make_ptr_flcmdopt " \
                        "dict (whose contents is %s) should have a " \
                        "'specifier' key" % dictflcmdopt[numb])
            else:
                pyspecifier[numb] = dictflcmdopt[numb]['specifier']
                s_specifier[numb] = library.convert_to_stringc( \
                        pyspecifier[numb])
            if not 'argKind' in dictflcmdopt[numb]:     # no argKind passed
                raise library.XFormsTypeError("fls_make_ptr_flcmdopt dict " \
                        "whose contents is %s) should have a 'argKind' " \
                        "key" % dictflcmdopt[numb])
            else:
                pyargKind[numb] = dictflcmdopt[numb]['argKind']
                i_argKind[numb] = library.convert_to_intc(pyargKind[numb])
            if not 'value' in dictflcmdopt[numb]:       # no value passed
                raise library.XFormsTypeError("fls_make_ptr_flcmdopt dict " \
                        "(whose contents is %s) should have a 'value' " \
                        "key" % dictflcmdopt[numb])
            else:
                pyvalue[numb] = dictflcmdopt[numb]['value']
                s_value[numb] = library.convert_to_stringc(pyvalue[numb])

            flcmdopt[numb].option = s_option[numb]
            flcmdopt[numb].specifier = s_specifier[numb]
            flcmdopt[numb].argKind = i_argKind[numb]
            flcmdopt[numb].value = s_value[numb]

            library.keep_elem_refs(dictflcmdopt[numb], flcmdopt[numb], \
                    pyoption[numb], s_option[numb], pyspecifier[numb], \
                    s_specifier[numb], pyargKind[numb], i_argKind[numb], \
                    pyvalue[numb], s_value[numb])

        #flcmdopt[-1].option = ""    # this ends array, preventing SegFault

        ptr_flcmdopt = cty.pointer(flcmdopt[0])
        library.keep_elem_refs(dictflcmdopt, ptr_flcmdopt)
        return ptr_flcmdopt

    else:
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " a python dict or a list of dicts" % \
                (dictflcmdopt, type(dictflcmdopt)))


def fls_make_ptr_flresource(dictflresource):
    """fls_make_ptr_flresource(dictflresource) -> ptr_flresource

    Taking a python dict (for one dict item) or a list of dicts (for more
    than one dict item) with keys corresponding to xfdata.FL_RESOURCE
    attributes prepares and returns a C-compatible pointer to
    xfdata.FL_RESOURCE. Keys are: 'res_name', 'res_class', 'type', 'var',
    'defval', 'nbytes'."""

    # one dict
    if isinstance(dictflresource, dict):

        if not 'res_name' in dictflresource:      # no res_name passed
            raise library.XFormsTypeError("fls_make_ptr_flresource dict (" \
                    "whose contents is %s) should have a 'res_name' key" % \
                    dictflresource)
        else:
            pyclsresname = dictflresource['res_name']
            s_clsresname = library.convert_to_stringc(pyclsresname)
        if not 'res_class' in dictflresource:   # no res_class passed
            raise library.XFormsTypeError("fls_make_ptr_flresource dict (" \
                    "whose contents is %s) should have a 'res_class' key" % \
                    dictflresource)
        else:
            pyclsresclass = dictflresource['res_class']
            s_clsresclass = library.convert_to_stringc(pyclsresclass)
        if not 'type' in dictflresource:     # no type passed
            raise library.XFormsTypeError("fls_make_ptr_flresource dict (" \
                    "whose contents is %s) should have a 'type' key" % \
                    dictflresource)
        else:
            pyclstype = dictflresource['type']
            i_clstype = library.convert_to_intc(pyclstype)
        if not 'var' in dictflresource:       # no var passed
            raise library.XFormsTypeError("fls_make_ptr_flresource dict (" \
                    "whose contents is %s) should have a 'var' key" % \
                    dictflresource)
        else:
            pyclsvar = dictflresource['var']
            # managing different C types
            if i_clstype.value == xfdata.FL_SHORT:
                tmpclsvar = library.convert_to_shortc(pyclsvar)
            elif i_clstype.value == xfdata.FL_BOOL or \
                    i_clstype.value == xfdata.FL_INT:
                tmpclsvar = library.convert_to_intc(pyclsvar)
            elif i_clstype.value == xfdata.FL_LONG:
                tmpclsvar = library.convert_to_longc(pyclsvar)
            elif i_clstype.value == xfdata.FL_FLOAT:
                tmpclsvar = library.convert_to_floatc(pyclsvar)
            elif i_clstype.value == xfdata.FL_STRING:
                tmpclsvar = library.convert_to_stringc(pyclsvar)
            else:
                tmpclsvar = None
            ptr_clsvar = cty.pointer(tmpclsvar)
        if not 'defval' in dictflresource:   # no defval passed
            raise library.XFormsTypeError("fls_make_ptr_flresource dict (" \
                    "whose contents is %s) should have a 'defval' key" % \
                    dictflresource)
        else:
            pyclsdefval = dictflresource['defval']
            s_clsdefval = library.convert_to_stringc(pyclsdefval)
        if not 'nbytes' in dictflresource:     # no nbytes passed
            raise library.XFormsTypeError("fls_make_ptr_flresource dict (" \
                    "whose contents is %s) should have a 'nbytes' key" % \
                    dictflresource)
        else:
            pyclsnbytes = dictflresource['nbytes']
            i_clsnbytes = library.convert_to_intc(pyclsnbytes)

        structflresource = xfdata.FL_RESOURCE()      # * 2)()
        structflresource.res_name = s_clsresname
        structflresource.res_class = s_clsresclass
        structflresource.type = i_clstype
        structflresource.var = cty.cast(ptr_clsvar, cty.c_void_p)
        structflresource.defval = s_clsdefval
        structflresource.nbytes = i_clsnbytes

        #structflresource[1].text = None  # ends array, preventing SegFault

        ptr_flresource = cty.pointer(structflresource)
        library.keep_elem_refs(dictflresource, structflresource, \
                ptr_flresource, pyclsresname, s_clsresname, pyclsresclass, \
                s_clsresclass, pyclstype, i_clstype, pyclsvar, ptr_clsvar, \
                pyclsdefval, s_clsdefval, pyclsnbytes, i_clsnbytes)
        return ptr_flresource

    # more dicts
    elif isinstance(dictflresource, list):

        dictlength = len(dictflresource)
        structflresource = (xfdata.FL_RESOURCE * dictlength)()  # +1
        pyclsresname = s_clsresname = [" "] * dictlength
        pyclsresclass = s_clsresclass = [" "] * dictlength
        pyclstype = i_clstype = [0] * dictlength
        pyclsvar = tmpclsvar = ptr_clsvar = [None] * dictlength
        pyclsdefval = s_clsdefval = [" "] * dictlength
        pyclsnbytes = i_clsnbytes = [0] * dictlength

        for numb in range(0, dictlength):

            if not 'res_name' in dictflresource[numb]:  # no res_name passed
                raise library.XFormsTypeError("fls_make_ptr_flresource " \
                        "dict (whose contents is %s) should have a " \
                        "'res_name' key" % dictflresource[numb])
            else:
                pyclsresname[numb] = dictflresource[numb]['res_name']
                s_clsresname[numb] = library.convert_to_stringc( \
                        pyclsresname[numb])
            if not 'res_class' in dictflresource[numb]:  # no res_class passed
                raise library.XFormsTypeError("fls_make_ptr_flresource " \
                        "dict (whose contents is %s) should have a " \
                        "'res_class' key" % dictflresource[numb])
            else:
                pyclsresclass[numb] = dictflresource[numb]['res_class']
                s_clsresclass[numb] = library.convert_to_stringc( \
                        pyclsresclass[numb])
            if not 'type' in dictflresource[numb]:     # no type passed
                raise library.XFormsTypeError("fls_make_ptr_flresource " \
                        "dict (whose contents is %s) should have a " \
                        "'type' key" % dictflresource[numb])
            else:
                pyclstype[numb] = dictflresource[numb]['type']
                i_clstype[numb] = library.convert_to_intc(pyclstype[numb])
            if not 'var' in dictflresource[numb]:       # no var passed
                raise library.XFormsTypeError("fls_make_ptr_flresource " \
                        "dict (whose contents is %s) should have a " \
                        "'var' key" % dictflresource[numb])
            else:
                pyclsvar[numb] = dictflresource[numb]['var']
                # managing different C types
                if i_clstype[numb].value == xfdata.FL_SHORT:
                    tmpclsvar[numb] = library.convert_to_shortc( \
                            pyclsvar[numb])
                elif i_clstype[numb].value == xfdata.FL_BOOL or \
                        i_clstype[numb].value == xfdata.FL_INT:
                    tmpclsvar[numb] = library.convert_to_intc( \
                            pyclsvar[numb])
                elif i_clstype[numb].value == xfdata.FL_LONG:
                    tmpclsvar[numb] = library.convert_to_longc( \
                            pyclsvar[numb])
                elif i_clstype[numb].value == xfdata.FL_FLOAT:
                    tmpclsvar[numb] = library.convert_to_floatc( \
                            pyclsvar[numb])
                elif i_clstype[numb].value == xfdata.FL_STRING:
                    tmpclsvar[numb] = library.convert_to_stringc( \
                            pyclsvar[numb])
                else:
                    tmpclsvar[numb] = None
                ptr_clsvar[numb] = cty.pointer(tmpclsvar[numb])
            if not 'defval' in dictflresource[numb]:   # no defval passed
                raise library.XFormsTypeError("fls_make_ptr_flresource dict " \
                        "(whose contents is %s) should have a 'defval' key" % \
                        dictflresource[numb])
            else:
                pyclsdefval[numb] = dictflresource[numb]['defval']
                s_clsdefval[numb] = library.convert_to_stringc( \
                        pyclsdefval[numb])
            if not 'nbytes' in dictflresource[numb]:     # no nbytes passed
                raise library.XFormsTypeError("fls_make_ptr_flresource dict " \
                        "(whose contents is %s) should have a 'nbytes' key" % \
                        dictflresource[numb])
            else:
                pyclsnbytes[numb] = dictflresource[numb]['nbytes']
                i_clsnbytes[numb] = library.convert_to_intc(pyclsnbytes[numb])

            structflresource[numb].res_name = s_clsresname[numb]
            structflresource[numb].res_class = s_clsresclass[numb]
            structflresource[numb].type = i_clstype[numb]
            structflresource[numb].var = cty.cast(pyclsvar[numb], cty.c_void_p)
            structflresource[numb].defval = s_clsdefval[numb]
            structflresource[numb].nbytes = i_clsnbytes[numb]

            library.keep_elem_refs(dictflresource[numb], \
                structflresource[numb], pyclsresname[numb], \
                s_clsresname[numb], pyclsresclass[numb], s_clsresclass[numb], \
                pyclstype[numb], i_clstype[numb], pyclsvar[numb], \
                ptr_clsvar[numb], pyclsdefval[numb], s_clsdefval[numb], \
                pyclsnbytes[numb], i_clsnbytes[numb])

        #structflresource[-1].res_name = ""
        # this ends array, preventing SegFault?

        ptr_flresource = cty.pointer(structflresource[0])
        library.keep_elem_refs(dictflresource, ptr_flresource, \
                structflresource)
        return ptr_flresource

    else:
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " a python dict or a list of dicts" % \
                (dictflresource, type(dictflresource)))


def fls_make_ptr_flpoint(dictflpoint):
    """fls_make_ptr_flpoint(dictflpoint) -> ptr_flpoint

    Taking a python dict (for one dict item) or a list of dicts (for more
    than one dict item) with keys corresponding to xfdata.FL_POINT
    attributes prepares and returns a C-compatible pointer to
    xfdata.FL_POINT. Keys are: 'x' and 'y'."""

    # one dict
    if isinstance(dictflpoint, dict):

        pyclsx = sh_clsx = 0
        pyclsy = sh_clsy = 0
        if not 'x' in dictflpoint:      # no x passed
            raise library.XFormsTypeError("fls_make_ptr_flpoint dict (" \
                    "whose contents is %s) should have a 'x' key" % \
                    dictflpoint)
        else:
            pyclsx = dictflpoint['x']
            sh_clsx = library.convert_to_shortc(pyclsx)
            print("pyclsx, sh_clsx", pyclsx, sh_clsx)

        if not 'y' in dictflpoint:      # no y passed
            raise library.XFormsTypeError("fls_make_ptr_flpoint dict (" \
                    "whose contents is %s) should have a 'y' key" % \
                    dictflpoint)
        else:
            pyclsy = dictflpoint['y']
            sh_clsy = library.convert_to_shortc(pyclsy)
            print("pyclsy, sh_clsy", pyclsy, sh_clsy)
            structflpoint = (xfdata.FL_POINT *2)()      # * 2)()
        structflpoint[0].x = sh_clsx
        structflpoint[0].y = sh_clsy
        structflpoint[-1].x = 0  # ends array, preventing SegFault
        structflpoint[-1].y = 0  # ends array, preventing SegFault

        ptr_flpoint = cty.pointer(structflpoint[0])
        library.keep_elem_refs(dictflpoint, structflpoint, \
                ptr_flpoint, pyclsx, sh_clsx, pyclsy, sh_clsy)
        return ptr_flpoint

    # more dicts
    elif isinstance(dictflpoint, list):

        dictlength = len(dictflpoint)
        structflpoint = (xfdata.FL_POINT * (dictlength+1))()  # +1
        pyclsx = sh_clsx = [0] * dictlength
        pyclsy = sh_clsy = [0] * dictlength

        for numb in range(0, dictlength):

            if not 'x' in dictflpoint[numb]:  # no x passed
                raise library.XFormsTypeError("fls_make_ptr_flpoint dict (" \
                        "whose contents is %s) should have a 'x' key" % \
                        dictflpoint[numb])
            else:
                pyclsx[numb] = dictflpoint[numb]['x']
                sh_clsx[numb] = library.convert_to_shortc(pyclsx[numb])
            if not 'y' in dictflpoint[numb]:  # no y passed
                raise library.XFormsTypeError("fls_make_ptr_flpoint dict (" \
                        "whose contents is %s) should have a 'y' key" % \
                        dictflpoint[numb])
            else:
                pyclsy[numb] = dictflpoint[numb]['y']
                sh_clsy[numb] = library.convert_to_shortc(pyclsy[numb])

            structflpoint[numb].x = sh_clsx[numb]
            structflpoint[numb].y = sh_clsy[numb]

            library.keep_elem_refs(dictflpoint[numb], structflpoint[numb], \
                pyclsx[numb], sh_clsx[numb], pyclsy[numb], sh_clsy[numb])

        structflpoint[-1].x = 0  # ends array, preventing SegFault
        structflpoint[-1].y = 0  # ends array, preventing SegFault
        ptr_flpoint = cty.pointer(structflpoint[0])
        library.keep_elem_refs(dictflpoint, ptr_flpoint, \
                structflpoint)
        return ptr_flpoint

    else:
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " a python dict or a list of dicts" % \
                (dictflpoint, type(dictflpoint)))


def fls_make_ptr_flrect(dictflrect):
    """fls_make_ptr_flrect(dictflrect) -> ptr_flrect

    Taking a python dict (for one dict item) or a list of dicts (for more than
    one dict item) with keys corresponding to xfdata.FL_RECT attributes
    prepares and returns a C-compatible pointer to xfdata.FL_RECT. Keys are:
    'x', 'y', 'width' and 'height'."""

    # one dict
    if isinstance(dictflrect, dict):

        pyclsx = sh_clsx = pyclsy = sh_clsy = pyclswidth = ush_clswidth = 0
        pyclsheight = ush_clsheight = 0
        if not 'x' in dictflrect:      # no x passed
            raise library.XFormsTypeError("fls_make_ptr_flrect dict (whose "
                    "contents is %s) should have a 'x' key" % \
                    dictflrect)
        else:
            pyclsx = dictflrect['x']
            sh_clsx = library.convert_to_shortc(pyclsx)

        if not 'y' in dictflrect:      # no y passed
            raise library.XFormsTypeError("fls_make_ptr_flrect dict (whose "
                    "contents is %s) should have a 'y' key" % \
                    dictflrect)
        else:
            pyclsy = dictflrect['y']
            sh_clsy = library.convert_to_shortc(pyclsy)

        if not 'width' in dictflrect:      # no width passed
            raise library.XFormsTypeError("fls_make_ptr_flrect dict (whose "
                    "contents is %s) should have a 'width' key" % \
                    dictflrect)
        else:
            pyclswidth = dictflrect['width']
            ush_clswidth = library.convert_to_ushortc(pyclswidth)

        if not 'height' in dictflrect:      # no height passed
            raise library.XFormsTypeError("fls_make_ptr_flrect dict (whose "
                    "contents is %s) should have a 'height' key" % \
                    dictflrect)
        else:
            pyclsheight = dictflrect['height']
            ush_clsheight = library.convert_to_ushortc(pyclsheight)

        structflrect = (xfdata.FL_RECT * 2)()      # * 2)()
        structflrect[0].x = sh_clsx
        structflrect[0].y = sh_clsy
        structflrect[0].width = ush_clswidth
        structflrect[0].height = ush_clsheight
        structflrect[-1].x = 0  # ends array, preventing SegFault
        structflrect[-1].y = 0  # ends array, preventing SegFault
        structflrect[-1].width = 0  # ends array, preventing SegFault
        structflrect[-1].width = 0  # ends array, preventing SegFault

        ptr_flrect = cty.pointer(structflrect[0])
        library.keep_elem_refs(dictflrect, structflrect, ptr_flrect, pyclsx, \
                sh_clsx, pyclsy, sh_clsy, pyclswidth, ush_clswidth, \
                pyclsheight, ush_clsheight)
        return ptr_flrect

    # more dicts
    elif isinstance(dictflrect, list):

        dictlength = len(dictflrect)
        structflrect = (xfdata.FL_RECT * (dictlength+1))()  # +1
        pyclsx = sh_clsx = [0] * dictlength
        pyclsy = sh_clsy = [0] * dictlength
        pyclswidth = ush_clswidth = [0] * dictlength
        pyclsheight = ush_clsheight = [0] * dictlength

        for numb in range(0, dictlength):

            if not 'x' in dictflrect[numb]:  # no x passed
                raise library.XFormsTypeError("fls_make_ptr_flrect dict (whose "
                        "contents is %s) should have a 'x' key" % \
                        dictflrect[numb])
            else:
                pyclsx[numb] = dictflrect[numb]['x']
                sh_clsx[numb] = library.convert_to_shortc(pyclsx[numb])
            if not 'y' in dictflrect[numb]:  # no y passed
                raise library.XFormsTypeError("fls_make_ptr_flrect dict (whose "
                        "contents is %s) should have a 'y' key" % \
                        dictflrect[numb])
            else:
                pyclsy[numb] = dictflrect[numb]['y']
                sh_clsy[numb] = library.convert_to_shortc(pyclsy[numb])
            if not 'width' in dictflrect:      # no width passed
                raise library.XFormsTypeError("fls_make_ptr_flrect dict (whose "
                        "contents is %s) should have a 'width' key" % \
                        dictflrect[numb])
            else:
                pyclswidth[numb] = dictflrect['width']
                ush_clswidth[numb] = library.convert_to_ushortc( \
                        pyclswidth[numb])
            if not 'height' in dictflrect:      # no height passed
                raise library.XFormsTypeError("fls_make_ptr_flrect dict (whose "
                        "contents is %s) should have a 'height' key" % \
                        dictflrect[numb])
            else:
                pyclsheight[numb] = dictflrect['height']
                ush_clsheight[numb] = library.convert_to_ushortc( \
                        pyclsheight[numb])

            structflrect[numb].x = sh_clsx[numb]
            structflrect[numb].y = sh_clsy[numb]
            structflrect[numb].width = ush_clswidth[numb]
            structflrect[numb].height = ush_clsheight[numb]

            library.keep_elem_refs(dictflrect[numb], structflrect[numb], \
                pyclsx[numb], sh_clsx[numb], pyclsy[numb], sh_clsy[numb], \
                pyclswidth[numb], pyclsheight[numb])

        structflrect[-1].x = 0  # ends array, preventing SegFault
        structflrect[-1].y = 0  # ends array, preventing SegFault
        structflrect[-1].width = 0  # ends array, preventing SegFault
        structflrect[-1].height = 0  # ends array, preventing SegFault
        ptr_flrect = cty.pointer(structflrect[0])
        library.keep_elem_refs(dictflrect, ptr_flrect, structflrect)
        return ptr_flrect

    else:
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " a python dict or a list of dicts" % \
                (dictflrect, type(dictflrect)))


def fls_make_ptr_flimagetext(dictflimagetext):
    """fls_make_ptr_flimagetext(dictflimagetext) -> ptr_flimagetext

    Taking a python dict with keys corresponding to xfdata.FLIMAGE_TEXT
    attributes prepares and returns a C-compatible pointer to
    xfdata.FLIMAGE_TEXT. Keys are: 'str', 'len', 'x', 'y', 'color', 'bcolor',
    'nobk', 'size', 'style', 'angle' and 'align'. """

    # one dict only
    if isinstance(dictflimagetext, dict):

        pyclsstr = s_clsstr = ""
        pyclslen = i_clslen = pyclsx = i_clsx = pyclsy = i_clsy = 0
        pyclscolor = ui_clscolor = pyclsbcolor = ui_clsbcolor = 0
        pyclsnobk = i_clsnobk = pyclssize = i_clssize = pyclsstyle = 0
        i_clsstyle = pyclsangle = i_clsangle = pyclsalign = i_clsalign = 0

        if not 'str' in dictflimagetext:      # no str passed
            raise library.XFormsTypeError("fls_make_ptr_flimagetext dict (" \
                    "whose contents is %s) should have a 'str' key" % \
                    dictflimagetext)
        else:
            pyclsstr = dictflimagetext['str']
            s_clsstr = library.convert_to_stringc(pyclsstr)

        if not 'len' in dictflimagetext:      # no len passed
            raise library.XFormsTypeError("fls_make_ptr_flimagetext dict (" \
                    "whose contents is %s) should have a 'len' key" % \
                    dictflimagetext)
        else:
            pyclslen = dictflimagetext['len']
            i_clslen = library.convert_to_intc(pyclslen)

        if not 'x' in dictflimagetext:      # no x passed
            raise library.XFormsTypeError("fls_make_ptr_flimagetext dict (" \
                    "whose contents is %s) should have a 'x' key" % \
                    dictflimagetext)
        else:
            pyclsx = dictflimagetext['x']
            i_clsx = library.convert_to_intc(pyclsx)

        if not 'y' in dictflimagetext:      # no y passed
            raise library.XFormsTypeError("fls_make_ptr_flimagetext dict (" \
                    "whose contents is %s) should have a 'y' key" % \
                    dictflimagetext)
        else:
            pyclsy = dictflimagetext['y']
            i_clsy = library.convert_to_intc(pyclsy)

        if not 'color' in dictflimagetext:      # no color passed
            raise library.XFormsTypeError("fls_make_ptr_flimagetext dict (" \
                    "whose contents is %s) should have a 'color' key" % \
                    dictflimagetext)
        else:
            pyclscolor = dictflimagetext['color']
            ui_clscolor = library.convert_to_uintc(pyclscolor)

        if not 'bcolor' in dictflimagetext:      # no bcolor passed
            raise library.XFormsTypeError("fls_make_ptr_flimagetext dict (" \
                    "whose contents is %s) should have a 'bcolor' key" % \
                    dictflimagetext)
        else:
            pyclscolor = dictflimagetext['bcolor']
            ui_clsbcolor = library.convert_to_uintc(pyclsbcolor)

        if not 'bcolor' in dictflimagetext:      # no bcolor passed
            raise library.XFormsTypeError("fls_make_ptr_flimagetext dict (" \
                    "whose contents is %s) should have a 'bcolor' key" % \
                    dictflimagetext)
        else:
            pyclscolor = dictflimagetext['bcolor']
            ui_clsbcolor = library.convert_to_uintc(pyclsbcolor)

        if not 'nobk' in dictflimagetext:      # no nobk passed
            raise library.XFormsTypeError("fls_make_ptr_flimagetext dict (" \
                    "whose contents is %s) should have a 'nobk' key" % \
                    dictflimagetext)
        else:
            pyclsnobk = dictflimagetext['nobk']
            i_clsnobk = library.convert_to_intc(pyclsnobk)

        if not 'size' in dictflimagetext:      # no size passed
            raise library.XFormsTypeError("fls_make_ptr_flimagetext dict (" \
                    "whose contents is %s) should have a 'size' key" % \
                    dictflimagetext)
        else:
            pyclssize = dictflimagetext['size']
            i_clssize = library.convert_to_intc(pyclssize)

        if not 'style' in dictflimagetext:      # no style passed
            raise library.XFormsTypeError("fls_make_ptr_flimagetext dict (" \
                    "whose contents is %s) should have a 'style' key" % \
                    dictflimagetext)
        else:
            pyclsstyle = dictflimagetext['style']
            i_clsstyle = library.convert_to_intc(pyclsstyle)

        if not 'angle' in dictflimagetext:      # no angle passed
            raise library.XFormsTypeError("fls_make_ptr_flimagetext dict (" \
                    "whose contents is %s) should have a 'angle' key" % \
                    dictflimagetext)
        else:
            pyclsangle = dictflimagetext['angle']
            i_clsangle = library.convert_to_intc(pyclsangle)

        if not 'align' in dictflimagetext:      # no align passed
            raise library.XFormsTypeError("fls_make_ptr_flimagetext dict (" \
                    "whose contents is %s) should have a 'align' key" % \
                    dictflimagetext)
        else:
            pyclsalign = dictflimagetext['align']
            i_clsalign = library.convert_to_intc(pyclsalign)

        structflimagetext = (xfdata.FLIMAGE_TEXT)()
        structflimagetext.str = s_clsstr
        structflimagetext.len = i_clslen
        structflimagetext.x = i_clsx
        structflimagetext.y = i_clsy
        structflimagetext.color = ui_clscolor
        structflimagetext.bcolor = ui_clsbcolor
        structflimagetext.nobk = i_clsnobk
        structflimagetext.size = i_clssize
        structflimagetext.style = i_clsstyle
        structflimagetext.angle = i_clsangle
        structflimagetext.align = i_clsalign

        ptr_flimagetext = cty.pointer(structflimagetext)
        library.keep_elem_refs(dictflimagetext, structflimagetext, \
                ptr_flimagetext, pyclsstr, s_clsstr, pyclslen, i_clslen, \
                pyclsx, i_clsx, pyclsy, i_clsy, pyclscolor, ui_clscolor, \
                pyclsbcolor, ui_clsbcolor, pyclsnobk, i_clsnobk, pyclssize, \
                i_clssize, pyclsstyle, i_clsstyle, pyclsangle, i_clsangle, \
                pyclsalign, i_clsalign)
        return ptr_flimagetext

    else:
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " a python dict" % \
                (dictflimagetext, type(dictflimagetext)))


def fls_make_ptr_flimagemarker(dictflimagemarker):
    """fls_make_ptr_flimagetext(dictflimagemarker) -> ptr_flimagemarker

    Taking a python dict with keys corresponding to xfdata.FLIMAGE_MARKER
    attributes prepares and returns a C-compatible pointer to
    xfdata.FLIMAGE_MARKER. Keys are: 'name', 'w', 'h', 'x', 'y', 'color',
    'bcolor', 'angle', 'fill', 'thickness', 'style'. Other keys ('display',
    'gc', 'win', 'psdraw') are filled by XForms. """

    # one dict only
    if isinstance(dictflimagemarker, dict):

        pyclsname = s_clsname = ""
        pyclsw = i_clsw = pyclsh = i_clsh = pyclsx = i_clsx = 0
        pyclsy = i_clsy = pyclscolor = ui_clscolor = pyclsbcolor = 0
        ui_clsbcolor = pyclsangle = i_clsangle = pyclsfill = i_clsfill = 0
        pyclsthickness = i_clsthickness = pyclsstyle = i_clsstyle = 0

        if not 'name' in dictflimagemarker:      # no name passed
            raise library.XFormsTypeError("fls_make_ptr_flimagemarker dict (" \
                    "whose contents is %s) should have a 'name' key" % \
                    dictflimagemarker)
        else:
            pyclsname = dictflimagemarker['name']
            s_clsname = library.convert_to_stringc(pyclsname)

        if not 'w' in dictflimagemarker:      # no w passed
            raise library.XFormsTypeError("fls_make_ptr_flimagemarker dict (" \
                    "whose contents is %s) should have a 'w' key" % \
                    dictflimagemarker)
        else:
            pyclsw = dictflimagemarker['w']
            i_clsw = library.convert_to_intc(pyclsw)

        if not 'h' in dictflimagemarker:      # no h passed
            raise library.XFormsTypeError("fls_make_ptr_flimagemarker dict (" \
                    "whose contents is %s) should have a 'h' key" % \
                    dictflimagemarker)
        else:
            pyclsh = dictflimagemarker['h']
            i_clsh = library.convert_to_intc(pyclsh)

        if not 'x' in dictflimagemarker:      # no x passed
            raise library.XFormsTypeError("fls_make_ptr_flimagemarker dict (" \
                    "whose contents is %s) should have a 'x' key" % \
                    dictflimagemarker)
        else:
            pyclsx = dictflimagemarker['x']
            i_clsx = library.convert_to_intc(pyclsx)

        if not 'y' in dictflimagemarker:      # no y passed
            raise library.XFormsTypeError("fls_make_ptr_flimagemarker dict (" \
                    "whose contents is %s) should have a 'y' key" % \
                    dictflimagemarker)
        else:
            pyclsy = dictflimagemarker['y']
            i_clsy = library.convert_to_intc(pyclsy)

        if not 'color' in dictflimagemarker:      # no color passed
            raise library.XFormsTypeError("fls_make_ptr_flimagemarker dict (" \
                    "whose contents is %s) should have a 'color' key" % \
                    dictflimagemarker)
        else:
            pyclscolor = dictflimagemarker['color']
            ui_clscolor = library.convert_to_uintc(pyclscolor)

        if not 'bcolor' in dictflimagemarker:      # no bcolor passed
            raise library.XFormsTypeError("fls_make_ptr_flimagemarker dict (" \
                    "whose contents is %s) should have a 'bcolor' key" % \
                    dictflimagemarker)
        else:
            pyclsbcolor = dictflimagemarker['bcolor']
            ui_clsbcolor = library.convert_to_uintc(pyclsbcolor)

        if not 'angle' in dictflimagemarker:      # no angle passed
            raise library.XFormsTypeError("fls_make_ptr_flimagemarker dict (" \
                    "whose contents is %s) should have a 'angle' key" % \
                    dictflimagemarker)
        else:
            pyclsangle = dictflimagemarker['angle']
            i_clsangle = library.convert_to_intc(pyclsangle)

        if not 'fill' in dictflimagemarker:      # no fill passed
            raise library.XFormsTypeError("fls_make_ptr_flimagemarker dict (" \
                    "whose contents is %s) should have a 'fill' key" % \
                    dictflimagemarker)
        else:
            pyclsfill = dictflimagemarker['fill']
            i_clsfill = library.convert_to_intc(pyclsfill)

        if not 'thickness' in dictflimagemarker:      # no thickness passed
            raise library.XFormsTypeError("fls_make_ptr_flimagemarker dict (" \
                    "whose contents is %s) should have a 'thickness' key" % \
                    dictflimagemarker)
        else:
            pyclsthickness = dictflimagemarker['thickness']
            i_clsthickness = library.convert_to_intc(pyclsthickness)

        if not 'style' in dictflimagemarker:      # no style passed
            raise library.XFormsTypeError("fls_make_ptr_flimagemarker dict (" \
                    "whose contents is %s) should have a 'style' key" % \
                    dictflimagemarker)
        else:
            pyclsstyle = dictflimagemarker['style']
            i_clsstyle = library.convert_to_intc(pyclsstyle)

        structflimagemarker = (xfdata.FLIMAGE_TEXT)()
        structflimagemarker.name = s_clsname
        structflimagemarker.w = i_clsw
        structflimagemarker.h = i_clsh
        structflimagemarker.x = i_clsx
        structflimagemarker.y = i_clsy
        structflimagemarker.color = ui_clscolor
        structflimagemarker.bcolor = ui_clsbcolor
        structflimagemarker.angle = i_clsangle
        structflimagemarker.fill = i_clsfill
        structflimagemarker.thickness = i_clsthickness
        structflimagemarker.style = i_clsstyle
        # 'display', 'gc', 'win', 'psdraw' NOT to be filled by user.

        ptr_flimagemarker = cty.pointer(structflimagemarker)
        library.keep_elem_refs(dictflimagemarker, structflimagemarker, \
                ptr_flimagemarker, pyclsname, s_clsname, pyclsw, i_clsw, \
                pyclsh, i_clsh, pyclsx, i_clsx, pyclsy, i_clsy, pyclscolor, \
                ui_clscolor, pyclsbcolor, ui_clsbcolor, pyclsangle, \
                i_clsangle, pyclsfill, i_clsfill, pyclsthickness, \
                i_clsthickness, pyclsstyle, i_clsstyle)
        return ptr_flimagemarker

    else:
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " a python dict" % \
                (dictflimagemarker, type(dictflimagemarker)))


def fls_make_ptr_fleditkeymap(dictfleditkeymap):
    """fls_make_ptr_fleditkeymap(dictfleditkeymap) -> ptr_fleditkeymap

    Taking a python dict with keys corresponding to xfdata.FL_EditKeymap
    attributes prepares and returns a C-compatible pointer to
    xfdata.FL_EditKeymap. Keys are: 'del_prev_char', 'del_next_char',
    'del_prev_word', 'del_next_word', 'moveto_prev_line', 'moveto_next_line',
    'moveto_prev_char', 'moveto_next_char', 'moveto_prev_word',
    'moveto_next_word', 'moveto_prev_page', 'moveto_next_page', 'moveto_bol',
    'moveto_eol', 'moveto_bof', 'moveto_eof', 'transpose', 'paste',
    'backspace', 'del_to_bol', 'del_to_eol', 'clear_field', 'del_to_eos'.
    You are not required to manually pass all keys' values; remaining keys
    are filled with 0, so default keymap will be used. If you pass None
    instead of a dict, all keys are filled with 0 (default keymap)."""

    # one dict only
    if isinstance(dictfleditkeymap, dict):

        pydelprevchar = l_delprevchar = pydelnextchar = l_delnextchar = 0
        pydelprevword = l_delprevword = pydelnextword = l_pydelnextword = 0
        pymovetoprevline = l_movetoprevline = pymovetonextline = 0
        l_movetonextline = pymovetoprevchar = l_movetoprevchar = 0
        pymovetonextchar = l_movetonextchar = pymovetoprevword = 0
        l_movetoprevword = pymovetonextword = l_movetonextword = 0
        pymovetoprevpage = l_movetoprevpage = pymovetonextpage = 0
        l_movetonextpage = pymovetobol = l_movetobol = pymovetoeol = 0
        l_movetoeol = pymovetobof = l_movetobof = pymovetoeof = l_movetoeof = 0
        pytranspose = l_transpose = pypaste = l_paste = pybackspace = 0
        l_backspace = pydeltobol = l_deltobol = pydeltoeol = l_deltoeol = 0
        pyclearfield = l_clearfield = pydeltoeos = l_deltoeos = 0

        if not 'del_prev_char' in dictfleditkeymap:
            pydelprevchar = 0
        else:
            pydelprevchar = dictfleditkeymap['del_prev_char']
        l_delprevchar = library.convert_to_longc(pydelprevchar)

        if not 'del_next_char' in dictfleditkeymap:
            pydelnextchar = 0
        else:
            pydelnextchar = dictfleditkeymap['del_next_char']
        l_delnextchar = library.convert_to_longc(pydelnextchar)

        if not 'del_prev_word' in dictfleditkeymap:
            pydelprevword = 0
        else:
            pydelprevword = dictfleditkeymap['del_prev_word']
        l_delprevword = library.convert_to_longc(pydelprevword)

        if not 'del_next_word' in dictfleditkeymap:
            pydelnextword = 0
        else:
            pydelnextword = dictfleditkeymap['del_next_word']
        l_delnextword = library.convert_to_longc(pydelnextword)

        if not 'moveto_prev_line' in dictfleditkeymap:
            pymovetoprevline = 0
        else:
            pymovetoprevline = dictfleditkeymap['moveto_prev_line']
        l_movetoprevline = library.convert_to_longc(pymovetoprevline)

        if not 'moveto_next_line' in dictfleditkeymap:
            pymovetonextline = 0
        else:
            pymovetonextline = dictfleditkeymap['moveto_next_line']
        l_movetonextline = library.convert_to_longc(pymovetonextline)

        if not 'moveto_prev_char' in dictfleditkeymap:
            pymovetoprevchar = 0
        else:
            pymovetoprevchar = dictfleditkeymap['moveto_prev_char']
        l_movetoprevchar = library.convert_to_longc(pymovetoprevchar)

        if not 'moveto_next_char' in dictfleditkeymap:
            pymovetonextchar = 0
        else:
            pymovetonextchar = dictfleditkeymap['moveto_next_char']
        l_movetonextchar = library.convert_to_longc(pymovetonextchar)

        if not 'moveto_prev_word' in dictfleditkeymap:
            pymovetoprevword = 0
        else:
            pymovetoprevword = dictfleditkeymap['moveto_prev_word']
        l_movetoprevword = library.convert_to_longc(pymovetoprevword)

        if not 'moveto_next_word' in dictfleditkeymap:
            pymovetonextword = 0
        else:
            pymovetonextword = dictfleditkeymap['moveto_next_word']
        l_movetonextword = library.convert_to_longc(pymovetonextword)

        if not 'moveto_prev_page' in dictfleditkeymap:
            pymovetoprevpage = 0
        else:
            pymovetoprevpage = dictfleditkeymap['moveto_prev_page']
        l_movetoprevpage = library.convert_to_longc(pymovetoprevpage)

        if not 'moveto_next_page' in dictfleditkeymap:
            pymovetonextpage = 0
        else:
            pymovetonextpage = dictfleditkeymap['moveto_next_page']
        l_movetonextpage = library.convert_to_longc(pymovetonextpage)

        if not 'moveto_bol' in dictfleditkeymap:
            pymovetobol = 0
        else:
            pymovetobol = dictfleditkeymap['moveto_bol']
        l_movetobol = library.convert_to_longc(pymovetobol)

        if not 'moveto_eol' in dictfleditkeymap:
            pymovetoeol = 0
        else:
            pymovetoeol = dictfleditkeymap['moveto_eol']
        l_movetoeol = library.convert_to_longc(pymovetoeol)

        if not 'moveto_bof' in dictfleditkeymap:
            pymovetobof = 0
        else:
            pymovetobof = dictfleditkeymap['moveto_bof']
        l_movetobof = library.convert_to_longc(pymovetobof)

        if not 'moveto_eof' in dictfleditkeymap:
            pymovetoeof = 0
        else:
            pymovetoeof = dictfleditkeymap['moveto_eof']
        l_movetoeof = library.convert_to_longc(pymovetoeof)

        if not 'transpose' in dictfleditkeymap:
            pytranspose = 0
        else:
            pytranspose = dictfleditkeymap['transpose']
        l_transpose = library.convert_to_longc(pytranspose)

        if not 'paste' in dictfleditkeymap:
            pypaste = 0
        else:
            pypaste = dictfleditkeymap['paste']
        l_paste = library.convert_to_longc(pypaste)

        if not 'backspace' in dictfleditkeymap:
            pybackspace = 0
        else:
            pybackspace = dictfleditkeymap['backspace']
        l_backspace = library.convert_to_longc(pybackspace)

        if not 'del_to_bol' in dictfleditkeymap:
            pydeltobol = 0
        else:
            pydeltobol = dictfleditkeymap['del_to_bol']
        l_deltobol = library.convert_to_longc(pydeltobol)

        if not 'del_to_eol' in dictfleditkeymap:
            pydeltoeol = 0
        else:
            pydeltoeol = dictfleditkeymap['del_to_eol']
        l_deltoeol = library.convert_to_longc(pydeltoeol)

        if not 'clear_field' in dictfleditkeymap:
            pyclearfield  = 0
        else:
            pyclearfield  = dictfleditkeymap['clear_field']
        l_clearfield  = library.convert_to_longc(pyclearfield )

        if not 'del_to_eos' in dictfleditkeymap:
            pydeltoeos = 0
        else:
            pydeltoeos = dictfleditkeymap['del_to_eos']
        l_deltoeos = library.convert_to_longc(pydeltoeos)

        structfleditkeymap = (xfdata.FL_EditKeymap)()
        structfleditkeymap.del_prev_char = l_delprevchar
        structfleditkeymap.del_next_char = l_delnextchar
        structfleditkeymap.del_prev_word = l_delprevword
        structfleditkeymap.del_next_word = l_delnextword
        structfleditkeymap.moveto_prev_line = l_movetoprevline
        structfleditkeymap.moveto_next_line = l_movetonextline
        structfleditkeymap.moveto_prev_char = l_movetoprevchar
        structfleditkeymap.moveto_next_char = l_movetonextchar
        structfleditkeymap.moveto_prev_word = l_movetoprevword
        structfleditkeymap.moveto_next_word = l_movetonextword
        structfleditkeymap.moveto_prev_page = l_movetoprevpage
        structfleditkeymap.moveto_next_page = l_movetonextpage
        structfleditkeymap.moveto_bol = l_movetobol
        structfleditkeymap.moveto_eol = l_movetoeol
        structfleditkeymap.moveto_bof = l_movetobof
        structfleditkeymap.moveto_eof = l_movetoeof
        structfleditkeymap.transpose = l_transpose
        structfleditkeymap.paste = l_paste
        structfleditkeymap.backspace = l_backspace
        structfleditkeymap.del_to_bol = l_deltobol
        structfleditkeymap.del_to_eol = l_deltoeol
        structfleditkeymap.clear_field = l_clearfield
        structfleditkeymap.del_to_eos = l_deltoeos

        ptr_fleditkeymap = cty.pointer(structfleditkeymap)
        library.keep_elem_refs(dictfleditkeymap, structfleditkeymap, \
                ptr_fleditkeymap, pydelprevchar, l_delprevchar, pydelnextchar,
                l_delnextchar, pydelprevword, l_delprevword, pydelnextword, \
                l_delnextword, pymovetoprevline, l_movetoprevline, \
                pymovetonextline, l_movetonextline, pymovetoprevchar, \
                l_movetoprevchar, pymovetonextchar, pymovetoprevword, \
                l_movetoprevword, pymovetonextword, l_movetonextword, \
                pymovetoprevpage, l_movetoprevpage, pymovetonextpage, \
                l_movetonextpage, pymovetobol, l_movetobol, pymovetoeol, \
                l_movetoeol, pymovetobof, l_movetobof, pymovetoeof, \
                l_movetoeof, pytranspose, l_transpose, pypaste, l_paste, \
                pybackspace, l_backspace, pydeltobol, l_deltobol, pydeltoeol, \
                l_deltoeol, pyclearfield, l_clearfield, pydeltoeos, l_deltoeos)
        return ptr_fleditkeymap

    elif not dictfleditkeymap:  # None passed, all keys set to zero
        pydelprevchar = 0
        l_delprevchar = library.convert_to_longc(pydelprevchar)
        pydelnextchar = 0
        l_delnextchar = library.convert_to_longc(pydelnextchar)
        pydelprevword = 0
        l_delprevword = library.convert_to_longc(pydelprevword)
        pydelnextword = 0
        l_delnextword = library.convert_to_longc(pydelnextword)
        pymovetoprevline = 0
        l_movetoprevline = library.convert_to_longc(pymovetoprevline)
        pymovetonextline = 0
        l_movetonextline = library.convert_to_longc(pymovetonextline)
        pymovetoprevchar = 0
        l_movetoprevchar = library.convert_to_longc(pymovetoprevchar)
        pymovetonextchar = 0
        l_movetonextchar = library.convert_to_longc(pymovetonextchar)
        pymovetoprevword = 0
        l_movetoprevword = library.convert_to_longc(pymovetoprevword)
        pymovetonextword = 0
        l_movetonextword = library.convert_to_longc(pymovetonextword)
        pymovetoprevpage = 0
        l_movetoprevpage = library.convert_to_longc(pymovetoprevpage)
        pymovetonextpage = 0
        l_movetonextpage = library.convert_to_longc(pymovetonextpage)
        pymovetobol = 0
        l_movetobol = library.convert_to_longc(pymovetobol)
        pymovetoeol = 0
        l_movetoeol = library.convert_to_longc(pymovetoeol)
        pymovetobof = 0
        l_movetobof = library.convert_to_longc(pymovetobof)
        pymovetoeof = 0
        l_movetoeof = library.convert_to_longc(pymovetoeof)
        pytranspose = 0
        l_transpose = library.convert_to_longc(pytranspose)
        pypaste = 0
        l_paste = library.convert_to_longc(pypaste)
        pybackspace = 0
        l_backspace = library.convert_to_longc(pybackspace)
        pydeltobol = 0
        l_deltobol = library.convert_to_longc(pydeltobol)
        pydeltoeol = 0
        l_deltoeol = library.convert_to_longc(pydeltoeol)
        pyclearfield  = 0
        l_clearfield  = library.convert_to_longc(pyclearfield )
        pydeltoeos = 0
        l_deltoeos = library.convert_to_longc(pydeltoeos)

        structfleditkeymap = (xfdata.FL_EditKeymap)()
        structfleditkeymap.del_prev_char = l_delprevchar
        structfleditkeymap.del_next_char = l_delnextchar
        structfleditkeymap.del_prev_word = l_delprevword
        structfleditkeymap.del_next_word = l_delnextword
        structfleditkeymap.moveto_prev_line = l_movetoprevline
        structfleditkeymap.moveto_next_line = l_movetonextline
        structfleditkeymap.moveto_prev_char = l_movetoprevchar
        structfleditkeymap.moveto_next_char = l_movetonextchar
        structfleditkeymap.moveto_prev_word = l_movetoprevword
        structfleditkeymap.moveto_next_word = l_movetonextword
        structfleditkeymap.moveto_prev_page = l_movetoprevpage
        structfleditkeymap.moveto_next_page = l_movetonextpage
        structfleditkeymap.moveto_bol = l_movetobol
        structfleditkeymap.moveto_eol = l_movetoeol
        structfleditkeymap.moveto_bof = l_movetobof
        structfleditkeymap.moveto_eof = l_movetoeof
        structfleditkeymap.transpose = l_transpose
        structfleditkeymap.paste = l_paste
        structfleditkeymap.backspace = l_backspace
        structfleditkeymap.del_to_bol = l_deltobol
        structfleditkeymap.del_to_eol = l_deltoeol
        structfleditkeymap.clear_field = l_clearfield
        structfleditkeymap.del_to_eos = l_deltoeos

        ptr_fleditkeymap = cty.pointer(structfleditkeymap)
        library.keep_elem_refs(dictfleditkeymap, structfleditkeymap, \
                ptr_fleditkeymap, pydelprevchar, l_delprevchar, pydelnextchar,
                l_delnextchar, pydelprevword, l_delprevword, pydelnextword, \
                l_delnextword, pymovetoprevline, l_movetoprevline, \
                pymovetonextline, l_movetonextline, pymovetoprevchar, \
                l_movetoprevchar, pymovetonextchar, pymovetoprevword, \
                l_movetoprevword, pymovetonextword, l_movetonextword, \
                pymovetoprevpage, l_movetoprevpage, pymovetonextpage, \
                l_movetonextpage, pymovetobol, l_movetobol, pymovetoeol, \
                l_movetoeol, pymovetobof, l_movetobof, pymovetoeof, \
                l_movetoeof, pytranspose, l_transpose, pypaste, l_paste, \
                pybackspace, l_backspace, pydeltobol, l_deltobol, pydeltoeol, \
                l_deltoeol, pyclearfield, l_clearfield, pydeltoeos, l_deltoeos)
        return ptr_fleditkeymap

    else:
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " a python dict, or 'None' (for all keys to be set to 0)." % \
                (dictfleditkeymap, type(dictfleditkeymap)))


def fls_make_flpopupcb(pyfn_popupcb):
    """fls_make_flpopupcb(pyfn_popupcb) -> cfn_popupcb

    Taking a python callback function name, prepares and returns a
    C-compatible xfdata.FL_POPUP_CB function."""

    if hasattr(pyfn_popupcb, '__call__'):
        cfn_popupcb = xfdata.FL_POPUP_CB(pyfn_popupcb)
        library.keep_cfunc_refs(pyfn_popupcb, cfn_popupcb)
        return cfn_popupcb
    else:
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " a python function" % (pyfn_popupcb, type(pyfn_popupcb)))


def fls_donothing_flpopupcb(ptr_flpopupreturn):
    """ Replaces a callback function not defined for class instances
        as e.g. xfdata.FL_POPUP_ITEM."""
    return 0


def fls_make_flimagesetup_and_pointer():
    """ Makes a xfdata.FLIMAGE_SETUP() class instance and its pointer,
    and returns both """
    baseval = xfdata.FLIMAGE_SETUP()
    ptrbaseval = cty.pointer(baseval)
    return baseval, ptrbaseval


def fls_import_xbmdata_from_file(fname):
    """fls_import_xbmdata_from_file(fname) -> width, height, xbmcontents

    Taking a .xbm filename, it reads it and returns all elements, to be used
    with flbitmap.fl_set_bitmapbutton_data()."""

    width = 0
    height = 0
    tmpxbmcontents1 = ""
    tmpxbmcontents2 = ""
    xbmcontents = []

    if fname.endswith(".xbm") or fname.endswith(".XBM"):
        if os.path.exists(fname):
            try:
                xbmfil = open(fname)
            except IOError:
                raise library.XFormsGenericError("File %s cannot be " \
                    "opened." % fname)
            iswidth = True      # first defined
            iscontentsarea = False
            iscommentarea = False
            for line in xbmfil:
                if "/*" in line and "*/" in line:     # comment inlined
                    continue
                elif "/*" in line:        # start of a comment
                    iscommentarea = True
                    continue
                elif "*/" in line:        # end of a comment
                    iscommentarea = False
                    continue
                elif iscommentarea:     # in the middle of a comment
                    continue
                elif not iscommentarea:
                    if line.startswith("#define"):
                        try:
                            defineunused, varunused, varvalue = line.split()
                        except ValueError:
                            raise library.XFormsValueError("File %s has an" \
                                    "incorrect format." % fname)
                        if iswidth:
                            width = varvalue
                            iswidth = False
                        else:
                            height = varvalue
                    elif "[]" in line:      # start of contents
                        iscontentsarea = True
                        tmpxbmcontents1 += line
                    elif iscontentsarea:
                        tmpxbmcontents1 += line
            # remove unuseful chars
            tmpxbmcontents1 = tmpxbmcontents1.replace("\n", "")
            tmpxbmcontents1 = tmpxbmcontents1.replace(";", "")
            tmpxbmcontents1 = tmpxbmcontents1.replace("=", "")
            tmpxbmcontents1 = tmpxbmcontents1.replace(",", " ")
            tmpxbmcontents1 = tmpxbmcontents1.replace("  ", " ")
            tmpxbmcontents1 = tmpxbmcontents1.replace("}", "")
            indx = tmpxbmcontents1.find("{")
            if indx != -1:       # found!
                tmpxbmcontents2 = tmpxbmcontents1[indx+1:-1]
            else:
                raise library.XFormsValueError("File %s has an incorrect " \
                        "format." % fname)
            tmpxbmcontents2 = tmpxbmcontents2.split()
            for numb in range(0, len(tmpxbmcontents2)):
                hexval = int(tmpxbmcontents2[numb], 16)
                xbmcontents.append(hexval)
            return width, height, xbmcontents

        else:   # not existing
            raise library.XFormsGenericError("File %s does not exist." % fname)
    else:       # not a .xbm file
        raise library.XFormsGenericError("File %s should be a .xpm file." % \
                fname)


def fls_import_xpmdata_from_file(fname):
    """fls_import_xpmdata_from_file(fname) -> xpmcontents

    Taking a .xpm filename, it reads it and returns contents, to be used
    with flbitmap.fl_set_pixmapbutton_data()."""

    tmpxpmcontents1 = ""
    tmpxpmcontents2 = ""
    xpmcontents = []

    if fname.endswith(".xpm") or fname.endswith(".XPM"):
        if os.path.exists(fname):
            try:
                xpmfil = open(fname)
            except IOError:
                raise library.XFormsGenericError("File %s cannot be " \
                        "opened." % fname)
            iscontentsarea = False
            iscommentarea = False
            for line in xpmfil:
                if "/*" in line and "*/" in line:     # comment inlined
                    continue
                elif "/*" in line:        # start of a comment
                    iscommentarea = True
                    continue
                elif "*/" in line:        # end of a comment
                    iscommentarea = False
                    continue
                elif iscommentarea:     # in the middle of a comment
                    continue
                elif not iscommentarea:
                    if "[]" in line:      # start of contents
                        iscontentsarea = True
                        tmpxpmcontents1 += line
                    elif iscontentsarea:
                        tmpxpmcontents1 += line
            # remove unuseful chars
            tmpxpmcontents1 = tmpxpmcontents1.replace("\n", "")
            tmpxpmcontents1 = tmpxpmcontents1.replace(";", "")
            tmpxpmcontents1 = tmpxpmcontents1.replace("=", "")
            tmpxpmcontents1 = tmpxpmcontents1.replace('"', "")
            tmpxpmcontents1 = tmpxpmcontents1.replace("  ", " ")
            tmpxpmcontents1 = tmpxpmcontents1.replace("\t", "    ")
            tmpxpmcontents1 = tmpxpmcontents1.replace("}", "")
            indx = tmpxpmcontents1.find("{")
            if indx != -1:       # found!
                tmpxpmcontents2 = tmpxpmcontents1[indx+1:-1]
            else:
                raise library.XFormsValueError("File %s has an incorrect " \
                        "format." % fname)
            xpmcontents = tmpxpmcontents2.split(",")
            return xpmcontents

        else:   # not existing
            raise library.XFormsGenericError("File %s does not exist." % fname)
    else:       # not a .xpm file
        raise library.XFormsGenericError("File %s should be a .xpm file." % \
                fname)


def fls_convert_ptrvoid_to_ptrflobject(pvdata):
    """Taking a pointer to void param (from a callback/handler function just
    invoked) and re-casts it to a ptr_flobject and returns it so user can
    retrieve real value passed to function caller."""

    retval = None
    if not isinstance(pvdata, int):
        # void * is considered int by ctypes when passed (memory address)
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " userdata of pointer to void type." % \
                (pvdata, type(pvdata)))
    else:
        retval = cty.cast(pvdata, cty.POINTER(xfdata.FL_OBJECT))
    return retval


def fls_convert_ptrvoid_to_ptrflform(pvdata):
    """Taking a pointer to void param (from a callback/handler function just
    invoked) and re-casts it to a ptr_flform and returns it so user can
    retrieve real value passed to function caller. It is the counterpart
    of library.convert_userdata_to_ptrvoid()."""

    retval = None
    if not isinstance(pvdata, int):
        # void * is considered int by ctypes when passed (memory address)
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " userdata of pointer to void type." % \
                (pvdata, type(pvdata)))
    else:
        retval = cty.cast(pvdata, cty.POINTER(xfdata.FL_FORM))
    return retval


def fls_convert_ptrvoid_to_ptrflpopup(pvdata):
    """Taking a pointer to void param (from a callback/handler function just
    invoked) and re-casts it to a ptr_flpopup and returns it so user can
    retrieve real value passed to function caller. It is the counterpart
    of library.convert_userdata_to_ptrvoid()."""

    retval = None
    if not isinstance(pvdata, int):
        # void * is considered int by ctypes when passed (memory address)
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " userdata of pointer to void type." % \
                (pvdata, type(pvdata)))
    else:
        retval = cty.cast(pvdata, cty.POINTER(xfdata.FL_POPUP))
    return retval


def fls_convert_ptrvoid_to_ptrlongc(pvdata):
    """Taking a pointer to void param (from a callback/handler function just
    invoked) and re-casts it to a pointer to c_long and returns it so user
    can retrieve real value passed to function caller. It is the counterpart
    of library.convert_userdata_to_ptrvoid()."""

    retval = None
    if not isinstance(pvdata, int):
        # void * is considered int by ctypes when passed (memory address)
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " userdata of pointer to void type." % \
                (pvdata, type(pvdata)))
    else:
        retval = cty.cast(pvdata, cty.POINTER(cty.c_long))
    return retval


def fls_convert_ptrvoid_to_ptrfloatc(pvdata):
    """Taking a pointer to void param (from a callback/handler function just
    invoked) and re-casts it to a pointer to c_double and returns it so user
    can retrieve real value passed to function caller. It is the counterpart
    of library.convert_userdata_to_ptrvoid()."""

    retval = None
    if not isinstance(pvdata, int):
        # void * is considered int by ctypes when passed (memory address)
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " userdata of pointer to void type." % \
                (pvdata, type(pvdata)))
    else:
        retval = cty.cast(pvdata, cty.POINTER(cty.c_double))
    return retval


def fls_convert_ptrvoid_to_ptrstringc(pvdata):
    """Taking a pointer to void param (from a callback/handler function just
    invoked) and re-casts it to a pointer to c_char_p and returns it so user
    can retrieve real value passed to function caller. It is the counterpart
    of library.convert_userdata_to_ptrvoid()."""

    retval = None
    if not isinstance(pvdata, int):
        # void * is considered int by ctypes when passed (memory address)
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " userdata of pointer to void type." % \
                (pvdata, type(pvdata)))
    else:
        retval = cty.cast(pvdata, cty.POINTER(cty.c_char_p))
    return retval


# TODO: verify where can be used this one.
def fls_convert_ptrvoid_to_ptrxevent(pvdata):
    """Taking a pointer to void param (from a callback/handler function just
    invoked) and re-casts it to a pointer to xfdata.XEvent and returns it so
    user can retrieve real value passed to function caller."""

    retval = None
    if not isinstance(pvdata, int):
        # void * is considered int by ctypes when passed (memory address)
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " userdata of pointer to void type." % \
                (pvdata, type(pvdata)))
    else:
        retval = cty.cast(pvdata, cty.POINTER(xfdata.XEvent))
    return retval

