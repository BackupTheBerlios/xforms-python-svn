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
import xformslib as xfl



# Forms and Objects
class FD_S(object):
    S = None
    vdata = None
    cdata = ""
    ldata = 0


def timeoutCB(tid, stuff):
    xfl.fl_show_alert("Standby", "This may abort", "with SEGV", 1)


def pressedCB(pobj, data):
    tid = xfl.fl_add_timeout(300, timeoutCB, None)
    print("tid=%d\n" % tid)


def create_form_S():

    fdui = FD_S()
    old_unit = xfl.fl_get_coordunit()

    xfl.fl_set_coordunit(xfl.FL_COORD_centiMM)

    fdui.S = xfl.fl_bgn_form(xfl.FL_NO_BOX, 10837, 8467)
    xfl.fl_add_box(xfl.FL_UP_BOX, 0, 0, 10837, 8467, "")
    pobj = xfl.fl_add_button(xfl.FL_NORMAL_BUTTON, 1693, 1693, \
            7451, 4403, "Press Me")
    xfl.fl_set_object_callback(pobj, pressedCB, 0)
    xfl.fl_end_form()

    xfl.fl_set_coordunit(old_unit)

    return fdui


def main(lsysargv, sysargv):

    xfl.fl_initialize(lsysargv, sysargv, "S", 0, 0)

    print("This demo is supposed to CRASH with a SegFault runtime error, " \
          "some time after pressing 'Press me' button.")
    print("This is an EXPECTED behaviour, don't worry!\n")

    frmS = create_form_S()
    xfl.fl_show_form(frmS.S, xfl.FL_PLACE_CENTER, xfl.FL_FULLBORDER, \
            "Crash Test")
    while xfl.fl_do_forms():
        pass

    return 0



if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
