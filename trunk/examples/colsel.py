#!/usr/bin/env python

#  This file is part of xforms-python, and it has been ported from
#  colsel.c XForms demo, with some adaptations.
#
#  See CREDITS file for XForms copyright attribution, and LICENSE
#  file for xforms-python license and copyright attribution.
#
# default color chooser from the internal/built-in colormap
#


import sys
from xformslib import library as xf
from xformslib import xfdata as xfc


def main(lsysargv, sysargv):

    i = 0
    xf.fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0 )

    print "Click one of trasparent colors to exit"
    while True:
        i = xf.fl_show_colormap(i)
        if i > xfc.FL_YELLOWGREEN:
            break
    return 0


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

