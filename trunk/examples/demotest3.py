#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  demotest3.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
#

import sys
#sys.path.append("..")
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flgoodies import *
from xformslib.flbutton import *
from xformslib.flmisc import *
from xformslib.xfdata import *




# Forms and Objects
class FD_S(object):
    S = None
    vdata = None
    cdata = ""
    ldata = 0




def timeoutCB(tid, stuff):
    fl_show_alert("Standby", "This may abort", "with SEGV", 1)


def pressedCB(pobj, data):
    tid = fl_add_timeout(300, timeoutCB, None)
    print "tid=%d\n" % tid


def create_form_S():

    fdui = FD_S()
    old_unit = fl_get_coordunit()

    fl_set_coordunit(FL_COORD_centiMM)

    fdui.S = fl_bgn_form(FL_NO_BOX, 10837, 8467)
    fl_add_box(FL_UP_BOX, 0, 0, 10837, 8467, "")
    pobj = fl_add_button(FL_NORMAL_BUTTON, 1693, 1693, 7451, 4403, "Press Me")
    fl_set_object_callback(pobj, pressedCB, 0)
    fl_end_form()

    fl_set_coordunit(old_unit)

    return fdui


def main(lsysargv, sysargv):

    fl_initialize(lsysargv, sysargv, "S", 0, 0)

    print "This demo is supposed to CRASH with a SegFault runtime error, " \
          "some time after pressing 'Press me' button."
    print "This is an EXPECTED behaviour, don't worry!\n"

    frmS = create_form_S()
    fl_show_form(frmS.S, FL_PLACE_CENTER, FL_FULLBORDER, "Crash Test")
    while fl_do_forms():
        pass

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

