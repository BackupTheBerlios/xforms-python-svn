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

def valchange_cb(ob, data):

    buf = "%.3f" % xf.fl_get_thumbwheel_value(ob)
    xf.fl_set_object_label(report, buf)



def returnchange_cb(ob, data):

    n = xf.fl_get_choice(ob)

    if n == 1:
        n = xfc.FL_RETURN_END_CHANGED
    elif n == 2:
        n = xfc.FL_RETURN_CHANGED
    elif n == 3:
        n = xfc.FL_RETURN_END
    else:
        n = xfc.FL_RETURN_ALWAYS

    xf.fl_set_thumbwheel_return(vert, n)
    xf.fl_set_thumbwheel_return(hor, n)



def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, 0, 0, 0)
    fd_twheelform = create_form_twheelform()

    # show the first form
    xf.fl_show_form(fd_twheelform, xfc.FL_PLACE_CENTERFREE, \
                    xfc.FL_FULLBORDER, "twheelform")

    xf.fl_do_forms()
    return 0



def create_form_twheelform():
    global hor, vert, report

    twheelform = xf.fl_bgn_form(xfc.FL_NO_BOX, 220, 260)

    obj = xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 220, 260, "")

    obj = xf.fl_add_frame(xfc.FL_ENGRAVED_FRAME, 15, 70, 190, 130, "")

    vert = xf.fl_add_thumbwheel(xfc.FL_VERT_THUMBWHEEL, \
                                30, 90, 20, 100, "")
    xf.fl_set_object_callback(vert, valchange_cb, 0)
    xf.fl_set_thumbwheel_step(vert, 0.01)

    hor = xf.fl_add_thumbwheel(xfc.FL_HOR_THUMBWHEEL, \
                               60, 130, 120, 23, "")
    xf.fl_set_object_callback(hor, valchange_cb, 0)
    xf.fl_set_thumbwheel_step(hor, 0.01)

    report = xf.fl_add_text(xfc.FL_NORMAL_TEXT, 60, 90, \
                            120, 30, "")
    xf.fl_set_object_lalign(report, xfc.FL_ALIGN_CENTER | \
                            xfc.FL_ALIGN_INSIDE)

    returnsetting = xf.fl_add_choice(xfc.FL_NORMAL_CHOICE2, \
                                     35, 20, 160, 30, "")
    xf.fl_set_object_boxtype(returnsetting, xfc.FL_EMBOSSED_BOX)
    xf.fl_set_object_callback(returnsetting, returnchange_cb, 0)
    xf.fl_addto_choice(returnsetting, "End & Changed")
    xf.fl_set_choice_item_mode(returnsetting, 1, xfc.FL_PUP_NONE)
    xf.fl_addto_choice(returnsetting, "Whenever Changed")
    xf.fl_set_choice_item_mode(returnsetting, 2, xfc.FL_PUP_NONE)
    xf.fl_addto_choice(returnsetting, "Always At End")
    xf.fl_set_choice_item_mode(returnsetting, 3, xfc.FL_PUP_NONE)
    xf.fl_addto_choice(returnsetting, "Always")
    xf.fl_set_choice_item_mode(returnsetting, 4, xfc.FL_PUP_NONE)
    xf.fl_set_choice(returnsetting, 2)

    obj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 120, 215, \
                           80, 30, "Enough")
    xf.fl_set_object_lalign(obj, xfc.FL_ALIGN_CENTER)

    xf.fl_end_form()

    return twheelform



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

