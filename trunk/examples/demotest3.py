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
from xformslib import library as xf
from xformslib import xfdata as xfc


# Forms and Objects
class FD_S(object):
    S = None
    vdata = None
    cdata = ""
    ldata = 0




def timeoutCB(tid, stuff):
    xf.fl_show_alert("Standby", "This may abort", "with SEGV", 1)




def pressedCB(pobj, data):
    tid = xf.fl_add_timeout(300, timeoutCB, None)
    print "tid=%d\n" % tid




def create_form_S():

    fdui = FD_S()
    old_unit = xf.fl_get_coordunit()

    xf.fl_set_coordunit(xfc.FL_COORD_centiMM)

    fdui.S = xf.fl_bgn_form(xfc.FL_NO_BOX, 10837, 8467)

    xf.fl_add_box(xfc.FL_UP_BOX, 0, 0, 10837, 8467, "")

    pobj = xf.fl_add_button(xfc.FL_NORMAL_BUTTON, 1693, 1693, 7451, 4403, "Press Me")
    xf.fl_set_object_callback(pobj, pressedCB, 0)

    xf.fl_end_form()

    xf.fl_set_coordunit(old_unit)

    return fdui




def main(lsysargv, sysargv):

    xf.fl_initialize(lsysargv, sysargv, "S", 0, 0)

    print "This demo is supposed to CRASH with a SegFault runtime error, some time" \
          " after pressing 'Press me' button."
    print "This is an EXPECTED behaviour, don't worry!\n"

    frmS = create_form_S()

    xf.fl_show_form(frmS.S, xfc.FL_PLACE_CENTER, xfc.FL_FULLBORDER, "Crash Test")

    while xf.fl_do_forms():
        pass

    return 0




if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

