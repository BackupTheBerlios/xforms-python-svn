#!/usr/bin/env python3

#  This file is part of xforms-python, and it has been ported from
#  colsel.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# default color chooser from the internal/built-in colormap
#

import sys
import xformslib as xfl


def main(lsysargv, sysargv):
    i = 0
    xfl.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0 )
    print("Click one of trasparent colors to exit")
    while True:
        i = xfl.fl_show_colormap(i)
        if i >= 157:
            break
    xfl.fl_finish()
    return 0


if __name__ == '__main__':
    print("********* colsel.py *********")
    main(len(sys.argv), sys.argv)
