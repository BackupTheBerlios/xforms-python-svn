#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  thumbwheel.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
#

import sys
#sys.path.append("..")
from xformslib import library as xf
from xformslib import xfdata as xfc



# callbacks and freeobj handles for form twheelform

def valchange_cb(pobj, data):

    buf = "%.3f" % xf.fl_get_thumbwheel_value(pobj)
    xf.fl_set_object_label(preport, buf)



def returnchange_cb(pobj, data):

    n = xf.fl_get_choice(pobj)

    if n == 1:
        n = xfc.FL_RETURN_END_CHANGED
    elif n == 2:
        n = xfc.FL_RETURN_CHANGED
    elif n == 3:
        n = xfc.FL_RETURN_END
    else:
        n = xfc.FL_RETURN_ALWAYS

    xf.fl_set_thumbwheel_return(pvert, n)
    xf.fl_set_thumbwheel_return(phor, n)



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, 0, 0, 0)
    fd_twheelform = create_form_twheelform()

    # show the first form
    xf.fl_show_form(fd_twheelform, xfc.FL_PLACE_CENTERFREE, \
                    xfc.FL_FULLBORDER, "twheelform")

    xf.fl_do_forms()
    return 0



def create_form_twheelform():
    global phor, pvert, preport

    twheelform = xf.fl_bgn_form(xfc.FL_NO_BOX, 220, 260)

    pobj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 220, 260, "")

    pobj = xf.fl_add_frame(xfc.FL_ENGRAVED_FRAME, 15, 70, 190, 130, "")

    pvert = xf.fl_add_thumbwheel(xfc.FL_VERT_THUMBWHEEL, \
                                 30, 90, 20, 100, "")
    xf.fl_set_object_callback(pvert, valchange_cb, 0)
    xf.fl_set_thumbwheel_step(pvert, 0.01)

    phor = xf.fl_add_thumbwheel(xfc.FL_HOR_THUMBWHEEL, \
                                60, 130, 120, 23, "")
    xf.fl_set_object_callback(phor, valchange_cb, 0)
    xf.fl_set_thumbwheel_step(phor, 0.01)

    preport = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 60, 90, \
                             120, 30, "")
    xf.fl_set_object_lalign(preport, xfc.FL_ALIGN_CENTER | \
                            xfc.FL_ALIGN_INSIDE)

    preturnsetting = xf.fl_add_choice(xfc.FL_NORMAL_CHOICE2, \
                                     35, 20, 160, 30, "")
    xf.fl_set_object_boxtype(preturnsetting, xfc.FL_EMBOSSED_BOX)
    xf.fl_set_object_callback(preturnsetting, returnchange_cb, 0)
    xf.fl_addto_choice(preturnsetting, "End & Changed")
    xf.fl_set_choice_item_mode(preturnsetting, 1, xfc.FL_PUP_NONE)
    xf.fl_addto_choice(preturnsetting, "Whenever Changed")
    xf.fl_set_choice_item_mode(preturnsetting, 2, xfc.FL_PUP_NONE)
    xf.fl_addto_choice(preturnsetting, "Always At End")
    xf.fl_set_choice_item_mode(preturnsetting, 3, xfc.FL_PUP_NONE)
    xf.fl_addto_choice(preturnsetting, "Always")
    xf.fl_set_choice_item_mode(preturnsetting, 4, xfc.FL_PUP_NONE)
    xf.fl_set_choice(preturnsetting, 2)

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 120, 215, \
                            80, 30, "Enough")
    xf.fl_set_object_lalign(pobj, xfc.FL_ALIGN_CENTER)

    xf.fl_end_form()

    return twheelform



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

