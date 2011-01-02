#!/usr/bin/env python
# -*- coding: iso8859-1 -*-

""" Support functions to deal with xforms-python wrapper's functions.
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

#######################################################################
# This file contains support functions to manage Structures contained
# in xfdata who can be passed directly to a function..
#######################################################################


import os
import ctypes as cty
from xformslib import xfdata
from xformslib import library


def make_flpopupitem(dictpopupitems):
    """make_flpopupitem(dictpopupitems) -> ptr_flpopupitem

    Taking a python dict (for one dict item) or a python list of dicts (for
    more than one dict item) with keys corresponding to xfdata.FL_POPUP_ITEM
    attributes, prepares and returns a C-compatible pointer to
    xfdata.FL_POPUP_ITEM. Keys are: 'text', 'callback', 'shortcut', 'type'
    and 'state'."""

    # one dict
    if isinstance(dictpopupitems, dict):

        if not 'text' in dictpopupitems:      # no text passed
            raise library.XFormsTypeError("make_flpopupitem dict (whose "
                    "contents is %s) should have a 'text' key" % \
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
            raise library.XFormsTypeError("make_flpopupitem dict (whose "
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
                raise library.XFormsTypeError("make_flpopupitem dict (whose"
                        " contents is %s) should have a 'text' key" % \
                        dictpopupitems[numb])
            else:
                pyclstext[numb] = dictpopupitems[numb]['text']
                s_clstext[numb] = library.convert_to_stringc(pyclstext[numb])
            if not 'callback' in dictpopupitems[numb]:
                pyclscallback[numb] = donothing_flpopupcb
            else:                       # no callback passed
                pyclscallback[numb] = dictpopupitems[numb]['callback']
                cfn_clscallback[numb] = xfdata.FL_POPUP_CB(pyclscallback[numb])
            if not 'shortcut' in dictpopupitems[numb]:  # no shortcut passed
                raise library.XFormsTypeError("make_flpopupitem dict (whose "
                        "contents is %s) should have a 'shortcut' key" % \
                        dictpopupitems[numb])
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


def make_fliopt(dictfliopt):
    """make_fliopt(dictfliopt) -> ptr_fliopt

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


def make_flcmdopt(dictflcmdopt):
    """make_flcmdopt(dictflcmdopt) -> ptr_flcmdopt

    Taking a python dict (for one dict item) or a list of dicts (for more
    than one dict item) with keys corresponding to xfdata.FL_CMD_OPT
    attributes, prepares and returns a C-compatible pointer to
    xfdata.FL_CMD_OPT. Keys are: 'option', 'specifier', 'argKind',
    'value'."""

    # one dict
    if isinstance(dictflcmdopt, dict):

        if not 'option' in dictflcmdopt:      # no option passed
            raise library.XFormsTypeError("make_flcmdopt dict (whose "
                    "contents is %s) should have a 'option' key" % \
                    dictflcmdopt)
        else:
            pyoption = dictflcmdopt['option']
            s_option = library.convert_to_stringc(pyoption)

        if not 'specifier' in dictflcmdopt:   # no specifier passed
            raise library.XFormsTypeError("make_flcmdopt dict (whose "
                    "contents is %s) should have a 'specifier' key" % \
                    dictflcmdopt)
        else:
            pyspecifier = dictflcmdopt['specifier']
            s_specifier = library.convert_to_stringc(pyspecifier)

        if not 'argKind' in dictflcmdopt:     # no argKind passed
            raise library.XFormsTypeError("make_flcmdopt dict (whose "
                    "contents is %s) should have a 'argKind' key" % \
                    dictflcmdopt)
        else:
            pyargKind = dictflcmdopt['argKind']
            i_argKind = library.convert_to_intc(pyargKind)

        if not 'value' in dictflcmdopt:       # no value passed
            raise library.XFormsTypeError("make_flcmdopt dict (whose "
                    "contents is %s) should have a 'value' key" % \
                    dictflcmdopt)
        else:
            pyvalue = dictflcmdopt['value']
            s_value = library.convert_to_stringc(pyvalue)

        flcmdopt = xfdata.FL_CMD_OPT()      # * 2)()
        flcmdopt.option = s_option
        flcmdopt.specifier = s_specifier
        flcmdopt.argKind = i_argKind
        flcmdopt.value = s_value
        #flcmdopt[1].text = None    # this ends array, preventing SegFault

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
                raise library.XFormsTypeError("make_flcmdopt dict (whose "
                        "contents is %s) should have a 'option' key" % \
                        dictflcmdopt[numb])
            else:
                pyoption[numb] = dictflcmdopt[numb]['option']
                s_option[numb] = library.convert_to_stringc(pyoption[numb])
            if not 'specifier' in dictflcmdopt[numb]:   # no specifier passed
                raise library.XFormsTypeError("make_flcmdopt dict (whose "
                        "contents is %s) should have a 'specifier' key" % \
                        dictflcmdopt[numb])
            else:
                pyspecifier[numb] = dictflcmdopt[numb]['specifier']
                s_specifier[numb] = library.convert_to_stringc( \
                        pyspecifier[numb])
            if not 'argKind' in dictflcmdopt[numb]:     # no argKind passed
                raise library.XFormsTypeError("make_flcmdopt dict (whose "
                        "contents is %s) should have a 'argKind' key" % \
                        dictflcmdopt[numb])
            else:
                pyargKind[numb] = dictflcmdopt[numb]['argKind']
                i_argKind[numb] = library.convert_to_intc(pyargKind[numb])
            if not 'value' in dictflcmdopt[numb]:       # no value passed
                raise library.XFormsTypeError("make_flcmdopt dict (whose "
                        "contents is %s) should have a 'value' key" % \
                        dictflcmdopt[numb])
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


def make_flresource(dictflresource):
    """make_flresource(dictflresource) -> ptr_flresource

    Taking a python dict (for one dict item) or a list of dicts (for more
    than one dict item) with keys corresponding to xfdata.FL_RESOURCE
    attributes prepares and returns a C-compatible pointer to
    xfdata.FL_RESOURCE. Keys are: 'res_name', 'res_class', 'type', 'var',
    'defval', 'nbytes'."""

    # one dict
    if isinstance(dictflresource, dict):

        if not 'res_name' in dictflresource:      # no res_name passed
            raise library.XFormsTypeError("make_flresource dict (whose "
                    "contents is %s) should have a 'res_name' key" % \
                    dictflresource)
        else:
            pyclsresname = dictflresource['res_name']
            s_clsresname = library.convert_to_stringc(pyclsresname)
        if not 'res_class' in dictflresource:   # no res_class passed
            raise library.XFormsTypeError("make_flresource dict (whose "
                    "contents is %s) should have a 'res_class' key" % \
                    dictflresource)
        else:
            pyclsresclass = dictflresource['res_class']
            s_clsresclass = library.convert_to_stringc(pyclsresclass)
        if not 'type' in dictflresource:     # no type passed
            raise library.XFormsTypeError("make_flresource dict (whose "
                    "contents is %s) should have a 'type' key" % \
                    dictflresource)
        else:
            pyclstype = dictflresource['type']
            i_clstype = library.convert_to_intc(pyclstype)
        if not 'var' in dictflresource:       # no var passed
            raise library.XFormsTypeError("make_flresource dict (whose "
                    "contents is %s) should have a 'var' key" % \
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
            raise library.XFormsTypeError("make_flresource dict (whose "
                    "contents is %s) should have a 'defval' key" % \
                    dictflresource)
        else:
            pyclsdefval = dictflresource['defval']
            s_clsdefval = library.convert_to_stringc(pyclsdefval)
        if not 'nbytes' in dictflresource:     # no nbytes passed
            raise library.XFormsTypeError("make_flresource dict (whose "
                    "contents is %s) should have a 'nbytes' key" % \
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
                raise library.XFormsTypeError("make_flresource dict (whose "
                        "contents is %s) should have a 'res_name' key" % \
                        dictflresource[numb])
            else:
                pyclsresname[numb] = dictflresource[numb]['res_name']
                s_clsresname[numb] = library.convert_to_stringc( \
                        pyclsresname[numb])
            if not 'res_class' in dictflresource[numb]:  # no res_class passed
                raise library.XFormsTypeError("make_flresource dict (whose "
                        "contents is %s) should have a 'res_class' key" % \
                        dictflresource[numb])
            else:
                pyclsresclass[numb] = dictflresource[numb]['res_class']
                s_clsresclass[numb] = library.convert_to_stringc( \
                        pyclsresclass[numb])
            if not 'type' in dictflresource[numb]:     # no type passed
                raise library.XFormsTypeError("make_flresource dict (whose "
                        "contents is %s) should have a 'type' key" % \
                        dictflresource[numb])
            else:
                pyclstype[numb] = dictflresource[numb]['type']
                i_clstype[numb] = library.convert_to_intc(pyclstype[numb])
            if not 'var' in dictflresource[numb]:       # no var passed
                raise library.XFormsTypeError("make_flresource dict (whose "
                        "contents is %s) should have a 'var' key" % \
                        dictflresource[numb])
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
                raise library.XFormsTypeError("make_flresource dict (whose "
                        "contents is %s) should have a 'defval' key" % \
                        dictflresource[numb])
            else:
                pyclsdefval[numb] = dictflresource[numb]['defval']
                s_clsdefval[numb] = library.convert_to_stringc( \
                        pyclsdefval[numb])
            if not 'nbytes' in dictflresource[numb]:     # no nbytes passed
                raise library.XFormsTypeError("make_flresource dict (whose "
                        "contents is %s) should have a 'nbytes' key" % \
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

        #flcmdopt[-1].option = ""    # this ends array, preventing SegFault

        ptr_flresource = cty.pointer(structflresource[0])
        library.keep_elem_refs(dictflresource, ptr_flresource, \
                structflresource)
        return ptr_flresource

    else:
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " a python dict or a list of dicts" % \
                (dictflresource, type(dictflresource)))


def make_flpopupcb(pyfn_popupcb):
    """make_flpopupcb(pyfn_popupcb) -> cfn_popupcb

    Taking a python callback function name, prapares and returns a
    C-compatible xfdata.FL_POPUP_CB function."""

    if hasattr(pyfn_popupcb, '__call__'):
        cfn_popupcb = xfdata.FL_POPUP_CB(pyfn_popupcb)
        library.keep_cfunc_refs(pyfn_popupcb, cfn_popupcb)
        return cfn_popupcb
    else:
        raise library.XFormsTypeError("Parameter %s (of type %s) must be" \
                " a python function" % (pyfn_popupcb, type(pyfn_popupcb)))


def donothing_flpopupcb(ptr_flpopupreturn):
    """ Replaces a callback function not defined for class instances
        as e.g. xfdata.FL_POPUP_ITEM."""
    return 0


def import_xbmdata_from_file(fname):
    """import_xbmdata_from_file(fname) -> width, height, xbmcontents

    Taking a .xbm filename, it reads it and returns all elements, to be used
    with flbitmap.fl_set_bitmapbutton_data()."""

    width = 0
    height = 0
    tmpxbmcontents1 = ""
    tmpxbmcontents2 = ""
    xbmcontents = []

    if fname.endswith(".xbm") or fname.endwith(".XBM"):
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
                raise XFormsValueError("File %s has an incorrect format." % \
                        fname)
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


def import_xpmdata_from_file(fname):
    """import_xpmdata_from_file(fname) -> xpmcontents

    Taking a .xpm filename, it reads it and returns contents, to be used
    with flbitmap.fl_set_pixmapbutton_data()."""

    tmpxpmcontents1 = ""
    tmpxpmcontents2 = ""
    xpmcontents = []

    if fname.endswith(".xpm") or fname.endwith(".XPM"):
        if os.path.exists(fname):
            try:
                xbmfil = open(fname)
            except IOError:
                raise library.XFormsGenericError("File %s cannot be opened." \
                        % fname)
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
                raise XFormsValueError("File %s has an incorrect format." % \
                        fname)
            xpmcontents = tmpxpmcontents2.split(",")
            return xpmcontents

        else:   # not existing
            raise library.XFormsGenericError("File %s does not exist." % fname)
    else:       # not a .xbm file
        raise library.XFormsGenericError("File %s should be a .xpm file." % \
                fname)

