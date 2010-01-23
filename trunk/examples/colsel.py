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
from xformslib.flbasic import *
from xformslib.flxbasic import *
from xformslib.flgoodies import *
from xformslib.xfdata import *



def main(lsysargv, sysargv):

    i = 0
    fl_initialize(lsysargv, sysargv, "FormDemo", 0, 0 )

    print "Click one of trasparent colors to exit"
    while True:
        i = fl_show_colormap(i)
        if i > FL_YELLOWGREEN:
            break
    fl_finish()


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

