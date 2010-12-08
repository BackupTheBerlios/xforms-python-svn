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


import ctypes as cty
from xformslib import vers
from xformslib import xfdata
from xformslib import library


def make_flpopupitem(dictofpopupitems):
    """make_flpopupitem(dictofpopupitems) -> pPopupItem

    Taking a python dict (for one dict item) with a structure corresponding
    to xfdata.FL_POPUP_ITEM prepares and returns a C-compatible pointer
    to xfdata.FL_POPUP_ITEM. """

    # one dict
    if isinstance(dictofpopupitems, dict):

        pyclstext = dictofpopupitems['text']
        print pyclstext
        spitext = library.convert_to_string(pyclstext)
        print spitext
        if 'callback' in dictofpopupitems:
            pyclscallback = dictofpopupitems['callback']
            print pyclscallback
        else:                       # no callback passed
            pyclscallback = library.donothing_popupcb
        c_picallback = xfdata.FL_POPUP_CB(pyclscallback)
        print c_picallback
        pyclsshortcut = dictofpopupitems['shortcut']
        print pyclsshortcut
        spishortcut = library.convert_to_string(pyclsshortcut)
        print spishortcut
        pyclstype = dictofpopupitems['type']
        print pyclstype
        library.checkfatal_allowed_value_in_list(pyclstype, \
                xfdata.POPUPTYPE_list)
        ipitype = library.convert_to_int(pyclstype)
        print ipitype
        pyclsstate = dictofpopupitems['state']
        print pyclsstate
        library.checkfatal_allowed_value_in_list(pyclsstate, \
                xfdata.POPUPSTATE_list)
        ipistate = library.convert_to_int(pyclsstate)
        print ipistate

        popupitem = (xfdata.FL_POPUP_ITEM * 2)()
        popupitem[0].text = spitext
        popupitem[0].callback = c_picallback
        popupitem[0].shortcut = spishortcut
        popupitem[0].type = ipitype
        popupitem[0].state = ipistate
        popupitem[1].text = None    # this ends array, preventing SegFault
        print popupitem

        ppopupitem = cty.pointer(popupitem[0])
        print popupitem, popupitem[0], ppopupitem
        library.keep_cfunc_refs(pyclscallback, c_picallback)
        library.keep_elem_refs(dictofpopupitems, pyclstext, spitext, \
                pyclsshortcut, spishortcut, pyclstype, ipitype, pyclsstate, \
                ipistate, popupitem, ppopupitem)
        return ppopupitem

    # more dicts
    elif isinstance(dictofpopupitems, list):
        
        dictlength = len(dictofpopupitems)
        popupitem = (xfdata.FL_POPUP_ITEM * (dictlength+1))()
        pyclstext = spitext = [" "] * dictlength
        pyclscallback = c_picallback = [None] * dictlength
        pyclsshortcut = spishortcut = [" "] * dictlength
        pyclstype = ipitype = [0] * dictlength
        pyclsstate = ipistate = [0] * dictlength

        for numb in range(0, dictlength):
            pyclstext[numb] = dictofpopupitems[numb]['text']
            print pyclstext[numb]
            spitext[numb] = library.convert_to_string(pyclstext[numb])
            print spitext[numb]
            if 'callback' in dictofpopupitems[numb]:
                pyclscallback[numb] = dictofpopupitems[numb]['callback']
                print pyclscallback[numb]
            else:                       # no callback passed
                pyclscallback[numb] = library.donothing_popupcb
            c_picallback[numb] = xfdata.FL_POPUP_CB(pyclscallback[numb])
            print c_picallback[numb]
            pyclsshortcut[numb] = dictofpopupitems[numb]['shortcut']
            print pyclsshortcut[numb]
            spishortcut[numb] = library.convert_to_string(pyclsshortcut[numb])
            print spishortcut[numb]
            pyclstype[numb] = dictofpopupitems[numb]['type']
            print pyclstype[numb]
            library.checkfatal_allowed_value_in_list(pyclstype[numb], \
                    xfdata.POPUPTYPE_list)
            ipitype[numb] = library.convert_to_int(pyclstype[numb])
            print ipitype[numb]
            pyclsstate[numb] = dictofpopupitems[numb]['state']
            print pyclsstate[numb]
            library.checkfatal_allowed_value_in_list(pyclsstate[numb], \
                    xfdata.POPUPSTATE_list)
            ipistate[numb] = library.convert_to_int(pyclsstate[numb])
            print ipistate[numb]

            popupitem[numb].text = spitext[numb]
            popupitem[numb].callback = c_picallback[numb]
            popupitem[numb].shortcut = spishortcut[numb]
            popupitem[numb].type = ipitype[numb]
            popupitem[numb].state = ipistate[numb]

            library.keep_cfunc_refs(pyclscallback[numb], c_picallback[numb])
            library.keep_elem_refs(pyclstext[numb], spitext[numb], pyclsshortcut[numb],
                spishortcut[numb], pyclstype[numb], ipitype[numb],
                pyclsstate[numb], ipistate[numb],)

        popupitem[-1].text = None    # this ends array, preventing SegFault

        ppopupitem = cty.pointer(popupitem[0])
        print "popupitem", popupitem, "popupitem[0]", popupitem[0], "ppopupitem", ppopupitem
        library.keep_elem_refs(dictofpopupitems, popupitem, ppopupitem)

        return ppopupitem

    else:
        raise library.XFormsTypeError("Parameter %s (of type %s) must be a " \
                "python dict or a python list of dicts" % \
                (dictofpopupitems, type(dictofpopupitems)))


# ***** following functions are not used now *****
#def create_pPopupItem_from_dict(dictofpopupitems):
#    """ create_pPopupItem_from_dict(dictofpopupitems) -> pPopupItem
#
#    Taking a python dict (for one dict item ONLY) with a structure similar
#    to xfdata.FL_POPUP_ITEM prepares and returns a C-compatible pointer
#    to xfdata.FL_POPUP_ITEM. """
#    if not isinstance(dictofpopupitems, dict):
#        raise XFormsTypeError("Parameter %s (of type %s) must be a python" \
#                        " dict" % (dictofpopupitems, type(dictofpopupitems)))
#
#    pyclstext = dictofpopupitems['text']
#    print pyclstext
#    spitext = convert_to_string(pyclstext)
#    print spitext
#    if 'callback' in dictofpopupitems:
#        pyclscallback = dictofpopupitems['callback']
#        print pyclscallback
#    else:                       # no callback passed
#        pyclscallback = donothing_popupcb
#    c_picallback = xfdata.FL_POPUP_CB(pyclscallback)
#    print c_picallback
#    pyclsshortcut = dictofpopupitems['shortcut']
#    print pyclsshortcut
#    spishortcut = convert_to_string(pyclsshortcut)
#    print spishortcut
#    pyclstype = dictofpopupitems['type']
#    print pyclstype
#    checkfatal_allowed_value_in_list(pyclstype, xfdata.POPUPTYPE_list)
#    ipitype = convert_to_int(pyclstype)
#    print ipitype
#    pyclsstate = dictofpopupitems['state']
#    print pyclsstate
#    checkfatal_allowed_value_in_list(pyclsstate, xfdata.POPUPSTATE_list)
#    ipistate = convert_to_int(pyclsstate)
#    print ipistate
#
#    popupitem = (xfdata.FL_POPUP_ITEM * 2)()
#    popupitem[0].text = spitext
#    popupitem[0].callback = c_picallback
#    popupitem[0].shortcut = spishortcut
#    popupitem[0].type = ipitype
#    popupitem[0].state = ipistate
#    popupitem[1].text = None        # this ends array, preventing SegFault#
#
#    ppopupitem = cty.pointer(popupitem[0])
#    print popupitem, popupitem[0], ppopupitem
#    keep_cfunc_refs(pyclscallback, c_picallback)
#    keep_elem_refs(dictofpopupitems, pyclstext, spitext, pyclsshortcut,
#                spishortcut, pyclstype, ipitype, pyclsstate, ipistate,
#                popupitem, ppopupitem)
#    return popupitem[0], ppopupitem


#def create_pPopupItem_from_list(listofpopupitems):
#    """ create_pPopupItem_from_list(listofpopupitems) -> pPopupItem
#
#    Taking a python single list/several lists of popup items, with
#    elements in the same order as xfdata.FL_POPUP_ITEM (text, callback,
#    shortcut, type, state) prepares and returns a C-compatible pointer to
#    xfdata.FL_POPUP_ITEM."""
#    # hack to manage both single list and a list of several lists passed as
#    # arguments
#    try:
#        tmpval = listofpopupitems[1][0]
#        tmpval = tmpval
#
#    except TypeError:
#        if not isinstance(listofpopupitems, (list, tuple)):
#            raise XFormsTypeError("Parameter %s (of type %s) must be a " \
#                "python list or tuple" % (listofpopupitems, \
#                type(listofpopupitems)))
#
#        # only one list passed (array of 2 member)
#        popupitem = (xfdata.FL_POPUP_ITEM * 2)()   # 1 list and 1 None
#
#        spitext = convert_to_string(listofpopupitems[0])
#        popupitem[0].text = spitext
#        print spitext
#        c_picallback = xfdata.FL_POPUP_CB(listofpopupitems[1])
#        print c_picallback
#        popupitem[0].callback = c_picallback
#        spishortcut = convert_to_string(listofpopupitems[2])
#        popupitem[0].shortcut = spishortcut
#        print spishortcut
#        checkfatal_allowed_value_in_list(listofpopupitems[3], \
#            xfdata.POPUPTYPE_list)
#        ipitype = convert_to_int(listofpopupitems[3])
#        popupitem[0].type = ipitype
#        print ipitype
#        checkfatal_allowed_value_in_list(listofpopupitems[4], \
#            xfdata.POPUPSTATE_list)
#        ipistate = convert_to_int(listofpopupitems[4])
#        popupitem[0].state = ipistate
#        print ipistate
#
#        popupitem[1].text = None      # ends array, preventing SegFault
#        print popupitem
#
#        ppopupitem = cty.pointer(popupitem[0])
#        print ppopupitem
#        keep_cfunc_refs(listofpopupitems[1], c_picallback)
#        keep_elem_refs(spitext, spishortcut, ipitype, ipistate,
#                       listofpopupitems, popupitem, ppopupitem)
#        return ppopupitem
#        # end of 1 list
#
#    else:
#        if not isinstance(listofpopupitems, (list, tuple)):
#            raise XFormsTypeError("Parameter %s (of type %s) must be a " \
#                "python list or tuple" % (listofpopupitems, \
#                type(listofpopupitems)))
#
#        # series of lists passed (array of n+1 members)
#        numarray = len(listofpopupitems)
#        lngarray = numarray + 1         # consider final None
#        popupitem = (xfdata.FL_POPUP_ITEM * lngarray)()
#        curitem = 0
#
#        for indx in range(0, numarray):
#            spitext = convert_to_string(listofpopupitems[indx][0])
#            popupitem[indx].text = spitext
#            c_picallback = xfdata.FL_POPUP_CB(listofpopupitems[indx][1])
#            popupitem[indx].callback = c_picallback
#            spishortcut = convert_to_string(listofpopupitems[indx][2])
#            popupitem[indx].shortcut = spishortcut
#            checkfatal_allowed_value_in_list(listofpopupitems[indx][3], \
#                                      xfdata.POPUPTYPE_list)
#            ipitype = convert_to_int(listofpopupitems[indx][3])
#            popupitem[indx].type = ipitype
#            checkfatal_allowed_value_in_list(listofpopupitems[indx][4], \
#                                      xfdata.POPUPSTATE_list)
#            ipistate = convert_to_int(listofpopupitems[indx][4])
#            popupitem[indx].state = ipistate
#
#            keep_cfunc_refs(listofpopupitems[indx][1], c_picallback)
#            keep_elem_refs(popupitem[indx], spitext, spishortcut,
#                           ipitype, ipistate)
#            curitem = indx
#
#        curitem += 1
#        popupitem[curitem].text = None    # ends array, preventing SegFault
#        ppopupitem = cty.pointer(popupitem[0])
#        keep_elem_refs(listofpopupitems, popupitem, ppopupitem)
#        return ppopupitem
#        # end of series of lists


#def create_argslist_for_entrytxt(singlelist, elemsnum):
#    """Handles mutable arguments of e.g. fl_popup_add_entries
#    singlelist has following format:
#    ["entrytxt sometext", series of special sequencies params]
#    Elements not inserted are replaced by None. Then they are converted
#    to some ctypes types when possible.
#    """

#    singlelist2 = singlelist[:]      # use a copy to be manipulated
#    finallist = elemsnum * [None]
#    while len(singlelist2) < elemsnum:
#        singlelist2.append(None)
#    singlelist2[0] = convert_to_string(singlelist2[0])  # 1st must be a str
#    for e in range(0, len(singlelist2)):
#        if not singlelist2[e]:
#            # it is None
#            finallist[e] = cty.cast(singlelist2[e], cty.c_void_p)
#        elif isinstance(singlelist2[e], str):
#            # it is a str
#            finallist[e] = convert_to_string(singlelist2[e])
#        elif hasattr(singlelist2[e], '__call__'):
#            # it is a function
#            finallist[e] = xfdata.FL_POPUP_CB(singlelist2[e])
#            keep_cfunc_refs(finallist[e], singlelist2[e])
#        elif isinstance(singlelist2[e], cty.POINTER(xfdata.FL_POPUP)):
#            # it is a popup
#            finallist[e] = cty.cast(singlelist2[e], \
#                cty.POINTER(xfdata.FL_POPUP))
#        elif isinstance(singlelist2[e], long):
#            # it is a long (maybe from %x)
#            finallist[e] = convert_to_long(singlelist2[e])
#        else:
#            # every other type
#            finallist[e] = singlelist2[e]
#    return singlelist2, finallist


