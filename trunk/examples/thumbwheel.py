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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flthumbwheel import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *
from xformslib import deprecated




class Flthumbwheel(object):
    def __init__(self, lsysargv, sysargv):
        fl_initialize(lsysargv, sysargv, 0, 0, 0)
        fd_twheelform = self.create_form_twheelform()
        # show the first form
        fl_show_form(fd_twheelform, FL_PLACE_CENTERFREE, \
                        FL_FULLBORDER, "twheelform")
        fl_do_forms()


    # callbacks and freeobj handles for form twheelform

    def valchange_cb(self, pobj, data):
        buf = "%.3f" % fl_get_thumbwheel_value(pobj)
        fl_set_object_label(self.preport, buf)


    def returnchange_cb(self, pobj, data):
        n = deprecated.fl_get_choice(pobj)
        if n == 1:
            n = FL_RETURN_END_CHANGED
        elif n == 2:
            n = FL_RETURN_CHANGED
        elif n == 3:
            n = FL_RETURN_END
        else:
            n = FL_RETURN_ALWAYS
        fl_set_thumbwheel_return(self.pvert, n)
        fl_set_thumbwheel_return(self.phor, n)


    def create_form_twheelform(self):
        twheelform = fl_bgn_form(FL_NO_BOX, 220, 260)

        pobj = fl_add_box(FL_UP_BOX, 0, 0, 220, 260, "")

        pobj = fl_add_frame(FL_ENGRAVED_FRAME, 15, 70, 190, 130, "")

        self.pvert = fl_add_thumbwheel(FL_VERT_THUMBWHEEL, \
                                       30, 90, 20, 100, "")
        fl_set_object_callback(self.pvert, self.valchange_cb, 0)
        fl_set_thumbwheel_step(self.pvert, 0.01)

        self.phor = fl_add_thumbwheel(FL_HOR_THUMBWHEEL, \
                                      60, 130, 120, 23, "")
        fl_set_object_callback(self.phor, self.valchange_cb, 0)
        fl_set_thumbwheel_step(self.phor, 0.01)

        self.preport = fl_add_text(FL_NORMAL_TEXT, 60, 90, \
                                   120, 30, "")
        fl_set_object_lalign(self.preport, FL_ALIGN_CENTER | \
                             FL_ALIGN_INSIDE)

        preturnsetting = deprecated.fl_add_choice(deprecated.FL_NORMAL_CHOICE2, \
                                                  35, 20, 160, 30, "")
        fl_set_object_boxtype(preturnsetting, FL_EMBOSSED_BOX)
        fl_set_object_callback(preturnsetting, self.returnchange_cb, 0)
        deprecated.fl_addto_choice(preturnsetting, "End & Changed")
        deprecated.fl_set_choice_item_mode(preturnsetting, 1, \
                                           deprecated.FL_PUP_NONE)
        deprecated.fl_addto_choice(preturnsetting, "Whenever Changed")
        deprecated.fl_set_choice_item_mode(preturnsetting, 2, \
                                           deprecated.FL_PUP_NONE)
        deprecated.fl_addto_choice(preturnsetting, "Always At End")
        deprecated.fl_set_choice_item_mode(preturnsetting, 3, \
                                           deprecated.FL_PUP_NONE)
        deprecated.fl_addto_choice(preturnsetting, "Always")
        deprecated.fl_set_choice_item_mode(preturnsetting, 4, \
                                           deprecated.FL_PUP_NONE)
        deprecated.fl_set_choice(preturnsetting, 2)

        pobj = fl_add_button(FL_NORMAL_BUTTON, 120, 215, \
                             80, 30, "Enough")
        fl_set_object_lalign(pobj, FL_ALIGN_CENTER)

        fl_end_form()
        return twheelform




if __name__ == '__main__':
    Flthumbwheel(len(sys.argv), sys.argv)

