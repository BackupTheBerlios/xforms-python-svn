#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  free1.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# This demo is meant to demonstrate the use of a free
#  object in a form.
#

import sys
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *



class Flfree1(object):

    def __init__(self, lsysargv, sysargv):

        self.dcol = 1
        self.on = 1

        fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0)

        pform = fl_bgn_form(FL_UP_BOX, 400, 400)
        pobj1 = fl_add_button(FL_NORMAL_BUTTON, 320, 20, 40, 30, \
                            "Exit")
        fl_set_object_callback(pobj1, self.done, 0)

        pobj2 = fl_add_free(FL_CONTINUOUS_FREE, 40, 80, 320, 280, \
                          "", self.handle_free1)
        fl_end_form()

        depth  = fl_get_visual_depth()

        # Can't do it if less than 4 bit deep...
        if depth < 4:
            print "This Demo requires a depth of at least 4 bits\n"
            fl_finish()
            sys.exit(1)
        # ...but too large a depth also won't do
        elif depth > 7:
            depth = 7

        self.cole = (1 << depth) - 1
        if self.cole > 64:
            self.cole = 64

        pobj2.contents.u_ldata = col = FL_FREE_COL1
        self.cole += col

        for i in range(col, self.cole + 1):
            j =  255 * (i - col) / (self.cole - col)
            fl_mapcolor(i, j, j, j)

        fl_show_form(pform, FL_PLACE_CENTER, FL_NOBORDER, \
                    "Free Object")
        fl_do_forms()


    # The call back routine

    def handle_free1(self, pobj, event, mx, my, key, ev):

        if event == FL_DRAW:
            fl_rectf(pobj.contents.x, pobj.contents.y, pobj.contents.w, \
                     pobj.contents.h, pobj.contents.u_ldata)
        elif event == FL_RELEASE:
            self.on = not self.on
        elif event == FL_STEP:
            if self.on:
                if pobj.contents.u_ldata >= self.cole:
                    self.dcol = -1
                elif pobj.contents.u_ldata <= FL_FREE_COL1:
                    self.dcol = 1
                pobj.contents.u_ldata += self.dcol
                fl_redraw_object(pobj)
        return 0


    def done(self, pobj, data):
        fl_finish()
        sys.exit(0)





if __name__ == '__main__':
    Flfree1(len(sys.argv), sys.argv)

