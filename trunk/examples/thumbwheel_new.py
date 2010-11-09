#!/usr/bin/env python

#  This file is part of xforms-python, and it is a variation of
#  thumbwheel.c XForms demo, not using deprecated functions, with some
#  adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
#

import sys
#sys.path.append("..")
import xformslib as xfl



class Flthumbwheel(object):
    def __init__(self, lsysargv, sysargv):
        xfl.fl_initialize(lsysargv, sysargv, 0, 0, 0)
        fd_twheelform = self.create_form_twheelform()
        # show the first form
        xfl.fl_show_form(fd_twheelform, xfl.FL_PLACE_CENTERFREE, \
                xfl.FL_FULLBORDER, "twheelform")
        xfl.fl_do_forms()


    # callbacks and freeobj handles for form twheelform
    def valchange_cb(self, pobj, data):
        buf = "%.3f" % xfl.fl_get_thumbwheel_value(pobj)
        xfl.fl_set_object_label(self.preport, buf)


    def returnchange_cb(self, pobj, data):
        n = xfl.fl_get_select_item(pobj).contents.val
        dictreturn = {1 : xfl.FL_RETURN_END_CHANGED, \
                2 : xfl.FL_RETURN_CHANGED, 3 : xfl.FL_RETURN_END, \
                4 : xfl.FL_RETURN_ALWAYS}
        n = dictreturn[n]
        xfl.fl_set_thumbwheel_return(self.pvert, n)
        xfl.fl_set_thumbwheel_return(self.phor, n)


    def create_form_twheelform(self):
        twheelform = xfl.fl_bgn_form(xfl.FL_NO_BOX, 220, 260)

        pobj = xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 220, 260, "")
        pobj = xfl.fl_add_frame(xfl.FL_ENGRAVED_FRAME, 15, 70, 190, 130, "")
        self.pvert = xfl.fl_add_thumbwheel(xfl.FL_VERT_THUMBWHEEL, \
                30, 90, 20, 100, "")
        xfl.fl_set_object_callback(self.pvert, self.valchange_cb, 0)
        xfl.fl_set_thumbwheel_step(self.pvert, 0.01)
        self.phor = xfl.fl_add_thumbwheel(xfl.FL_HOR_THUMBWHEEL, \
                60, 130, 120, 23, "")
        xfl.fl_set_object_callback(self.phor, self.valchange_cb, 0)
        xfl.fl_set_thumbwheel_step(self.phor, 0.01)
        self.preport = xfl.fl_add_text(xfl.FL_NORMAL_TEXT, 60, 90, \
                120, 30, "")
        xfl.fl_set_object_lalign(self.preport, xfl.FL_ALIGN_CENTER | \
                xfl.FL_ALIGN_INSIDE)
        preturnsetting = xfl.fl_add_select(xfl.FL_NORMAL_SELECT, \
                35, 20, 160, 30, "")
        xfl.fl_set_object_boxtype(preturnsetting, xfl.FL_EMBOSSED_BOX)
        xfl.fl_set_object_callback(preturnsetting, self.returnchange_cb, 0)
        xfl.fl_add_select_items(preturnsetting, "End & Changed")
        xfl.fl_add_select_items(preturnsetting, "Whenever Changed")
        xfl.fl_add_select_items(preturnsetting, "Always At End")
        xfl.fl_add_select_items(preturnsetting, "Always")
        pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 120, 215, \
                80, 30, "Enough")
        xfl.fl_set_object_lalign(pobj, xfl.FL_ALIGN_CENTER)

        xfl.fl_end_form()
        return twheelform



if __name__ == '__main__':
    Flthumbwheel(len(sys.argv), sys.argv)
