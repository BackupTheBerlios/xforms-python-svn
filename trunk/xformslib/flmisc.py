#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" xforms-python's functions to manage miscellaneous flobjects.
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


##################
# forms.h (box.h)
##################

# fl_create_box function placeholder (internal)


def fl_add_box(boxtype, xpos, ypos, width, height, label):
    """fl_add_box(boxtype, xpos, ypos, width, height, label) -> ptr_flobject

    Adds a ractangular box area flobject. It is simply used to give the
    dialogue form a nicer appearance. It can be used to visually group other
    objects together. The bottom of each form is a box.

    Parameters
    ----------
        boxtype : int
            type of the box to be added. Values (from xfdata.py)
            - FL_NO_BOX (No box at all, it is transparent, just a label),
            - FL_UP_BOX (A box that comes out of the screen),
            - FL_DOWN_BOX (A box that goes down into the screen),
            - FL_BORDER_BOX (A flat box with a border),
            - FL_SHADOW_BOX (A flat box with a shadow),
            - FL_FRAME_BOX (A flat box with an engraved frame),
            - FL_ROUNDED_BOX (A rounded box),
            - FL_EMBOSSED_BOX (A flat box with an embossed frame),
            - FL_FLAT_BOX (A flat box without a border, normally invisible
              unless given a different color than the surroundings),
            - FL_RFLAT_BOX (A rounded box without a border, normally invisible
              unless given a different color than the surroundings),
            - FL_RSHADOW_BOX (A rounded box with a shadow),
            - FL_OVAL_BOX (A box shaped like an ellipse),
            - FL_ROUNDED3D_UPBOX (A rounded box coming out of the screen),
            - FL_ROUNDED3D_DOWNBOX (A rounded box going into the screen),
            - FL_OVAL3D_UPBOX (An oval box coming out of the screen),
            - FL_OVAL3D_DOWNBOX (An oval box going into the screen),
            - FL_OVAL3D_FRAMEBOX (An oval box with an engraved frame),
            - FL_OVAL3D_EMBOSSEDBOX (An oval box with an embossed frame)
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            text label of box

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            box flobject added

    Examples
    --------
        >>> pboxobj = fl_add_box(xfdata.FL_UP_BOX, 120, 150, 200, 250,
                "MyBox")

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_add_box = library.cfuncproto(
        library.load_so_libforms(), "fl_add_box",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_box(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_flinitialized()
    library.checkfatal_allowed_value_in_list(boxtype, xfdata.BOXTYPE_list)
    i_boxtype = library.convert_to_intc(boxtype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_bytestrc(label)
    library.keep_elem_refs(boxtype, xpos, ypos, width, height, label, \
            i_boxtype, i_xpos, i_ypos, i_width, i_height, s_label)
    retval = _fl_add_box(i_boxtype, i_xpos, i_ypos, i_width, \
            i_height, s_label)
    return retval


#####################
# forms.h (choice.h)
#####################

# fl_create_choice() function placeholder (internal and deprecated)
# fl_add_choice() function placeholder (deprecated)
# fl_clear_choice() function placeholder (deprecated)
# fl_addto_choice() function placeholder (deprecated)
# fl_replace_choice() function placeholder (deprecated)
# fl_delete_choice() function placeholder (deprecated)
# fl_set_choice() function placeholder (deprecated)
# fl_set_choice_text() function placeholder (deprecated)
# fl_get_choice() function placeholder (deprecated)
# fl_get_choice_item_text() function placeholder (deprecated)
# fl_get_choice_maxitems() function placeholder (deprecated)
# fl_get_choice_text() function placeholder (deprecated)
# fl_set_choice_fontsize() function placeholder (deprecated)
# fl_set_choice_fontstyle() function placeholder (deprecated)
# fl_set_choice_align() function placeholder (deprecated)
# fl_get_choice_item_mode() function placeholder (deprecated)
# fl_set_choice_item_mode() function placeholder (deprecated)
# fl_set_choice_item_shortcut() function placeholder (deprecated)
# fl_set_choice_item_entries() function placeholder (deprecated)
# fl_set_choice_notitle() function placeholder (deprecated)



#################################
# forms.h (clipbd.h)
# prototypes for clipboard stuff
#################################

# TODO: in X11 XStoreBuffer seems to take char * as data
def fl_stuff_clipboard(ptr_flobject, clipbdtype, datablock, size, \
        pyfn_LoseSelectionCb):
    """fl_stuff_clipboard(ptr_flobject, clipbdtype, datablock, size,
    pyfn_LoseSelectionCb) -> size

    Stores data in clipboard, read-write buffer shared by all applications
    running on the X server.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            clipboard flobject
        clipbdtype : long
            type of clipboard (not used)
        datablock : pointer to void?
            data contents to be stored (in str?) *todo*
        size : long
            size (in bytes) of the contents pointed to by datablock.
        pyfn_LoseSelectionCb : python function callback, returned unused value
            name referring to function(ptr_flobject, [long]type) -> [int]num.
            Function to be invoked if selection is lost; type is unused. For
            textual content the application that loses the clipboard should
            typically undo the visual cues about the selection.

    Returns
    -------
        size : int
            size of stuffed data?, or 0 (on failure)

    Examples
    --------
            >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    #FL_LOSE_SELECTION_CB = cty.CFUNCTYPE(cty.c_int, cty.POINTER( \
    #                       xfdata.FL_OBJECT), cty.c_long)
    _fl_stuff_clipboard = library.cfuncproto(
        library.load_so_libforms(), "fl_stuff_clipboard",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_long, cty.c_void_p,
        cty.c_long, xfdata.FL_LOSE_SELECTION_CB],
        """int fl_stuff_clipboard(FL_OBJECT * ob, long int type,
           const char * data, long int size,
           FL_LOSE_SELECTION_CB lose_callback)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    l_clipbdtype = library.convert_to_longc(clipbdtype)
    ptr_vdata = cty.cast(datablock, cty.c_void_p)
    l_size = library.convert_to_longc(size)
    library.verify_function_type(pyfn_LoseSelectionCb)
    cfn_LoseSelectionCb = xfdata.FL_LOSE_SELECTION_CB(pyfn_LoseSelectionCb)
    library.keep_cfunc_refs(cfn_LoseSelectionCb, pyfn_LoseSelectionCb)
    library.keep_elem_refs(ptr_flobject, clipbdtype, datablock, size, \
            l_clipbdtype, ptr_vdata, l_size)
    retval = _fl_stuff_clipboard(ptr_flobject, l_clipbdtype, ptr_vdata, \
            l_size, cfn_LoseSelectionCb)
    return retval


def fl_request_clipboard(ptr_flobject, clipbdtype, pyfn_SelectionCb):
    """fl_request_clipboard(ptr_flobject, clipbdtype, pyfn_SelectionCb)
    -> result

    Retrieves data previously stuffed into the clipboard. Contents is
    available in invoked callback function.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            clipboard flobject
        clipbdtype : long
            type of clipboard (not used)
        pyfn_SelectionCb : python function callback, returned value
            name referring to function(ptr_flobject, [long]type,
            [pointer to void]datablock, [long]size) -> [int]num.
            Function to be invoked when the clipboard content is obtained;
            type is unused. The content data passed to the callback
            function should not be modified.

    Returns
    -------
        result : int
            positive number (if the requesting flobject owns the selection,
            i.e. the callback could be invoked before the function returned),
            or 0 (if it does not own the selection), or -1 (if there is no
            selection)

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + NoDemo = Maybe

    """
    #FL_SELECTION_CB = cty.CFUNCTYPE(cty.c_int, cty.POINTER(xfdata.FL_OBJECT),
    #                                cty.c_long, cty.c_void_p, cty.c_long)
    _fl_request_clipboard = library.cfuncproto(
        library.load_so_libforms(), "fl_request_clipboard",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), cty.c_long,
        xfdata.FL_SELECTION_CB],
        """int fl_request_clipboard(FL_OBJECT * ob, long int type,
           FL_SELECTION_CB got_it_callback)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    l_clipbdtype = library.convert_to_longc(clipbdtype)
    library.verify_function_type(pyfn_SelectionCb)
    cfn_SelectionCb = xfdata.FL_SELECTION_CB(pyfn_SelectionCb)
    library.keep_cfunc_refs(cfn_SelectionCb, pyfn_SelectionCb)
    library.keep_elem_refs(ptr_flobject, clipbdtype, l_clipbdtype)
    retval = _fl_request_clipboard(ptr_flobject, l_clipbdtype, \
            cfn_SelectionCb)
    return retval



###################
# forms.h (flps.h)
###################

# postscript stuff


def flps_init():
    """flps_init() -> ptr_flpscontrol

    Customizes the output by changing the PostScript output control parameters.

    Returns
    -------
        ptr_flpscontrol : pointer to xfdata.FLPS_CONTROL
            xfdata.FLPS_CONTROL class instance

    Examples
    --------
        >>> pflpsCntrl = flps_init()

    Notes
    -----
        Status: NN-UTest + Doc + NoDemo = Maybe

    """
    _flps_init = library.cfuncproto(
        library.load_so_libflimage(), "flps_init",
        cty.POINTER(xfdata.FLPS_CONTROL), [],
        """FLPS_CONTROL * flps_init()""")
    library.check_if_flinitialized()
    retval = _flps_init()
    return retval


def fl_object_ps_dump(ptr_flobject, fname):
    """fl_object_ps_dump(ptr_flobject, fname) -> result

    Finds out hardcopies of some flobjects in a what-you-see-is-what-you-get
    (WYSIWYG) way, especially those that are dynamic and of vector-graphics in
    nature. It outputs the specified flobject in PostScript. The flobject must
    be visible at the time of the function call. The hardcopy should mostly be
    WYSIWYG and centered on the printed page. The orientation is determined
    such that a balanced margin results, i.e., if the width of the flobject is
    larger than the height, landscape mode will be used. Further, if the
    flobject is too big to fit on the printed page, a scale factor will be
    applied so the flobject fits. The box underneath the flobject is by
    default not drawn and in the default black&white mode, all curves are
    drawn in black.

    Parameters
    ----------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            object. Only the xfdata.FL_XYPLOT flobject is supported.
        fname : str
            name of output file. If it is empty (""), a fselector will be
            shown to ask the user for a file name.

    Returns
    -------
        result : int
            0 (on success), or -1 (on errors)

    Examples
    --------
        >>> if fl_object_ps_dump(pxyplobj, "myhardcopy.ps") < 0:
        >>> ... <something>

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_object_ps_dump = library.cfuncproto(
        library.load_so_libflimage(), "fl_object_ps_dump",
        cty.c_int, [cty.POINTER(xfdata.FL_OBJECT), xfdata.STRING],
        """int fl_object_ps_dump(FL_OBJECT * ob, const char * fname)""")
    library.check_if_flinitialized()
    library.verify_flobjectptr_type(ptr_flobject)
    s_fname = library.convert_to_bytestrc(fname)
    library.keep_elem_refs(ptr_flobject, fname, s_fname)
    retval = _fl_object_ps_dump(ptr_flobject, s_fname)
    return retval


####################
# forms.h (frame.h)
####################

# fl_create_frame function placeholder (internal)


def fl_add_frame(frametype, xpos, ypos, width, height, label):
    """fl_add_frame(frametype, xpos, ypos, width, height, label)
    -> ptr_flobject

    Adds a frame flobject. It is simply used to give the dialogue form a nicer
    appearance. It can be used to visually group other objects together.
    Frames are almost the same as a box, except that the interior of the
    bounding box is not filled. Use of frames can speed up drawing in certain
    situations, e.g. to place a group of radio buttons within an
    xfdata.FL_ENGRAVED_FRAME. If we were to use an xfdata.FL_FRAME_BOX to
    group the buttons, visually they would look the same; however, the latter
    is faster as we do not have to fill the interior of the bounding box and
    can also reduce flicker. Frames are useful in decorating free objects and
    canvases.

    Parameters
    ----------
        frametype : int
            type of frame to be added. Values (from xfdata.py)
            - FL_NO_FRAME (Nothing is drawn),
            - FL_UP_FRAME (A frame appears coming out of the screen),
            - FL_DOWN_FRAME (A frame that goes down into the screen),
            - FL_BORDER_FRAME (A frame with a simple outline),
            - FL_SHADOW_FRAME (A frame with a shadow),
            - FL_ENGRAVED_FRAME (A frame appears to be engraved),
            - FL_ROUNDED_FRAME (A rounded frame),
            - FL_EMBOSSED_FRAME (A frame appears embossed),
            - FL_OVAL_FRAME (An elliptic box).
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            text label of frame

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            frame flobject added

    Examples
    --------
        >>> frmobj = fl_add_frame(xfdsata.FL_BORDER_FRAME, 100, 100,
                400, 300, "MyFrame")

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_add_frame = library.cfuncproto(
        library.load_so_libforms(), "fl_add_frame",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_frame(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_flinitialized()
    library.checkfatal_allowed_value_in_list(frametype, \
            xfdata.FRAMETYPE_list)
    i_frametype = library.convert_to_intc(frametype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_bytestrc(label)
    library.keep_elem_refs(frametype, xpos, ypos, width, height, label, \
            i_frametype, i_xpos, i_ypos, i_width, i_height, s_label)
    retval = _fl_add_frame(i_frametype, i_xpos, i_ypos, i_width, \
            i_height, s_label)
    return retval


# labeld frame

# fl_create_labelframe() function placeholder (internal)


def fl_add_labelframe(frametype, xpos, ypos, width, height, label):
    """fl_add_labelframe(frametype, xpos, ypos, width, height, label)
    -> ptr_flobject

    Adds a labelframe flobject. It is almost the same as a frame except that
    the label is placed on the frame instead of inside or outside of the
    bounding box as in a regular frame.

    Parameters
    ----------
        frametype : int
            type of labelframe to be added. Values (from xfdata.py)
            - FL_NO_FRAME (Nothing is drawn),
            - FL_UP_FRAME (A frame appears coming out of the screen),
            - FL_DOWN_FRAME (A frame that goes down into the screen),
            - FL_BORDER_FRAME (A frame with a simple outline),
            - FL_SHADOW_FRAME (A frame with a shadow),
            - FL_ENGRAVED_FRAME (A frame appears to be engraved),
            - FL_ROUNDED_FRAME (A rounded frame),
            - FL_EMBOSSED_FRAME (A frame appears embossed),
            - FL_OVAL_FRAME (An elliptic box).
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            text label of labelframe

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            labelframe flobject added

    Examples
    --------
        >>> lfrmobj = fl_add_labelframe(xfdata.FL_SHADOW_FRAME, 100,
                100, 400, 300, "MyFrame")

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_add_labelframe = library.cfuncproto(
        library.load_so_libforms(), "fl_add_labelframe",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_labelframe(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_flinitialized()
    library.checkfatal_allowed_value_in_list(frametype, \
            xfdata.FRAMETYPE_list)
    i_frametype = library.convert_to_intc(frametype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_bytestrc(label)
    library.keep_elem_refs(frametype, xpos, ypos, width, height, label, \
            i_frametype, i_xpos, i_ypos, i_width, i_height, s_label)
    retval = _fl_add_labelframe(i_frametype, i_xpos, i_ypos, i_width, \
            i_height, s_label)
    return retval



#####################
# forms.h (free.h)
# Object Class: Free
#####################

# fl_create_free() function placeholder (internal)


def fl_add_free(freetype, xpos, ypos, width, height, label, pyfn_HandlePtr):
    """fl_add_free(freetype, xpos, ypos, width, height, label, pyfn_HandlePtr)
    -> ptr_flobject

    Adds a free object.

    Parameters
    ----------
        freetype : int
            type of free to be added. Value (from xfdata.py)
            - FL_NORMAL_FREE (The flobject will receive the events FL_DRAW,
              FL_ENTER, FL_LEAVE, FL_MOTION, FL_PUSH, FL_RELEASE and FL_MOUSE),
            - FL_INACTIVE_FREE or FL_SLEEPING_FREE (The flobject only receives
              FL_DRAW events. This should be used for flobjects without
              interaction, e.g. a picture),
            - FL_INPUT_FREE (Same as FL_NORMAL_FREE but the flobject also
              receives FL_FOCUS, FL_UNFOCUS and FL_KEYBOARD events. The
              ptr_flobject.contents.wantkey is by default set to FL_KEY_NORMAL,
              i.e., the free flobject will receive all normal keys (0-255)
              except <Tab> and <Return> key. If you are interested in <Tab> or
              <Return> key, you need to change ptr_flobject.contents.wantkey
              to FL_KEY_TAB or FL_KEY_ALL),
            - FL_CONTINUOUS_FREE (Same as FL_NORMAL_FREE but the flobject also
              receives FL_STEP events. This should be used for flobjects that
              change themselves continuously),
            - FL_ALL_FREE (The flobject receives all types of events).
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            text label of free
        pyfn_HandlePtr : python function, returned value
            name referring to function(ptr_flobject, [int]event, [int]xpos,
            [int]ypos, [int]key, [pointer to void]ptr_xevent) -> [int]num
            Function does the redrawing and handles the interaction with the
            free flobject. First param is the flobject to which the event
            applies; event indicates what has to happen to the object; xpos
            and ypos indicate the position of the mouse (only meaningful with
            mouse related events) relative to the form origin; key is the
            KeySym of the key typed in by the user (only for xfdata.FL_KEYPRESS
            events). ptr_xevent is pointer to X Event that causes the
            invocation of this handler. event and ptr_xevent.contents.type can
            both be used to obtain the event types. The routine should return
            whether the status of the object has changed, i.e., whether
            flbasic.fl_do_forms() or flbasic.fl_check_forms() should return
            this flobject.

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            free flobject added

    Examples
    --------
        >>> *todo*

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    #FL_HANDLEPTR = cty.CFUNCTYPE(cty.c_int, cty.POINTER(FL_OBJECT), \
    #   cty.c_int, FL_Coord, FL_Coord, cty.c_int, cty.c_void_p)
    _fl_add_free = library.cfuncproto(
        library.load_so_libforms(), "fl_add_free",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING,
        xfdata.FL_HANDLEPTR],
        """FL_OBJECT * fl_add_free(int type, FL_Coord x, FL_Coord y,
           FL_Coord w, FL_Coord h, const char * label, FL_HANDLEPTR handle)""")
    library.check_if_flinitialized()
    library.checkfatal_allowed_value_in_list(freetype, xfdata.FREETYPE_list)
    i_freetype = library.convert_to_intc(freetype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_bytestrc(label)
    library.verify_function_type(pyfn_HandlePtr)
    cfn_HandlePtr = xfdata.FL_HANDLEPTR(pyfn_HandlePtr)
    library.keep_cfunc_refs(cfn_HandlePtr, pyfn_HandlePtr)
    library.keep_elem_refs(freetype, xpos, ypos, width, height, label, \
            i_freetype, i_xpos, i_ypos, i_width,i_height, s_label)
    retval = _fl_add_free(i_freetype, i_xpos, i_ypos, i_width, i_height, \
            s_label, cfn_HandlePtr)
    return retval



#####################
# forms.h (menu.h)
# Object Class: Menu
#####################

# fl_create_menu() function placeholder (internal and deprecated)
# fl_add_menu() function placeholder (deprecated)
# fl_clear_menu() function placeholder (deprecated)
# fl_set_menu() function placeholder (deprecated)
# fl_addto_menu() function placeholder (deprecated)
# fl_replace_menu() function placeholder (deprecated)
# fl_delete_menu() function placeholder (deprecated)
# fl_set_menu_item_callback() function placeholder (deprecated)
# fl_set_menu_item_shortcut() function placeholder (deprecated)
# fl_set_menu_item_mode() function placeholder (deprecated)
# fl_show_menu_symbol() function placeholder (deprecated)
# fl_set_menu_popup() function placeholder (deprecated)
# fl_get_menu_popup() function placeholder (deprecated)
# fl_get_menu() function placeholder (deprecated)
# fl_get_menu_item_text() function placeholder (deprecated)
# fl_get_menu_maxitems() function placeholder (deprecated)
# fl_get_menu_item_mode() function placeholder (deprecated)
# fl_get_menu_text() function placeholder (deprecated)
# fl_set_menu_entries() function placeholder (deprecated)
# fl_set_menu_notitle() function placeholder (deprecated)
# fl_set_menu_item_id() function placeholder (deprecated)


###################
# forms.h (text.h)
###################

# fl_create_text() function placeholder (internal)


def fl_add_text(texttype, xpos, ypos, width, height, label):
    """fl_add_text(texttype, xpos, ypos, width, height, label) -> ptr_flobject

    Adds a text flobject. It simply consists of a label maybe placed in a box.

    Parameters
    ----------
        texttype : int
            type of text to be added. Values (from xfdata.py) FL_NORMAL_TEXT
            (Normal text type)
        xpos : int
            horizontal position (upper-left corner)
        ypos : int
            vertical position (upper-left corner)
        width : int
            width in coord units
        height : int
            height in coord units
        label : str
            text label of text

    Returns
    -------
        ptr_flobject : pointer to xfdata.FL_OBJECT
            text flobject added

    Examples
    --------
        >>> ptxtobj = fl_add_text(xfdata.FL_NORMAL_TEXT, 140, 120, 400, 500,
                "My text flobject")

    Notes
    -----
        Status: NA-UTest + Doc + Demo = OK

    """
    _fl_add_text = library.cfuncproto(
        library.load_so_libforms(), "fl_add_text",
        cty.POINTER(xfdata.FL_OBJECT), [cty.c_int, xfdata.FL_Coord,
        xfdata.FL_Coord, xfdata.FL_Coord, xfdata.FL_Coord, xfdata.STRING],
        """FL_OBJECT * fl_add_text(int type, FL_Coord x, FL_Coord y,
            FL_Coord w, FL_Coord h, const char * label)""")
    library.check_if_flinitialized()
    library.checkfatal_allowed_value_in_list(texttype, xfdata.TEXTTYPE_list)
    i_texttype = library.convert_to_intc(texttype)
    i_xpos = library.convert_to_FL_Coord(xpos)
    i_ypos = library.convert_to_FL_Coord(ypos)
    i_width = library.convert_to_FL_Coord(width)
    i_height = library.convert_to_FL_Coord(height)
    s_label = library.convert_to_bytestrc(label)
    library.keep_elem_refs(texttype, xpos, ypos, width, height, label, \
            i_texttype, i_xpos, i_ypos, i_width, i_height, s_label)
    retval = _fl_add_text(i_texttype, i_xpos, i_ypos, i_width, i_height, \
            s_label)
    return retval


###############################
# forms.h (xpopup.h)
# Prototypes for xpop-up menus
###############################

# fl_setpup_entries() function placeholder (deprecated)
# fl_newpup() function placeholder (deprecated)
# fl_defpup() function placeholder (deprecated)
# fl_addtopup() function placeholder (deprecated)
# fl_setpup_mode() function placeholder (deprecated)
# fl_freepup() function placeholder (deprecated)
# fl_dopup() function placeholder (deprecated)
# fl_setpup_default_cursor() function placeholder (deprecated)
# fl_setpup_default_color() function placeholder (deprecated)
# fl_setpup_default_pup_checked_color() function placeholder (deprecated)
# fl_setpup_default_fontsize() function placeholder (deprecated)
# fl_setpup_default_fontstyle() function placeholder (deprecated)
# fl_setpup_fontsize placeholder (deprecated)
# fl_setpup_fontstyle placeholder (deprecated)
# fl_setpup_color placeholder (deprecated)
# fl_setpup_default_checkcolor placeholder (deprecated)
# fl_setpup_checkcolor placeholder (deprecated)
# fl_setpup_default_bw() function placeholder (deprecated)
# fl_setpup_shortcut() function placeholder (deprecated)
# fl_setpup_position() function placeholder (deprecated)
# fl_setpup_selection() function placeholder (deprecated)
# fl_setpup_shadow() function placeholder (deprecated)
# fl_setpup_softedge() function placeholder (deprecated)
# fl_setpup_bw() function placeholder (deprecated)
# fl_setpup_title() function placeholder (deprecated)
# FL_PUP_ENTERCB placeholder (deprecated)
# fl_setpup_entercb() function placeholder (deprecated)
# FL_PUP_LEAVECB placeholder (deprecated)
# fl_setpup_leavecb() function placeholder (deprecated)
# fl_setpup_pad() function placeholder (deprecated)
# fl_setpup_cursor() function placeholder (deprecated)
# fl_setpup_maxpup() function placeholder (deprecated)
# fl_getpup_mode() function placeholder (deprecated)
# fl_getpup_text() function placeholder (deprecated)
# fl_showpup() function placeholder (deprecated)
# fl_hidepup() function placeholder (deprecated)
# fl_getpup_items() function placeholder (deprecated)
# fl_current_pup() function placeholder (deprecated)
# fl_setpup_itemcb() function placeholder (deprecated)
# fl_setpup_menucb() function placeholder (deprecated)
# fl_setpup_submenu() function placeholder (deprecated)
# fl_setpup() function placeholder (deprecated)


# from XForms upstream: the following (fl_fheight) etc. were never documented
# and were removed from V0.89, but apparently this broke some applications
# that were using them. Put them back in 10/22/00

def fl_gc_():
    """fl_gc_() -> gc

    Finds out non-text graphics context.

    Returns
    -------
        gctx : xfdata.GC
            graphics context id

    Examples
    --------
        >>> graphctx = fl_gc_()

    Notes
    -----
        Status: NN-UTest + Doc + NoDemo = Maybe

    """
    _fl_gc_ = library.cfuncproto(
        library.load_so_libforms(), "fl_gc_",
        xfdata.GC, [],
        """GC fl_gc_()""")
    library.check_if_flinitialized()
    retval = _fl_gc_()
    return retval

#fl_gc = fl_gc_()       # commented to prevent a SegmentationFault? --LK
fl_gc = fl_gc_


def fl_textgc_():
    """fl_textgc_() -> txtgc

    Finds out text graphics context,

    Returns
    -------
        txtgc = xfdata.GC
            graphics context id

    Examples
    --------
        >>> graphctx = fl_textgc_()

    Notes
    -----
        Status: NN-UTest + Doc + NoDemo = Maybe

    """
    _fl_textgc_ = library.cfuncproto(
        library.load_so_libforms(), "fl_textgc_",
        xfdata.GC, [],
        """GC fl_textgc_()""")
    library.check_if_flinitialized()
    retval = _fl_textgc_()
    return retval

#fl_textgc = fl_textgc_()   # commented to prevent a SegmentationFault? --LK
fl_textgc = fl_textgc_


def fl_fheight_():
    """fl_fheight_() -> fheight

    Finds out font height

    Returns
    -------
        fheight : int
            font height

    Examples
    --------
        >>> fonth = fl_fheight_()

    Notes
    -----
        Status: NN-UTest + NoDoc + NoDemo = Maybe

    """
    _fl_fheight_ = library.cfuncproto(
        library.load_so_libforms(), "fl_fheight_",
        cty.c_int, [],
        """int fl_fheight_()""")
    library.check_if_flinitialized()
    retval = _fl_fheight_()
    return retval

#fl_fheight = fl_fheight_()  # commented to prevent a SegmentationFault? --LK
fl_fheight = fl_fheight_


def fl_fdesc_():
    """fl_fdesc_() -> fdescndt

    Finds out descendent of font.

    Returns
    -------
        fdescndt : int
            font descendent

    Examples
    --------
        >>> fontdesc = fl_fdesc_()

    Notes
    -----
        Status: NN-UTest + Doc + NoDemo = Maybe

    """
    _fl_fdesc_ = library.cfuncproto(
        library.load_so_libforms(), "fl_fdesc_",
        cty.c_int, [],
        """int fl_fdesc_()""")
    library.check_if_flinitialized()
    retval = _fl_fdesc_()
    return retval

#fl_fdesc = fl_fdesc_()   # commented to prevent a SegmentationFault? --LK
fl_fdesc = fl_fdesc_


def fl_cur_win_():
    """fl_cur_win_() -> win

    Finds out current window.

    Returns
    -------
        win : long_pos
            window id

    Examples
    --------
        >>> win0 = fl_cur_win_()

    Notes
    -----
        Status: NN-UTest + Doc + NoDemo = Maybe

    """
    _fl_cur_win_ = library.cfuncproto(
        library.load_so_libforms(), "fl_cur_win_",
        xfdata.Window, [],
        """Window fl_cur_win_()""")
    library.check_if_flinitialized()
    retval = _fl_cur_win_()
    return retval

#fl_cur_win = fl_cur_win_()  # commented to prevent a SegmentationFault--LK
fl_cur_win = fl_cur_win_


def fl_cur_fs_():
    """fl_cur_fs_() -> ptr_xfontstruct

    Finds out current font structure.

    Returns
    -------
        ptr_xfontstruct : pointer to xfdata.XFontStruct
            font structure class instance

    Examples
    --------
        >>> pxfntstruct = fl_cur_fs_()

    Notes
    -----
        Status: NN-UTest + Doc + NoDemo = Maybe

    """
    _fl_cur_fs_ = library.cfuncproto(
        library.load_so_libforms(), "fl_cur_fs_",
        cty.POINTER(xfdata.XFontStruct), [],
        """XFontStruct * fl_cur_fs_()""")
    library.check_if_flinitialized()
    retval = _fl_cur_fs_()
    return retval


#fl_cur_fs = fl_cur_fs_()  # commented to prevent a SegmentationFault --LK
fl_cur_fs = fl_cur_fs_


def fl_display_():
    """fl_display_() -> ptr_display

    Finds out current X display.

    Returns
    -------
        ptr_display : pointer to xfdata.Display
            current display

    Examples
    --------
        >>> pdispl = fl_display_()

    Notes
    -----
        Status: NN-UTest + Doc + NoDemo = Maybe

    """
    _fl_display_ = library.cfuncproto(
        library.load_so_libforms(), "fl_display_",
        cty.POINTER(xfdata.Display), [],
        """Display * fl_display_()""")
    library.check_if_flinitialized()
    retval = _fl_display_()
    return retval



# flps_apply_gamma() function placeholder (internal)
# flps_arc() function placeholder (internal)
# flps_circ() function placeholder (internal)
# flps_color() function placeholder (internal)
# flps_draw_box() function placeholder (internal)
# flps_draw_checkbox() function placeholder (internal)
# flps_draw_frame() function placeholder (internal)
# flps_draw_symbol() function placeholder (internal)
# flps_draw_tbox() function placeholder (internal)
# flps_draw_text() function placeholder (internal)
# flps_draw_text_beside() function placeholder (internal)
# flps_emit_header() function placeholder (internal)
# flps_emit_prolog() function placeholder (internal)
# flps_get_gray255() function placeholder (internal)
# flps_get_linestyle() function placeholder (internal)
# flps_get_linewidth() function placeholder (internal)
# flps_get_namedcolor() function placeholder (internal)
# flps_invalidate_color_cache() function placeholder (internal)
# flps_invalidate_font_cache() function placeholder (internal)
# flps_invalidate_linewidth_cache() function placeholder (internal)
# flps_invalidate_symbol_cache() function placeholder (internal)
# flps_line() function placeholder (internal)
# flps_lines() function placeholder (internal)
# flps_linestyle() function placeholder (internal)
# flps_linewidth() function placeholder (internal)
# flps_log() function placeholder (internal)
# flps_output() function placeholder (internal)
# flps_oval() function placeholder (internal)
# flps_pieslice() function placeholder (internal)
# flps_poly() function placeholder (internal)
# flps_rectangle() function placeholder (internal)
# flps_reset_cache() function placeholder (internal)
# flps_reset_linewidth() function placeholder (internal)
# flps_restore_flps() function placeholder (internal)
# flps_rgbcolor() function placeholder (internal)
# flps_roundrectangle() function placeholder (internal)
# flps_set_clipping() function placeholder (internal)
# flps_set_font() function placeholder (internal)
# flps_unset_clipping() function placeholder (internal)

